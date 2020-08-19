<?php
// file eddy.php file read , write utility ;
/* current problem:
   <div> shows file with proper breaks
   but textarea doesn't 
   -- tried wrap=hard (html5) nogo
   ? can i put a div as inar and read its contents in reflex? NO shadow with hidden input?
*/
// pja 10-29-2019 added hidden inar;
//---------------- no code msg for write_file 
// pja 10-07-2018 edits ;
// pja 2018-08-18 ;
// pja 2018-08-17 pja original ;
// ;
// program reflexes to do work ;
// all submits are named mvc with different values ;
// reflex picks up values ;
// ;
// problems ;
// - nowdoc does not parse so $val prints as "$val" ;
// -- will need to replace in str  ;
// ;
//// main //// ;
/* // blank all ;
$fnIn = '';
$fnOut = '';
$inar = "";
$outar = "";
*/
// unpack ;
include_once 'unpack.php';
include_once 'Redirect.php';
// test mvc switch ;
echo "dump before code <br/>";
dumpPAPX($Pa,$Px);
echo "<br /> <br /> end dump";
$mvc = '';
$mvc = getPAPX('mvc',$Pa,$Px);
$ccc=0; // preset ;
if (empty($mvc) == true) { $ccc = 1; }
if ($mvc == '') { $ccc = 1; }
list($Pa,$Px) = writePAPX('ccc',$ccc,$Pa,$Px);
if ($ccc != 1 ) { //--// mvc has command ;
	$lcmd = getPAPX('mvc',$Pa,$Px);// hold local ;
	list($Pa,$Px) = writePAPX('mvc','',$Pa,$Px);
	// clear mvc ;
	// do work ;
	// cmd fan on mvc
	switch ($lcmd) {
    case "get_file":
        $fnIn = getPAPX('fnIn',$Pa,$Px);
        $myFile = $fnIn ;
        $inar = file_get_contents( $myFile ) ;
        include_once 'cv.php';
        $inar = repl($inar);
        // $inar = nl2br($inar);
        list($Pa,$Px) = writePAPX('inar',$inar,$Pa,$Px);
        break;
        
    case "transfer":
        $x1 = "inar to outar";
        list($Pa,$Px) = writePAPX('status',$x1,$Pa,$Px);
        $inar = getPAPX('inar',$Pa,$Px);
        list($Pa,$Px) = writePAPX('outar',$inar,$Pa,$Px);
        list($Pa,$Px) = writePAPX('inar','',$Pa,$Px);
        break;
    case "write_File":
        echo('no code under =write_file=');
        break;
          
    case 2:
        echo "i equals 2";
        break;
    } // end switch 
	
	// pack and go to server['php_self'] ;
	list($Pa,$Px) = writePAPX('to',$_SERVER['PHP_SELF'],$Pa,$Px);
	 // dump papx ;
	 dumpPAPX($Pa,$Px);
     doRe($Pa,$Px);
} else { //--// no mvc ;
	// load texts ;
	//dumpPAPX($Pa,$Px);
	$fnIn = getPAPX('fnIn',$Pa,$Px);
	$fnOut = getPAPX('fnOut',$Pa,$Px);
	$inar = getPAPX('inar',$Pa,$Px);
	$outar = getPAPX('outar',$Pa,$Px);
	// disp page - template is nowdoc ;
	$page = <<<'vx'
<html>
   <head>
      <title> eddy v0.1 </title>
      
   </head>
   <body>
      <form name='f1' id='f1' action="%PHP_SELF" method='POST' >
      <input name='inar' type='hidden' >%inar</input>
<table border='3'>
<tr> <td>.</td> <td>.</td> <td>.</td> <td>.</td> <td>.</td> <td>.</td> 
</tr>
<tr>
<td>.</td> <td> filename <input type='text' name='fnIn' >%fnIn</input></td>
<td> <input type='submit' name='mvc' value='get_file'/> </td> <td>.</td> 
<td>.</td> <td> filename <input type='text' name='fnOut' >%fnOut</input></td>
</tr>
<td>.</td>
<td> <div name='inar'>%inar</div> </td> <td>.</td> <td> <input type='submit' name='mvc' value='transfer'/> </td> <td>.</td>  
<td> <textarea cols='40' rows='10' name='outar'>%outar</textarea> 
</td> </tr>
<tr> <td>.</td> <td>.</td> <td>.</td> <td>.</td> <td>.</td> <td> <input type='submit' name='mvc' value='write_File'/> </td> 
</tr>
</table>
<div name="status">Status: %status</div>
      </form>
   </body>
</html>
vx
;
	// substitute values
	$fnIn = getPAPX('fnIn',$Pa,$Px);
	$fnOut = getPAPX('fnOut',$Pa,$Px);
	$inar = getPAPX('inar',$Pa,$Px);
	$outar = getPAPX('outar',$Pa,$Px);
	$status = getPAPX('status',$Pa,$Px);
	$page1 = str_replace("%fnIn",$fnIn,$page);
	$page1 = str_replace("%fnOut",$fnOut,$page1);
	$page1 = str_replace("%inar",$inar,$page1);
	$page1 = str_replace("%outar",$outar,$page1);
	$page1 = str_replace("%status",$status,$page1);
	$page1 = str_replace("%PHP_SELF",$_SERVER['PHP_SELF'],$page1);
	echo($page1);
	dumpPAPX($Pa,$Px);
} // end mvc if ;
?>

