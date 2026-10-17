let move = document.querySelector("#inside");
let btn = document.querySelector("button");

let count = 0;
btn.addEventListener("mouseenter", function () {
    btn.style.backgroundColor = "black";
});

btn.addEventListener("mouseleave", function () {
    btn.style.backgroundColor = "white";
});
move.addEventListener("click" , () =>{
    if ((count)%2==0){
        move.innerText="ON"
        move.style.transform = "translate(70px)"
        move.style.backgroundColor="aqua"
        count+=1
        
    }else{
        move.innerText="OFF"
        move.style.transform = "translate(0px)"
        move.style.color = "black"
        move.style.backgroundColor="silver"
        count+=1
        
    }

})


