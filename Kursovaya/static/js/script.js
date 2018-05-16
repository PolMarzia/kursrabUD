var flag = true;
var state = 0;
$(document).ready(function(){
	$(".stud").css("display","none");
	$(".form-body").css("display","none");
	$(".prep").css("display","none");
	$(".left").click(function(){
		if(flag){
			$(".stud").css("display","block");
			$(".form-body").css("display","block");
			$(".prep").css("display","block");
			flag = false
		}
		$(".prep").hide();
		$(".stud").show();
		$(".form-section").css("text-align","left");
		state = 1
	})
	$(".right").click(function(){
		if(flag){
			$(".stud").css("display","block");
			$(".form-body").css("display","block");
			$(".prep").css("display","block");
			flag = false
		}
		$(".stud").hide();
		$(".prep").show();
		$(".form-section").css("text-align","right");
		state = 2
	})
	$(".button").click(function(){
		$(".main-header").css("min-height","40vh");
		$(".header-title1").css("padding-top","30px");
		$(".header-title2").fadeOut(200);
		$(".form-body").fadeIn();
	})
})