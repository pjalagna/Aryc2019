<?php
/*
file DBDE.php
pja 3/10/2019

test

$_REQUEST['trace']='on';
$_REQUEST['db']='foo.db';
$_REQUEST['cmd']='read';
$_REQUEST['sq']='select * from sqlite_master;';
include_once ('DBDE.php');
*/
// includes
include_once 'LocalIniStuff.php'; //local
$libLoc = getLini('libLoc');
include_once($libLoc . 'papx.php');
include_once($libLoc . 'htmlStuff.php');
include_once($libLoc .'PDODAO.PHP');
// unpack
global $Pa,$Px,$cats;
list($Pa,$Px) = pxUnpack();

// cmd fan
$cmd = getPAPX('cmd',$Pa,$Px);
$db = getPAPX('db',$Pa,$Px);
$dbh = openDB($db);
// cmd fan
switch ($cmd) {
    case '':
        cmdBlank();
    break;
    case 'read':
        cmdRead();
    break;
    case 'ICAT':
        cmdICAT();
    break;
    case 'ex':
        cmdex();
    break;
    case 'ISQS':
        cmdISQS();
    break;
    
    default:
        print("<br/> unknown command (" . $cmd . ")");
        dumpPAPX($Pa,$Px);
        cmdBlank();
    break;
} //switch
print('done');
function cmdex(){
    global $Pa,$Px,$dbh;
    $sq = getPAPX('sq',$Pa,$Px);
    print('<br/>sq=('.$sq.")");
    $ans = executeDB($dbh,$sq);
    print_r($ans);
}
function cmdRead(){
    global $Pa,$Px,$dbh;
    $sq = getPAPX('sq',$Pa,$Px);
    print('<br/>sq=('.$sq.")");
    $ans = readDB($dbh,$sq);
    if (onlogg()==true) { logg('ans'); print_r($ans); }
    if (onlogg()==true) { logg('ans0'); print_r($ans[0]); }
    foreach ($ans as $k1 => $value) {
       foreach ($value as $k2 => $rx) {
           echo "[$k1] . [$k2] . ($rx) <br>";
       }
    }
    print('<br/>done reading');
} // cmdRead

function cmdBlank() {
    // build page
    $t1 = mkTable('t1',1,11,$width='',$height='');
    // t1.1.1 == f1(t2(sq,t2a(b-read,b-ex)))
    $f1 = mkForm($_SERVER['PHP_SELF']);
    $t2 = mkTable('t2',2,1);
    $t2 = str_replace('<!--t2.1.1-->',mkTxtAr('sq')[0],$t2);
    $t2a = mkTable('t2a',1,2);
    $t2a = str_replace('<!--t2a.1.1-->',mkButton('cmd','read',"value='read'")[0],$t2a);
    $t2a = str_replace('<!--t2a.1.2-->',mkButton('cmd','ex',"value='ex'")[0],$t2a);
    $t2 = str_replace('<!--t2.2.1-->',$t2a,$t2);
    $f1 = str_replace('<!--formBody-->',$t2,$f1);
    $f1 = str_replace('<!--hidden-->',pxHids(),$f1);
    $t1 = str_replace('<!--t1.1.1-->',$f1,$t1);
    
    //t1.1.2 == f2(tf2(insert cat vals)
    $f2 = mkForm($_SERVER['PHP_SELF']);
    $f2 = str_replace('<!--hidden-->',pxHids(),$f2);
    $tf2 = mkTable('tf2',7,1);
    $tf2 = str_replace('<!--tf2.1.1-->',mkTxt('Insert')[0],$tf2);
    $tf2 = str_replace('<!--tf2.2.1-->',mkTxt('cix')[0],$tf2);
    $tf2 = str_replace('<!--tf2.3.1-->',mkTxt('subLevel')[0],$tf2);
    $tf2 = str_replace('<!--tf2.4.1-->',mkTxt('Label')[0],$tf2);
    $tf2 = str_replace('<!--tf2.5.1-->',mkTxt('catDir')[0],$tf2);
    //mkTxtAr('sq')[0],$t2);
    $tf2 = str_replace('<!--tf2.6.1-->',mkTxtAr('SeriesS')[0],$tf2);
    $tf2 = str_replace('<!--tf2.7.1-->', mkButton('cmd','I-Cat',"value='ICAT'")[0],$tf2);
    $f2 = str_replace('<!--formBody-->',$tf2,$f2);
    $t1 = str_replace('<!--t1.1.2-->',$f2,$t1);
    
    // t1.1.3 == f3(tf3[3,1]="sqs",stna,stsq,((cmd=sqi))
    $f3 = mkForm($_SERVER['PHP_SELF']);
    $f3 = str_replace('<!--hidden-->',pxHids(),$f3);
    $tf3 = mkTable('tf3',4,1);
    $tf3 = str_replace('<!--tf3.1.1-->',"SQS",$tf3);
    //sqs ( sqname, sqstmt , primary key (sqname) )) 
    $tf3 = str_replace('<!--tf3.2.1-->',mkTxt('sqname')[0],$tf3);
    $tf3 = str_replace('<!--tf3.3.1-->',mkTxtAr('sqstmt')[0],$tf3);
    $tf3 = str_replace('<!--tf3.4.1-->', mkButton('cmd','I-sqs',"value='ISQS'")[0],$tf3);
    $f3 = str_replace('<!--formBody-->',$tf3,$f3);
    $t1 = str_replace('<!--t1.1.4-->',$f3,$t1);
    
    print($t1);
} // cmdBlank
function cmdICAT(){
    global $Pa,$Px,$dbh;
    //dumpPAPX($Pa,$Px);
    $sq = "insert or replace into Cat (cid , subsection , Label, catDir , seriesStatement ) values (";
    $sq = $sq . "'" . getPAPX('cix',$Pa,$Px) . "',"; //cid , 
    $sq = $sq . "'" .getPAPX('subLevel',$Pa,$Px). "',"; //subsection , 
    $sq = $sq . "'" .getPAPX('Label',$Pa,$Px). "',";//Label, 
    $sq = $sq ."'" . getPAPX('catDir',$Pa,$Px). "',";//catDir , 
    $sq = $sq . "'" .getPAPX('SeriesS',$Pa,$Px). "'";//seriesStatement, 
    $sq = $sq . ");";
    print($sq);
    $ans = executeDB($dbh,$sq);
    print_r($ans);
} //ICAT
function cmdISQS(){
    global $Pa,$Px,$dbh;
    $sq = "insert or replace into sqs (sqname , sqstmt ) values (";
    $sq = $sq . "'" . getPAPX('sqname',$Pa,$Px) . "',"; 
    $sq = $sq . "'" . getPAPX('sqstmt',$Pa,$Px) . "'";
    $sq = $sq . ");";
    print($sq);
    $ans = executeDB($dbh,$sq);
    print_r($ans);
} // ISQS
?>

