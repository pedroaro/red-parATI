
function LoadPosts(){
  $('#skills').css('display', 'none');
  $('#friends').css('display', 'none');
  $('#photos').css('display', 'none');
  $('#posts').css('display', 'block');
  $(".btn-primary").each(function() {
    $( this ).removeClass("btn-primary").addClass("btn-default");
  });
  $("#publicaciones").removeClass("btn-default").addClass("btn-primary");

}
function LoadSkills(){
  $('#posts').css('display', 'none');
  $('#friends').css('display', 'none');
  $('#photos').css('display', 'none');
  $('#skills').css('display', 'block');
  $(".btn-primary").each(function() {
    $( this ).removeClass("btn-primary").addClass("btn-default");
  });
  $("#habilidades").removeClass("btn-default").addClass("btn-primary");
}
function LoadFriends(){
  $('#posts').css('display', 'none');
  $('#skills').css('display', 'none');
  $('#photos').css('display', 'none');
  $('#friends').css('display', 'block');
  $(".btn-primary").each(function() {
    $( this ).removeClass("btn-primary").addClass("btn-default");
  });
  $("#amigos").removeClass("btn-default").addClass("btn-primary");
}

function LoadPhotos(){
  $('#posts').css('display', 'none');
  $('#skills').css('display', 'none');
  $('#friends').css('display', 'none');
  $('#photos').css('display', 'block');
  $(".btn-primary").each(function() {
    $( this ).removeClass("btn-primary").addClass("btn-default");
  });
  $("#fotos").removeClass("btn-default").addClass("btn-primary");
}

function ModoNocturno() {
  document.body.classList.toggle('nightmode');
};

$(document).ready(function(){
  var date_input=$('input[name="date"]'); //our date input has the name "date"
  var container=$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
  date_input.datepicker({
    format: 'mm/dd/yyyy',
    container: container,
    todayHighlight: true,
    autoclose: true,
  })
})