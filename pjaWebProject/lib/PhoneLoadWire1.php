<?php
# file PhoneLoadWire1.php
/*
pja 3/20/2019 converted to db
pja 12/31/2018
pja 12-13-2018  not completed


*/
function PDoloadWire1($width) {
// phone version just image for pic
include_once 'LocalIniStuff.php'; //local
$libLoc = getLini('libLoc');
$db = getLini('dbn');
$picloc = getLini('picLoc');
logg('picloc=('.$picloc.")");
include_once ($libLoc .'fin.php');
include_once ($libLoc .'strParser.php');
include_once ($libLoc .'zDAOPDO.php');
include_once ($libLoc .'iniStuff.php');
include_once ($libLoc .'PicStuff.php');

$Screen = 'Page1-phone';
// get catmax

$cat = rand(1 ,2);
$cat = 1; //test
// get ix max of cat
$ix = rand(1 ,12);
$ix = 3; //test
// set db according to ini
//$catLoc = getXByCatIx("catDir",$cat,$ix);
$url = zByCatIx($db,"picURL",$cat,$ix);
$picPath = $url;
logg('picpath =(' . $picPath .")<br/>");
// wire1 needs detX,cat,ix,picURL, statement
// use dx dy * 7
$factor = 1000;
list($rawW,$rawH) = getPicHW($picPath);
list($dh,$dw) = getPicDhDw($rawW,$rawH,$factor);
$statement = zByCatIx($db,'SeriesStatement',$cat,0) ;
// get phonepic.html to wire
$wire1 = fin($libLoc . 'phonepic.html');
# substitutes
// dx
$wire1 = str_replace('%dx%',$dw,$wire1);
// dy
$wire1 = str_replace('%dy%',$dh,$wire1);
#cat
$wire1 = str_replace('%cat%',$cat,$wire1);
#ix,
$wire1 = str_replace('%ix%',$ix,$wire1);
#picURL
$wire1 = str_replace('%picURL%',$picPath,$wire1);
$wire1 = str_replace('%width%',$width,$wire1);
logg('plw1-ret=(' . $wire1 . ")");
return($wire1);
} #loadWire1
?>
