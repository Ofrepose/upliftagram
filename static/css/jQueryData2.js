$(function(){

	let heartState = false;
	let laughState = false;
	let cryState = false;
	let commentState = false;

	let commentBoxState = false;

	$("#0002").hide();

	$("#0002").css("height","0px");
	$("#0002").css("width","100%");



	function removeStates(){
		$("#heart").css('background-image','url("images/i/loveFire.png")');
		$("#laugh").css('background-image','url("images/i/laugh.png")');
		$("#cry").css('background-image','url("images/i/cry.png")');
		commentState = false;
		heartState = false;
		laughState = false;
		cryState = false;
		commentBoxState = false;
	};

	function shrinkem(x, state){
		$(x).animate({
			'width':'30px',
			'height':'100% - 5px',
		},200);		

		$(x).animate({
			'width':'35px',
			'height':'100%',
		},200);

		removeStates();

		return state = false;

	};

	function returnSlide(){
		$("#heart").animate({
			'width':'35px',
			'height':'100%',
		},300);
		$("#laugh").animate({
			'width':'35px',
			'height':'100%',
		},300);
		$("#cry").animate({
			'width':'35px',
			'height':'100%',
		},300);


		
		

		$("#comment").css('background-image','url("images/i/commentLove.png")');

		return commentState = false;
	}

	function returnComment(){
		$("#0002").animate({
			// 'width':'0px',
			'height':'0px',
		},800);

		setTimeout(function(){
			$("#0002").hide();
			$("#0001").show();
		},800);
		setTimeout(function(){
			$("#0001").animate({
				'width':'100%',
				'height':'100%',
			},800);
		},800);

		returnSlide();

		return commentState = false;
	}





	// EMOTICON CLICKS



	// HEART CLICK

	$("#heart").click(function(){
		if(heartState === true){
			return shrinkem('#heart', heartState);
		}
		removeStates();
		$("#heart").animate({
			'width':'40px',
			'height':'100% + 5px',
		},200);

		$("#heart").css('background-image','url("images/i/loveFireFilled.png")');

		$("#heart").animate({
			'width':'35px',
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
			'width':'40px',
			'height':'100% + 5px',
		},200);

		$("#laugh").css('background-image','url("images/i/laughFilled.png")');

		$("#laugh").animate({
			'width':'35px',
			'height':'100%',
		},200);

		return laughState = true;

		// SEND JSON DATA TO SERVER HERE FOR CLICK
	});

	// CRY LIKE

	$("#cry").click(function(){
		if(cryState === true){
			return shrinkem('#cry', cryState);
		}
		removeStates();
		$("#cry").animate({
			'width':'40px',
			'height':'100% + 5px',
		},200);

		$("#cry").css('background-image','url("images/i/cryFilled.png")');

		$("#cry").animate({
			'width':'35px',
			'height':'100%',
		},200);

		return cryState = true;

		// SEND JSON DATA TO SERVER HERE FOR CLICK
	});

	// COMMENT CLICKED

	$("#comment").click(function(){

		if(commentState === true){
			return returnComment();
		}
		$("#heart").animate({
			'width':'0px',
			'height':'0%',
		},300);
		$("#laugh").animate({
			'width':'0px',
			'height':'0%',
		},300);
		$("#cry").animate({
			'width':'0px',
			'height':'0%',
		},300);
		$("#0002").show();
		$("#0002").animate({
				'height':'100%',
			},0);
		
		

		

		$("#comment").css('background-image','url("images/i/commentLoveFilled.png")');

		// $("#0002").show();
		




		return commentState = true;
	});


})