<?php
/*
file plan2.php

dbtest form
hidden readList
btn name database
btn open
input sql
btn set sql select 
btn readAll to list
btn set index
btn readByIndex
btn close

*/
include_once ("htmlStuff.php");
include_once ('papx.php');
global $Pa,$Px;
list($Pa,$Px) = pxUnpack();


$fr = mkForm($_SERVER['PHP_SELF']);
$fr = str_replace('<!--hidden-->',pxHids(),$fr);

if (getPAPX('psw',$Pa,$Px)==''){
    // display if psw == ''
    $pg = mkPage('plan2','plan2');
    $fr = mkForm($_SERVER['PHP_SELF']);
    $fr = str_replace('<!--hidden-->',pxHids(),$fr);
    $hd1 = mkHidden('psw','proc'); 
    $hd2 = mkHidden('readList',''); //readList
    
    $tb1 = mkTable('tb1',3,8,$width='',$height='') ;
    // <!--tb1.col.row-->
    /*
    $hd1 = mkHidden('psw','proc'); 
    $hd2 = mkHidden('readList',''); //readList
    btn name database
    btn open
    input sql
    btn set sql select 
    btn readAll to list
    btn set index
    btn readByIndex
    btn close
    */
} else {
    // process

} // 'psw'
?>

