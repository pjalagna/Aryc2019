#file dev1service
import unpack
def main(ffile): 
    """ service for dev1 records \n
        records dev input record to database via DAO
    """
    # unpack t, msg from message
    lt = unpack.xml1('t',ffile,0)
    lm = unpack.xml1('msg',ffile,0)
    import DAOClass
    d = DAOClass.DAO('Hub.db')
    # write t record
    d.writeTCVR(0,"dev1",'td',lt,lt)
    d.writeTCVR(0,"dev1",'msg',lm,lt)
#end main
