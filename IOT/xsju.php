<?php
// xsju.php
// use xsju.php?fn=file&tx=text
// write a one word text to file
// write1 (posted 
// fn=file to write 
// copy=text
// sw=append switch
$fn = $_GET['fn'];
$copy = $_GET['tx'];
$myfile = fopen($fn, "w") or die("Unable to open w file!") ;
fwrite($myfile, $copy) ;
fclose($myfile) ;
?>