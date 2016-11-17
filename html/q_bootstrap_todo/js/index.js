function doInsert(form)
{
    var sessionid=form.sessionbox.value;
    var title=encodeURIComponent(form.titlebox.value);
    var classname=encodeURIComponent(form.classbox.value);
    var content=encodeURIComponent(form.contentbox.value);
    var duedate=encodeURIComponent(form.datebox.value);
    var priority=encodeURIComponent(form.prioritybox.value);
    var xhttp=new XMLHttpRequest();

    xhttp.onreadystatechange=function(){
        var dest=document.getElementById("formaddresp");

        if(this.status==200 && this.readyState==4)
        {
            var jobj=JSON.parse(this.responseText);
            dest.innerHTML="Data added. ID: "+jobj["msgid"];
        }

        else if(this.status==400)
        {
            dest.innerHTML="Couldn't post data to server.";
        }
    }

    xhttp.open("PUT", "cgi-bin/messages/"+sessionid+"/"+priority+"/"+content+"/"+classname+"/"+duedate+"/"+title, true);
    xhttp.send();
}

function doUpdate(form)
{
    var xhttp=new XMLHttpRequest();
    var sessionid=form.sessionbox.value;
    updatesessionid=sessionid;

    xhttp.onreadystatechange=function(){
            var dest=document.getElementById("listdiv");
            var destcontent="";

            if(this.status==200)
            {
                var jobj=JSON.parse(this.responseText);
                var i=0;

                for(var key in jobj)
                {
                    var idstr=key+"id";
                    destcontent=destcontent+"<div id=\""+idstr+"\" class=\"topdiv\"><p>Object id: "+key+". Title: "+jobj[key];
                    destcontent=destcontent+" <a onclick=\"doMessage("+key+")\" href=\"javascript:void(0);\">Expand</a>";
                    destcontent=destcontent+"</p></div>\n";

                    //i++;
                }

                dest.innerHTML=destcontent;
            }

            else if(this.status==400)
            {
                dest.innerHTML="Server was unable to fulfill request. This is bad!";
            }
        }

    xhttp.open("GET", "cgi-bin/messages/"+sessionid+"/list", true);
    xhttp.send();
}

function doMessage(msgid)
{
    var idstr=msgid+"id";
    var xhttp=new XMLHttpRequest();

    xhttp.onreadystatechange=function(){
            var dest=document.getElementById(idstr);

            if(this.status==200 && this.readyState==4)
            {
                var jobj=JSON.parse(this.responseText);
                var attriblist=["text", "class", "duedate"];
                var attribname=["Text", "Class name", "Due date"];

                for(var a in attriblist)
                {
                    //Create a title element:
                    var topelem=document.createElement("p");
                    topelem.appendChild(document.createTextNode(attribname[a]+":"));

                    var elem=document.createElement("div");
                    elem.setAttribute("class", "subdiv");

                    elem.appendChild(document.createTextNode(jobj[attriblist[a]]));
                    topelem.appendChild(elem);
                    dest.appendChild(topelem);
                }
            }

            else if(this.status==400)
            {
                dest.innerHTML="Could not retrieve message from server.";
            }
        }

    xhttp.open("GET", "cgi-bin/messages/"+updatesessionid+"/"+msgid, true);
    xhttp.send();
}
