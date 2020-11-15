let cityLabel = findLabel('id_city');
let citySelect = document.getElementById('id_city');
let countySelect = document.getElementById('id_county');


function findLabel(for_id) {
    
    var labels = document.getElementsByTagName('label');
    
    for(let label of labels) {
        if (label.htmlFor == for_id) {
            
            return label;
        }
    }
}


function toggleCities() {
    selectedCountyOption = countySelect.selectedOptions[0]

    if (selectedCountyOption.value == "") {
        emptySelectList(citySelect)
        appendSelectCities(citySelect, null)
    } else {
        emptySelectList(citySelect)
        appendSelectCities(citySelect, selectedCountyOption.value)
    }
}

function emptySelectList(selectList) {
    selectList.innerText = "";
}

function appendSelectCities(selectList, selectedCountyId) {
    let option = document.createElement('option');
    option.value = "0";
    option.innerHTML = "---------";
    option.selected = true;
    selectList.appendChild(option);
    selectList.disabled = true;

    if (selectedCountyId !== null) {
        for(city of cities) {
            if (city.county_id == selectedCountyId) {
                let option = document.createElement('option');
                option.value = city.id;
                
                option.innerHTML = city.full_name;
                selectList.appendChild(option);
            }
        }
        selectList.disabled = false;
    }
}