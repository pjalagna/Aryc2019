<?php
# file LocalIniStuff.php
/*
pja 1/17/2019 deleted rename of fout
pja 1/8/2019 points to lib
pja 1/3/2019

*/
function Localfin($filename) {
    $fileToOpen = fopen($filename,"r");
    $content = fread($fileToOpen, filesize($filename));
    #$content = nl2br($content);
    fclose($fileToOpen);
    return($content);
} // end fin


function getLIni($tag){
$tagr = Localfin($tag . '.txt');
$tagr = trim($tagr);
return($tagr);
} //
?>
