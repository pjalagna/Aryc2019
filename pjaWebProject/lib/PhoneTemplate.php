<?php
/*
file PhoneTemplate.php
*/
function PTemplate_main(){
include_once 'LocalIniStuff.php'; // callers local
$libLoc = getLini('libLoc'); // callers local file
$picLoc = getLini('picLoc');
include_once ($libLoc.'fin.php');
include_once ($libLoc.'llogg.php');
logg('phone template.php begin');
include_once ($libLoc.'zDAOPDO.php');
//$ans = fin($libLoc . 'PhoneWire1.html');

$sec1 = <<< sec1
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html><head>
<!-- page width 300 -->
</head><body>

sec1
;
$ans = $ans . $sec1;

$sec2 = <<< sec2x
<!-- phone template-->
<table style="text-align: left; width: 100%;" border="0">
<tbody>
<tr>
<td style="vertical-align: top;">
<center>
%logo%
</center>
</td>
</tr>
<tr><td><center>%pic%</center></td></tr>

<tr>
<td style="vertical-align: top;">
<center>
%toc%
</center>
</td>
</tr>

</tbody>
</table>
sec2x
;
$ans = $ans . $sec2;

logg('pt-ret=(' . $ans . ")");
return($ans);
} //function
?>
