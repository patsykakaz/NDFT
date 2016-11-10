
$(document).ready(function(){
    $('#i18n').css('top',$('#logo').outerHeight()/2);

});

$(window).load(function(){
    $('#i18n').css('top',$('#logo').outerHeight()/2);
    navCat();
});

$(window).resize(function(){
    navCat();
});

function navCat(){
    if($('#all_navCat').outerHeight() > $('.navCat').outerHeight()){
        Fsize = parseFloat($('.navCat').css('font-size'))-0.05;
        $('.navCat').css('font-size',Fsize);
        $('.navCat').attr('rel',Fsize);
        setTimeout(navCat(),10);
    }
}