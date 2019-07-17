// JavaScript Document
var Public_font = {
	_id : null,
	init : function(titid, conclass, conid, boxid, nums) {
		var activenums = nums ? nums : 99;
		var cli = $("." + titid).find("li");
		cli.each ( function (index) {
			if (cli.index(this)+1 <= activenums) {
				$(this).mouseover( function (event) {
					// cli.index(this); 当前索引
					cli.each ( function () {
						$(this).removeClass(conclass);
						$("." + conid).children("." + boxid).hide();
					});
					$(this).addClass(conclass);
					var thisindex = cli.index(this)+1;
					$("." + conid + " ." + boxid + ":nth-child(" + thisindex + ")").show();
				});
			}
		});
	}
}
//Public_font.init("I1_div5", "I2_tit_now", "I1_div6", "I2_m_con", "8");  最后一个选填

// 图片选项卡切换
var Public_Images = {
	_id : null,
	init : function(titid, conclass, conid, boxid, type, nums) {
		var type = type ? type : 'jpg';
		var nums = nums ? nums : 999;
		var cli = $("." + titid).find("li");
		cli.each ( function (index) {
			$(this).mouseover( function (event) {
				// cli.index(this); 当前索引
				if (cli.index(this) < nums) {
					cli.each ( function () {
						var perobj = Public_Images.getobj(this);
						perobj.attr("src", perobj.attr("src").replace(conclass + "." + type, "." + type));
						$("." + conid).children("." + boxid).hide();
					});
					var thisobj = Public_Images.getobj(this);
					thisobj.attr("src", thisobj.attr("src").replace("." + type, conclass + "." + type));
					var thisindex = cli.index(this)+1;
					$("." + conid + " ." + boxid + ":nth-child(" + thisindex + ")").show();
				}
			});
		});
	},
	// 取得需要变化的子元素
	getobj : function (obj) {
		if ($(obj).children("a").length > 0) {
			perobj = $(obj).children("a").children("img");
		} else {
			perobj = $(obj).children("img");
		}
		return perobj;
	}
}
//Public_Images.init("I2_4", "_1", "I2_5", "I2_con");

// 图片切换效果
function bohai_changes (boxCell, mainCell, numCell, times) {
	times = times ? times : 5000;
	/*鼠标移过，左右按钮显示*/
	$(boxCell).hover(function(){
		//$(this).find(".prev,.next,.bd_btn").fadeIn(500);
		$(this).find(".bd_btn").fadeIn(500);
	},function(){
		$(this).find(".bd_btn").fadeOut(500);
	})
	$(boxCell).slide({ titCell:numCell + " ul" , mainCell:mainCell + " ul" , effect:"fold", autoPlay:true, delayTime:700 , interTime:times, autoPage:true });
}

var RecSR1 = {
	_id : null,
	init : function(titid, conclass, conid, boxid) {
		var cli = $("." + titid).find("li");
		cli.each ( function (index) {
			$(this).mouseover( function (event) {
				// cli.index(this); 当前索引
				cli.each ( function () {
					var perobj = Public_Images.getobj(this);
					perobj.attr("src", perobj.attr("src").replace(conclass + ".gif", ".gif"));
					perobj.attr("src", perobj.attr("src").replace(conclass + ".jpg", ".jpg"));
					$(this).children("div").hide();
				});
				var thisobj = Public_Images.getobj(this);
				thisobj.attr("src", thisobj.attr("src").replace(".gif", conclass + ".gif"));
				thisobj.attr("src", thisobj.attr("src").replace(".jpg", conclass + ".jpg"));
				$(this).children("div").show();
			});
		});
	},
	// 取得需要变化的子元素
	getobj : function (obj) {
		if ($(obj).children("a").length > 0) {
			perobj = $(obj).children("a").children("img");
		} else {
			perobj = $(obj).children("img");
		}
		return perobj;
	}
}


// 获得浏览器窗口尺寸
function get_window_size() {
	var winWidth;
	var winHeight;
	//获取窗口宽度 
	if (window.innerWidth) 
	winWidth = window.innerWidth; 
	else if ((document.body) && (document.body.clientWidth)) 
	winWidth = document.body.clientWidth; 
	//获取窗口高度 
	if (window.innerHeight) 
	winHeight = window.innerHeight; 
	else if ((document.body) && (document.body.clientHeight)) 
	winHeight = document.body.clientHeight; 
	//通过深入Document内部对body进行检测，获取窗口大小 
	if (document.documentElement && document.documentElement.clientHeight && document.documentElement.clientWidth) 
	{ 
	winHeight = document.documentElement.clientHeight; 
	winWidth = document.documentElement.clientWidth; 
	}
	var arr = new Array();
	arr[0] = winWidth;
	arr[1] = winHeight;

	return arr;
}

// 重设置BANNER尺寸
function re_ban () {
	var thisban = 1000;
	if (window.innerWidth) 
	winWidth = window.innerWidth; 
	else if ((document.body) && (document.body.clientWidth)) 
	winWidth = document.body.clientWidth; 
	var bodywidth = winWidth;
	$(".banner").css({"width": winWidth + "px"});
	$(".banner .hd li").css({"width": winWidth + "px"});
	$(".banner .bd").css({"width": winWidth + "px"});
}