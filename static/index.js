console.log("hello world");

const button=document.getElementById('button');
const input=document.getElementById('input')
console.log(input)


// button.onclick=()=>{
//     if(input.value===''){
//         alert("please fill form correctly.");
    
//     }
//     else{
//         console.log("successfully submited")
//     }
// }

const info=document.getElementById("btn");
const close=document.getElementById("close");
const sidebar=document.getElementById("sidebar");

info.addEventListener('click',function open(){
    console.log("opend");
    sidebar.style.right=`0px`;
    sidebar.style.display='inline';
    sidebar.style.transition=`0.5s`;
});

close.addEventListener("click",function closed(){
    console.log("closed");
    sidebar.style.transition=`0.5s`;
    sidebar.style.right=`-200%`;
    // sidebar.style.display='none';
    
    
})


const closelogo=document.getElementById("closelogo");
const message=document.getElementById("message");

closelogo.addEventListener("click",function msgclose(){
    
    message.style.display="none";
    console.log("message close");
});

var a=setTimeout(function msgclose(){
    message.style.display="none";
    message.style.transition=`0.5s`;
    clearTimeout(a);
},8000);



