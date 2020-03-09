<?php
/* file tocT.php
pja 3/22/2019 adjusted for loop
pja 3/20/2019 converted to db
pja 12-17-2018
fails at while
generates the toc via cats.txt
*/
function doTocT($width){
// get callers ini path to lib
include_once 'LocalIniStuff.php';
$libLoc = getLini('libLoc');
$db = getLini('dbn');
$toc1 = <<<toc1x
<table style="width: 200px; height: 600px;" name="toc-frame">
<tbody><tr> <td> 
toc1x
;

$entryT = <<<entryx
<table name="%label%">
<tbody><tr>
<td>  </td> <td>  </td> <td> 
<a href="Page2.php?ix=1&cat=%cat%&width=%width%">%label%</a> </td>
</tr>
</tbody>
</table>
entryx
;

$tocbox = '';

// get cats
include_once ($libLoc .'zDAOPDO.php'); 
// per cat get name, link
$iox = zByCatIx($db,'catMax',$ctr,0);
for ($ctr=1;$ctr<=$iox;$ctr++){ 
	$iox = zByCatIx($db,'catMax',$ctr,0);
	// get label // fails here
	$label = zByCatIx($db,'CLabel',$ctr,0);
	// get template
	$entry = $entryT;
	// replace needle, new, str label/catName
	$entry = str_replace('%label%',$label,$entry);
	$entry = str_replace('%cat%',$ctr,$entry);
	$entry = str_replace('%width%',$width,$entry);
	// add entry to tocbox
	$tocbox = $tocbox . $entry;
} // fend
$toc2 = <<<toc2x
<br/>
<br/>
<table name="home">
<tbody><tr>
<td> </td> <td> <a href="Page1.php">Home</a> </td>
</tr>
</tbody></table>

<table name="commercial">
<tbody><tr>
<td> </td> <td> commercial </td>
</tr>
</tbody></table>
<!-- <table style="width: 105px; height: 309px;" -->
<table style="width: 105px; height: 100px;" name="tocbuffer2">
<tbody><tr>
<td style="height: 305px;"> . </td>

</tr>
</tbody></table>

 </td> </tr>
</tbody></table>
toc2x
;

// return($toc1 . $tocbox . $toc2 );
return($toc1 . $tocbox . $toc2 );
} // end doTocT()
?>