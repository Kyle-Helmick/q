
// This function was taken from W3Schools:
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
} 

function doLogin(form)
{
    var xhttp=new XMLHttpRequest();
    var username=form.usernamebox.value;
    var password=form.passwordbox.value;

    xhttp.onreadystatechange= function() {
            var resptag=document.getElementById("loginresp");

            if(this.readyState=4 && this.status==200)
            {
                var jobj=JSON.parse(this.responseText);
                resptag.innerHTML="Logged in successfully!"+jobj['sessionid'];
		
		setCookie("sessionid", jobj['sessionid'], 1);
		
		// Redirect users to their q on session creation:
		window.location.href="/q_bootstrap_todo/index.html";
            }
            else if(this.status==400)
            {
                resptag.innerHTML="Invalid username/password.";
            }
        }

    xhttp.open("GET", "/cgi-bin/login/"+username+"/"+password, true);
    xhttp.send();
}
