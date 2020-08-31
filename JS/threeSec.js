// file threeSec.js
function wait3sec(){
   var ms = 3000 + new Date().getTime();
   while(new Date() < ms){ }
   console.log('fin 3 sec');
}

function clickH(){
    console.log('click event '+new Date().getTime());
}

document.addEventListener('click',clickH);
console.log('before 3sec');
wait3sec();
console.log('after 3sec');