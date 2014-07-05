function llenarEscolaridad(escolaridad, carrera, certificaciones) {
	$('.escolaridad > h1').text(escolaridad);
	$('#nescuela > p').text(carrera);
	$('#certificaciones > p').text(certificaciones);
}
function llenarEscolaridadEdit(escolaridad, carrera, certificaciones) {
	$('#contenido4 > select').val(escolaridad);
	$('textarea#carrera').val(carrera);
	$('textarea#certificaciones').val(certificaciones);
}