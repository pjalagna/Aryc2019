
<?php
# file LoadWire3.php
/*
pja 9/16/2019 added pic bio marker
pja 4/7/2019 fixed spacing of buttons
pja 4/4/2019 redid table layout
pja 3/20/2019 converted to db
pja 3/17/2019 added snaps image
pa 3/12/2019 changed window size, table borders to 0
-- changed mouseover to  buttons
*/
function DoloadWire3(){
include_once 'LocalIniStuff.php'; //local
global $libLoc,$db;
$libLoc = getLini('libLoc');
$db = getLini('dbn');
//print('libLoc=(' . $libLoc . ")<br/>");
global $picLoc;
$picLoc = getLini('picLoc');
//print('picLoc=(' . $picLoc . ")<br/>");
include_once ($libLoc . 'zDAOPDO.php');
include_once ($libLoc . 'PicStuff.php');
include_once ($libLoc . 'fin.php');
include_once ($libLoc . 'llogg.php');
include_once ($libLoc . 'papx.php');
include_once ($libLoc . 'htmlStuff.php');
#t3c3
$fnjs = <<<fnjsx
<script>

function goBack() {
    vt = document.baseURI;
    ixn = getix(vt);
    catmax = getcatMax(vt);
    cat = getcat(vt);
  mt = "Page2.php" + "?cat=" + cat + "&ix=" + ixn + "&catmax=" + catmax + "&nop=1" ; 
    window.location = mt;
}
function goHome() {
    vt = document.baseURI;
    mt = "Page1.php" 
    window.location = mt;
}




function getix(vt){

    fo = vt.indexOf("ix", 0);
    if (fo==-1) { 
        ans = 1; 
    } else {
    bo = vt.indexOf("&", fo);

    ix = vt.substr(fo,bo-fo); // ix=x
    fc = ix.indexOf('=');
    ixnc = ix.substr(fc+1);
    ans = (ixnc*1);
    }
    
    return(ans);
}
function getcatMax(vt){

    fo = vt.indexOf("catmax", 0);
    if (fo==-1) { 
        ans = 1; 
    } else {
    bo = vt.indexOf("&", fo);

    catmax = vt.substr(fo,bo-fo); // ix=x
    fc = catmax.indexOf('=');
    catmaxc = catmax.substr(fc+1);
    ans = (catmaxc*1);
    }
    
    return(ans);
}
function getcat(vt){

    fo = vt.indexOf("cat", 0);
    if (fo==-1) { 
        ans = 1; 
    } else {
    bo = vt.indexOf("&", fo);
    ix = vt.substr(fo,bo-fo); // ix=x
    fc = ix.indexOf('=');
    ixna = ix.substr(fc+1);
    ans = (ixna*1);
    }

    return(ans);
}
function getwidth(vt){

    fo = vt.indexOf("width", 0);
    if (fo==-1) { 
        ans = 1; 
    } else {
    bo = vt.indexOf("&", fo);
    ix = vt.substr(fo,bo-fo); // ix=x
    fc = ix.indexOf('=');
    ixna = ix.substr(fc+1);
    ans = (ixna*1);
    }

    return(ans);
}
function gethook(vt){

    fo = 0;
    bo = vt.indexOf("?", fo);

    ans = vt.substr(fo,bo-fo); 

    return(ans);
}

function moveup() { 

    vt = document.baseURI;
    ixn = getix(vt);
    catmax = getcatMax(vt);
    width = getwidth(vt);
 
    ixn++;
    if (catmax < ixn ) { ixn = 1; }
    cat = getcat(vt);
    hook = gethook(vt);
    mt = hook + "?cat=" + cat + "&ix=" + ixn + "&catmax=" + catmax + "&width=" + width + "&nop=1" ; 
    window.location = mt;
}

function movedown() { 

    vt = document.baseURI;
    ixn = getix(vt);
    catmax = getcatMax(vt);
    width = getwidth(vt);
 
    ixn--;
    if (ixn==0) { ixn = catmax; }
 
    cat = getcat(vt);
    hook = gethook(vt);
    mt = hook + "?cat=" + cat + "&ix=" + ixn + "&catmax=" + catmax + "&width=" + width + "&nop=1" ; 
    window.location = mt;
}
</script>
fnjsx
;
$ans = $fnjs;
global $libLoc,$picLoc,$db;
$cat = $_REQUEST['cat'];
$ix = $_REQUEST['ix'];
$width = $_REQUEST['width'];
//$catdir = getXByCatIx("catDir",$cat,$ix);
//print('catdir=(' . $catdir . ")<br/>");
$url = zByCatIx($db,"picURL",$cat,$ix);
//print('url=(' . $url . ")<br/>");
$picURL = $url;
//print('picURL=(' . $picURL . ")<br/>");
$label = zByCatIx($db,'picLabel',$cat,$ix);
$box1a = <<<box1aD
<center>
<img style="border: 0px solid ; width: %dw%px; height: %dh%px;" alt="" src="%picURL%"> 
</center>
box1aD
;
$factor = 625; // by width
list($rawW,$rawH) = getPicHW($picURL);
list($dh,$dw) = getPicDhDw($rawW,$rawH,$factor);
$box1a = str_replace('%picURL%',$picURL,$box1a);
$box1a = str_replace('%dw%',$dw,$box1a);
$box1a = str_replace('%dh%',$dh,$box1a);
$box1 = <<<box1D
<table style="text-align: left; width: 100%; height: 20px;" border="0"
cellpadding="2" cellspacing="2">
<tbody>
<tr>
  <td>
    <center><div> %artStmt% </div></center>
  </td>
</tr>
<tr>
<td style="vertical-align: center; width: 600px; height: 10px;">
<center>
%pic%
</center>
</td>
</tr>
<tr>
<td style="vertical-align: center; width: 600px; height: 600px;">
<center>
%box1a%
</center>
</td>
</tr>
<tr>
<td>
<table style="text-align: left; width: 100%; height: 20px;" border="0"
cellpadding="2" cellspacing="2">
<tr>
<!-- 1 -->
<td style="vertical-align: center; width: 40px; height: 10px;">
</td>
<td style="vertical-align: center; width: 10px; height: 10px;">
</td>
<td style="vertical-align: center; width: 10px; height: 10px;">
<center>
<img src="previous.png" onclick="movedown()" height="20"
width="20">
</center>
</td>
<td style="vertical-align: center; width: 60px; height: 10px;">
<center>
<!--purchase info hook-->
</center>
</td>
<td style="vertical-align: center; width: 10px; height: 10px;">
<center>
<img src="next.png" onclick="moveup()" height="20"
width="20">
</center>
</td>
<td style="vertical-align: center; width: 10px; height: 10px;">

</td>
<!-- 2 -->
<td style="vertical-align: center; width: 40px; height: 10px;">
</td>
</tr>
</tbody>
</table>
</tr>
</tbody>
</table>
box1D
;
// substitute
$box1 = str_replace("%pic%",$label,$box1);
// add art stmt
$Pix = zByCatIx($db,"catixProfile",$cat,$ix);
$art = zByPix($db, "artStatement",$Pix);
$box1 = str_replace("%artStmt%",$art,$box1);
// 
$box1 = str_replace("%box1a%",$box1a,$box1);
$ans = $ans .$box1 ;
return($ans);
} //
?>
