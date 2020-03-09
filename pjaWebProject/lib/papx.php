<?php
/* file papx.php
internal database
cloned from unpack.php - removed request pickup
pja 1/2/2019

// getPAPX($name,$Pa,$Px) // -> string
// writePAPX($name,$value,$Pa,$Px) -> list($Pa,$Px)
*/
global $Pa,$Px;
$Pa = array();
$Px = array();
function pxHids(){
    // create hidden html from papx
    global $Pa,$Px;
    $stmtT = <<<estmt
	<br /> <input type='hidden' name='%na%' id='%na%' value='%val%' />
estmt
;
    $ans = '';
	foreach ( array_keys($Pa) as $i ) {
		$na = $Px[$Pa[$i]][0];
		$val = $Px[$Pa[$i]][1];
		// not null not empty
		$c =0;
		if ($na == 'NULL') { $c=1; }
		if ($val == '') { $c=1; }
		if ($c == 0) {
			$stmt = $stmtT;
			$stmt = str_replace("%na%",$na,$stmt);
			$stmt = str_replace("%val%",$val,$stmt);
		    $ans = $ans . $stmt;
		} //endif
	} // foreach
    return($ans);
} // hids
function pxUnpack(){
    // loads papx with input parameters
	global $Pa,$Px;
	$Pa = array();
	$Px = array();
	// write a null record first (o index failure)
	list($Pa,$Px) = writePAPX('NULL','NULL',$Pa,$Px);
	foreach ($_REQUEST as $k => $v) {
	    // not null not empty
	    $c =0;
	    if ($k == 'NULL') { $c=1; }
	    if ($v == '') { $c=1; }
	    if ($c == 0) {
			 list($Pa,$Px) = writePAPX($k,$v,$Pa,$Px);
		}//endif
	}
    return(array($Pa,$Px));
} // unpack

function getPAPX($name,$Pa,$Px){
    include_once 'llogg.php';
    try { 
        if (empty($Pa[$name]) == true) {
            $ans = '';
        } else {   
            $ans = $Px[$Pa[$name]][1];
        }
    } catch (Exception $e) {
        $ans = '';
    }
    logg ('<br/>getPAPXL=(' . $name . ')-[' . $ans . ']');
    return($ans);
}
function writePAPX($name,$value,$Pa,$Px){
    include_once 'llogg.php';
    // returns to caller PaPx
    $j = count($Px);
    $Pa[$name] = $j;
    $Px[$j]= array();
    $Px[$j][0] = $name;
    $Px[$j][1] = $value;
    logg('<br /> writePAPXL name (' . $name . ') has (' . $value . ') '); // test
    logg ('<br /> verify read (' . getPAPX($name,$Pa,$Px) . ') ?');  // test
    return array($Pa,$Px);
}
function dumpPAPX($Pa,$Px){
    print("<br/>dump Pa<br/>");
    print_r($Pa);
    print("<br/> dump Px<br/>");
    print_r($Px);
    print("<br/> end dump PaPx<br/>");
} // end dump
?>