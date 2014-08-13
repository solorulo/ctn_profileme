function setupHerramientas() {
    graficaHerramientas();
    tablaHerramientas();
}

function setupHabilidades() {
    graficaHabilidades();
    tablaHabilidades();
}

function setupProyectos() {
    tablaProyectos();
    listaProyectos();
}

function setupHobbies() {
    fillChecks();
    showHobbies();
}

$(document).ready(function() {
    $('#menu').slicknav();
    setupExplodes();
    setupHerramientas();
    setupHabilidades();
    setupProyectos();
    setupHobbies();
    $(".checkHb").click(function() {
        showHobbies();
    });
    $('.generate').submit(function() {
        var texto = $('.generate-input2').val();
        var numero = parseInt($('.generate-input').val());
        if (insertFilaTabla($('.generate-input2'), $('.generate-input'), $('#links'), 'dynamic-link')) {
            categoriasHabilidades.push(texto);
            dataHabilidades.push(numero);

            graficaHabilidades();
            $('#Totalh').animate({
                scrollTop: $('#links').height()
            }, "slow");
        } else {
            showError('Introduce una habilidad');
        }
        $('.generate-input2').focus();
        return false;
    });
    $('.formulario2').submit(function(e) {
        var texto = $('.text').val();
        var numero = parseInt($('.range').val());
        // TODO verifica que no exista ya el texto
        if (insertFilaTabla($('.text'), $('.range'), $('#h'), 'lista')) {
            categoriasHerramientas.push(texto);
            dataHerramientas.push(numero);
            graficaHerramientas();
            $('#Totalhe').animate({
                scrollTop: $('#h').height()
            }, "slow");
        } else {
            showError('Introduce una herramienta');
        }
        $('.text').focus();
        return false;
    });
    $('.formulario3').submit(function(e) {
        e.preventDefault();
        // Grab the input value
        var val1 = $('.nombre').val();
        var val2 = $('.descripcion').val();
        var val3 = $('.enlace').val();

        // If empty value
        if (!val1) {

            alert('Please enter something.');

        } else {
            // Change the submit value
            $('.agregarP').val('Agregar');

            // Add to dataProjects array
            project = new Object();

            project.nombre = val1;
            project.descripcion = val2;
            project.url = val3;

            dataProyectos.push(project);

            // Create the links with the input value as innerHTML
            var li = document.createElement('li');
            li.className = 'proyecto';
            li.innerHTML = val1 + "<input type='submit'class='borrar2'value='X'>" + "<br>" + val2 + "<br><br>" + val3;

            // Append it and attach the event (via onclick)
            $('#p').append(li);
            li.onclick = function() {
                $(li).hide(400);
            }
            $('.nombre').val('');
            $('.descripcion').val('');
            $('.enlace').val('');
        }

        // Prevent the form submitting
        return false;
    });
    $('.chabilidades .explode2').click(function(event) {
        // guardar habilidades
        var abilitiesJSObj = new Array();
        var abilitiesLength = categoriasHabilidades.length;

        for (var i = 0; i < abilitiesLength; i++) {
            var ability = new Object();
            ability.nombre = categoriasHabilidades[i];
            ability.puntos = dataHabilidades[i];

            abilitiesJSObj.push(ability);
        }

        $.ajax({
            url: 'registrarHabilidades',
            type: 'POST',
            // success: successF,
            // error: errorF,
            //contentType: 'application/json',
            data: {
                'data': JSON.stringify(abilitiesJSObj),
            },
            headers: {
                'X-CSRFToken': csrftoken
            },
        });
    });
    $('.cherramientas .explode3').click(function(event) {
        // guardar herramientas
        var toolsJSObj = new Array();
        var toolsLength = categoriasHerramientas.length;

        for (var i = 0; i < toolsLength; i++) {
            var tool = new Object();
            tool.nombre = categoriasHerramientas[i];
            tool.puntos = dataHerramientas[i];

            toolsJSObj.push(tool);
        }

        $.ajax({
            url: 'registrarHerramientas',
            type: 'POST',
            // success: successF,
            // error: errorF,
            //contentType: 'application/json',
            data: {
                'data': JSON.stringify(toolsJSObj),
            },
            headers: {
                'X-CSRFToken': csrftoken
            },
        });
    });
    $('#editarPro .explode6').click(function(event) {
        // guardar proyectos
        $.ajax({
            url: 'registrarProyectos',
            type: 'POST',
            // success: successF,
            // error: errorF,
            //contentType: 'application/json',
            data: {
                'data': JSON.stringify(dataProyectos),
            },
            headers: {
                'X-CSRFToken': csrftoken
            },
        });
        tablaProyectos();
        listaProyectos();
    });
    $('#btnG').click(function(event) {
        // guardar hobbies
        var hobbiesJSObj = new Array();

        for (var i in hobbies) {
            hobbiesJSObj.push(i);
        }

        $.ajax({
            url: 'registrarHobbies',
            type: 'POST',
            // success: successF,
            // error: errorF,
            //contentType: 'application/json',
            data: {
                'data': JSON.stringify(hobbiesJSObj),
            },
            headers: {
                'X-CSRFToken': csrftoken
            },
        });
    });
    $('#contenido4 .explode5').click(function(event) {
        // guardar escolaridad
        var es = $('#escolaridadSelect').val();
        var cr = $('textarea#carrera').val();
        var ce = $('textarea#certificaciones').val();
        $.ajax({
            url: 'registrarEscolaridad',
            type: 'POST',
            // success: successF,
            // error: errorF,
            //contentType: 'application/json',
            data: {
                'escolaridad': es,
                'carrera': cr,
                'certificaciones': ce,
            },
            headers: {
                'X-CSRFToken': csrftoken
            },
        });
    });
});

var editingBasicInfo = false;
var editingAbilities = false;
var editingTools = false;
var editingHobbies = false;
var editingSchool = false;
var editingProjects = false;

function setupExplodes() {

    // Edit/Save basic info button
    $('.explode').click(function(e) {
        $('.contenido').toggle('fade', 500);
        $('#datos1').toggle('fade', 500);

        /*
         * Save function
         */
        if (editingBasicInfo) {
            var name = $('#nameText').val();
            var profesion = $('#profesionText').val();
            var age = $('#ageText').val();
            var tel = $('#telephoneText').val();
            var email = $('#emailText').val();
            var job = $('#jobText').val();
            var locality = $('#localityText').val();

            // if ( !name || !profesion || !age || !tel || !email || !job || !locality ) {
            //     return;
            // }

            $.ajax({
                url: 'updateUserBasicInfo',
                type: 'POST',
                data: {
                    'name': name,
                    'profesion': profesion,
                    'age': age,
                    'tel': tel,
                    'email': email,
                    'job': job,
                    'locality': locality,
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function(data) {},
            });
        }

        editingBasicInfo = !editingBasicInfo;
    });

    // Edit/Save abilities
    $('.explode2').click(function() {
        $('#contenido').toggle('fade', 500);
        $('#habilidades').toggle('fade', 500);

        /*
         *
         */
        if (editingAbilities) {
            var abilitiesJSObj = new Array();
            var abilitiesLength = categoriasHabilidades.length;

            for (var i = 0; i < abilitiesLength; i++) {
                var ability = new Object();
                ability.nombre = categoriasHabilidades[i];
                ability.puntos = dataHabilidades[i];

                abilitiesJSObj.push(ability);
            }

            $.ajax({
                url: 'registrarHabilidades',
                type: 'POST',
                data: {
                    'data': JSON.stringify(abilitiesJSObj),
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function(data) {},
            });
        }

        editingAbilities = !editingAbilities;
    });

    // Edit/Save tools
    $('.explode3').click(function() {
        $('#contenido2').toggle('fade', 500);
        $('.herramientas').toggle('fade', 500);

        /*
         *
         */
        if (editingTools) {
            var toolsJSObj = new Array();
            var toolsLength = categoriasHerramientas.length;

            for (var i = 0; i < toolsLength; i++) {
                var tool = new Object();
                tool.nombre = categoriasHerramientas[i];
                tool.puntos = dataHerramientas[i];

                toolsJSObj.push(tool);
            }

            $.ajax({
                url: 'registrarHerramientas',
                type: 'POST',
                data: {
                    'data': JSON.stringify(toolsJSObj),
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function(data) {},
            });
        }

        editingTools = !editingTools;
    });

    $('.explode4').click(function() {
        $('#hobbies').toggle('fade', 500);
        $('.EditH').toggle('fade', 500);

        /*
         *
         */
        if (editingHobbies) {
            var hobbiesJSObj = new Array();

            for (var i in hobbies) {
                hobbiesJSObj.push(i);
            }

            $.ajax({
                url: 'registrarHobbies',
                type: 'POST',
                data: {
                    'data': JSON.stringify(hobbiesJSObj),
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function(data) {},
            });
        }

        editingHobbies = !editingHobbies
    });

    $('.explode5').click(function() {
        $('#contenido4').toggle('fade', 500);
        $('.escolaridad').toggle('fade', 500);

        /*
         *
         */
        if (editingSchool) {
            $.ajax({
                url: 'registrarEscolaridad',
                type: 'POST',
                data: {
                    'escolaridad': $('#escolaridadSelect').val(),
                    'carrera': $('#carrera').val(),
                    'certificaciones': $('#certificaciones').val(),
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function(data) {},
            });
        }

        editingSchool = !editingSchool
    });

    $('.explode6').click(function() {
        $('.contenido5').toggle('fade', 500);
        $('#datosP').toggle('fade', 500);

        /*
         *
         */
        if (editingProjects) {
            $.ajax({
                url: 'registrarProyectos',
                type: 'POST',
                data: {
                    'data': JSON.stringify(dataProyectos),
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function(data) {},
            });
        }

        editingProjects = !editingProjects;
    });
}

function showError(msg) {
    $('.error > p').text(msg || 'Error');
    $('.error').fadeIn(400).delay(3000).fadeOut(400);
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
}

var csrftoken = getCookie('csrftoken');