
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
    $('.small_img').mouseover(function(){
        target = $('#illustration .second:eq('+$(this).attr('rel')+')');
        console.log(target);
        target.addClass('lift');
    });
    $('.small_img').mouseout(function(){
        target = $('#illustration .second:eq('+$(this).attr('rel')+')');
        console.log(target);
        target.removeClass('lift');
    });
}