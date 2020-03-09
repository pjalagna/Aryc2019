<?php
/*
file doR.php
pja 1/19/2019 renamed redir to xredir 
-- see who calls change callers to use redirect.php
pja 1/4/2019
*/
function genSessionID($un,$date) {
    $m = $date;
    $m = str_replace('0','s',$m);
    $m = str_replace('1','d',$m);
    $m = str_replace('2','v',$m);
    $m = str_replace('3','f',$m);
    $m = str_replace('4','w',$m);
    $m = str_replace('5','e',$m);
    $m = str_replace('6','r',$m);
    $m = str_replace('7','p',$m);
    $m = str_replace('8','u',$m);
    $m = str_replace('9','k',$m);
    $ans = str_replace(' ',$un,$m);
    return('X' . $ans);
} // genSessionID($un,$date)

function testSess($sess,$user) {
// true false
include_once 'LocalIniStuff.php'; //local
$libLoc = getLini('libLoc');
include_once ($libLoc . 'llogg.php');
logg('testSess');
logg('p1 sess=(' . $sess . ")");
logg('p1 user=(' . $user . ")");
    $date = date("Ym d");
    $m = genSessionID($user,$date);
    logg('g1 date=(' . $date . ")");
    logg('g1 m=(' . $m . ")");
    if ($sess == $m) {
        $ans = 'ok';
    } else {
        $ans = 'nok';
    } // endif
    logg('ret =(' . $ans . ")");
    return($ans);
} // testSess

function xredir($to,$varAR){
// redirect to 'to' with named variables in varAR
// as array in array [0] = key
//                   [1] = val
print('redir to=(' . $to . ")<br/>");
print_r($varAR);

$f1 = '<form id="my_form" action="%to%" method="POST">';
$f1 = str_replace ('%to%',$to,$f1);
$f3 = <<<f3x
</form>
 
<script type="text/javascript">
    //Our form submission function.
    function submitForm() {
        document.getElementById('my_form').submit();
    }
    //Call the function submitForm() as soon as the page has loaded.
    window.onload = submitForm;
</script>
f3x
;
$f2t = " <input type='hidden' name='%name%' value='%val%'/>";
foreach ($varAR as $x) {
   $j = $f2t;
   $key = $x [0];
   $vval = $x [1];
   $j = str_replace ('%name%',$key,$j);
   $j = str_replace ('%val%',$vval,$j);
   $ans = $ans . $j;
} // foreach
return($f1 . $ans . $f3);
} 

if ($_REQUEST['dtrace'] == 1) {

$send = array();
array_push($send,array('mox','f1'));
array_push($send,array('name','Paul'));
print(redir('dump.php',$send));
} elseif ($_REQUEST['trace'] == 'genSessionID'){
  $dd = date("Ymd");
  $user = 'notAnyone';
  print(genSessionID($user,$dd));
} elseif ($_REQUEST['trace'] == 'testSess'){
    $dd = date("Ym d");
    $user = 'notAnyone';
    $a = genSessionID($user,$dd);
    $dd2 = date("Ym d");
    $user2 = 'notAnyone';
    $n = genSessionID($user2,$dd2) . ';';
    print('a ' . testSess($a,$user));
} else {
  $nop = -1;
} //

?>