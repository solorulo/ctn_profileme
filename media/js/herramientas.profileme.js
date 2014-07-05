var categoriasHerramientas = [
				'Java',
				'JavaScript',
				'CSS',
				'HTML',
				'C#',
				'jQuery'
			];
var dataHerramientas = [100, 60, 50, 80, 10, 50];
function tablaHerramientas() {
	$('#h').empty();
	for (i in categoriasHerramientas) {
		var text = categoriasHerramientas[i];
		var number = dataHerramientas[i];
		var li = createFilaTabla(text, number, 'lista');
		$('#h').append(li);
	}
}
function graficaHerramientas() {
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
			categories: categoriasHerramientas,
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
			data: dataHerramientas,
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
}
