var sessionid;

function getCookie(cname) {
	var name = cname + "=";
	var ca = document.cookie.split(';');
	for(var i = 0; i < ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') {
			c = c.substring(1);
		}
		if(c.indexOf(name) == 0) {
			return c.substring(name.length,c.length);
		}
	}

	return "";
}

window.onload=function()
{
	sessionid=getCookie("sessionid");
	console.log("Session id is: " + sessionid);
	if(sessionid == "") {
		console.log("its empty fam");
		document.getElementById("queuep").style.display = "none";
		document.getElementById("logoutp").style.display = "none";
		document.getElementById("loginp").style.display = "inline";
		document.getElementById("queued").style.display = "none";
		document.getElementById("logoutd").style.display = "none";
		document.getElementById("logind").style.display = "inline";
	}
	else
	{
		console.log("its not empty fam");
		document.getElementById("queuep").style.display = "inline";
		document.getElementById("logoutp").style.display = "inline";
		document.getElementById("loginp").style.display = "none";
		document.getElementById("queued").style.display = "inline";
		document.getElementById("logoutd").style.display = "inline";
		document.getElementById("logind").style.display = "none";

	}
}
