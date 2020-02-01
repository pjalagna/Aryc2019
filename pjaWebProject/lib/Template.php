<?php
# template.php
/*
pja 3/20/2019 converted to db
pja 3/12/2019 removed footer 
*/
function Template_main($width){
include_once 'LocalIniStuff.php'; // callers local
$libLoc = getLini('libLoc'); // callers local file
$picLoc = getLini('picLoc');
include_once ($libLoc.'fin.php');
include_once ($libLoc.'llogg.php');
logg('template.php begin');
include_once ($libLoc.'zDAOPDO.php');
$ans = '';
$sec1 = <<< sec1
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html><head>
<!-- page width 1250 -->
</head><body>

<div  style="border: medium none ;" height="100" width="1250">
sec1
;
$ans = $ans . $sec1;
$bx = fin("banner.html");
$bx = str_replace('%picLoc%', $picLoc,$bx);
$ans = $ans . $bx;
$ans = $ans . '</div>';
# work area
$sec2 = <<< sec2
<table>
<tr><td>
<div  style="border: medium none ;" height="700" width="30%">
sec2
;
$ans = $ans . $sec2;
include_once ($libLoc .'tocT.php'); // genTOC to $toc

$ans = $ans . doTocT($width) ; 

$ans = $ans . '</div></td>';

$sec3 = <<< sec3
<td>
<div  style="border: medium none ;" height="700" width="700">
sec3
;
$ans = $ans . $sec3;
$ans = $ans . '#%wk%';
$ans = $ans . "</div></td></tr></table>";
$ans = $ans . "</body></html>";
return($ans);

} # main
