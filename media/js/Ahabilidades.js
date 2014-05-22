		$(document).ready(function(){
		
			// Create function outside loop
			function dynamicEvent() {
				this.innerHTML = $('.dynamic-link').hide(400);
				this.className += ' dynamic-success';
			}
			//$('.borrar').click(function(){

				//('.dynamic-link').hide(400);

			//})			
	
			$('.generate').submit ( function() {
				// Grab the input value
				var dynamicValue = $('.generate-input').val();
				var dynamicValue2 = $('.generate-input2').val();
				
				// If empty value
				if(!dynamicValue) {
				
					alert('Please enter something.');
					
				} else {
					// Change the submit value
					$('.generate-submit').val( 'Click your item below!');
					
					// Create the links with the input value as innerHTML
					var li = document.createElement('li');
					li.className = 'dynamic-link';
					li.innerHTML = dynamicValue2 + "<input type='submit'class='borrar'value='X'>"+"<br><br>" + dynamicValue + "%";
					
					// Append it and attach the event (via onclick)
					$('#links').append(li);
					li.onclick = dynamicEvent;
				}
				
				// Prevent the form submitting
				return false;
			});
		});
		