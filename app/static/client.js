var el = x => document.getElementById(x);
var prediction_api_path = '/analyze';
var api_response_key_name = 'result';
var DEBUG = true;
/*
function showPicker(inputId) { el('file-input').click(); }

function showPicked(input) {
    el('upload-label').innerHTML = input.files[0].name;
    var reader = new FileReader();
    reader.onload = function (e) {
        el('image-picked').src = e.target.result;
        el('image-picked').className = '';
    }
    reader.readAsDataURL(input.files[0]);
}
*/

function analyze() {
    //var uploadFiles = el('file-input').files;
    //if (uploadFiles.length != 1) alert('Please select 1 file to analyze!');
    var age = el('form-age').value;
    var fnlwgt = el('form-fnlwgt').value;
    var education_num = el('form-education-num').value;
    var workclass = el('form-workclass').value;
    var education = el('form-education').value;
    var marital_status = el('form-marital-status').value;
    var occupation = el('form-occupation').value;
    var relationship = el('form-relationship').value;
    var race = el('form-race').value;
    
    el('analyze-button').innerHTML = 'Analyzing...';
    var xhr = new XMLHttpRequest();
    var loc = window.location
    xhr.open('POST', `${loc.protocol}//${loc.hostname}:${loc.port}${prediction_api_path}`, true);
    xhr.onerror = function() {alert (xhr.responseText);}
    xhr.onload = function(e) {
        if (this.readyState === 4) {
            var response = JSON.parse(e.target.responseText);
            el('result-label').innerHTML = `${response[api_response_key_name]}`;
        }
        el('analyze-button').innerHTML = 'Analyze';
    }

    var formData = new FormData();
    formData.append('age', age);
    formData.append('fnlwgt', fnlwgt);
    formData.append('education-num', education_num);
    formData.append('workclass', workclass);
    formData.append('education', education);
    formData.append('marital-status', marital_status);
    formData.append('occupation', occupation);
    formData.append('relationship', relationship);
    formData.append('race', race);
    if (DEBUG) {
        console.log('formData entries:')
        for (var pair of formData.entries()) {
            console.log(pair[0]+ ', ' + pair[1]); 
        }    
    }
 
    xhr.send(formData);
}

