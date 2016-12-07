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

function clearListCookies()
{
	document.cookie = "sessionid="+getCookie("sessionid")+";expires=Thu, Jan 1970 00:00:00 GMT;"+"domain="+document.domain+";path=/";
}

window.onload=function()
{
	sessionid=getCookie("sessionid");
	console.log("Session id is: " + sessionid);
	if(sessionid == "") {
		console.log("its empty fam");
	}
	else
	{
		console.log("its not empty fam");
	}
}
