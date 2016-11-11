
$(document).ready(function(){
    $('#i18n').css('top',$('#logo').outerHeight()/2);

});

$(window).load(function(){
    $('.navbar.navbar-default').css('opacity',1);
    $('#i18n').css('top',$('#logo').outerHeight()/2);
    if($(window).width()>991){
        navCat();
    }
});

$(window).resize(function(){
    $('.navCat').css('font-size',18);
    if($(window).width()>991){
        navCat();
    }
});

function navCat(){
    $("#all_navCat").removeClass('hide');
    if($('#all_navCat').outerHeight() > $('.navCat').outerHeight()){
        Fsize = parseFloat($('.navCat').css('font-size'))-0.05;
        console.log(Fsize);
        $('.navCat').css('font-size',Fsize);
        $('.navCat').attr('rel',Fsize);
        if(Fsize>0){
            setTimeout(navCat(),10);
        }
    }
}