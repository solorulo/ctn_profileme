 /*jslint unparam: true, regexp: true */
 /*global window, $ */
 $(function() {
 	'use strict';
 	// Change this to the location of your server-side upload handler:
 	var url = '/uploadUserPhoto',
 		uploadButton = $('<button/>')
 		.addClass('btn btn-primary')
 		.prop('disabled', true)
 		.text('Processing...')
 		.on('click', function() {
 			var $this = $(this),
 				data = $this.data();
 			$this
 				.off('click')
 				.text('Abort')
 				.on('click', function() {
 					$this.remove();
 					data.abort();
 				});
 			data.submit().always(function() {
 				$this.remove();
 			});
 		});
 	$('#fileupload').fileupload({
 		formData: [{
 			name: 'csrfmiddlewaretoken',
 			value: csrftoken
 		}, ],
 		url: url,
 		dataType: 'json',
 		autoUpload: false,
 		acceptFileTypes: /(\.|\/)(gif|jpe?g|png)$/i,
 		maxFileSize: 5000000, // 5 MB
 		// Enable image resizing, except for Android and Opera,
 		// which actually support image resizing, but fail to
 		// send Blob objects via XHR requests:
 		disableImageResize: /Android(?!.*Chrome)|Opera/
 			.test(window.navigator.userAgent),
 		previewMaxWidth: 200,
 		previewMaxHeight: 200,
 		previewCrop: true
 	}).on('fileuploadadd', function(e, data) {
 		data.context = $('<div/>').appendTo('#files');
 		$.each(data.files, function(index, file) {
 			var node = $('<p/>');
 			node.appendTo(data.context);
 			data.submit();
 		});
 	}).on('fileuploadprocessalways', function(e, data) {
 		var index = data.index,
 			file = data.files[index],
 			node = $(data.context.children()[index]);
 		if (file.preview) {
 			// $('#imagen_N').prepend(file.preview);
 			// $('#tex_nf').hide();
 			// $('#userPhoto').hide();
 		}
 		if (file.error) {
 			node
 				.append('<br>')
 				.append($('<span class="text-danger"/>').text(file.error));
 		}
 		if (index + 1 === data.files.length) {
 			data.context.find('button')
 				.text('Upload')
 				.prop('disabled', !!data.files.error);
 		}
 	}).on('fileuploadprogressall', function(e, data) {
 		var progress = parseInt(data.loaded / data.total * 100, 10);
 		$('#progress .progress-bar').css(
 			'width',
 			progress + '%'
 		);
 	}).on('fileuploaddone', function(e, data) {
 		$.each(data.result.files, function(index, file) {
 			if (file.url) {
 				var link = $('<a>')
 					.attr('target', '_blank')
 					.prop('href', file.url);
 				$(data.context.children()[index])
 					.wrap(link);
 			} else if (file.error) {
 				var error = $('<span class="text-danger"/>').text(file.error);
 				$(data.context.children()[index])
 					.append('<br>')
 					.append(error);
 			}
 		});
 	}).on('fileuploadfail', function(e, data) {
 		$.each(data.files, function(index, file) {
 			var imgUrl = 'http://profileme.com.mx/media/' + file.name;
 			$('#userPhoto').attr('onError', "alert('error')");
 			$('#userPhoto').attr('src', imgUrl);
 			//$('#userPhoto').attr('src', imgUrl);
 			var error = $('<span/>').text('File upload failed.');
 			$(data.context.children()[index])
 				.append('<br>')
 				.append(error);
 		});
 	}).prop('disabled', !$.support.fileInput)
 		.parent().addClass($.support.fileInput ? undefined : 'disabled');
});