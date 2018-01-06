// Toggle Function
$('.toggle').click(function(){
	// Switches the Icon
	$(this).children('i').toggleClass('fa-plus');
	// Switches the forms  
	if($('#password').css('display') == 'block'){
		$('#password').animate({
		    height: "toggle",
		    'padding-top': 'toggle',
		    'padding-bottom': 'toggle',
		    opacity: "toggle"
		  }, "slow");
		$('#register').animate({
		    height: "toggle",
		    'padding-top': 'toggle',
		    'padding-bottom': 'toggle',
		    opacity: "toggle"
		}, "slow");
	}else{
		$('#login').animate({
			height: "toggle",
			'padding-top': 'toggle',
			'padding-bottom': 'toggle',
			opacity: "toggle"
		}, "slow");

		$('#register').animate({
		    height: "toggle",
		    'padding-top': 'toggle',
		    'padding-bottom': 'toggle',
		    opacity: "toggle"
		}, "slow");
	}
});

$('.cta').click(function(){
	if(!($('.toggle').children('i').hasClass('fa-plus'))){
		$('.toggle').children('i').toggleClass('fa-plus');
	}
  // Switches the forms  
	if($('#login').css('display') == 'block' || $('#register').css('display') == 'block'){
		if($('#login').css('display') == 'block'){
			$('#login').animate({
			    height: "toggle",
			    'padding-top': 'toggle',
			    'padding-bottom': 'toggle',
			    opacity: "toggle"
			  }, "slow");
		}
		if($('#register').css('display') == 'block'){
			$('#register').animate({
			    height: "toggle",
			    'padding-top': 'toggle',
			    'padding-bottom': 'toggle',
			    opacity: "toggle"
			  }, "slow");
		}
	}else if($('#password').css('display') == 'block'){
		$('#login').animate({
	    	height: "toggle",
		    'padding-top': 'toggle',
		    'padding-bottom': 'toggle',
		    opacity: "toggle"
		}, "slow");
	}
	$('#password').animate({
	    height: "toggle",
	    'padding-top': 'toggle',
	    'padding-bottom': 'toggle',
	    opacity: "toggle"
	}, "slow");
});