$(function(){

	$("#loginDiv").hide();
	$('#login').click(function(){
		$('#slogan').hide();
		$("#loginDiv").show();
		$('.tMain').css('display','block');
		$(":header").css('display','inline-block');
	});
})