from django.core.management.base import BaseCommand
from django.conf import settings
from events.models import Event, County, City
from cars.models import Car, Model, Manufacturer
from drivers.models import Driver
from championships.models import (
    Championship,
    Category,
    CategoryDriverPosition, Discipline)
from pathlib import Path
import json

ISSUE_CREATE = {
    'cars.car'                              : lambda pk, model, kwargs: Car.objects.create(pk=pk, model=model, **kwargs),
    'events.event'                          : lambda pk, kwargs: Event.objects.create(pk=pk, **kwargs),
    'drivers.Driver'                        : lambda pk, kwargs: Driver.objects.create(pk=pk, **kwargs),
    'championships.category'                : lambda pk, kwargs: Category.objects.create(pk=pk, **kwargs),
    'championships.discipline'              : lambda pk, kwargs: Championship.objects.create(pk=pk, **kwargs),
    'championships.championship'            : lambda pk, kwargs: Championship.objects.create(pk=pk, **kwargs),
    'championships.categorydriverposition'  : lambda pk, kwargs: CategoryDriverPosition.objects.create(pk=pk, **kwargs),
}


class Command(BaseCommand):
    help = 'Loads input data'

    def handle(self, *args, **options):
        self.delete_objects()
        self.load_county_cities()
        self.load_manufacturers_models()

        content = get_json_from_static_file(filename='data.json')
        self.load_data(content)

    def load_manufacturers_models(self):
        dictionary = get_json_from_static_file('proizvodjaci_modeli.json')
        for manufacturer in dictionary:
            make_id = manufacturer['id'] + 1
            make = Manufacturer.objects.create(
                    id=make_id, 
                    name=manufacturer['name'])
            
            for model in manufacturer['brands']:
                model_id = model['id'] + 1
                Model.objects.create(
                    id=model_id,
                    name=model['name'],
                    manufacturer=make)
            if settings.DEBUG:
                self.stdout.write(self.style.SUCCESS('"<Manufacturer:{}>" and dependencies created successfully'.format(make)))

    def load_county_cities(self):
        dictionary = get_json_from_static_file('gradovi_opcine.json')
        city_id = 0
        for zupanija in dictionary:
            county = County.objects.create(
                id=zupanija['id'], 
                name=zupanija['naziv'])
            for grad in zupanija['gradovi']:
                city_id += 1
                City.objects.create(
                    id=city_id,
                    name=grad,
                    county=county)
            for opcina in zupanija['opcine']:
                city_id += 1
                City.objects.create(
                    id=city_id,
                    name=opcina,
                    county=county)
            if settings.DEBUG:
                self.stdout.write(self.style.SUCCESS('"<County:{}>" and dependencies created successfully'.format(county)))
            
    def load_data(self, content):
        Discipline().create()
        for object in content:
            db_table_name = object['model']
            if db_table_name == 'cars.car':
                self.load_cars(db_table_name, object)
            else:
                self.load_other_data(db_table_name, object)

    def load_cars(self, db_table_name, object):
        car_model_name = object['fields'].pop('model_name')
        model = Model.objects.get(name=car_model_name)
        object = ISSUE_CREATE[db_table_name](pk=object['pk'], model=model, kwargs=object['fields'])
        self.stdout.write(self.style.SUCCESS('"{}" created successfully'.format(object)))
            
    def load_other_data(self, db_table_name, object):
        db_table_name = object['model']
        object = ISSUE_CREATE[db_table_name](pk=object['pk'], kwargs=object['fields'])
        self.stdout.write(self.style.SUCCESS('"<{}>" created successfully'.format(object)))
   

    def delete_objects(self):
        Car.objects.all().delete()
        Model.objects.all().delete()
        Manufacturer.objects.all().delete()

        Event.objects.all().delete()
        County.objects.all().delete()
        City.objects.all().delete()
        
        Driver.objects.all().delete()

        Championship.objects.all().delete()
        Discipline.objects.all().delete()
        Category.objects.all().delete()
        CategoryDriverPosition.objects.all().delete()

    
def get_json_from_static_file(filename):
    static_root = Path(settings.STATIC_ROOT).resolve()
    with open(static_root / 'input_data' / filename, 'r', encoding='utf8') as f:
        return json.load(f)