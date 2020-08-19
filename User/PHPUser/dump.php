<?php
/*
file dump.php
pja 1/4/2019
*/
// unpack
print("dump php<br/>");
foreach ($_REQUEST as $key => $vval) {
    print('[' . $key . '] vval=(' . $vval . ")<br/>");
} // foreach
?>