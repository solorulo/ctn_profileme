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

	// Create function outside loop
	function dynamicEvent() {
		this.innerHTML = $('.dynamic-link').hide(400);
		this.className += ' dynamic-success';
	}

	function dynamicEvent2(obj3) {
		obj3.hide(400);
	}

	$('.generate').submit(function() {
		// Grab the input value
		var dynamicValue = $('.generate-input').val();
		var dynamicValue2 = $('.generate-input2').val();

		// If empty value
		if (!dynamicValue2) {

			alert('Please enter something.');

		} else {
			// Change the submit value
			$('.generate-submit').val('Agregar');

			// Create the links with the input value as innerHTML
			var li = document.createElement('li');
			li.className = 'dynamic-link';
			li.innerHTML = dynamicValue2 + "<input type='submit'class='borrar'value='X'>" + "<br>" + dynamicValue + "%";

			// Append it and attach the event (via onclick)
			$('#links').append(li);

			li.onclick = function() {
				dynamicEvent2($(li))
			}
			$('form')[0].habilidad.value = "";
		}

		// Prevent the form submitting
		return false;
	});
	// Create function outside loop
	function Aherramientas() {
		this.innerHTML = $('.lista').hide(400);
		this.className += 'lista-success2';
	}

	function Aherramientas2(obj) {
		obj.hide(400);
	}


	$('.formulario2').submit(function(e) {
		e.preventDefault();
		// Grab the input value
		var valor1 = $('.text').val();
		var valor2 = $('.range').val();

		// If empty value
		if (!valor1) {

			alert('Please enter something.');

		} else {
			// Change the submit value
			$('.agregarV').val('Agregar');

			// Create the links with the input value as innerHTML
			var li = document.createElement('li');
			li.className = 'lista';
			li.innerHTML = valor1 + "<input type='submit'class='borrar'value='X'>" + "<br>" + valor2 + "%";

			// Append it and attach the event (via onclick)
			$('#h').append(li);
			// li.onclick = Aherramientas;
			li.onclick = function() {
				Aherramientas2($(li));
			}
			$('form')[0].herramientas.value = "";
		}

		// Prevent the form submitting
		return false;
	});

	// Create function outside loop
	function Aproyectos() {
		this.innerHTML = $('.proyecto').hide(400);
		this.className += 'proyecto-success2';
	}

	function Aproyectos2(obj2) {
		obj2.hide(400);
	}


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
			}
			$('.nombre').val('');
			$('.descripcion').val('');
			$('.enlace').val('');
		}

		// Prevent the form submitting
		return false;
	});

	$('#container2').highcharts({
		chart: {
			type: 'column',
			backgroundColor: 'transparent',
			margin: [60, 60, 100, 80],
		},
		credits: {
			enabled: false
		},

		title: {
			text: 'Herramientas',

			style: {
				marginleft: '0px',
				color: '#ff738f',
				fontWeight: 'Verdana, sans-serif'
			}

		},

		xAxis: {
			categories: [
				'Java',
				'JavaScript',
			],

			labels: {
				rotation: -90,
				align: 'right',
				style: {
					color: '#ff738f',
					fontSize: '11px',
					fontFamily: 'Verdana, sans-serif'
				}
			}
		},
		yAxis: {
			min: 0,
			title: {
				style: {
					color: '#ff738f',
					fontWeight: 'Verdana, sans-serif'
				}

			}

		},

		legend: {
			enabled: false
		},

		tooltip: {
			formatter: function() {
				return '<b>' + this.x + '</b><br/>' +
					Highcharts.numberFormat(this.y);
			}
		},
		exporting: {
			enabled: false
		},

		series: [{
			name: 'Population',
			data: [100, 200],
			color: '#459fff',
			dataLabels: {
				enabled: true,
				rotation: -90,
				color: 'white',
				align: 'right',
				x: 4,
				y: 10,

				style: {
					fontSize: '10px',
					fontFamily: 'Verdana, sans-serif'
				}
			}
		}]
	});
});

$(document).ready(nalgasychichis);

function nalgasychichis() {
	$('#container').highcharts({
		chart: {
			polar: true,
			backgroundColor: 'transparent',
			type: 'line'

		},
		credits: {
			enabled: false
		},
		title: {
			text: 'Habilidades',
			x: -80,
			style: {
				color: '#459fff',
				fontWeight: 'Verdana, sans-serif'
			}

		},
		pane: {
			size: '80%'
		},
		xAxis: {
			categories: ['Pert,CPM', 'Business Intelligence', 'Gantt', 'Canvas Bussiness Model',
				'Plan de negocios'
			],
			labels: {
				align: 'right',
				style: {
					color: '#459fff',
					fontSize: '11px',
					fontFamily: 'Verdana, sans-serif'
				}
			},
			tickmarkPlacement: 'on',
			lineWidth: 0

		},
		yAxis: {
			gridLineInterpolation: 'polygon',
			lineWidth: 0,
			min: 0
		},
		tooltip: {
			shared: true,
			pointFormat: '<span style="color:{series.color}">{series.name}: <b>{point.y:,.0f}</b><br/>'
		},
		legend: {
			enabled: false,
			align: 'right',
			verticalAlign: 'top',
			y: 70,
			layout: 'vertical'
		},
		exporting: {
			enabled: false

		},
		series: [{

			name: "Choko",
			data: [990, 4440, 660, 770, 1000],
			color: '#459fff',
			pointPlacement: 'on',

		}]
	});
	// the button action
	var i = 0;
	$('#button').click(function() {
		var chart = $('#agregar').highcharts();
		chart.data[0].addPoint(50 * (i % 3));
		i++;
	});


	// $('.foo1').carouFredSel({

	// 	auto: false,

	// 	prev: "#foo1_prev",

	// 	next: "#foo1_next"

	// });
}

$(function() {
	$('#container2').highcharts({
		chart: {
			type: 'column',
			backgroundColor: 'transparent',
			margin: [60, 60, 100, 80],
		},
		credits: {
			enabled: false
		},
		title: {
			text: 'Herramientas',
			style: {
				marginleft: '0px',
				color: '#ff738f',
				fontWeight: 'Verdana, sans-serif'
			}
		},
		xAxis: {
			categories: [
				'Java',
				'JavaScript',
				'CSS',
				'HTML',
				'C#',
				'jQuery'
			],
			labels: {
				rotation: -90,
				align: 'right',
				style: {
					color: '#ff738f',
					fontSize: '11px',
					fontFamily: 'Verdana, sans-serif'

				}
			}
		},
		yAxis: {
			min: 0,
			title: {
				style: {
					color: '#ff738f',
					fontWeight: 'Verdana, sans-serif'
				}

			}

		},
		legend: {
			enabled: false
		},
		tooltip: {
			formatter: function() {
				return '<b>' + this.x + '</b><br/>' +
					Highcharts.numberFormat(this.y);
			}
		},
		exporting: {
			enabled: false

		},
		series: [{
			name: 'Population',
			data: [100, 60, 50, 80, 10, 50],
			color: '#459fff',
			dataLabels: {
				enabled: true,
				rotation: -90,
				color: 'white',
				align: 'right',
				x: 4,
				y: 10,
				style: {
					fontSize: '10px',
					fontFamily: 'Verdana, sans-serif'
				}
			}
		}]
	});
});
$(document).ready(function() {
	$('#menu').slicknav();
});