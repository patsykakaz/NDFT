
$(document).ready(function(){
    $('#i18n').css('top',$('#logo').outerHeight()/2);

});

$(window).load(function(){
    $('.navbar.navbar-default').css('opacity',1);
    $('#i18n').css('top',$('#logo').outerHeight()/2);
    navCat();
});

$(window).resize(function(){
    navCat();
});

function navCat(){
    if($(window).width()>768){
        $("#all_navCat").removeClass('hide');
        if($('#all_navCat').outerHeight() > $('.navCat').outerHeight()){
            Fsize = parseFloat($('.navCat').css('font-size'))-0.05;
            console.log(Fsize);
            $('.navCat').css('font-size',Fsize);
            $('.navCat').attr('rel',Fsize);
            setTimeout(navCat(),10);
        }
    }else{
        $("#all_navCat").addClass('hide');
    }
}