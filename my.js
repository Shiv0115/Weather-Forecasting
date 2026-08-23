function myClickFunction(){       
        var elementName = document.getElementById("click-demo");  

        if (elementName.style.fontStyle != "italic"){ 
            elementName.style.fontStyle = "italic"; 
        } 
        else{ 
            elementName.style.fontStyle = "normal"; 
        } 
    } 