import { Component } from '@angular/core';
@Component({
  selector: 'my-app',
  template: `
	<div class='frontpage'>
	  <h1>
	    q - A Life Organization App
	  </h1>
	</div>

	<div class="login">
	  <h2>Welcome!</h2>
	  <form>
	    Username:  <input type="text" name="username" /> <br>
	    Password:  <input type="text" name="password" />
	  </form>
	
	  <div class="button">
	    <a href=""><h3>Login</h3></a>
	    <a href=""><h3>Create an Account</h3></a>
	  </div>
	</div>
    `
})
export class AppComponent { }

