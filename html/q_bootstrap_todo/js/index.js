var dialog;
var dialogCloseButton;
var sessionid;

// Taken from example function at http://www.w3schools.com/js/js_cookies.asp
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length,c.length);
        }
    }
    return "";
} 

window.onload=function()
{
    dialog=document.getElementById("newMessageBox");
    dialogCloseButton=document.getElementById("closeButton");
    
    dialogCloseButton.onclick=function()
    {
	dialog.style.display="none";
    }
    
    sessionid=getCookie("sessionid");
    doUpdate();
}

function showDialog()
{
    dialog.style.display="block";
}

function showEditDialog(msgid)
{
    var xhttp=new XMLHttpRequest();
    
    xhttp.onreadystatechange=function(){
        //var dest=document.getElementById("formaddresp");

        if(this.status==200 && this.readyState==4)
        {
            var jobj=JSON.parse(this.responseText);
            var form=document.getElementById("insertForm");
            
            form.titlebox.value=jobj['title'];
            form.contentbox.value=jobj['text'];
            form.datebox.value=jobj['duedate'];
            form.prioritybox.value=jobj['priority'];
            
            doDeleteMessage(msgid);
            showDialog();
            doUpdate();
        }

        else if(this.status==400)
        {
            //TODO: Insert code to show some kind of error message here.
        }
    }
    
    xhttp.open("GET", "/cgi-bin/messages-fast/"+sessionid+"/"+msgid);
    xhttp.send();
}

function dialogOnClick()
{
    var insertForm=document.getElementById("insertForm");
    
    doInsert(insertForm);
}

function doInsert(form)
{
    var title=encodeURIComponent(form.titlebox.value);
    var classname="none";//encodeURIComponent(form.classbox.value);
    var content=encodeURIComponent(form.contentbox.value);
    var duedate=encodeURIComponent(form.datebox.value);
    var priority=encodeURIComponent(form.prioritybox.value);
    var xhttp=new XMLHttpRequest();

    xhttp.onreadystatechange=function(){
        //var dest=document.getElementById("formaddresp");

        if(this.status==200 && this.readyState==4)
        {
	    doUpdate();
            dialog.style.display="none";
            //var jobj=JSON.parse(this.responseText);
            //dest.innerHTML="Data added. ID: "+jobj["msgid"];
        }

        else if(this.status==400)
        {
            //dest.innerHTML="Couldn't post data to server.";
        }
    }

    xhttp.open("PUT", "/cgi-bin/messages/"+sessionid+"/"+priority+"/"+content+"/"+classname+"/"+duedate+"/"+title, true);
    xhttp.send();
}

var updatesessionid;
var contentDict;

function genDestContent(key, title)
{
    var destcontent="";
    
    destcontent=destcontent+'<div class="container"><div class="row"><div class="col-sm-8 col-sm-offset-2">';
    destcontent=destcontent+"<h3>Object id: "+key+". Title: "+title;
    destcontent=destcontent+" <a onclick=\"doMessage("+key+")\" href=\"javascript:void(0);\">Expand</a>";
    destcontent=destcontent+" <a onclick=\"doCloseMessage("+key+")\" href=\"javascript:void(0);\">Collapse</a>"
    destcontent=destcontent+" <a onclick=\"doDeleteMessage("+key+")\" href=\"javascript:void(0);\">Delete</a>";
    destcontent=destcontent+" <a onclick=\"showEditDialog("+key+")\" href=\"javascript:void(0);\">Edit</a>";
    destcontent=destcontent+"</h3></div></div></div>\n";
                
    return destcontent;
}

function doUpdate()
{
    var xhttp=new XMLHttpRequest();
    updatesessionid=sessionid;

    xhttp.onreadystatechange=function(){
            

            if(this.status==200 && this.readyState==4)
            {
                var jobj=JSON.parse(this.responseText);
                contentDict=jobj;
                
                for(var key in jobj)
                {
                    var destcontent="";
                    //console.log(key);
                    var idstr=key+"id";
                    
                    var elem=document.getElementById(idstr);
                    console.log(elem);
                    
                    if(elem!=null)
                    {
                        console.log("Deleting element: "+elem);
                        elem.parentNode.removeChild(elem);
                        elem=document.getElementById(idstr);
                        console.log("After deletion: "+elem);
                    }
                    
                    var dest=document.createElement("section");//getElementById("contentContainer");
                    dest.setAttribute("class", "pad-lg light-gray-bg");
                    dest.setAttribute("id", idstr);
                    
                    destcontent=genDestContent(key, jobj[key]['title']);
                    
                    dest.innerHTML=destcontent;
                    
                    document.getElementById("contentContainer").appendChild(dest);
                    //i++;
                }

                //dest.innerHTML=dest.innerHTML+destcontent;
            }

            else if(this.status==400)
            {
                dest.innerHTML="Server was unable to fulfill request. This is bad!";
            }
        }

    xhttp.open("GET", "/cgi-bin/messages-fast/"+sessionid+"/list", true);
    xhttp.send();
}

function doCloseMessage(msgid)
{
    var elem=document.getElementById(msgid+"id");
    
    elem.innerHTML=genDestContent(msgid, contentDict[msgid]['title']);
}

function doDeleteMessage(msgid)
{
    var xhttp=new XMLHttpRequest();
    
    xhttp.onreadystatechange=function(){
        if(this.status==200 && this.readyState==4)
        {
            var elem=document.getElementById(msgid+"id");
            elem.parentNode.removeChild(elem);
            doUpdate();
        }
    }
    
    xhttp.open("DELETE", "/cgi-bin/messages/"+sessionid+"/"+msgid, true);
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

    xhttp.open("GET", "/cgi-bin/messages-fast/"+updatesessionid+"/"+msgid, true);
    xhttp.send();
}
