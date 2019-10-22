<?php
/*
file basii.php
pja 10-22-2019

architecture is DB based
a user id is key for threading

usage 
screen basii(user, script/"init", outArea)
table <user> TCVR
-- subtables
--- nds, stk, rstk, llib
----          call stack
----                local lib
*/
//unpack
//script==init?
/// yes
//// create table user as TCVR table
//// append to output "done"
/// no
//// clear nds,stk,rstk, outputArea
//// push script to rstk
//// run pgf(user)
//// append to output "done"
//endif
?>
