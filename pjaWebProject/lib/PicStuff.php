<?php
# file PicStuff.php
/*
pja 3/12/2019 edited getPicDhDw
pja 1/3/2019

*/
function getPicHW($picPath)  {
// list($rawW,$rawH) = getPicHW($picPath);
   $size = getimagesize($picPath);
   $rawW = $size[0];
   $rawH = $size[1];
   return(array($rawW,$rawH));
} // getPicHW($picPath)
function getPicDhDw($rawW,$rawH,$factor){
// list($dw,$dh) = getPicDhDw($rawW,$rawH,$factor);
    if ($factor == 0) { $factor = 100; }
    /*if ($rawW <= $rawH) { */
        $dw=$factor; 
        $dh= ($rawW/$rawH * $factor); 
    /*} else { 
        $dh = $factor;
        $dw = ($rawH/$rawW)*$factor;
    //} // endif*/
    return(array($dw,$dh));
} //
?>
