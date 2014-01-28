 window.onload = function() {
    'use strict';
    //U.addEvent is a cross-browser way to add an event handler to a DOM object.
    //U.$ is a shortcut to getElementById
    //Idea taken from Larry Ullman's "Modern Javascript: Develop and Design
    U.addEvent(U.$('addbtn'), 'click', addRows);
}

function addRows() {
    'use strict';
    var numRowsToAdd = 1;
    for(var i = 0; i < numRowsToAdd; i++){
        addRow();
    }
}

function addRow() {
    'use strict';
    var sourceNode = document.querySelector('.formrow');
    var newRow = sourceNode.cloneNode(true);
    //every row except the first row should have a delete button associated with it.
    var delButton = document.createElement('input');
    delButton.className = 'delbtn';
    delButton.type = 'button';
    delButton.name = 'delbtn';
    delButton.value = 'X';
    U.addEvent(delButton, 'click', function() {removeRow(delButton)});
    newRow.appendChild(delButton);
    var fieldset = U.$('Totalhe2');
    fieldset.appendChild(newRow);
}

function removeRow(obj) {
    'use strict';
    var theRow = obj.parentNode;
    var theRowParent = theRow.parentNode;
    theRowParent.removeChild(theRow);
}