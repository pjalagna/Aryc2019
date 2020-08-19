<?php
/*
file htmlStuff.php
pja 4/8/2019 added optional hidden formname to mkForm
pja 3/12/2019 changed border to 0
pja 1/21/2019 
   a-added mkForm
   b-deleted page tags from mkPage
pja 1/15/2019 added mkSelect
pja 12/31/2019

routines for creating html elements
mkFileI($name,$label) - input with hidden fileHold
mkPage($pageName,$pageLabel) // -> string
mkTable(TableName,ColMax,RowMax,width,height) // -> string(--tableName.col.row--)
mkForm(action,{name},{extra}) --> str(w(hidden(formName)),--hidden--,--formBody--)
mkRadio($label,$value) -> str,id
mkDiv($label) // -> list($s,$id) // use id for submit list
mkTxtAr($label,{value}) // --> list($s,$id)
mkTxt($label) // --> list($s,$id);$s=str(<!--input-->)
mkSelect($name,$opsAR,$event='') --> string
mkButton(na,lable,{oncommand}) // --> list($s,$id)
*/
function mkFileI($name,$label){
    // makes input file type and hidden to pass this inputs name
    $T = "<input name='%name%' type='file'>%label%</input> <input type='hidden' name='fileHold' value='%name%'/>";
    $ans = $T;
    $ans = str_replace('%name%',$name,$ans);
    $ans = str_replace('%label%',$label,$ans);
    return($ans); 
} //mkFileI
function mkForm($action,$xtra='',$name=''){
    $lab = $name;
    $lab = str_replace(' ','#',$lab);
    $ans = <<<ansx
<form action="%action%" method='POST' %xtra% >
    <input type='hidden' name='formid' id='formid' value='%label%'/>
    <!--hidden-->
    <!--formBody-->
</form>
ansx
;
    $ans = str_replace("%action%",$action,$ans);
    $ans = str_replace("%xtra%",$xtra,$ans);
    $ans = str_replace("%label%",$lab,$ans);
    return($ans);
} //mkForm
function mkButton($na,$lab,$onx=''){
$T = '<button name="%na%" id="%na%" %onx% >%lab%</button>';
$ans = $T;
$ans = str_replace("%na%",$na,$ans);
$ans = str_replace("%onx%",$onx,$ans);
$ans = str_replace("%lab%",$lab,$ans);
return(array($ans,$na));
} // mkButton
function mkRadio($label,$value){
    $e = '<input type="radio" name="' . $label . '" value="' . $value .  '">';
    return(array($e,$label));
} //
function mkDivL($label){
/*
pja 1/2/2019 added div marker
*/
   $label = trim($label);
   $id = trim(str_replace(' ','-',$label));
   $e = $label .'<div name="' . $id .'" id="' . $id .'">' ."<!--" . $id . "--></div>";
   return(array($e,$id));
} // mkdivL
function mkDiv($tag,$value=''){
/*
pja 1/6/2019 no front lable
*/
   $e = '<div name="' . $tag .'" id="' . $tag .'"><!--div--></div>';
   if ($value != ''){ //t1
      $e = str_replace('<!--div-->',$value,$e);
   }//t1
   return(array($e,$tag));
} // mkdiv
function mkTxtAr($label,$value='') {
   $label = trim($label);
   $id = trim(str_replace(' ','-',$label));
   $e = $label .' <textarea rows="10" cols="50" 
   name="' . $id .'" id="' . $id .'"><!--textarea--></textarea>';
   if ($value != ''){ //t1
      $e = str_replace('<!--textarea-->',$value,$e);
   }//t1
   return(array($e,$id));
} // mkTxt
function mkTxt($label,$value='') {
   $label = trim($label);
   $id = trim(str_replace(' ','-',$label));
   $e = $label .' <input type="text" name="' . $id .'" id="' . $id .'" value="" ><!--input--></input>';
   if ($value != ''){ //t1
      $e = str_replace('value=""','value="'.$value.'"',$e);
   }//t1
   return(array($e,$id));
} // mkTxt
function mkHidden($name,$value='') {
   $name = trim($name);
   $id = trim(str_replace(' ','-',$name));
   $e = $label .' <input type="hidden" name="' . $id .'" id="' . $id .'" value="" ><!--input--></input>';
   if ($value != ''){ //t1
      $e = str_replace('value=""','value="'.$value.'"',$e);
   }//t1
   return(array($e,$id));
} // mkTxt
function mkImg($picURL,$dx,$dy){
    $ans = '<img style="width: %dx%px; height: %dy%px;" alt=""
src="%picURL%">';
    $ans = str_replace('%dx%',$dx,$ans);
    $ans = str_replace('%dy%',$dy,$ans);
    $ans = str_replace('%picURL%',$picURL,$ans);
    logg('mkImg(' . $ans . ")");
    $id = '';
    return(array($ans,$id));
}//
function mkPage($pageName,$pageLabel){
/*
page(*name,*pageLabel,title,headBegin,headEnd,bodyBegin,bodyEnd)

makes a simple page with markers for insertion
pja 1/2/2019
*/
$today = date("l jS \of F Y h:i:s A");

$template = <<<templatex
<!DOCTYPE html>
<html>
   <!-- Page Name pageName -->
   <!-- generation date %today% -->
   <head>
       <title>PageLabel</title>
       <!--head-begin-->
       <!--head-end-->
   </head>
   <body>
   <!--body-begin-->
   <!--body-end-->
   </body>
</html>
templatex
;
// replace
$ans = $template;
$ans = str_replace('%today%',$today,$ans);
$ans = str_replace('PageName',$pageName,$ans);
$ans = str_replace('PageLabel',$pageLabel,$ans);
return($ans);
} // makepage
function mkTable($TableName,$ColMax,$RowMax,$width='',$height='') {
// creates a table with markers 
/* 
pja 1/1/2019 added line number to <tr> - if i need to replace row
pja 12/31/2018
test as 
include_once 'htmlStuff.php';
$TableName = 'myTable';
$ColMax = 3;
$RowMax = 5;
$width = 500;
$height = 200;
$x = mkTable($TableName,$ColMax,$RowMax,$width,$height);
print($x);
*/
    $template = '<td style="%width%  %height%"><!--TableName.Col.Row--></td> ';
    if ($width ==''){ 
        $w = ''; 
    } else { 
        $w = "width: " . $width . "px; ";
    }
    if ($height =='') {
        $h = ''; 
    } else { 
        $h = "height: " . $height . "px; " ;
    }
    $ans = '<table name="' . $TableName . '" border="0"> ';
    for ($r=1; $r<=$RowMax; $r++) {
        $ans = $ans . " <tr line='" . $r . "'> ";
        for ($c=1;$c<=$ColMax; $c++) {
            $j = $template;
            $j = str_replace("%width%",$w,$j);
            $j = str_replace("%height%",$h,$j);
            $f = "<!--" .$TableName .'.'.$c.'.'.$r."--></td>";
            $j = str_replace("<!--TableName.Col.Row--></td>",$f,$j);
            $ans = $ans . $j;
        } // end for c
        $ans = $ans . " </tr> ";
    } // end for r
    $ans = $ans . ' </table>';
    return($ans);
} // mkTable
function mkSelect($name,$opsAR,$addNew='', $event='') {
    // name , options array k=>v , event 
    $pl1T = "<select name='%plname%' id='%plname%' %event% ></br>";
	$pl2T = "<option value='%vval%'>%vval%</option></br>";
	$ans = $pl1T;
	$ans = str_replace('%plname%',$name,$ans);
	$ans = str_replace('%event%',$event,$ans);
	// add header elect
	$ans = $ans . $pl2T;
	$ans = str_replace('%vval%','(select)',$ans);
	if ($addNew != '') {
	    $ans = $ans . $pl2T;
	    $ans = str_replace('%vval%','(new)',$ans);
	}
	foreach ( $opsAR as $key => $vval ) { 
		if ($vval[0] == '.') { 
			$nop =1 ; //skip
		} else {
			$cv = $pl2T; 
			$cv = str_replace('%vval%',$vval,$cv);
			$ans = $ans . $cv;
		} // endif
	} // foreach
    return($ans . "</select>");
} // mkselect
?>