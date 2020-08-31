b(); /* hoisted */
console.log(a); /* var instance is hoisted but not filled so - undefined */
var j = 'hello';
console.log(j); /* var instance and value known */
function b (){
    console.log('here at b');
    var bv = 50;
    console.log('j='+j); /* scope path back to global */
}
function a(){
   var av = 20;
   console.log('here at a befor b');
   b();
   console.log('here at a after b');
}
var k = a;
k(); /* execute a var */
a();
