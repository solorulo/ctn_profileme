// JavaScript Document

function draggerTarget(dragger, target) {
	dragger.draggable()
	dragger.mouseout(function() {
		var lim_izq = target.position().left;
		var lim_der = target.position().left+target.width();
		var lim_sup = target.position().top;
		var lim_inf = target.position().top+target.height();
			
		if (mouseX > lim_izq && mouseX < lim_der && mouseY >lim_sup && mouseY < lim_inf ) {
			//resultado();
			//alert("ok");
			dragger.attr("correcto", "true");
			target.css("background-color", "#ff0000");
			
		} 
		dragger.css("left", dragger.attr("left") );
		dragger.css("top", dragger.attr("top") );
	});
}