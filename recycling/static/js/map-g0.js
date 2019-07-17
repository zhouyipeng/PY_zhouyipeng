// search
//获得Cookie解码后的值
function GetCookieVal(offset) {
    var endstr = document.cookie.indexOf(";", offset);
    if (endstr == -1) endstr = document.cookie.length;
    return unescape(document.cookie.substring(offset, endstr));
}
//设定Cookie值-将值保存在Cookie中
function SetCookie(name, value) {
    var expdate = new Date(); //获取当前日期
    var argv = SetCookie.arguments; //获取cookie的参数
    var argc = SetCookie.arguments.length; //cookie的长度
    var expires = (argc > 2) ? argv[2] : null; //cookie有效期
    var path = (argc > 3) ? argv[3] : null; //cookie路径
    var domain = (argc > 4) ? argv[4] : null; //cookie所在的应用程序域
    var secure = (argc > 5) ? argv[5] : false; //cookie的加密安全设置
    if (expires != null) expdate.setTime(expdate.getTime() + (expires * 1000));
    document.cookie = name + "=" + escape(value) + ((expires == null) ? "": ("; expires=" + expdate.toGMTString())) + ((path == null) ? "": ("; path=" + path)) + ((domain == null) ? "": ("; domain=" + domain)) + ((secure == true) ? "; secure": "");
}
//删除指定的Cookie
function DelCookie(name) {
    var exp = new Date();
    exp.setTime(exp.getTime() - 1);
    var cval = GetCookie(name); //获取当前cookie的值
    document.cookie = name + "=" + cval + "; expires=" + exp.toGMTString(); //将日期设置为过期时间
}
//获得Cookie的值-name用来搜索Cookie的名字
function GetCookie(name) {
    var arg = name + "=";
    var argLen = arg.length; //指定Cookie名的长度
    var cookieLen = document.cookie.length; //获取cookie的长度
    var i = 0;
    while (i < cookieLen) {
        var j = i + argLen;
        if (document.cookie.substring(i, j) == arg) //依次查找对应cookie名的值
        return GetCookieVal(j);
        i = document.cookie.indexOf(" ", i) + 1;
        if (i == 0) break;
    }
    return null;
}

function $$(id) {
    if (document.getElementById) {
        return document.getElementById(id);
    } else if (document.layers) {
        return document.layers[id];
    } else {
        return false;
    }
} (function() {
    function initHead() {
        setTimeout(showSubSearch, 0)
    };
    function showSubSearch() {
        $$("bt1").onmouseover = function() {
            $$("bt2").style.display = "";
            $$("bt1").className = "select select_hover"
        };
        $$("bt1").onmouseout = function() {
            $$("bt2").style.display = "none";
            $$("bt1").className = "select"
        };
        $$("map-g1").onclick = function() {
            selSubSearch(1);
            $$("q").focus()
        };
        $$("map-g2").onclick = function() {
            selSubSearch(2);
            $$("q").focus()
        };
        $$("map-g3").onclick = function() {
            selSubSearch(3);
            $$("q").focus()
        };
        $$("map-g4").onclick = function() {
            selSubSearch(4);
            $$("q").focus()
        };
        $$("map-g5").onclick = function() {
            selSubSearch(5);
            $$("q").focus()
        };
        $$("map-g6").onclick = function() {
            selSubSearch(6);
            $$("q").focus()
        };
        $$("map-g7").onclick = function() {
            selSubSearch(7);
            $$("q").focus()
        };
        $$("map-g8").onclick = function() {
            selSubSearch(8);
            $$("q").focus()
        };
        $$("map-g9").onclick = function() {
            selSubSearch(9);
            $$("q").focus()
        };
        $$("map-g10").onclick = function() {
            selSubSearch(10);
            $$("q").focus()
        };
        $$("map-g11").onclick = function() {
            selSubSearch(11);
            $$("q").focus()
        };
        $$("map-g12").onclick = function() {
            selSubSearch(12);
            $$("q").focus()
        };
    };

    function selSubSearch(iType) {
        hbb = [];
        hbb = {
				1 : ["大家电", "5"],
				2 : ["小家电", "8"],
				3 : ["手机", "9"],
				4 : ["废电池", "9"],
				5 : ["废灯管", "12"],
				6 : ["废纸", "13"],
				7 : ["废塑料", "7"],
				8 : ["废铜烂铁", "10"],
				9 : ["报废汽车", "10"],
				10 : ["其他废车", "10"],
				11 : ["厨房五金", "10"],
				12 : ["其他", "10"]
        };
        $$("map-g0").innerHTML = hbb[iType][0];
        $$("bt2").style.display = "none";
        SetCookie('sousuosss', iType);
        $$("catid").value = hbb[iType][1];
    };
    initHead();
})();

hbb = [];
hbb = {
				1 : ["大家电", "5"],
				2 : ["小家电", "8"],
				3 : ["手机", "9"],
				4 : ["废电池", "9"],
				5 : ["废灯管", "5"],
				6 : ["废纸", "13"],
				7 : ["废塑料", "7"],
				8 : ["废铜烂铁", "10"],
				9 : ["报废汽车", "10"],
				10 : ["其他废车", "10"],
				11 : ["厨房五金", "10"],
				12 : ["其他", "10"]
};
if (GetCookie('sousuosss')) {
    var sss = GetCookie('sousuosss');
    $$("map-g0").innerHTML = hbb[sss][0];
    $$("catid").value = hbb[sss][1];
}


