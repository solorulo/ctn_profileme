 $(document).ready(function() {
    $('a[href*=#]').bind('click',function(event){
        var $anchor = $(this);
 
        /*
        if you don't want to use the easing effects:
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1000);
        */
    $('html, body').stop().animate({
           scrollTop: $($anchor.attr('href')).offset().top
        }, 2000,'easeInOutExpo');
   
        event.preventDefault();
    });
});