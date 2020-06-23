<?PHP
// file XXParse.php
// pja 03-10-2020
// needs to follow the hierarchy 
//
include_once "genn.php";

function XParse ($url) {
        $fileContents= file_get_contents($url);
        $fileContents = str_replace(array("\n", "\r", "\t"), '', $fileContents);
        $fileContents = trim(str_replace('"', "'", $fileContents));
        $simpleXml = simplexml_load_string($fileContents);
        $json = json_encode($simpleXml);
        $jsonAR = json_decode($json);
        return array($simpleXml,$json,$jsonAR);
}
$url = 'https://stratml.us/carmel/iso/UC4SwStyle.xml' ;
//$url = "https://aryc.000webhostapp.com/works-in-progress/xmTest.xml";
list($simpleXml,$json,$jsonAR) = Xparse($url);



//echo "<br/><br/>";
print("<table border='3'>");
print("<tr><td>RDF</td></tr>");
print("<tr><td>recordNumber</td><td>subject</td><td>predicate</td><td>object</td></tr>");
$arr = $jsonAR; 
$parent = array(); 
array_push($parent,'StrategicPlan');
$ans = dive($parent,$arr);
//print('<br/> final parent');
//var_dump($parent);
//print('<br/> final rec');
//var_dump($rec);
print("</table>");

echo "<br/>//==========================================";
print('<br/>simpleXml<br/>');
var_dump($simpleXml);
echo "<br/>//==========================================";
echo "<br/>//==========================================";
print('<br/>json<br/>');
var_dump($json);
echo "<br/>//==========================================";
echo "<br/>//==========================================";
print('<br/>jsonAR<br/>');
var_dump($jsonAR);
echo "<br/>//==========================================";

function dive($parent,$arr){
    foreach($arr as $x => $x_value) {
        //print('<br/>x=(' . $x . ')-( ' . gettype ($x_value) . ')<br/>');
        if (gettype ($x_value)=='object'){
            array_push($parent,$x);
            $parent= dive($parent,$x_value);
            //print('<br/> parent=');
            //var_dump($parent);
            //print('<br/> rec=');
            //var_dump($rec);
            array_pop($parent); 
        } elseif (gettype ($x_value)=='array'){
            array_push($parent,$x);
            $parent = dive($parent,$x_value);
            //print('<br/> parent');
            //var_dump($parent);
            //print('<br/> rec==');
            //var_dump($rec);
            array_pop($parent); 
        } elseif (gettype ($x_value)=='string'){
            writeRDF($parent,$x,$x_value);
            //print('<br/><br/>=parent=');
            //var_dump($parent);
            //print( "<br/>Key=") ;
		    //var_dump($x);
		    //print("StringValue="); 
		    //var_dump($x_value);
		    //echo "<br/><br/>";
		    //$rec = array('record=',$x,$x_value);    
        } else {
            writeRDF($parent,$x,$x_value);
            //print('<br/><br/>=parent=');
            //var_dump($parent);
            //print( "<br/>Key=") ;
		    //var_dump($x);
		    //print("OtherValue="); 
		    //var_dump($x_value);
		    //echo "<br/><br/>";
		    //$rec = array('record=',$x,$x_value);      
        }//endif
    } //endfor
    return($parent); 
}
function writeRDF($parent,$element,$value){
    WriteSPO('','','');
    WriteSPO('','','');
    /* gen custodyChain */
    $custodyChain = genX();
    /* element EhasValue value */
    WriteSPO($element,"EhasValue", $value);
    /* (element EhasValue value) hasCustody custodyChain */
    $subject = "(".$element.","."EhasValue".",". $value . ")";
    WriteSPO($subject,"hasCustody",$custodyChain);
    /* value  ValueOfE element  */
    WriteSPO($value,"ValueOfE", $element);
    /* (value  ValueOfE element) hasCustody custodyChain */
    $subject = "(".$value.","."ValueOfE".",". $element . ")";
    WriteSPO($subject,"hasCustody",$custodyChain);
    
    /* parent=element ParentChild child=blank */
    $subject = $element;
    $predicate = "ParentChild";
    $object = "";
    WriteSPO($subject,$predicate,$object);
    /* (parent ParentChild child) hasCustody custodyChain */
    $subject = "(".$subject . ",".$predicate.",". $object . ")";
    $predicate = "hasCustody";
    $object = $custodyChain;
    WriteSPO($subject,$predicate,$object);
    /* child=blank  ChildOfParent parent=element */
    $subject = "";
    $predicate = "ChildOfParent";
    $object = $element;
    WriteSPO($subject,$predicate,$object);
    /* (child  ChildOfParent parent) hasCustody custodyChain */
    $subject = "(".$subject.",".$predicate.",". $object . ")";
    $predicate = "hasCustody";
    $object = $custodyChain;
    WriteSPO($subject,$predicate,$object);
    $child = $element;
    $drain = $parent;
    // per parent copy
    foreach ($drain as $d) {
        //-// /* parent ParentChild child */
        WriteSPO($d,"ParentChild", $child);
        //-// /* (parent ParentChild child) hasCustody custodyChain */
        $subject = "(". $d .","."ParentChild" . "," . $child . ")";
        WriteSPO($subject,"hasCustody", $custodyChain);
        //-// /* child  ChildOfParent parent */
        WriteSPO($child, "ChildOfParent", $d);
        //-// /* (child  ChildOfParent parent) hasCustody custodyChain */
        WriteSPO("(" . $child .",".  "ChildOfParent" .",".  $d .")", "hasCustody", $custodyChain);
        $child = $d;
    }
    
    $s = ''; $o=$d;
    WriteSPO($s,"ParentChild", $o); /* parent=blank ParentChild child=lastParent */
    /* (parent ParentChild child) hasCustody custodyChain */
    $subject = "(". $s .","."ParentChild" . "," . $d . ")";
    WriteSPO($subject,"hasCustody", $custodyChain);
    /* child=lastParent  ChildOfParent parent=blank */
    $s = $d; $o = '';
    WriteSPO($s,"ChildOfParent",$o);
    /* (child  ChildOfParent parent) hasCustody custodyChain */
    WriteSPO("(" . $s .",".  "ChildOfParent" .",".  $o .")", "hasCustody", $custodyChain);
} //writeRDF
function WriteSPO($subject,$predecate,$object){
    $ix = genX();
    print("<tr>");
    print("<td>"); print($ix); print("</td>");
    print("<td>"); print($subject); print("</td>");
    print("<td>"); print($predecate); print("</td>");
    print("<td>"); print($object); print("</td>");
    print("</tr>");
}//WriteSPO
?>