<?php
/*
file dbDAO_tester.PHP
pja 2/17/2019 review
pja 12/12/2018
*/
print('db tester running </br>');
include_once 'dbDAO.php';
$g = new dbDAO('tic');
$g->dbOpen('tic');
print('db tester running </br>');
print($g->getFilename());

$sqlC = "create table IF NOT EXISTS TCVR ( ix, T , C , V , R , primary key(ix) );";
$g->dbCreate($sqlC);
// add data
$ix = 0;

$t = 'cat';
$r = '-';
$ix = $ix + 1;
$c = 'picURL';
$v = 'nowhere.php';
$sqlI = 'INSERT INTO "TCVR" ("ix", "T", "C" , "V", "R") VALUES ($ix, $t, $c , $v, $r );';
$g->dbWrite($sqlI);

$ix = $ix + 1;
$c = 'descURL';
$v = 'notes.txt';
$sqlI = 'INSERT INTO "TCVR" ("ix", "T", "C" , "V", "R") VALUES ($ix, $t, $c , $v, $r );';
$g->dbWrite($sqlI);

// read
$sqlS = ' select * from TCVR;';
$result = $g->dbSeek($sqlS);
#print_r($result);
print('<br/> select size=(' . count($result) . ")");
// dump
foreach($result as $x => $x_value) {
    print "Key=" . $x . ", Value=" . $x_value;
    print "<br>";
}

$sqlCC = 'select count(*) from TCVR;';
$resultC = $g->dbSeek($sqlCC);
#print_r($resultC);
print('<br/> selectCC size=(' . count($resultC) . ")");
foreach($resultC as $x => $x_value) {
    print "Key=" . $x . ", Value=" . $x_value;
    print "<br>";
}
// */
?>

