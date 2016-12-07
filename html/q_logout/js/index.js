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

// This function was taken from W3Schools:
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/;";
} 

function clearListCookies()
{
    var sessionid=getCookie("sessionid");
    setCookie("sessionid", "", -1);
    
    
    
    var xhttp=new XMLHttpRequest();

    xhttp.onreadystatechange= function() {
            var confirmationtext=document.getElementById("confirmationtext");

            if(this.readyState=4 && this.status==200)
            {
                window.location.href="/index.html";
            }
            else if(this.status==400)
            {
                confirmationtext.innerHTML="Error: Could not log out!";
            }
        }

    xhttp.open("DELETE", "/cgi-bin/login/"+sessionid, true);
    xhttp.send();
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
