<?php
/** file dirt.php
pja 4/8/2019
shows list of files in current directory
*/
    $files = scandir(".",1);
    var_dump($files);
?>
