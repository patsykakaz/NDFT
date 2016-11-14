
$(document).ready(function(){
});

$(window).load(function(){
    illustration();
});

$(window).resize(function(){
    illustration();
});

function illustration(){
    $('#illustration').height($('#illustration').width()*0.75);
    $('.small_img').width((
            $('#illustration').width()-40)/3
        );
    $('.small_img').mouseover(function(){
        target = $('#illustration .second:eq('+$(this).attr('rel')+')');
        // console.log(target);
        target.addClass('lift');
        $('#illustration img:first').css('opacity',0);
    });
    $('.small_img').mouseout(function(){
        target = $('#illustration .second:eq('+$(this).attr('rel')+')');
        // console.log(target);
        $('#illustration img:first').css('opacity',1);
        target.removeClass('lift');
    });
}