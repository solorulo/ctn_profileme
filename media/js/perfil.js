
function insertFilaTabla(textInput, numberInput, listContainer, liClass) {
	// Grab the input value
	var dynamicValue = numberInput.val();
	var dynamicValue2 = textInput.val();

	// If empty value
	if (!dynamicValue2) {

		alert('Please enter something.');
		return false;
	} else {

		// Create the links with the input value as innerHTML
		var li = document.createElement('li');
		li.className = liClass;
		li.innerHTML = dynamicValue2 + "<input type='submit'class='borrar'value='X'>" + "<br>" + dynamicValue + "%";

		// Append it and attach the event (via onclick)
		listContainer.append(li);

		li.onclick = function() {
			$(li).hide(400);
		}
		textInput.val('');
	}
	return true;
}
$(document).ready(function() {
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

	$('.generate').submit(function() {
		var texto = $('.generate-input2').val();
		var numero = parseInt($('.generate-input').val());
		if (insertFilaTabla($('.generate-input2'), $('.generate-input'), $('#links'), 'dynamic-link')) {
			categoriasHabilidades.push(texto);
			dataHabilidades.push(numero);
			graficaHabilidades();
		}
		return false;
	});

	$('.formulario2').submit(function(e) {
		var texto = $('.text').val();
		var numero = parseInt($('.range').val());
		if (insertFilaTabla($('.text'), $('.range'), $('#h'), 'lista')) {
			categoriasHerramientas.push(texto);
			dataHerramientas.push(numero);
			graficaHerramientas();
		}
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
				Aproyectos2($(li));
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

$(document).ready(graficaHabilidades);
$(document).ready(graficaHerramientas);

$(document).ready(function() {
	$('#menu').slicknav();
});