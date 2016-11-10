
$(document).ready(function(){
    $('#i18n').css('top',$('#logo').outerHeight()/2);
});

$(window).load(function(){
    $('#i18n').css('top',$('#logo').outerHeight()/2);
    navCat();
});

$(window).resize(function(){
    // navCat();
});

function navCat(){
    i = 0;
    Fsize = parseInt($('.navCat').css('font-size'));
    while($('#all_navCat').height() > $('.navCat').outerHeight() & i< 30){
        Fsize = Fsize-1;
        $('.navCat').css('font-size',Fsize);
        i += 1;
    }
}