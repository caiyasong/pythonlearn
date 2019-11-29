       //放大镜
       $(function(){
       	       //用户名显示
			var a=$.cookie("loginUser");
			console.log(a);
			if(a){
			$("#p").html("您好："+a+"用户！"+"<a class='exit'>退出</a>");
			}else{
			 $("#p").html();
			}
			$(".exit").click(function(){
				$(this).css("cursor","pointer")
				$.cookie("loginUser","",{expires:20,path:"/"})
				window.location.reload();
			})
			//同步购物车商品数量
			var b=$.cookie("cart")?JSON.parse($.cookie("cart")):[];
             $(".num_first").html(b.length);
			
       	       $("#p2").click(function(){
       	       	location.href="#";
       	       })
				var _smallImg=$("#smallimg");
				var _smallArea=$("#smallArea");
				var _bigImg=$("#bigimg");
				var _bigArea=$("#bigArea");
				_smallArea.width(_smallImg.width()/_bigImg.width()*_bigArea.width());
				_smallArea.height(_smallImg.height()/_bigImg.height()*_bigArea.height());
				var  suv=_bigImg.width()/_smallImg.width();
				_smallImg.mousemove(function(e){
					_smallArea.show();
					_bigArea.show();
					var x=e.pageX-_smallImg.offset().left-_smallArea.width()/2;
					var y=e.pageY-_smallImg.offset().top-_smallArea.height()/2;
					if(x<0){
						x=0;
					}else if(x>_smallImg.width()-_smallArea.width()){
						x=_smallImg.width()-_smallArea.width();
					}
				   if(y<0){
						y=0;
					}else if(y>_smallImg.height()-_smallArea.height()){
						y=_smallImg.height()-_smallArea.height();
					}
				  _smallArea.css({left:x,top:y});
				  _bigImg.css({left:-x*suv,top:-y*suv});
				
				})
				_smallImg.mouseleave(function(){
					_smallArea.hide();
					_bigArea.hide();
				})
			})
    
      //商品分类移入、移出
      $(function(){
		   	$("#nav_feiLei").mouseenter(function(){
		   		$(".sideNav").show();
		   		var navLit=$(".navList");
			
			navLit.mouseenter(function(){
				$(this).find("ul").show().parent().siblings().find("ul").hide();
               $(this).find("h3 a").removeClass().addClass("change").parent().parent().siblings().find("h3 a").removeClass("change")
			   $(this).find("h3").addClass("fuck").parent().siblings().find("h3").removeClass("fuck");
			});
               
			navLit.mouseleave(function(){
				$(this).find("ul").hide();
				$(this).find("h3 a").removeClass("change");
				$(this).find("h3").removeClass("fuck");
					
			})
		   	})
		   	$(".sideNav").mouseleave(function(){
		   		$(".sideNav").hide();
		   	})
		   })
          
       //加入购物车
       // $(function(){
       // 	  $(".borli span em").click(function(){
       // 	  	$(this).parent().children("em").removeClass("selected");
       // 	  	$(this).addClass("selected");
       // 	  })
//        	  $("#addShopCart").click(function() {
//        	  	     //同步购物车商品数量
//
//                 var shu = $(".borli em[class='selected']");
//                 var num = $("#txtNum").val();
//                 var goodname=$(".xuanxiang li h1").html();
//                 var goodcolor=$(".borli em[class='selected']").html();
//                 var goodprice=$(".price").html();
//                 var goodsprice=$(".sprice").html();
//                 var goodNo=$("#goodsNo").val();
//                 console.log(goodNo)
//                 console.log(goodsprice);
//
//                 var shulist = "";
//                 if ($(".borli em").length > 0) {
//                     if (shu.length > 0) {
//                         if (num > 0) {
//                             shu.each(function() {
//                                 shulist = shulist + $(this).attr("id") + "|";
//                             });
//                             var goodList=$.cookie("cart")?JSON.parse($.cookie("cart")):[];
//                               var isExit=false;
//                              for(var i=0;i<goodList.length;i++){
//                                	if(goodList[i].name==goodname&&goodList[i].color==goodcolor){
//                                		goodList[i].num=parseInt(goodList[i].num)+parseInt(num) ;
//                                		isExit=true;
//                                	}
//
//                                }
//                              if(!isExit){
//                              	var goods={
//                             	//img:"img/minP20160313145249235.jpg",
//                             	img:"/static/img/"+goodNo+".jpg",
//                             	name:goodname,
//                             	color:goodcolor,
//                             	price:goodprice,
//                             	sprice:goodsprice,
//                             	num:num
//                             }
//                             goodList.push(goods);
//                              }
//
//                             $.cookie("cart",JSON.stringify(goodList),{expires:30,path:"/"});
//                             console.log($.cookie("cart"));
//                             alert("加入购物车成功！")
// //                          window.location.reload()
//                             var b=$.cookie("cart")?JSON.parse($.cookie("cart")):[];
//                             $(".num_first").html(b.length);
// //                          console.log(b)
// //			                if(b){
// //			                $(".num_first").html(b)
// //			                }else{
// //				            $(".num_first").html(0)
// //			                 }
// //                          window.location.href="我的购物车.html";
//                         } else {
//                             alert("购买个数输入有误！");
//                             return false;
//                         }
//                     } else {
//                         alert("您还没选择属性");
//                         return false;
//                     }
//                 } else {
//                     if (num > 0) {
// //                      window.location.href = "我的购物车.html"
//                         alert("加入购物车成功！")
//                     } else {
//                         alert("购买个数输入有误！");
//                         return false;
//                     }
//                 }
//             });
//               $("#rightBuy").click(function() {
//                 var shu = $(".borli em[class='selected']");
//                 var num = $("#txtNum").val();
//                 var goodname=$(".xuanxiang li h1").html();
//                 var goodcolor=$(".borli em[class='selected']").html();
//                 var goodprice=$(".price").html();
//                 var goodsprice=$(".sprice").html();
//                 var goodNo=$("#goodsNo").val();
//                 console.log(goodsprice);
//
//                 var shulist = "";
//                 if ($(".borli em").length > 0) {
//                     if (shu.length > 0) {
//                         if (num > 0) {
//                             shu.each(function() {
//                                 shulist = shulist + $(this).attr("id") + "|";
//                             });
//                             var goodList=$.cookie("cart")?JSON.parse($.cookie("cart")):[];
//                                var isExit=false;
//                                for(var i=0;i<goodList.length;i++){
//                                	if(goodList[i].name==goodname&&goodList[i].color==goodcolor){
//                                		goodList[i].num++;
//                                		isExit=true;
//                                	}
//                                }
//                                if(!isExit){
//                             	var goods={
//                             	img:"/static/img/"+goodNo+".jpg",
//                             	name:goodname,
//                             	color:goodcolor,
//                             	price:goodprice,
//                             	sprice:goodsprice,
//                             	num:num
//                             }
//                             goodList.push(goods);
//                             }
//                             $.cookie("cart",JSON.stringify(goodList),{expires:30,path:"/"});
//                             console.log($.cookie("cart"));
//                          window.location.href="我的购物车.html";
//                         } else {
//                             alert("购买个数输入有误！");
//                             return false;
//                         }
//                     } else {
//                         alert("您还没选择属性");
//                         return false;
//                     }
//                 } else {
//                     if (num > 0) {
//                       // window.location.href = "我的购物车.html"
//                         alert("加入购物车成功！")
//                     } else {
//                         alert("购买个数输入有误！");
//                         return false;
//                     }
//                 }
//             });
//        })