
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
    });
    $('.small_img').mouseout(function(){
        target = $('#illustration .second:eq('+$(this).attr('rel')+')');
        // console.log(target);
        target.removeClass('lift');
    });
}