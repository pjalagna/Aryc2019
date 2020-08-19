<script>
// pickup of GET parameters
function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
}

function getUrlParam(parameter, defaultvalue){
    var urlparameter = defaultvalue;
    if(window.location.href.indexOf(parameter) > -1){
        urlparameter = getUrlVars()[parameter];
        }
    return urlparameter;
}
// <- and -> key functions 
window.onkeyup = function(e) {
   var key = e.keyCode ? e.keyCode : e.which;
//alert('key is' + key);
// get cat
var cat = getUrlParam('cat','Empty');
//alert('cat is' + cat);
// get ix
var ix = getUrlParam('ix','Empty'); 
//alert('ix is' + ix);
   if (key == 37) { // <
       ix--;
       if (ix == 0) { ix =12; } // mod rollover
              window.location = "http://localhost:8080/BigPic.php"+"?cat="+cat+"&ix="+ix;
       
   } else if (key == 39) {
       ix++;
       if (ix == 13) { ix =1; } // mod rollover
       window.location = "http://localhost:8080/BigPic.php"+"?cat="+cat+"&ix="+ix;
   }
}
</script>
