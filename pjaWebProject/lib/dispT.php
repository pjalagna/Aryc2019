<?php
/*
file dispT.php
pja 4/11/2019 exits to page3.php
pja 3/20/2019 converted to db
pja 3/12/2019 changed table border's to 0
pja 3/4/2019 added catixmax to bigPic send
pja 1/29/2019
pja 1/9/2019 use profile 
pja 12-30-2018

displays complete contents of cat as images
  in a (F x 5) table 
*/
function displayTable($cat,$width) {
include_once 'LocalIniStuff.php'; //local
global $libLoc,$db;
$libLoc = getLini('libLoc');
$db = getLini('dbn');
global $picLoc;
$picLoc = getLini('picLoc');
include_once ($libLoc . 'zDAOPDO.php');
include_once ($libLoc . 'PicStuff.php');
$catmax = zByCatIx($db,'catIxMax',$cat,0) ; 
    $mx = <<<mxx
<td style="vertical-align: center; height: %box%px; width: %box%px;"> 
<center>
<a href="Page3.php?ix=%ix%&cat=%cat%&catmax=%catmax%&width=%width%&nop=1">
<img style="width: %dw%px; height: %dh%px;" alt="" src="%picURL%" > 
</a>
</center>
</td>
mxx
;
// box, pic, dh, dw
// catx
    // get series statement to its own div
    $statement = zByCatIx($db,'SeriesStatement',$cat,0) ; 
    $ans = '<p>' . $statement . '</p><br/>';
    // set pic mod 
    if ($width < 400) { $pm= 1; } else { $pm=5; }
    logg('width=(' . $width . ")");
    logg('pm=(' . $pm . ")");
    $ans = $ans . " <table border='0'> <tr> ";
    $x =0;
    $ctl = 0;
    while ($ctl ==0) {
        $x++;
        if (($x % $pm) == 0) {
            $ans = $ans . " </tr> <tr> ";
        } // endif
        // get filename viz profile
        //$catdir = getXByCatIx("catDir",$cat,$x);
        //print('catdir=(' . $catdir . ")<br/>");
	    $url = zByCatIx($db,"picURL",$cat,$x);
	    if ($url == '') { $ctl=-1; 
	    } else {
	    $picURL = $url;
	    //print('picURL=(' . $picURL . ")<br/>");
        $filename = $picURL;
        $size = getimagesize($filename);
        $rawW = $size[0];
        $rawH = $size[1];
        if ($width < 400) { $box = 800; } else { $box = 200; }
        list($dw,$dh) = dwdh($rawW,$rawH ,$box);
        $j = $mx; // template // box, pic, dh, dw
        $j = str_replace('%box%',$box,$j);
        $j = str_replace('%picURL%',$filename ,$j);
        $j = str_replace('%dh%',$dh,$j);
        $j = str_replace('%dw%',$dw,$j);
        $j = str_replace('%cat%',$cat,$j);
        $j = str_replace('%ix%',$x,$j);
        $j = str_replace('%catmax%',$catmax,$j);
        $j = str_replace('%width%',$width,$j);
        //$j = str_replace('%iam%',$_SERVER[PHP_SELF],$j);
        $ans = $ans . $j;
        } // endif
    } // endfor
    $ans = $ans . "</tr> </table>";
    return($ans);
} // displayTable($loc)
function dwdh($rawW,$rawH ,$box){
    // maintains the ratio of raw-width to raw-height to fixed box
    if ($rawW <= $rawH) { 
        $dh= $box;
        $dw= ($rawW/$rawH) * $box ;
    } else { 
        $dw = $box;
        $dh = ($rawH/$rawW) * $box;
    } // endif
    return(array(floor($dw),floor($dh))); 
} // dwdh
if (isset($_GET['trace'])) { 
    $loc = $_GET['loc'];
    print(displayTable($loc,$width)); 
}
?>