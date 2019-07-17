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
        $$("st1").onmouseover = function() {
            $$("st2").style.display = "";
            $$("st1").className = "select select_hover"
        };
        $$("st1").onmouseout = function() {
            $$("st2").style.display = "none";
            $$("st1").className = "select"
        };
        $$("map-s1").onclick = function() {
            selSubSearch(1);
            $$("q").focus()
        };
        $$("map-s2").onclick = function() {
            selSubSearch(2);
            $$("q").focus()
        };
        $$("map-s3").onclick = function() {
            selSubSearch(3);
            $$("q").focus()
        };
        $$("map-s4").onclick = function() {
            selSubSearch(4);
            $$("q").focus()
        };
        $$("map-s5").onclick = function() {
            selSubSearch(5);
            $$("q").focus()
        };
        $$("map-s6").onclick = function() {
            selSubSearch(6);
            $$("q").focus()
        };
        $$("map-s7").onclick = function() {
            selSubSearch(7);
            $$("q").focus()
        };
        $$("map-s8").onclick = function() {
            selSubSearch(8);
            $$("q").focus()
        };
        $$("map-s9").onclick = function() {
            selSubSearch(9);
            $$("q").focus()
        };
        $$("map-s10").onclick = function() {
            selSubSearch(10);
            $$("q").focus()
        };
        $$("map-s11").onclick = function() {
            selSubSearch(11);
            $$("q").focus()
        };
        $$("map-s12").onclick = function() {
            selSubSearch(12);
            $$("q").focus()
        };
    };

    function selSubSearch(iType) {
        hbb = [];
        hbb = {
				1 : ["传真机", "5"],
				2 : ["电话单机", "8"],
				3 : ["电热水器", "9"],
				4 : ["复印机", "9"],
				5 : ["激光打印机", "12"],
				6 : ["监视器", "13"],
				7 : ["喷墨打印机", "7"],
				8 : ["燃气热水器", "10"],
				9 : ["吸油烟机", "10"],
				10 : ["针式打印机", "10"]
        };
        $$("map-s0").innerHTML = hbb[iType][0];
        $$("st2").style.display = "none";
        SetCookie('sousuosss', iType);
        $$("catid").value = hbb[iType][1];
    };
    initHead();
})();

hbb = [];
hbb = {
				1 : ["传真机", "5"],
				2 : ["电话单机", "8"],
				3 : ["电热水器", "9"],
				4 : ["复印机", "9"],
				5 : ["激光打印机", "5"],
				6 : ["监视器", "13"],
				7 : ["喷墨打印机", "7"],
				8 : ["燃气热水器", "10"],
				9 : ["吸油烟机", "10"],
				10 : ["针式打印机", "10"]

};
if (GetCookie('sousuosss')) {
    var sss = GetCookie('sousuosss');
    $$("map-s0").innerHTML = hbb[sss][0];
    $$("catid").value = hbb[sss][1];
}


