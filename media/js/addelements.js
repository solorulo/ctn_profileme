
$(function () {
    var counter = 0;

    $('.addbtn').click(function () {
        var elems = '<div class="box">'+
                '<h3>hfdhjhjkhdfkjhd</h3>'+ 
                '<h2>55</h2>'+ 
                '<input type="button" class="removebtn" value="." id="removebtn"' + (counter) + '"/>' +
        '</div>';
        $('#Totalhe2').append(elems);
        counter++;
    });

    $('.removebtn').live(function () {
        $(this).parent().remove();   
    });
});