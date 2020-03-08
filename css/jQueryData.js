$(function(){

	$("#loginDiv").hide();
	$('#login').click(function(){
		$('#slogan').hide();
		$("#loginDiv").show();
		$('.tMain').css('display','block');
		$(":header").css('display','inline-block');
	});
	// $(".tMain").click(function(){
	// 	$("#loginDiv").hide();
	// 	$('#slogan').show();
	// 	$('.tMain').css('display','flex');
	// 	$(":header").css('display','flex');

	// });
})