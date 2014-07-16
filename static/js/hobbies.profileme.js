var hobbies = {};
hobbies["soccer"]=true;

function fillChecks() {
	for (var i in hobbies) {
		$('#' + i).prop('checked', hobbies[i] || false);
	}
}

function showHobbies() {
	var lista = $('#hobbies > ul');
	lista.empty();
	for (var i in hobbies) {
		if (hobbies[i]) {
			var $li = $(document.createElement('li'));
			var img = document.createElement('img');
			img.src = "/static/img/iconosG/" + i + "-g.png";
			$li.append(img);
			lista.append($li);
		}
	}
}

$(document).ready(function(event) {
	$(".checkHb").click(function() {
		hobbies[$(this).attr("id")] = $(this).is(':checked');
	});
});