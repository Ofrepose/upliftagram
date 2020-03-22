$(function(){

	$("#loginDiv").hide();
	$("#suDiv").hide();
	$('#login').click(function(){
		$('#slogan').hide();
		$("#loginDiv").show();
		$('.tMain').css('display','block');
		$(":header").css('display','inline-block');
	});

	$("#signup").click(function(){
		$('#slogan').hide();
		$("#suDiv").show();
		$('.tMain').css('display','flex');
		$(":header").css('display','inline-block');
	})

	$("#createAccount").click(function(){
		$("#suForm").submit();
	})

	// $(".tMain").click(function(){
	// 	if($("#slogan").css('display','none')){
	// 		$('#slogan').show();
	// 		$("#loginDiv").hide();
	// 		$('.tMain').css('display','flex');
	// 		$(":header").css('display','flex');	
	// 	}
		
	// })
	// $(".tMain").click(function(){
	// 	$("#loginDiv").hide();
	// 	$('#slogan').show();
	// 	$('.tMain').css('display','flex');
	// 	$(":header").css('display','flex');

	// });
})