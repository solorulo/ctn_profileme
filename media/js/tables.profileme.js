function insertFilaTabla(textInput, numberInput, listContainer, liClass) {
	// Grab the input value
	var dynamicValue = numberInput.val();
	var dynamicValue2 = textInput.val();

	// If empty value
	if (!dynamicValue2) {
		return false;
	} else {

		// Create the links with the input value as innerHTML
		var li = createFilaTabla(dynamicValue2, dynamicValue, liClass);

		// Append it and attach the event (via onclick)
		listContainer.append(li);
		textInput.val('');
	}
	return true;
}
function createFilaTabla(text, number, liClass) {

	// Create the links with the input value as innerHTML
	var li = document.createElement('li');
	li.className = liClass;
	li.innerHTML = text + "<input type='submit'class='borrar'value='X'>" + "<br>" + number + "%";

	li.onclick = function() {
		$(li).hide(400);
	}
	return li;
}
function insertFilaTablaP(nameInput, descInput, urlInput, listContainer) {
	// Grab the input value
	var val1 = nameInput.val();
	var val2 = descInput.val();
	var val3 = urlInput.val();

	// If empty value
	if (!val1) {
		return false;
	} else {
		// Create the links with the input value as innerHTML
		var li = createFilaTablaP(val1, val2, val3);

		// Append it and attach the event (via onclick)
		listContainer.append(li);
		nameInput.val('');
		descInput.val('');
		urlInput.val('');
	}
	return true;
}
function createFilaTablaP(val1, val2, val3) {

	// Create the links with the input value as innerHTML
	var li = document.createElement('li');
	li.className = 'proyecto';
	li.innerHTML = val1 + "<input type='submit'class='borrar2'value='X'>" + "<br>" + val2 + "<br><br>" + val3;

	li.onclick = function() {
		$(li).hide(400);
	}
	return li;
}
