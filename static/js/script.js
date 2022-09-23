function normalNews(x) {
  x.className = 'list-group-item list-group-item-action';
}

function activeNews(x) {
  x.className = 'list-group-item list-group-item-action active';
}

function normalNav(x) {
  x.className = 'list-group-item list-group-item-action dropdown-toggle';
}

function activeNav(x) {
  x.className = 'list-group-item list-group-item-action dropdown-toggle active';
}

function rangeFunc(newVal){
     if(newVal === '0'){
          document.body.style.backgroundColor = 'black';
          // document.getElementById('navbar').style.backgroundColor = 'black';
     }else if (newVal === '5'){
          document.body.style.backgroundColor = 'gray';
     }else if (newVal === '10'){
          document.body.style.backgroundColor = 'darkgray';
     }else{
          document.body.style.backgroundColor = 'white';
     }
}


$(document).ready(function(){
    $(".dropright").hover(function(){
        var dropdownMenu = $(this).children(".dropdown-menu");
        if(dropdownMenu.is(":visible")){
            dropdownMenu.parent().toggleClass("open");
        }
    });
});
function normal(x) {
  x.className = 'list-group-item list-group-item-action';
}

function active(x) {
  x.className = 'list-group-item list-group-item-action active';
}

$(function() {
    $('.form-check-input').click(function() {
        if ($('.form-check-input').is(':checked')) {
            $('#submit').removeAttr('disabled');
        } else {
            $('#submit').attr('disabled', 'disabled');
        }
    });
});

function sizeValidation() {
    var uploadField =  document.getElementById('validatedCustomFile');
    if(uploadField.files[0].size > 5242980){
       alert("File is too big! max size 5 MB");
       uploadField.value = "";
    }
}

function func() {
    document.getElementById('b-delete').value = 'delete';
}
function showPhone() {
    document.getElementById('phone-1').style.display = 'grid';
    document.getElementById('show-b-p').style.display = 'none';
}
function showEmail() {
    document.getElementById('email-1').style.display = 'grid';
    document.getElementById('show-b-e').style.display = 'none';
}