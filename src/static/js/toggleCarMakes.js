let modelLabel = findLabel('id_model');
let modelSelect = document.getElementById('id_model');
let makeSelect = document.getElementById('id_make');


function findLabel(for_id) {

    var labels = document.getElementsByTagName('label');

    for (let label of labels) {
        if (label.htmlFor == for_id)
            return label;
    }
}


function toggleModels() {
    selectedmakeOption = makeSelect.selectedOptions[0]

    if (selectedmakeOption.value == "") {
        emptySelectList(modelSelect)
        appendSelectModels(modelSelect, null)
    } else {
        emptySelectList(modelSelect)
        appendSelectModels(modelSelect, selectedmakeOption.value)
    }
}

function emptySelectList(selectList) {
    selectList.innerText = "";
}

function appendSelectModels(selectList, selectedMakeId) {
    let option = document.createElement('option');
    option.value = "0";
    option.innerHTML = "---------";
    option.selected = true;
    selectList.appendChild(option);
    selectList.disabled = true;

    if (selectedMakeId !== null) {
        for (model of models) {
            if (model.manufacturer_id == selectedMakeId) {
                let option = document.createElement('option');
                option.value = model.id;

                option.innerHTML = model.name;
                selectList.appendChild(option);
            }
        }
        selectList.disabled = false;
    }
}