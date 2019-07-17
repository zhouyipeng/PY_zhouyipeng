// JavaScript Document
//注册窗口弹窗，
document.write('<style>');
document.writeln(".regist_a {background: none repeat scroll 0 0 #444444;display: none;height: 100%;left: 0;opacity: 0.9;position: absolute;top: 0;width: 100%;z-index: 2147483647;}");
document.writeln(".registFrame_a {display: none;height:600px;left: 50%;margin-left: -200px;margin-top:-280px;overflow: hidden;position:fixed;_position: absolute;top: 50%;width:405px;z-index: 2147483647;_top: expression(documentElement.scrollTop);_margin-top:0;}");
document.writeln(".registFrame_a h3 {background:url(images/login_1.png) center no-repeat;font-weight: bold;height: 63px;line-height: 63px;margin: 0;padding: 0 30px;}");
document.writeln(".registFrame_a h3 span {color: #808080;cursor: pointer;float: right;font-size: 20px; }");
document.writeln("#iframeNote_a {height: 100%;overflow: hidden;width: 100%;}");
document.write('</style>');
	var html='<div id="regist_a" class="regist_a"></div>'+
'<div id="registFrame_a" class="registFrame_a">'+
'	<h3><span onclick="registColos_a()">×</span>帐户注册</h3>'+
'   <iframe id="iframeNote" frameborder="0" scrolling="no" src="5注册a.html" ></iframe>'+
'</div>';
document.write(html);

var temp_h1 = document.body.clientHeight;
var temp_h2 = document.documentElement.clientHeight;
var isXhtml = (temp_h2<=temp_h1&&temp_h2!=0)?true:false; 
var htmlbody = isXhtml?document.body:document.documentElement;

function regist_a(){
	htmlbody.style.overflow = "hidden";
	htmlbody.scrollTop=0;
	window.scrollTo(0,0);
	document.getElementById("regist_a").style.display="block";
	document.getElementById("regist_a").style.height="3000px";
	document.getElementById("registFrame_a").style.display="block" ;
	document.getElementById("fo_a").style.display="none";//关闭登录窗口
	document.getElementById("RTfloat_a").style.display="none";//关闭登录窗口
}

function registColos_a(){ 
    document.getElementById("regist_a").style.display="none" ;
	document.getElementById("registFrame_a").style.display="none" ;
	htmlbody.style.overflow = "auto";
	document.getElementById("RTfloat_a").style.display="block";//开启登录窗口
}
/***********************/
//注册窗口弹窗，
document.write('<style>');
document.writeln(".regist_b {background: none repeat scroll 0 0 #444444;display: none;height: 100%;left: 0;opacity: 0.9;position: absolute;top: 0;width: 100%;z-index: 2147483647;}");
document.writeln(".registFrame_b {display: none;height:540px;left: 50%;margin-left: -200px;margin-top:-280px;overflow: hidden;position:fixed;_position: absolute;top: 50%;width:405px;z-index: 2147483647;_top: expression(documentElement.scrollTop);_margin-top:0;}");
document.writeln(".registFrame_b h3 {background:url(images/login_1.png) center no-repeat;font-weight: bold;height: 63px;line-height: 63px;margin: 0;padding: 0 30px;}");
document.writeln(".registFrame_b h3 span {color: #808080;cursor: pointer;float: right;font-size: 20px; }");
document.writeln("#iframeNote_b {height: 100%;overflow: hidden;width: 100%;}");
document.write('</style>');
	var html='<div id="regist_b" class="regist_b"></div>'+
'<div id="registFrame_b" class="registFrame_b">'+
'	<h3><span onclick="registColos_b()">×</span>帐户注册</h3>'+
'   <iframe id="iframeNote" frameborder="0" scrolling="no" src="5注册b.html" ></iframe>'+
'</div>';
document.write(html);

var temp_h1 = document.body.clientHeight;
var temp_h2 = document.documentElement.clientHeight;
var isXhtml = (temp_h2<=temp_h1&&temp_h2!=0)?true:false; 
var htmlbody = isXhtml?document.body:document.documentElement;

function regist_b(){
	htmlbody.style.overflow = "hidden";
	htmlbody.scrollTop=0;
	window.scrollTo(0,0);
	document.getElementById("regist_b").style.display="block";
	document.getElementById("regist_b").style.height="3000px";
	document.getElementById("registFrame_b").style.display="block" ;
	document.getElementById("fo_b").style.display="none";//关闭登录窗口
	document.getElementById("RTfloat_b").style.display="none";//关闭登录窗口
}

function registColos_b(){ 
    document.getElementById("regist_b").style.display="none" ;
	document.getElementById("registFrame_b").style.display="none" ;
	htmlbody.style.overflow = "auto";
	document.getElementById("RTfloat_b").style.display="block";//开启登录窗口
}
/***********************/
//注册窗口弹窗，
document.write('<style>');
document.writeln(".regist_c {background: none repeat scroll 0 0 #444444;display: none;height: 100%;left: 0;opacity: 0.9;position: absolute;top: 0;width: 100%;z-index: 2147483647;}");
document.writeln(".registFrame_c {display: none;height:315px;left: 50%;margin-left: -200px;margin-top:-280px;overflow: hidden;position:fixed;_position: absolute;top: 50%;width:405px;z-index: 2147483647;_top: expression(documentElement.scrollTop);_margin-top:0;}");
document.writeln(".registFrame_c h3 {background:url(images/login_1.png) center no-repeat;font-weight: bold;height: 63px;line-height: 63px;margin: 0;padding: 0 30px;}");
document.writeln(".registFrame_c h3 span {color: #808080;cursor: pointer;float: right;font-size: 20px; }");
document.writeln("#iframeNote_c {height: 100%;overflow: hidden;width: 100%;}");
document.write('</style>');
	var html='<div id="regist_c" class="regist_c"></div>'+
'<div id="registFrame_c" class="registFrame_c">'+
'	<h3><span onclick="registColos_c()">×</span>帐户注册</h3>'+
'   <iframe id="iframeNote" frameborder="0" scrolling="no" src="5注册c.html" ></iframe>'+
'</div>';
document.write(html);

var temp_h1 = document.body.clientHeight;
var temp_h2 = document.documentElement.clientHeight;
var isXhtml = (temp_h2<=temp_h1&&temp_h2!=0)?true:false; 
var htmlbody = isXhtml?document.body:document.documentElement;

function regist_c(){
	htmlbody.style.overflow = "hidden";
	htmlbody.scrollTop=0;
	window.scrollTo(0,0);
	document.getElementById("regist_c").style.display="block";
	document.getElementById("regist_c").style.height="3000px";
	document.getElementById("registFrame_c").style.display="block" ;
	document.getElementById("fo_c").style.display="none";//关闭登录窗口
	document.getElementById("RTfloat_c").style.display="none";//关闭登录窗口
}

function registColos_c(){ 
    document.getElementById("regist_c").style.display="none" ;
	document.getElementById("registFrame_c").style.display="none" ;
	htmlbody.style.overflow = "auto";
	document.getElementById("RTfloat_c").style.display="block";//开启登录窗口
}