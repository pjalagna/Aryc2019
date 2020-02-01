<?php
/* file redirect.php
pja 1/21/2019 recoded packNGo to not pack null or empty
pja 1/19/2019 added packNGo
pja 1/8/2019
works with send array 
// ie array([ array[0]==key [1]==val) ]
*/
function packNGo($Pa,$Px){
    // repacks papx for redirection
    include_once 'LocalIniStuff.php'; //local
    $libLoc = getLini('libLoc');
    include_once($libLoc . 'papx.php');
    include_once($libLoc . 'llogg.php');
    $to = getPAPX('to',$Pa,$Px);
	if ($to == '') { //1
	} else { //1
		list($Pa,$Px) = writePAPX('mvcStatus','',$Pa,$Px);
		$e1 = <<<e1m
<html>
    <head><title> redirect </title></head>
	<body onload="document.forms['fr'].submit()" >
			<form id='fr' name='fr' method='POST' action="%to%" >  <br />
e1m
; 
        // test w GET shld be POST
        $e1 = str_replace('%to%',$to,$e1);
        echo($e1); // good echo 
        // pack all of papx
        $stmtT = <<<estmt
	<br /> <input type='hidden' name='%na%' id='%na%' value='%val%' />
estmt
;
	    foreach ( array_keys($Pa) as $i ) {
			$na = $Px[$Pa[$i]][0];
			$val = $Px[$Pa[$i]][1];
			$stmt = $stmtT;
			$stmt = str_replace("%na%",$na,$stmt);
			$stmt = str_replace("%val%",$val,$stmt);
			echo($stmt); // good echo
	    } // foreach
	    echo (" </form> <br /> </body> <br /> </html> "); // good echo
	    exit;
    } // endif to=''
} // packNGo

function doReD($to, $send){
// include_once "SQSQ.php"; // not now
if ($to == '') // if1 
{ $nop=1;
} else { //if1
    $e1 = <<< e1m
<html>
    <head>
       <title> redirect </title>
    </head>
     <body onload="document.forms['fr'].submit()" >
        <form id='fr' name='fr' method='POST' action="%to%" >  <br />
e1m
; 
    // test w GET shld be POST
	// replace to
	$e1 = str_replace('%to%',$to,$e1);
	echo($e1); // good echo 
	// set up template
	$stmtT = <<<estmt
	<br /> <input type='hidden' name='%kx%' id='%kx%' value='%vx%' />
estmt
;
	// unpack send
	foreach ($send as $sx){
		$kx = $sx[0];
		$vx = $sx[1];
		// get template
		$stmt = $stmtT;
		// replace
		$stmt = str_replace('%kx%',$kx,$stmt);
		$stmt = str_replace('%vx%',$vx,$stmt);
		// echo
		echo($stmt); // good echo
	} // foreach sx
	echo (" </form> <br /> </body> <br /> </html> "); // good echo
		exit;
	} // endif if1
} // end doReD
?>
