// Readers

function get_keywords() { return $('#keywords input').val()  }
function get_date_range() { return $('#selection-dates input').val()  }
function get_limit() { return $('#limit input').val()  }
function get_sources() {
	var sources = $('#sources input').map(function(){
    	if ( $(this).prop('checked') ) { 
    		return $(this).data('src'); // If checked return the data-src
    	}
	}).get();
	return sources;
  }

// Compiler

function get_options_json() {
    data = JSON.stringify({
        sources : get_sources(),
        keywords : get_keywords(),
        limit : get_limit(),
        date_range : get_date_range(),
        csrfmiddlewaretoken: "{{ csrf_token }}"
    })
    return data;
}

// AJAX

function refresh_chart() {
    $.ajax({
        url: '/visualisations/charts/line/',
        type: 'POST',
        dataType: 'json',
        data: get_options_json(),
        success : function(response) {
        	// We don't ever reach "Success" with a JSON request because
        	// it expects a JSON return format, not HTML.   
        },
        complete : function(response) {
            $( "#chart_div" ).html(response.responseText);
        },
        error : function(err) {
            // console.log("AJAX error in request: " + JSON.stringify(err, null, 2));
        }
    });
 }


 // Bindings

$(document).ready(function() {
    $("#refresh").on('click', refresh_chart );
    refresh_chart();
    console.log("Page Events Successfully Registered");
});

