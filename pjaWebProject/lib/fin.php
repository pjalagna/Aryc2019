<?php
function fin($filename) {
    $content = file_get_contents($filename);
    return($content);
} // end fin
function fout($filename,$contents) {
   file_put_contents($filename,$contents);
};
function testfin() {
$box1 = <<<Don
<html>
<head><title> fin trial </title> </head>
<body>
# call print(fin('footerFrame.html'));
</body>
</html>
Don
;
return($box1);
}
?>

