# Flask_Image_Filtering
<br><br>
This is a collection of pages for a local, Flask-based site. 
<br><br>
Users are first taken to a login page.<br>
If they don't have an account they can create one which will be stored in a SQLite3 back-end.
<br><br>
The routes in app.py are written to prevent access to pages/routes without logging in<br>
e.g. by typing "/index" into the address bar.
<br><br>
A post-login main page allows users to upload image files from their computer.<br>
Once uploaded, images are returned to the browser as an img element.<br>
Javascript is then used to programmatically create buttons which are used for filter calling.<br>
Each filter POSTs to the webserver which then runs Python PIL-based code to alter the image. <br>
The filtered image is then reloaded into the browser.<br>
Post-login pages ("index.html", "filtered.html") have a logout button which reloads the login page.<br>
<br><br>
See each file for comments.
<br><br>

N.b. <br>
-currently browser cache needs to be disabled for filters to work properly<br>
(otherwise the shared name causes filtered images to be overwritten by the first iteration)
<br><br>
-passwords are only stored as plain text<br>
-there is no current support for concurrent sessions


