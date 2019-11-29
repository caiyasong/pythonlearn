//导航轮播图
  $(function(){
//	$.get("json/iFocus.json",function(dat){
//		for(var i=0;i<dat.length;i++){
//			var objstr=dat[i];
//			
//			var img=$("<img>");
//			img.attr("src",objstr.img);
//			var li=$("<li></li>");
//			
//			li.append(img);
//			$(".slider").append(li);
//			
//		}
//	})
	      var len=$(".slider li").length;
	      var index=0;
				var timer=setInterval(function(){
					index++;
					show();
				},3000);
					
			$("#slider_tab li").mouseenter(function(){
				clearInterval(timer);
				var i=$(this).index();
				index=i;
				show();
			});
			$("#slider_tab li").mouseleave(function(){
				timer=setInterval(function(){
					index++;
					show();
				},3000);
			})
				function show(){
					if(index==len){
						index=0;
					}else if(index<0){
						index=len-1;
					}
					$(".slider").find("li").eq(index).animate({opacity:1}).siblings().animate({opacity:0});
					$("#slider_tab").find("li").eq(index).addClass("tab").siblings().removeClass("tab");
				};
			
  })



//创建手机列表
$(function(){
	$.get("/static/json/phone.json",function(data){
		for(var i=0;i<data.length;i++){
			var obj=data[i];
			var ul=$("<ul></ul>");
			var li=$("<li></li>");
			var a1=$("<a></a>");
			var img=$("<img>");
			img.attr("src",obj.img);
			var p=$("<p></p>");
			var a2=$("<a>"+obj.content+"</a>");
			var b=$("<b>"+obj.price+"</b>");
			a1.append(img);
			p.append(a2);
			li.append(a1,p,b);
			ul.append(li);
			$("#phone_list").append(ul);
			
		}
	});
	// 会员促销鼠标划过
	$("#sale_bottom img").mouseenter(function(){
		 $(this).css("opacity","0.6").siblings().css("opacity","1");
	})
	$("#sale_bottom img").mouseleave(function(){
		$(this).css("opacity","1");
	})
	})
	//礼品箱包轮播图
	       $(function(){
	      var index=0;
				var len=$("#box_bottom").find("a").length;
			
				var timer=setInterval(function(){
					index++;
					show();
				},3000);
				function show(){
					if(index==len){
						index=0;
					}else if(index<0){
						index=len-1;
					}
					$("#box_bottom").find("a").eq(index).animate({opacity:1}).siblings().animate({opacity:0});
				}
	          })
	            
	//服饰鞋帽轮播图
	           $(function(){
	           	  var i=0;
				var len=$("#bottom_left").find("a").length;
			
				var timer=setInterval(function(){
					i++;
					show();
				},4000);
				function show(){
					if(i==len){
						i=0;
					}else if(i<0){
						i=len-1;
					}
					$("#bottom_left").find("a").eq(i).animate({opacity:1}).siblings().animate({opacity:0});
				}
	           })
	             
	//个护化妆轮播图
	         $(function(){
	         	 var index=0;
				var len=$("#dressImg").find("a").length;
			
				var timer=setInterval(function(){
					index++;
					show();
				},4000);
				function show(){
					if(index==len){
						index=0;
					}else if(index<0){
						index=len-1;
					}
					$("#dressImg").find("a").eq(index).animate({opacity:1}).siblings().animate({opacity:0});
				} 
	         })
	           

