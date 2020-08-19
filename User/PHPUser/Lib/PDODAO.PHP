<?php
/* file PDODAO.PHP
pja 3/7/2019 recoded for sqlite 
-- passed 3/7/2019

// test as
include_once ('PDODAO.PHP');
$dbh = openDB('foo.db');
$c = " create table if not exists TCVR ( ix , T , C , V , R , primary key(ix) );";
executeDB($dbh,$c);
$s = "select * from sqlite_master;";
$an = readDB($dbh,$s);
print_r($an);
closeDB($dbh);

*/
//include_once ('llogg.php');
function openDB($databaseName) {
    // open sqlite database returns handle
    try{     
        $dbh = new PDO('sqlite:'.$databaseName);
	}catch (PDOException $e){
            die ('DB Error' . $e);
    } // end open database
    return($dbh);    
}

function openDB_MS($databaseName, $user, $pass) {
    // open database returns handle
    try{     
        $dbh = new PDO('mysql:host=127.0.0.1;dbname='.$databaseName.';charset=utf8', $user , $pass );
	}catch (PDOException $e){
            die ('DB Error' . $e);
    } // end open database
    return($dbh);
      
}

function closeDB($dbh) {
    $dbh = null; // close db
}

function executeDB($dbh,$stmt)
{
    //include_once 'llogg.php';
    $q1p = $dbh->prepare($stmt);
    logg ('<br/>executeDB=='. $stmt);
    $q1p->execute();
} //

function writeDB($dbh,$stmt)
{
    //include_once 'llogg.php';
    logg('<br/>writeDB=='. $stmt);
    executeDB($dbh,$stmt);
} //

function readDB($dbh,$stmt)
{
    //sinclude_once 'llogg.php';
    logg('<br/>readDB=='. $stmt);
    $sq = $dbh->query($stmt);  // exe
    $sm2 = $sq->fetchAll();
    return($sm2); // return set w/o conversion
} //

?>
