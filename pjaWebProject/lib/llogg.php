<?php
/*
pja 1/29/2019 added onDev()
pja 1/21/2019 added onLogg() true/false on trace
// file logg

// prints if trace=on
*/
function logg($msg){
   if (isset($_REQUEST['trace']))
   {
     if ($_REQUEST['trace']  == 'on')
     {
       print('<br/>'.$msg);
     } // =on
   } // is set
} // logg
function onLogg() {
   // usage if(onLogg==true) { dothis; }
   logg('onLogg');
   $ans = false; // preset
   if (isset($_REQUEST['trace'])){
     if ($_REQUEST['trace']  == 'on') {
       $ans = true;
     }
   } // is set
   return($ans);
} // onLogg
function onDev() {
   // usage if(onDev==true) { dothis; }
   // used for testing tool functions
   logg('onDev');
   $ans = false; // preset
   if (isset($_REQUEST['Dev'])){
     if ($_REQUEST['Dev']  == 'on') {
       logg('onDev true<br/>');
       $ans = true;
     }
   } // is set
   return($ans);
} // onDev
function loggr($ar){ // prints arrays
   if (isset($_REQUEST['trace']))
   {
     if ($_REQUEST['trace']  == 'on')
     {
       print_r('<br/'.$msg);
     } // =on
   } // is set
} // loggr
?>

