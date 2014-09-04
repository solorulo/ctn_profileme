function setupHerramientas() {
    tablaHerramientas();
}

function setupHabilidades() {
    tablaHabilidades();
}

function setupProyectos() {
    tablaProyectos();
}

function setupHobbies() {
    fillChecks();
}

$(document).ready(function() {
    setupHerramientas();
    setupHabilidades();
    setupProyectos();
    setupHobbies();

    $('.generate').submit(function() {
        var texto = $('.generate-input2').val();
        var numero = parseInt($('.generate-input').val());
        if (insertFilaTabla($('.generate-input2'), $('.generate-input'), $('#links'), 'dynamic-link')) {
            categoriasHabilidades.push(texto);
            dataHabilidades.push(numero);
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

    /*
     *
     */
    $('.section7>.btnG>input[type=button]').click(function(event) {
        /*
         * Info básica
         */
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

        var errorP = false;

        function updateUserBasicInfo(successF, errorF) {
            return $.ajax({
                url: 'updateUserBasicInfo',
                type: 'POST',
                success: successF,
                error: errorF,
                //contentType: 'application/json',
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
            });
        }

        function registrarHabilidades(successF, errorF) {
            /*
             * Habilidades
             */
            var abilitiesJSObj = new Array();
            var abilitiesLength = categoriasHabilidades.length;

            for (var i = 0; i < abilitiesLength; i++) {
                var ability = new Object();
                ability.nombre = categoriasHabilidades[i];
                ability.puntos = dataHabilidades[i];

                abilitiesJSObj.push(ability);
            }

            return $.ajax({
                url: 'registrarHabilidades',
                type: 'POST',
                success: successF,
                error: errorF,
                //contentType: 'application/json',
                data: {
                    'data': JSON.stringify(abilitiesJSObj),
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
            });
        }

        function registrarHerramientas(successF, errorF) {
            /*
             * Herramientas
             */
            var toolsJSObj = new Array();
            var toolsLength = categoriasHerramientas.length;

            for (var i = 0; i < toolsLength; i++) {
                var tool = new Object();
                tool.nombre = categoriasHerramientas[i];
                tool.puntos = dataHerramientas[i];

                toolsJSObj.push(tool);
            }

            return $.ajax({
                url: 'registrarHerramientas',
                type: 'POST',
                success: successF,
                error: errorF,
                //contentType: 'application/json',
                data: {
                    'data': JSON.stringify(toolsJSObj),
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
            });
        }

        function registrarHobbies(successF, errorF) {

            /*
             * Hobbies
             */
            var hobbiesJSObj = new Array();

            for (var i in hobbies) {
                hobbiesJSObj.push(i);
            }

            return $.ajax({
                url: 'registrarHobbies',
                type: 'POST',
                success: successF,
                error: errorF,
                //contentType: 'application/json',
                data: {
                    'data': JSON.stringify(hobbiesJSObj),
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
            });

        }

        function registrarEscolaridad(successF, errorF) {
            /*
             *  Educación
             */
            return $.ajax({
                url: 'registrarEscolaridad',
                type: 'POST',
                success: successF,
                error: errorF,
                //contentType: 'application/json',
                data: {
                    'escolaridad': $('#escolaridadSelect').val(),
                    'carrera': $('#carrera').val(),
                    'certificaciones': $('#certificaciones').val(),
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
            });
        }

        function registrarProyectos(successF, errorF) {
            /*
             * Proyectos
             */
            return $.ajax({
                url: 'registrarProyectos',
                type: 'POST',
                success: successF,
                error: errorF,
                //contentType: 'application/json',
                data: {
                    'data': JSON.stringify(dataProyectos),
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
            });
        }

        //

        function registraDesmadre() {
        	var funcs = [updateUserBasicInfo, registrarHabilidades, registrarHerramientas, registrarHobbies, registrarEscolaridad, registrarProyectos];
        	var i = 0;
        	var obThis = this;
        	obThis['execute'] = function() {
        		if (errorP) {
        			alert("Ha ocurrido un error");
        			return;
        		}
        		if (i >= funcs.length) {
        			window.location = "/profile";
        			return;
        		}
        		funcs[i](function() {
                    obThis.execute();
                }, function() {
                    errorP = true;
                    alert("Ha ocurrido un error");
                });
        		i++;
        	}
        	return obThis;
        }
        registraDesmadre().execute();
    });
});