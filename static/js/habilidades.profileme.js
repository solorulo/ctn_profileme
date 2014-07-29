var categoriasHabilidades /*= ['Pert,CPM', 'Business Intelligence', 'Gantt', 'Canvas Bussiness Model',
	'Plan de negocios', 'Otra'
]*/;
var dataHabilidades /*= [990, 4440, 660, 770, 1000, 5]*/;

function tablaHabilidades() {
	$('#links').empty();
	for (i in categoriasHabilidades) {
		var text = categoriasHabilidades[i];
		var number = dataHabilidades[i];
		var li = createFilaTabla(text, number, 'dynamic-link');
		$('#links').append(li);
	}
}

function graficaHabilidades() {
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
			categories: categoriasHabilidades,
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
			name: "Porcentaje",
			data: dataHabilidades,
			color: '#459fff',
			pointPlacement: 'on',

		}]
	});
}
