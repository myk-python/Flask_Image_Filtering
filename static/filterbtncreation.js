
// Script will run as long as there is an uploaded Image.
var imgsrc =document.getElementById("filteredimg");
imgsrc=imgsrc.src;
// This is poor practice but needed because of the local hosting.
// When modifying the filepath, change 22 to the lenght of the path of the 
// folder containing the Image.
if (imgsrc.length > 22){
    var img =document.getElementById("filteredimg");
    // Arbitrary limitation of image to 70% of the inner height. 
    // Keeps images visible without altering native resolution.
    var usableheight = window.innerHeight*0.7;
    // Forced centering at element creation.
    // If the stylesheet is used instead, an empty image element is placed
    // in the window.
    img.setAttribute("Style", 
    "display:block; margin-left:auto; margin-right:auto;")
    img.height = usableheight;
    // Only worthwhile creating the filter buttons 
    // if an image is successfully displayed.
    buttoncreation();
}

function buttoncreation(){
    // filter_div allows CSS to position buttons horizontally.
    var formdiv=document.querySelector("#filter_div");
    for (i=1;i<4;i++){
        var f =i;
        var j =i;
        var k =i;
        // Creating three forms:
        // f=1, f=2, f=3.
        // Adding these to filter_div.
        // Within each form, add a hidden field
        // with the relevant filter number value 
        // (e.g. Filter_1).
        var f =document.createElement("form");
        f.setAttribute("id", "Filter_sub_"+i);
        f.setAttribute("class", "filter_btn_form");
        f.setAttribute("action", "/filtered");
        f.setAttribute("method", "POST");
        document.querySelector("#filter_div").appendChild(f);
        var j =document.createElement("input");
        var k = document.createElement("input");
        j.setAttribute("type", "submit");
        k.setAttribute("type","hidden");
        k.setAttribute("name", "Filter_"+i);
        k.setAttribute("value", "Filter_"+i);
        
        // Naming the specific submit buttons.
       

        if (i==1){
            
            j.value="GREYSCALE";
            document.querySelector("#Filter_sub_"+i).appendChild(k);
            document.querySelector("#Filter_sub_"+i).appendChild(j);

        }
        else if (i==2){
           
            j.value="SEPIA";
            document.querySelector("#Filter_sub_"+i).appendChild(k);
            document.querySelector("#Filter_sub_"+i).appendChild(j);
        }
        else if (i==3){
            
            j.value="REVERT";
            document.querySelector("#Filter_sub_"+i).appendChild(k);
            document.querySelector("#Filter_sub_"+i).appendChild(j);
        }
        
        
    }
}