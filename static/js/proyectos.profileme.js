var dataProyectos = [
	{ 
		'nombre':'Erbol', 
		'descripcion':'es una plataforma que su principal funcion es reforestar y sembrar productos organicos', 
		'url':'erbol.com.mx' 
	}, 
]

function tablaProyectos() {
	$('#p').empty();
	for (i in dataProyectos) {
		var nombre = dataProyectos[i].nombre;
		var descripcion = dataProyectos[i].descripcion;
		var url = dataProyectos[i].url;
		var li = createFilaTablaP(nombre, descripcion, url);
		$('#p').append(li);
	}
}

function listaProyectos() {
	var lista = $('#proyecto');
	lista.empty();
	for (i in dataProyectos) {
		var nombre = dataProyectos[i].nombre;
		var descripcion = dataProyectos[i].descripcion;
		var url = dataProyectos[i].url;
		var $lu = $(document.createElement('ul'))
		var liNombre = document.createElement('li');
		var liDescripcion = document.createElement('li');
		var liUrl = document.createElement('li');
		liNombre.innerHTML = nombre;
		liDescripcion.innerHTML = descripcion;
		liUrl.innerHTML = url;
		$lu.append(liNombre);
		$lu.append(liDescripcion);
		$lu.append(liUrl);
		lista.append($lu);
	}
}
