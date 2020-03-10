$(function(){

	let heartState = false;
	let laughState = false;
	let cryState = false;


	function removeStates(){
		$("#heart").css('background-image','url("images/i/loveFire.png")');
		$("#laugh").css('background-image','url("images/i/laugh.png")');
		$("#cry").css('background-image','url("images/i/cry.png")');
		heartState = false;
		laughState = false;
		cryState = false;
	};

	function shrinkem(x, state){
		$(x).animate({
			'width':'45px',
			'height':'100% - 5px',
		},200);		

		$(x).animate({
			'width':'50px',
			'height':'100%',
		},200);

		removeStates();

		return state = false;

	};





	// EMOTICON CLICKS



	// HEART CLICK

	$("#heart").click(function(){
		if(heartState === true){
			return shrinkem('#heart', heartState);
		}
		removeStates();
		$("#heart").animate({
			'width':'55px',
			'height':'100% + 5px',
		},200);

		$("#heart").css('background-image','url("images/i/loveFireFilled.png")');

		$("#heart").animate({
			'width':'50px',
			'height':'100%',
		},200);

		return heartState = true;

		// SEND JSON DATA TO SERVER HERE FOR CLICK
	});

	// LAUGH LIKE

	$("#laugh").click(function(){
		if(laughState === true){
			return shrinkem('#laugh', laughState);
		}
		removeStates();
		$("#laugh").animate({
			'width':'55px',
			'height':'100% + 5px',
		},200);

		$("#laugh").css('background-image','url("images/i/laughFilled.png")');

		$("#laugh").animate({
			'width':'50px',
			'height':'100%',
		},200);

		return laughState = true;

		// SEND JSON DATA TO SERVER HERE FOR CLICK
	});
})