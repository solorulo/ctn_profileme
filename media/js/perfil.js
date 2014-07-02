function setupHerramientas() {
	graficaHerramientas();
	tablaHerramientas();
}
function setupHabilidades() {
	graficaHabilidades();
	tablaHabilidades();
}
$(document).ready(function() {
	$('#menu').slicknav();
	setupExplodes();
	setupHerramientas();
	setupHabilidades();
	$('.generate').submit(function() {
		var texto = $('.generate-input2').val();
		var numero = parseInt($('.generate-input').val());
		if (insertFilaTabla($('.generate-input2'), $('.generate-input'), $('#links'), 'dynamic-link')) {
			categoriasHabilidades.push(texto);
			dataHabilidades.push(numero);
			graficaHabilidades();
			$('#Totalh').animate({ scrollTop: $('#links').height() }, "slow");
		}
		else {
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
			$('#Totalhe').animate({ scrollTop: $('#h').height() }, "slow");
		}
		else {
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

});

function setupExplodes() {

	$('.explode2').click(function() {
		$('#contenido').toggle('fade', 500);
		$('#habilidades').toggle('fade', 500);
	});

	$('.explode3').click(function() {
		$('#contenido2').toggle('fade', 500);
		$('.herramientas').toggle('fade', 500)
	});

	$('.explode').click(function() {
		$('.contenido').toggle('fade', 500);
		$('#datos1').toggle('fade', 500);

	});

	$('.explode4').click(function() {
		$('#hobbies').toggle('fade', 500);
		$('.EditH').toggle('fade', 500);
	});

	$('.explode5').click(function() {
		$('#contenido4').toggle('fade', 500);
		$('.escolaridad').toggle('fade', 500);
	});

	$('.explode6').click(function() {
		$('.contenido5').toggle('fade', 500);
		$('#datosP').toggle('fade', 500);
	});
}
function showError(msg) {
	$('.error > p').text(msg || 'Error');
	$('.error').fadeIn(400).delay(3000).fadeOut(400);
}
