$(document).ready(function(){

    $('.mover').click(function(){
          var clicks = $(this).data('clicks');
            if (clicks) {
                 $('#imagen').animate({
                    width:'36%'
                });

                $('#imagenD').animate({
                    top:'30%',
                    left: '0%',
                });

                $('#slogan').animate({
                    opacity:'1',
                });

            } 


            else {
                $('#imagen').animate({
                    width:'20%',

                });

                $('#imagenD').animate({
                    top:'17%',
                    left: '4%',

                });

                $('#slogan').animate({
                    opacity:'0.0',
                });

                
            }
          $(this).data("clicks", !clicks);

        });

       
    $('.restore').click(function(){
        $('#imagen').animate({
            width:'36%'
        });

        $('#imagenD').animate({
            top:'30%',
            left: '0%',
        });

        $('#slogan').animate({
            opacity:'1',
        });

    });

        
    $('.fade2').click(function(){
        $('.contenido').toggle('fade',500);


    });


    $('.BuscasE').click(function(){
        $('.Registro1').css('background','rgba(69,159,255,0.7)');
        $('#BEmpleados').css('display','block');
        $('#OfreceE').css('display','none');

    });

    $('.Ofrece').click(function(){
        $('.Registro1').css('background','#6f88c2')
        $('#OfreceE').css('display','block');
        $('#BEmpleados').css('display','none');
    });



    $('#OfreceE').css('display','none');
    $('.BuscasE').css('background','rgba(69,159,255,0.7)')
    $('.Ofrece').css('background','#6f88c2')
       
      
});