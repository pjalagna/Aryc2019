<?php
/* 
file dbDAO.php
pja 12/12/2018 orig

open,close
getDB
create, write, seek, delete
*/
// base class with member properties and methods
class dbDAO {

   var $fn; // sqlite filename
   var $db; // handle

   function __construct($filename)
   {
       $this->fn = $filename;
   }

   function getFilename()
   {
       return $this->fn;
   }

   function getDB()
   {
       return $this->db;
   }
   function dbOpen($fn) {
       $db = new SQLite3( $fn.'.sqlite', SQLITE3_OPEN_CREATE | SQLITE3_OPEN_READWRITE);
       $this->db = $db;
       $this->fn = $fn;
}
    function dbCreate($query) {
		$db = $this->db;
		// Create a table.
		$db->query($query);
		/* example 'CREATE TABLE IF NOT EXISTS "visits" (
			"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			"user_id" INTEGER,
			"url" VARCHAR,
			"time" DATETIME
		)' */
    } # end dbCreate
    function dbClose(){
        $db = $this->db;
        $db->close();
    } # end dbClose
    function dbWrite($statement){
        $db = $this->db;
        $st = $db->prepare($statement);
        $result = $st->execute();
        return($result);
    } // end dbWrite
    function dbSeek($statement){
       $db = $this->db;
       $st = $db->prepare($statement);
       $result = $st->execute();
       print_r($result->fetchArray(SQLITE3_ASSOC));
       return($result);
    } // end dbSeek
} // end of class dbDAO
