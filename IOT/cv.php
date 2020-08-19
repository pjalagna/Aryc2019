<?php
// file cv1.php
function repl($fh) {
// convert <;$//> in string 
// to *L* *C* *D* *S* *G*
str_replace("%body%", "black", "<body text='%body%'>") ;
$v1 = str_replace("<" , "*L*" , $fh) ;
$v1 = str_replace(">" , "*G*" , $v1) ;
$v1 = str_replace("$" , "<br />*D*" , $v1) ;
$v1 = str_replace(";" , " *C*<br />" , $v1) ;
$v1 = str_replace("//" , "<br />*S* " , $v1) ;
$v1 = str_replace("function" , "<br />*FN* " , $v1) ;
$v1 = str_replace("{" , "*OB*<br /> " , $v1) ;
$v1 = str_replace("}" , "<br />*CB* " , $v1) ;
return($v1);
} // end repl
?>