$(".openbth").click(function (){
    $(this).toggleClass('active');
    $('#g-nav').toggleClass('panelactive');
});

$("#g-nav a").click(function(){
    $(".openbth").removeClass('active');
    $("#g-nav").removeClass('panelactive');
});