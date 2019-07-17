//��¼���ڵ�����
document.write('<style>');
document.writeln(".code {background: #000;display: none;height: 100%;left: 0;opacity: 0.8;position: absolute;top: 0;width: 100%;z-index: 2147483647;}");
document.writeln(".codeFrame {display: none;height:950px;left: 50%;margin-left: -450px;margin-top:-150px;overflow: hidden;position:fixed;_position: absolute;top: 35%;width:910px;z-index: 2147483647;_top: expression(documentElement.scrollTop);_margin-top:0;}");
document.writeln(".codeFrame h3 {background:#FFF;font-weight: bold;height: 63px;line-height: 63px;margin: 0 auto;padding: 0 30px; width:440px;}");
document.writeln(".codeFrame h3 span {color: #808080;cursor: pointer;float: right;font-size: 20px; }");
document.writeln("#iframeNote {height: 100%;overflow: hidden;width: 100%;}");
document.write('</style>');
	var html='<div id="code" class="code"></div>'+
'<div id="codeFrame" class="codeFrame">'+
'	<h3><span onclick="codeColos()">关闭</span></h3>'+
'   <iframe id="iframeNote" frameborder="0" scrolling="no" src="code.html" ></iframe>'+
'</div>';
document.write(html);

var temp_h1 = document.body.clientHeight;
var temp_h2 = document.documentElement.clientHeight;
var isXhtml = (temp_h2<=temp_h1&&temp_h2!=0)?true:false; 
var htmlbody = isXhtml?document.body:document.documentElement;

function codeShow(){
	htmlbody.style.overflow = "hidden";
	htmlbody.scrollTop=0;
	window.scrollTo(0,0);
	document.getElementById("code").style.display="block";
	document.getElementById("code").style.height="3000px";
	document.getElementById("codeFrame").style.display="block" ;
	document.getElementById("fo").style.display="none";//�رյ�¼����
	document.getElementById("RTfloat").style.display="none";//�رյ�¼����
}

function codeColos(){ 
    document.getElementById("code").style.display="none" ;
	document.getElementById("codeFrame").style.display="none" ;
	htmlbody.style.overflow = "auto";
	document.getElementById("RTfloat").style.display="block";//������¼����
}

/****************/
document.write('<style>');
document.writeln(".ioscode {background: #000;display: none;height: 100%;left: 0;opacity: 0.8;position: absolute;top: 0;width: 100%;z-index: 2147483647;}");
document.writeln(".ioscodeFrame {display: none;height:950px;left: 50%;margin-left: -450px;margin-top:-150px;overflow: hidden;position:fixed;_position: absolute;top: 35%;width:910px;z-index: 2147483647;_top: expression(documentElement.scrollTop);_margin-top:0;}");
document.writeln(".ioscodeFrame h3 {background:#FFF;font-weight: bold;height: 63px;line-height: 63px;margin: 0 auto;padding: 0 30px; width:620px;}");
document.writeln(".ioscodeFrame h3 span {color: #808080;cursor: pointer;float: right;font-size: 20px; }");
document.writeln("#iosiframeNote {height: 100%;overflow: hidden;width: 100%;}");
document.write('</style>');
var html='<div id="ioscode" class="ioscode"></div>'+
    '<div id="ioscodeFrame" class="ioscodeFrame">'+
    '	<h3><span onclick="ioscodeColos()">关闭</span></h3>'+
    '   <iframe id="iframeNote" frameborder="0" scrolling="no" src="codeios.html" ></iframe>'+
    '</div>';
document.write(html);

var temp_h1 = document.body.clientHeight;
var temp_h2 = document.documentElement.clientHeight;
var isXhtml = (temp_h2<=temp_h1&&temp_h2!=0)?true:false;
var htmlbody = isXhtml?document.body:document.documentElement;

function ioscodeShow(){
    htmlbody.style.overflow = "hidden";
    htmlbody.scrollTop=0;
    window.scrollTo(0,0);
    document.getElementById("ioscode").style.display="block";
    document.getElementById("ioscode").style.height="3000px";
    document.getElementById("ioscodeFrame").style.display="block" ;
    document.getElementById("fo").style.display="none";//�رյ�¼����
    document.getElementById("iosRTfloat").style.display="none";//�رյ�¼����
}

function ioscodeColos(){
    document.getElementById("ioscode").style.display="none" ;
    document.getElementById("ioscodeFrame").style.display="none" ;
    htmlbody.style.overflow = "auto";
    document.getElementById("iosRTfloat").style.display="block";//������¼����
}

/****************/
document.write('<style>');
document.writeln(".androidcode {background: #000;display: none;height: 100%;left: 0;opacity: 0.8;position: absolute;top: 0;width: 100%;z-index: 2147483647;}");
document.writeln(".androidcodeFrame {display: none;height:950px;left: 50%;margin-left: -450px;margin-top:-150px;overflow: hidden;position:fixed;_position: absolute;top: 35%;width:910px;z-index: 2147483647;_top: expression(documentElement.scrollTop);_margin-top:0;}");
document.writeln(".androidcodeFrame h3 {background:#FFF;font-weight: bold;height: 63px;line-height: 63px;margin: 0 auto;padding: 0 30px; width:620px;}");
document.writeln(".androidcodeFrame h3 span {color: #808080;cursor: pointer;float: right;font-size: 20px; }");
document.writeln("#androidiframeNote {height: 100%;overflow: hidden;width: 100%;}");
document.write('</style>');
var html='<div id="androidcode" class="androidcode"></div>'+
    '<div id="androidcodeFrame" class="androidcodeFrame">'+
    '	<h3><span onclick="androidcodeColos()">关闭</span></h3>'+
    '   <iframe id="iframeNote" frameborder="0" scrolling="no" src="codeandroid.html" ></iframe>'+
    '</div>';
document.write(html);

var temp_h1 = document.body.clientHeight;
var temp_h2 = document.documentElement.clientHeight;
var isXhtml = (temp_h2<=temp_h1&&temp_h2!=0)?true:false;
var htmlbody = isXhtml?document.body:document.documentElement;

function androidcodeShow(){
    htmlbody.style.overflow = "hidden";
    htmlbody.scrollTop=0;
    window.scrollTo(0,0);
    document.getElementById("androidcode").style.display="block";
    document.getElementById("androidcode").style.height="3000px";
    document.getElementById("androidcodeFrame").style.display="block" ;
    document.getElementById("fo").style.display="none";//�رյ�¼����
    document.getElementById("androidRTfloat").style.display="none";//�رյ�¼����
}

function androidcodeColos(){
    document.getElementById("androidcode").style.display="none" ;
    document.getElementById("androidcodeFrame").style.display="none" ;
    htmlbody.style.overflow = "auto";
    document.getElementById("androidRTfloat").style.display="block";//������¼����
}