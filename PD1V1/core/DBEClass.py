class DBE():
        """ lud - 6-13-2013 2200
         DBE --< instance<IName>
                ++ --< database<DBName>

                behaviors 
                DBE.connect(DBPath,DBName)
                DBE.MakeInstance(DBName,IName)
                DBE.Prep(DBPath)
                .CreateTable(IName,TableName,{tv},{tv})
                .DropTable(IName,TableName)
                .write(IName,TableName,{tv})
                {tv} = .ReadRecord(IName,TableName,{tv})

                typical usage 
                import DBEClass
                dd = DBEClass.DBE()
                dd.DBConnect('db1.db','ddi')
                dd.DBMakeInstance('ddi','k1')
                dd.PrepDB('k1')
                dd.CreateTable('k1','alex', [ 'c1' , 'c2', 'c3' , '\0' ] , [ 'c1' , '\0' ])
                dd.Meta('k1','alex')
                dd.WriteRecord('k1', 'alex' , [ 'c1' , 'moxie' , 'c2' , 'dropsy' , 'c3' , 'hopsy' , '\0' ])
                dd.ReadRecord('k1','alex',[ 'c1' , 'moxie' , '\0' ])
 
        """
	def __init__(self):
                import SQClass
		self.myOb = {}
		self.myOb['e'] = SQClass.SQC # no ()
		self.myOb['DB'] = {} # databases
		self.myOb['IName'] = {} # instances 
		
		self.versionn = ' 06-10-2013 0133'
	#end init

	def DBConnect(self, DBPath, DBName ):
		self.myOb['DB'][DBName] = DBPath
	# end connect
	
	def DBMakeInstance(self, DBName, IName):
                """ links Instance name to DB Name """
                self.myOb['IName'][IName] = {}
                self.myOb['IName'][IName]['DB'] = self.myOb['e'](self.myOb['DB'][DBName])
                self.myOb['c'] = {}
                self.myOb['c'][IName] = self.myOb['IName'][IName]['DB'] # shorthand
        #end DBInit
	
	def PrepDB(self, IName):
		t1 = "Create table  if not exists TX ( TName  , CName  , Iteration , primary key (TName , Iteration ) );"
		self.myOb['c'][IName].SQX(t1)
	#end prep
		
	def DBClose(self, IName):
		self.myOb['c'][Iname].SQClose()
	#end DBClose
	
	def CreateTable(self, IName,TName,struct, keyStruct):
		t1 = "Create Table " + TName + " ( "
		ctr = 1
		for c in struct:
			if (c == "\0"):
				nop = -1 # skip
			else:
				t1 = t1 + c + " , "
				# insert into TX
				t2 = "Insert into TX VALUES ( '"  + TName + "' , '" + c + "' , '" + ctr.__str__() + "' );"
				self.myOb['c'][IName].SQX(t2)
				ctr = ctr + 1
			#endif
		#end for
		# backup to last , 
		t1 = t1[:-2]
		# add primary key if any
		if (len(keyStruct) > 1 ):
                        t1 = t1 + ", Primary key ("
                        for c in keyStruct:
                                if (c == "\0"):
                                        nop = -1 # skip
                                else:
                                        t1 = t1 + c + " , "
                                #endif
                        #end for
                        # backup to last , 
                        t1 = t1[:-2]
                        t1 = t1 + " ) "
		else:
		    nop = -1
		#endif
		t1 = t1 + " );"
		print('test','t1',t1)
		self.myOb['c'][IName].SQX(t1)
	#end cre table
	
	def dropTable(self, IName,TName):
		t1 = "drop table " + TName + " ;"
		self.myOb['c'][IName].SQX(t1)
		t2 = "delete from table TX where TName='" + TName + "' ;"
	        self.myOb['c'][IName].SQX(t2)
	#end dropTable
	
	def ReadRecord(self, IName,TName,struct2):
		""" [tv/0] = ReadRecord(IName,TName,[tv/0]) """
		stmt = "select * from " + TName + "  "
		# get condition
		fts = 0
		i = 0
		g1 = struct2[i]
		i = i + 1
		while (g1 != '\0'):
			g2 = struct2[i]
			i = i + 1
			# ftsw where else and
			if (fts == 0):
				fts = 1
				stmt = stmt + "where " + g1+ " ='" + g2 + "'"
			else:
				stmt = stmt + " and " + g1+ " ='" + g2 + "'"
			#endif
                        g1 = struct2[i]
                        i = i + 1
                #wend	
                # add ;
                stmt = stmt + "; "
                print("test","stmt",stmt)
                # get1 and format
		jj= self.myOb['c'][IName].SQReadAll("select * from tx where TName = '" + TName + "' order by iteration ASC ;")
		print('test','jj',jj)
		v2 = self.myOb['c'][IName].SQRead1(stmt)
		print('test','v2',v2)
		ret = []
		ret.append( '\0')
		for i in range(len(jj)):
			try:    
                                ret.append(v2[i]) #  = value
                        except:
                                ret.append("NONE")
                        finally:
                                nop = -1
                        #end try
			ret.append(jj[i][1] ) # = colName
		#end for
		
		print('test','ret',ret)
		return(ret)
	#end readrec
	
	
	def Meta(self,IName,TName):
                """ returns the column names of TN """
                jj= self.myOb['c'][IName].SQReadAll("select * from tx where TName = '" + TName + "' order by iteration ASC;")
		print('test','jj',jj)
		ret = []
		ret.append( '\0')
		for i in range(len(jj)):
			ret.append(jj[i][1] ) # = colName
			print('test','ret',ret)
		#end for
		return(ret)
	#end Meta

                
	def WriteRecord(self,IName,TName,struct2):
                """ WriteRecord(MyName,TName,[\0 val tag] <-- values """
                v1 = {} # list for values
                i = 0
		g1 = struct2[i]
		i = i + 1
		while (g1 != '\0'):
                        g2 = struct2[i]
			i = i + 1
			v1[g1] = g2
			g1 = struct2[i]
                        i = i + 1
			print('test','v1',v1)
		#wwend
		jj= self.myOb['c'][IName].SQReadAll("select * from tx where TName = '" + TName + "' order by iteration ASC ;")
		print('test','jj',jj)
	        stmt = 'Insert into ' + TName + ' VALUES ( '
	        for x in range(len(v1)):
                        stmt = stmt + "'" + v1[jj[x][1]] + "' , "
                        print('test','4stmt',stmt)
                #end for
                stmt = stmt[:-2] # backup onto last comma
                stmt = stmt + ") ;"
                print('test','stmt',stmt)
                self.myOb['c'][IName].SQX(stmt)
        #end def                       
	#end read record
                
	def ReadFirst(self, IName,TName,struct2):
		"""  [tv/0] = ReadFirst(MyName,TName,[tv/0]) """
		# create SQL
		# gen temp table name to self.temp
		# set jacob iteration to self.iteration = 0
		# read and return temp [i] with tx names
		# iteration++
		return('Needs code')
	# end ReadFirst
	def ReadNext(self, IName,TName,struct2):
		"""  [tv/0] = ReadNext(MyName,TName,[tv/0]) """
		# try read and return temp [i] with tx names ;  iteration++
		# else return "status= eof"
                return("needs code ")
	# end ReadNext

	def peekTX(self,IName):
                stmt = "select * from TX ;"
                ans = self.myOb['c'][IName].SQReadAll(stmt)
                return(ans)
        #end peekTX
        def peekTbl(self,IName, TName):
                stmt = "select * from " + TName + " ;"
                ans = self.myOb['c'][IName].SQReadAll(stmt)
                return(ans)
        #end peekTbl
        def peekMaster(self,IName):
                stmt = "select * from SQLite_Master ;"
                ans = self.myOb['c'][IName].SQReadAll(stmt)
                return(ans)
        #end peekTX
        
	
