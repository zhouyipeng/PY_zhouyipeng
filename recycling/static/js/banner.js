// JavaScript Document
document.writeln("<div class=\"banner_bg\">");
document.writeln("<div class=\"banner\">");
document.writeln("<div class=\"hd\">");
document.writeln("    <ul>");
document.writeln("        <li style=\"background:url(/static/images/banner1.jpg) center top no-repeat;\"><a href=\"\" target=\'_blank\'></a></li>");
document.writeln("        <li style=\"background:url(/static/images/banner2.jpg) center top no-repeat;\"><a href=\"\" target=\'_blank\'></a></li>");
document.writeln("        <li style=\"background:url(/static/images/banner3.jpg) center top no-repeat;\"><a href=\"\" target=\'_blank\'></a></li>");
document.writeln("    </ul>");
document.writeln("</div>");
document.writeln("<a class=\"prev\" href=\"javascript:void(0)\"></a><a class=\"next\" href=\"javascript:void(0)\"></a>");
document.writeln("<div class=\"bd\"><div class=\"kd\"><a class=\"prev\" href=\"javascript:void(0)\"></a> <a class=\"next\" href=\"javascript:void(0)\"></a></div>");
document.writeln("    <div class=\"bd_box\"><div class=\"bd_btn\"><ul></ul></div></div>");
document.writeln("</div>");
document.writeln("</div>");
document.writeln("</div>");
document.writeln("<div class='banner_box'>");
document.writeln("  <div class='banner_fix'>");
document.writeln("    <div class='banner_fix_1'>");
document.writeln("    <span class='yahei'>客服热线:</span> ");
document.writeln("    <p>400-866-6688</p> ");
document.writeln("    </div>");
document.writeln("    <div class='banner_fix_2'>");
document.writeln("    <dl> ");
document.writeln("       <dd> ");
document.writeln("         <a href='/scrap/'><img src='/static/images/I1_ico1.png'><div class='yahei'><strong>废品回收入口</strong></div></a> ");
document.writeln("       </dd>");
document.writeln("       <dt><img src='/static/images/I1_ico3.png'></dt> ");
document.writeln("       <dd> ");
document.writeln("         <a href='/overorder/'><img src='/static/images/I1_ico2.png'><div class='yahei'><strong>我要做回收哥</strong></div></a> ");
document.writeln("       </dd>");
document.writeln("    </dl>");
document.writeln("   </div>");
document.writeln(" </div>");
document.writeln("</div>");


oxbix_changes (".banner", ".hd", ".bd", 8000);
$(window).resize(function() { re_ban();});
re_ban()

// 图片切换效果
function oxbix_changes (boxCell, mainCell, numCell, times) {
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
