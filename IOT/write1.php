<?php
// write1 (posted 
// fn=file to write 
// copy=text
// sw=append switch
$fn = $_POST['fn'];
$copy = $_POST['copy'];
$sw = $_POST['sw'];
if ($sw != 'a')
{
 $myfile = fopen($fn, "a") or die("Unable to open a file!") ;
} else {
$myfile = fopen($fn, "w") or die("Unable to open w file!") ;
} ;
fwrite($myfile, $copy) ;
fclose($myfile) ;
?>