
jQuery(document).ready(function($) {

	// Populating the text contain elements
	$('.text-container').each(function(i, e) {

		$(e).load('/text/' + $(e).attr('id'));
	    });
    });
