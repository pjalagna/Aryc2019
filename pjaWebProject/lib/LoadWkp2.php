<?php
// file LoadWkp2.php
// pja 12-18-2018
// URL is a hack 
// --- need to use zDAO getPicURL(cat,ix)
// --- profile.txt needs full path from main per url
// click send you to bigPix(cat,ix)
// move to main dir change all URL calls to inc $URL[0].
function LoadWkp2Main($cat,$ix,$width) {
logg('lpwk2 begin');
include_once 'LocalIniStuff.php'; //local
global $libLoc;
$libLoc = getLini('libLoc');
include_once ($libLoc . 'dispT.php');
$ans = displayTable($cat,$width);
return($ans);
}//
?>