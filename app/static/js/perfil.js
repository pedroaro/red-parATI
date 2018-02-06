
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
  var valor = getCookie("nocturno");
  if (valor == "no") {
    document.cookie = "nocturno=si; expires=Thu, 18 Dec 2030 12:00:00 UTC; path=/";
  }else{
    document.cookie = "nocturno=no; expires=Thu, 18 Dec 2030 12:00:00 UTC; path=/";
  }
};

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

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