<?php
# file iniStuff.php
/*
pja 1/3/2019

*/
function getini($tag) {
   include_once 'fin.php';
   include_once 'strParser.php';
   $ini = fin('ini.xml');
   //s2split($inString,$front,$back,$offset)
   $front = "<" . $tag . ">";
   $back = "</" . $tag . ">";
   list($ans,$nop) = s2split($ini,$front,$back,0);
   return(trim($ans));
} // getini
?>
