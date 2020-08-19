<?php
// filename sfbe.php
// pja 10 13 2014  added line break after ">"
// pja 8-2-2014 added fclose
// read on get fn
$myFile = $_GET['fn'];
$fh = file_get_contents($myFile);
// convert <,$.> in string to *g* *d* *l*
str_replace("%body%", "black", "<body text='%body%'>");
$v1 = str_replace("<" , "*G*" , $fh);
$v2 = str_replace(">" , "*L* <br />" , $v1);
$v3 = str_replace("$" , "*D*" , $v2);
$v4 = str_replace(";" , " -- <br />" , $v3);
fclose($fh);
// display string
print ("<br /><div> " . $v4 . " </div>");
?>