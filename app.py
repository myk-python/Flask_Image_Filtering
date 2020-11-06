
from flask import Flask, request, render_template
from PIL import Image

# This could be more modular but works for now.
# Filter_1 is Greyscale, Filter_2 is Sepia.
def filterfn (filtertype,filename):
    
    if filtertype =="Filter_1":
        img = Image.open(filename)
        img = img.convert(mode="L")
        # Allows name appending whilst preserving extension.
        newname =filename[0:-4]+"_filtered"+filename[-4:]
        img.save(newname)
    
    elif filtertype=="Filter_2":
        img = Image.open(filename)
        img = img.convert(mode="L")
        # Create a sepia palette and attach it to the greyscaled image.
        pixel_grad = []
        r, g, b = 255,210,180
        for i in range(255):
            pixel_grad.extend((int(r*i/255), int(g*i/255), int(b*i/255)))

        newname =filename[0:-4]+"_filtered"+filename[-4:]
        img.putpalette(pixel_grad)
        img =img.convert("RGB")
        img.save(newname)
    

app = Flask(__name__)
# Try to disable browser cache to prevent overwriting of filtered images.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/", methods=["GET"])
def index():
    
    return render_template("index.html", IMGSRC='')
    

@app.route('/', methods=["POST"])
def uploading():
    
    # Not a secure method to get the file.
    # Use Werkzeug secure filename instead.
    # Should also ensure that file extension is in an allowed list.
    og =request.files['image'] 
    global ogfilename
    # Prevent spaces from breaking file handeling.
    ogfilename = og.filename.replace(' ','_')
    og.save(og.filename)
    xtn = og.filename[-3:]

    with open(og.filename, 'rb') as img:
        content = img.read()
    global saveloc
    # Put username below. 
    # On a webserver the path can be changed as needed.
    saveloc ='C:/Users/{USERNAME}/Desktop/VSCode/Flask_Image_Filter/static/imgs/'+ogfilename[0:-3]+xtn
    
    # This is creating a new image based on the upload. 
    # If permissions on the webserver are set properly, 
    # this is unnecessary.
    with open(saveloc, 'wb') as fimg:
        fimg.write(content)
    
    filename= ogfilename[0:-3]+xtn
    imgsrc ="/static/imgs/"+filename

    return render_template("index.html", IMGSRC=imgsrc)

# This route goes to an identical page to the index page but 
# includes the loaded img element. 
# If this page isn't separated, the img element leaves a
# failed upload box on the screen.

@app.route("/filtered", methods=["POST"])
def filtering():
    # Each filter type(e.g. greyscale, sepia) is associated with a hidden form.
    # Access each one through a loop.
    for i in range(1,4):
        filtertype = str(request.form.get("Filter_"+str(i)))
        # Allows dynamic activation of one filter at a time.
        if "None" not in filtertype:
            # Allows reversion of changes to image by leaving original unaltered.
            # If filters are added, will need to ammend to the relevent number 
            # (e.g. no. filters +1).
            if "3" not in filtertype:
                # Calls the filter function defined earlier.
                filterfn(filtertype, saveloc)
                imgsrc = "/static/imgs/"+ogfilename[0:-4]+"_filtered"+ogfilename[-4:]
            else:
                imgsrc = "/static/imgs/"+ogfilename
                
    

    return render_template("filtered.html", IMGSRC=imgsrc)


