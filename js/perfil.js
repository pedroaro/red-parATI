
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