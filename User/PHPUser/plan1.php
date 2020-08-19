<?php
/*
file plan1.php
pja 8/9/2020
using html stuff
/* design
build page 
-w form 
--w input "name of database"
--w button "name database" and 
--w div 
build proc on button move input to div
*/
/* prepare */
include_once ("htmlStuff.php");
include_once ('papx.php');
global $Pa,$Px;
list($Pa,$Px) = pxUnpack();

$pg = mkPage($pageName,$pageLabel);
/* <!--head-begin--> <!--head-end--> <!--body-begin--> <!--body-end--> */
$fr = mkForm($_SERVER['PHP_SELF']);
$fr = str_replace('<!--hidden-->',pxHids(),$fr);
/*
<!--hidden--> <!--formBody-->
*/
$inp1 = mkTxt("name of database",$value='');
/* return(array($e,$id)) */

$but1 = mkButton("button1",'select');
/* return(array($ans,$na)) */
/* div with label */
if (getPAPX('name-of-database',$Pa,$Px) != ''){
    $div1 = mkDivL(getPAPX('name-of-database',$Pa,$Px));
} else {
    $div1 = mkDivL("selectedName");
}
/* return(array($e,$id)) */

/* assemble */
$formStuff = $inp1[0] . $but1[0] . $div1[0] ;

/* place on form */
//$fr = str_replace("<!--formBody-->",$formStuff,$fr);
/* <!--formBody--> = $formStuff */
/* place form on page */
$fr = str_replace("<!--formBody-->","</br/>".$formStuff,$fr);
$pageStuff = $fr;
$pg = str_replace("<!--body-begin-->","</br/>".$pageStuff,$pg);
/* display */
print($pg);

function sayHi(){
    print("<br/> hello ");
} //end sayHi

?>



