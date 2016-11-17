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
                resptag.innerHTML="Session id: "+jobj['sessionid'];
            }

            else if(this.status==400)
            {
                resptag.innerHTML="Invalid username/password.";
            }
        }

    xhttp.open("GET", "cgi-bin/login/"+username+"/"+password, true);
    xhttp.send();
}
