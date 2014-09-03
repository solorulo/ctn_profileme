var hobbies = {};
// hobbies["soccer"] = true;

function fillChecks() {
	for (var i in hobbies) {
		$('#' + i).prop('checked', hobbies[i] || false);
	}
}

function showHobbies() {
	var lista = $('#hobbies > ul');
	lista.empty();
	var i = 1;
	for (var i in hobbies) {
		if (hobbies[i]) {
			var $li = $(document.createElement('li'));
			var img = document.createElement('img');
			img.src = "/static/img/iconosG/" + i + "-g.png";
			$li.append(img);
			lista.append($li);
			i ++;
			if (i == 4) {
				i = 1;
				break;
			}
		}
	}
}

$(document).ready(function(event) {
	$(".checkHb").click(function() {
		var id = $(this).attr("id");
		hobbies[id] = $(this).is(':checked');
		if (!hobbies[id]) {
			try {
				delete hobbies[id];
			} catch (e) { }
		}
	});
});
