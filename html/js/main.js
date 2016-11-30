function doCreate(form)
{
    var xhttp=new XMLHttpRequest();
    var username=form.usernamebox.value;
    var password=form.passwordbox.value;

    xhttp.onreadystatechange= function() {
            //var resptag=document.getElementById("loginresp");

            if(this.readyState==4 && this.status==200)
            {
                //var jobj=JSON.parse(this.responseText);
                //resptag.innerHTML="Session id: "+jobj['sessionid'];
            }

            else if(this.status==400)
            {
                //resptag.innerHTML="Invalid username/password.";
            }
        }

    xhttp.open("PUT", "/cgi-bin/login/"+username+"/"+password, true);
    xhttp.send();
    //alert("You typed "+username+", "+password);
}

$(document).ready(function(){


  //------------------------------------//
  //Navbar//
  //------------------------------------//
    	var menu = $('.navbar');
    	$(window).bind('scroll', function(e){
    		if($(window).scrollTop() > 140){
    			if(!menu.hasClass('open')){
    				menu.addClass('open');
    			}
    		}else{
    			if(menu.hasClass('open')){
    				menu.removeClass('open');
    			}
    		}
    	});


  //------------------------------------//
  //Scroll To//
  //------------------------------------//
  $(".scroll").click(function(event){
  	event.preventDefault();
  	$('html,body').animate({scrollTop:$(this.hash).offset().top}, 800);

  });

  //------------------------------------//
  //Wow Animation//
  //------------------------------------//
  wow = new WOW(
        {
          boxClass:     'wow',      // animated element css class (default is wow)
          animateClass: 'animated', // animation css class (default is animated)
          offset:       0,          // distance to the element when triggering the animation (default is 0)
          mobile:       false        // trigger animations on mobile devices (true is default)
        }
      );
      wow.init();



});
