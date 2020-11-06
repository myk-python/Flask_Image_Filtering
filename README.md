# Flask_Image_Filtering
<br><br>
This is a collection of pages for a local, Flask-based site. 
<br><br>
A main page allows users to upload image files from their computer.<br>
Once uploaded, images are returned to the browser as an img element.<br>
Javascript is then used to programmatically create buttons which are used for filter calling.<br>
Each filter POSTs to the webserver which then runs Python PIL-based code to alter the image. <br>
The filtered image is then reloaded into the browser.
<br><br>
See each file for comments.
<br><br>
N.b. currently browser cache needs to be disabled for filters to work properly.<br>
Otherwise the shared name causes filtered images to be overwritten by the first iteration.

