$(document).ready(function(){
        
    $('.fade2').click(function(){
        $('#imagenD').toggle('fade',500);
        $('.slogan').toggle('fade',500)
        $('.contenido').toggle('fade',1000);

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