
$(document).ready(function(){
});

$(window).load(function(){
    illustration();
});

$(window).resize(function(){

});

function illustration(){
    $('#illustration').height($('#illustration').width()*0.75);
    $('.small_img').width((
            $('#illustration').width()
                -(20 * ($('.small_img').length-1))
            )/($('.small_img').length)
        );
}