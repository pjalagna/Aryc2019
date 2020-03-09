<?php
/* file zPDOClass.php
pja 9/20/2019 added SQ protection on writes
$dbh = openDB($db);
$sq = "select * from sqlite_master";
$ans1 = readDB($dbh,$sq);
var_dump($ans1);
pja 5/23/2019 - needs rtn to create tables
pja 5/23/2019 - edits for db name
pja 3/11/2019 edits
pja 3/8/2019 cloned from zDAO to redit to use sqlite db
-- init() will store sql into table SQS ((recix) sqn* , sqstr)
NOT COMPLETE 
cats --< catix >0-- profile
T: cats ((recix) catid* , subsection, SeriesStatement, catDir, CatLabel)

T: catix ((recix) [cat,ix]*,pix)

T: profile ((recix) pix*,artStatement,picURL**1,PicLabel)

T: journal ((picURL,count) date,eventType,contactID,notes)
each picture has a journal entry updated for each event type (submission, acceptance, showing, sold, rejected, other)

T: contact ((contactID) Fname, Lname, businessName, address, city, state, zip)
T: contactEmail ((contactID,count) Email)
T: contactPhone ((contactID,count) Phone)

*=unique index
**1 note: picURL is full path.

== methods
init
getdbh($dbn) - handle from dbName
zOpen,zClose, getdbh

M: zByCatIx(token,cix,ix)
token:: catRec, catIxRec
catid* , subsection, SeriesStatement, catDir, CatLabel, catPix
catMax, catIxMax
::

M: writeCat,writeCatIx,writeProfile

M:(token,pix)
token:: ProfileRec, picURL, PLabel, artStatement, ixMax, profileMax ::
*/
include_once 'LocalIniStuff.php'; //local
global $libLoc,$dbn;
$libLoc = getLini('libLoc');
$dbn =  getLini('dbn');
include_once ($libLoc .'llogg.php');
include_once ($libLoc .'fin.php');
include_once ($libLoc .'strParser.php');
include_once ($libLoc .'zDAOPDO.php');
include_once ($libLoc .'PDODAO.PHP');
include_once ($libLoc .'SQSQ.PHP');

function zByCatIx($db,$token,$cat,$ix){
	// open db
	$dbh = openDB($db);
	switch ($token) {
	    case ('dbh'):
	        $ans = $dbh;
	    break;
	    case ('catMax'):
	        $sq = "select count(*) from Cat;";
	        $ans1 = readDB($dbh,$sq);
	        $ans = $ans1[0][0];
	        closeDB($dbh);
	        break;
	    case ('catList'):
	        $sq = "select cid from cat;";
	        $ans1 = readDB($dbh,$sq);
	        $ans = $ans1;
	        closeDB($dbh);
	        break;
	    case ('catIxMax'):
	        $sq = "select count(*) from catix where cat = '" . $cat . "';";
	        $ans1 = readDB($dbh,$sq);
	        $ans = $ans1[0][0];
	        closeDB($dbh);
	        break;
	    case ('catixRecAR'):
	        $sq = "select * from catix where cat ='".$cat."' and ix='".$ix."';";
	        $ans1 = readDB($dbh,$sq);
	        $ans = $ans1[0];
	        closeDB($dbh);
	    break;
		case ('catRec'):
		    $sq = "select * from cat where cid ='".$cat."';";
	        $ans1 = readDB($dbh,$sq);
	        $ans = $ans1[0];
	        closeDB($dbh);
		break;
		case ('CLabel'):
		    // get datRec
		    $sq = "select Label from Cat where cid = '" . $cat . "';";
	        $ans1 = readDB($dbh,$sq);
	        $ans = $ans1[0][0];
	        logg($ans);
	        closeDB($dbh);
		break;
		//SeriesStatement
		case ('SeriesStatement'):
		    $sq = "select seriesStatement from Cat where cid = '" . $cat . "';";
	        $ans1 = readDB($dbh,$sq);
	        $ans = $ans1[0][0];
	        logg($ans);
	        closeDB($dbh);
		    // get Label
		break;
		//<subsection></subsection>
		case ('subsection'):
		    $sq = "select subsection from Cat where cid = '" . $cat . "';";
	        $ans1 = readDB($dbh,$sq);
	        $ans = $ans1[0][0];
	        logg($ans);
	        closeDB($dbh);
		break;
		case ('catDir'):
		    $sq = "select catDir from Cat where cid = '" . $cat . "';";
	        $ans1 = readDB($dbh,$sq);
	        $ans = $ans1[0][0];
	        logg($ans);
	        closeDB($dbh);
		break;
		//catixProfile
		case ('catixProfile'):
		    
		    $sq = "select pix from CatIx where cat ='".$cat."' and ix='".$ix."';";
	        $ans1 = readDB($dbh,$sq);
	        $ans = $ans1[0][0];
	        logg($ans);
	        closeDB($dbh);
	    break;
		//ProfileRec
		case ('ProfileRec'):
		    // compound profile(pix<-cat.pix(cat,ix)
		    $a1 =  zByCatIx($db,'catixProfile',$cat,$ix);
		    $a2 = zByPix($db,'profileRec',$a1);
		    $ans = $a2[0][0];
		    // zpix('pix)
		break;
		//picURL
		case ('picURL'):
		    // compound profile.picURL(pix<-cat.pix(cat,ix))
		    $sq = "select picURL from profile 
where pix in (select pix from catix where cat = '".$cat."' and ix= '".$ix."');";
            $a1 = readDB($dbh,$sq);
            $ans = $a1[0][0];
		break;
		//pic <label></label>
		case ('picLabel'):
		    // compound profile.picLabel(pix<-cat.pix(cat,ix))
		    
		break;
		//<artStatement></artStatement>
		case ('artStatement'):
		    // compound profile.artStement(pix<-cat.pix(cat,ix))
		    
		break;
	} //switch
	if (onlogg()==true) { print('zAns'); print_r($ans); }
	return($ans);
} // 
function writeCatIxRec($db,$catid,$index,$Pix){
    $dbh = openDB($db);
    $sq = "insert or replace into catix ( cat, ix, pix) values ('". $catid."','".$index."','".$Pix."');";
    logg("WcatIxRec=(" . $sq . ")");
    $a1 = executeDB($dbh,$sq);
    closeDB($dbh);
    
}// end writeCatIxRec
function writeCatRec($db, $cid,$subsection,$LabelR,$catDirR,$seriesStatementR){
    $dbh = openDB($db);
    $Label = SQin($LabelR);
    $catDir = SQin($catDirR);
    $seriesStatement = SQin($seriesStatementR);
    $sq = "insert or replace into Cat ( cid , subsection , Label, catDir , seriesStatement ) values (" ."'".$cid."','".$subsection."','".$Label."','".$catDir."','".$seriesStatement."');";
    logg("WcatRec=(" . $sq . ")");
    $a1 = executeDB($dbh,$sq);
    closeDB($dbh);
} // writeCatRec
function zByPix($db, $token,$Pix){
	// get by db
	/* profile ( pix,picURL,artStatement,Label)
*/
	$dbh = openDB($db);
	switch ($token) {
	    ////ProfileRec, picURL, PLabel, artStatement,pixmax
		case ('ProfileRec'):
		   $sq = "select * from profile where pix = '" . $Pix ."';";
		   $a1 = readDB($dbh,$sq);
		   $ans = $a1[0];
		   closeDB($dbh);
		break;
		//picURL
		case ('picURL'):
		    $sq = "select picURL from profile where pix = '" . $Pix ."';";
		   $a1 = readDB($dbh,$sq);
		   $ans = $a1[0][0];
		   closeDB($dbh);
		break;
		//PLabel, artStatement
		case ('PLabel'):
		    $sq = "select Label from profile where pix = '" . $Pix ."';";
		   $a1 = readDB($dbh,$sq);
		   $ans = $a1[0][0];
		   closeDB($dbh);
		break;
		//artStatement
		case ('artStatement'):
		    $sq = "select artStatement from profile where pix = '" . $Pix ."';";
		   $a1 = readDB($dbh,$sq);
		   $ans = $a1[0][0];
		   closeDB($dbh);
		break;
		case ('pixMax'):
		    $sq = "select count(*) from profile;";
		    $a1 = readDB($dbh,$sq);
		    $ans=$a1[0][0];
		    logg($ans);
		    closeDB($dbh);
		break;
	}//switch
	return($ans);
} //
function inPix($db, $picURL){
    // returns 0 if no else x>0
    $dbh = openDB($db);
    $sq = "select picURL from profile where picURL = '".$picURL."';";
    $a1 = readDB($dbh,$sq);
    return(count($a1));
} // inPix
function writePixRec($db,$pix,$PLabel,$picURL,$ArtStmt){
    // picURL is complete path name
    $dbh = openDB($db);
    $sq = "insert or replace into profile (  pix, picURL, artStatement, Label ) values ( '".$pix ."','". $picURL."','".$ArtStmt."','".$PLabel."');" ;
    logg("WpixRec=(" . $sq . ")");
    $a1 = executeDB($dbh,$sq);
    closeDB($dbh);
} //end writePixRec
function DelCatRec($db,$cix,$all=''){
    // delete cat record 
    $dbh = openDB($db);
    if ($all=='') {
        $sq = "delete  from Cat where cid ='".$cix."';";
    }  else {
        $sq = "delete  from Cat;";
    }
    logg('del cat sq=('.$sq.")");
    $a1 = executeDB($dbh,$sq);
    closeDB($dbh);
} // DelCatRec
function DelPixRec($db,$pix,$all=''){
    // delete cat record 
    $dbh = openDB($db);
    if ($all=='') {
        $sq = "delete  from profile where pix ='".$pix."';";
    } else {
        $sq = "delete from profile where pix !='';"; // all
    }//endif all
    logg('delPix sq=('.$sq.")");
    $a1 = executeDB($dbh,$sq);
    closeDB($dbh);
} // DelpixRec
function DelCatIxRec($db,$cix,$ix,$all=''){
    // delete catix record 
    $dbh = openDB($db);
    // if ix =0 clear all of cat
    if ($ix==0) {//235
        $sq = "delete  from Catix where cat ='".$cix."';";
    } else {//235
        $sq = "delete  from Catix where cat ='".$cix."' and ix = '".$ix."';";
    }//235
    if ($all != '') { $sq="delete  from Catix"; }
    logg('del catIx sq=('.$sq.")");
    $a1 = executeDB($dbh,$sq);
    closeDB($dbh);
} // DelCatixRec
?>