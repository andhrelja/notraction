from django.core.management.base import BaseCommand

from django.conf import settings
from drivers.models import Driver, DriverSubCategoryPosition
from events.models import (
    Event,
    County,
    City
)
from cars.models import (
    Car,
    Model,
    Manufacturer
)
from championships.models import (
    Championship,
    Category)

from pathlib import Path
import json



class Command(BaseCommand):
    help = 'Loads input data'

    def handle(self, *args, **options):
        #self.delete_objects()
        self.load_cars_manufacturer()
        
        #self.load_cars_model()
        #self.load_events_county()
        #self.load_events_city()

        # self.load_events()
        # self.load_drivers()
        # self.load_cars()
        

    def load_cars_manufacturer(self):
        manufacturers_list = get_read_json_file('cars_manufacturer_v2.json')
        for manufacturer in manufacturers_list:
            self.stdout.write(self.style.MIGRATE_HEADING(
                'Applying Manufacturer'), ending=" ")

            manufacturer['image_url'] = manufacturer.pop('raw_image')
            try:
                make = Manufacturer.objects.get(id=manufacturer['id'])
            except Manufacturer.DoesNotExist:
                make = Manufacturer.objects.create(**manufacturer)
            
            if make.name == manufacturer['name']:
                make.image_url = manufacturer['image_url']
            else:
                for manufacturer1 in manufacturers_list:
                    if manufacturer1['name'] == make.name:
                        make.image_url = manufacturer1['raw_image']
                        break
                
            make.save()
            
            self.stdout.write(self.style.MIGRATE_LABEL(
                (':: {} ..'.format(make))), ending=" ")
            self.stdout.write(self.style.SUCCESS('OK'))

    def load_cars_model(self):
        models_list = get_read_json_file('cars_model.json')
        for model in models_list:
            self.stdout.write(self.style.MIGRATE_HEADING(
                'Applying Model'), ending=" ")
            model, _ = Model.objects.get_or_create(**model)
            self.stdout.write(self.style.MIGRATE_LABEL(
                (':: {} ..'.format(model))), ending=" ")
            self.stdout.write(self.style.SUCCESS('OK'))

    def load_events_county(self):
        counties_list = get_read_json_file('events_county.json')
        for county in counties_list:
            self.stdout.write(self.style.MIGRATE_HEADING(
                'Applying County'), ending=" ")
            county, _ = County.objects.get_or_create(**county)
            self.stdout.write(self.style.MIGRATE_LABEL(
                (':: {} ..'.format(county))), ending=" ")
            self.stdout.write(self.style.SUCCESS('OK'))

    def load_events_city(self):
        cities_list = get_read_json_file('events_city.json')

        for grad in cities_list:
            self.stdout.write(self.style.MIGRATE_HEADING(
                'Applying City'), ending=" ")
            city, _ = City.objects.get_or_create(**grad)
            self.stdout.write(self.style.MIGRATE_LABEL(
                (':: {} ..'.format(city))), ending=" ")
            self.stdout.write(self.style.SUCCESS('OK'))

    def load_drivers(self):
        drivers_list = get_read_json_file('drivers.json')
        for driver in drivers_list:
            self.stdout.write(self.style.MIGRATE_HEADING(
                'Applying Driver'), ending=" ")
            driver, _ = Driver.objects.get_or_create(**driver)
            self.stdout.write(self.style.MIGRATE_LABEL(
                (':: {} ..'.format(driver))), ending=" ")
            self.stdout.write(self.style.SUCCESS('OK'))

    def load_cars(self):
        cars_list = get_read_json_file('cars.json')
        for car in cars_list:
            self.stdout.write(self.style.MIGRATE_HEADING(
                'Applying Car'), ending=" ")
            car, _ = Car.objects.get_or_create(**car)
            self.stdout.write(self.style.MIGRATE_LABEL(
                (':: {} ..'.format(car))), ending=" ")
            self.stdout.write(self.style.SUCCESS('OK'))

    def load_events(self):
        events_list = get_read_json_file('events.json')
        for event in events_list:
            self.stdout.write(self.style.MIGRATE_HEADING(
                'Applying Event'), ending=" ")
            event, _ = Event.objects.get_or_create(**event)
            self.stdout.write(self.style.MIGRATE_LABEL(
                (':: {} ..'.format(event))), ending=" ")
            self.stdout.write(self.style.SUCCESS('OK'))

    def delete_objects(self):
        self.stdout.write(self.style.WARNING(
            'Deleting Car'), ending=" ")        
        Car.objects.all().delete()
        self.stdout.write(self.style.MIGRATE_LABEL(
            (':: {} ..'.format(Car))), ending=" ")
        self.stdout.write(self.style.ERROR('OK'))


        self.stdout.write(self.style.WARNING(
            'Deleting Model'), ending=" ")
        Model.objects.all().delete()
        self.stdout.write(self.style.MIGRATE_LABEL(
            (':: {} ..'.format(Model))), ending=" ")
        self.stdout.write(self.style.ERROR('OK'))


        self.stdout.write(self.style.WARNING(
            'Deleting Manufacturer'), ending=" ")
        Manufacturer.objects.all().delete()
        self.stdout.write(self.style.MIGRATE_LABEL(
            (':: {} ..'.format(Manufacturer))), ending=" ")
        self.stdout.write(self.style.ERROR('OK'))


        self.stdout.write(self.style.WARNING(
            'Deleting Event'), ending=" ")
        Event.objects.all().delete()
        self.stdout.write(self.style.MIGRATE_LABEL(
            (':: {} ..'.format(Event))), ending=" ")
        self.stdout.write(self.style.ERROR('OK'))


        self.stdout.write(self.style.WARNING(
            'Deleting County'), ending=" ")
        County.objects.all().delete()
        self.stdout.write(self.style.MIGRATE_LABEL(
            (':: {} ..'.format(County))), ending=" ")
        self.stdout.write(self.style.ERROR('OK'))


        self.stdout.write(self.style.WARNING(
            'Deleting City'), ending=" ")
        City.objects.all().delete()
        self.stdout.write(self.style.MIGRATE_LABEL(
            (':: {} ..'.format(City))), ending=" ")
        self.stdout.write(self.style.ERROR('OK'))


        self.stdout.write(self.style.WARNING(
            'Deleting Driver'), ending=" ")
        Driver.objects.all().delete()
        self.stdout.write(self.style.MIGRATE_LABEL(
            (':: {} ..'.format(Driver))), ending=" ")
        self.stdout.write(self.style.ERROR('OK'))


        self.stdout.write(self.style.WARNING(
            'Deleting Championship'), ending=" ")
        Championship.objects.all().delete()
        self.stdout.write(self.style.MIGRATE_LABEL(
            (':: {} ..'.format(Championship))), ending=" ")
        self.stdout.write(self.style.ERROR('OK'))


        self.stdout.write(self.style.WARNING(
            'Deleting Category'), ending=" ")
        Category.objects.all().delete()
        self.stdout.write(self.style.MIGRATE_LABEL(
            (':: {} ..'.format(Category))), ending=" ")
        self.stdout.write(self.style.ERROR('OK'))


        self.stdout.write(self.style.WARNING(
            'Deleting DriverSubCategoryPosition'), ending=" ")
        DriverSubCategoryPosition.objects.all().delete()
        self.stdout.write(self.style.MIGRATE_LABEL(
            (':: {} ..'.format(DriverSubCategoryPosition))), ending=" ")
        self.stdout.write(self.style.ERROR('OK'))


def get_read_json_file(filename):
    static_root = Path(settings.STATIC_ROOT).resolve()
    with open(static_root / 'input_data' / filename, 'r', encoding='utf8') as f:
        return json.load(f)
