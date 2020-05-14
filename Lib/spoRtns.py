"""
file spoRtns.py

pja 5/7/2020

routines to write 3-point snowflake arrays into SPO



"""

def spoInit():
    global SPO,Thing,pred
    SPO = {} # [subj][has][obj]
    Thing = {}
    pred = {}
#


def spoPlus(sub,predi,obj):
    global SPO,Thing,pred
    import time
    #does subject exist?
    try:
        tx = SPO[sub]
    except:
        SPO[sub] = {}
        Thing[sub] = ''
    finally:
        nop =1
    #
    #does spo[subject][pred] exist?
    try:
        tx = SPO[sub][predi]
    except:
        SPO[sub][predi] = {}
        pred[predi] = ''
    finally:
        nop =1
    #
    #does spo[subject][pred][obj] exist?
    doagain = 0
    try:
        tx = SPO[sub][predi][obj]
        print('spoPlus DUPLICATE ' + 'sub=(' + sub + ')'+ 'pred=(' + predi + ')' + 'obj=(' + obj + ')')
        doagain = 1
    except:
        SPO[sub][predi][obj] = ''
        Thing[obj] = ''
        print('spoPlus added ' + 'sub=(' + sub.__str__() + ')'+ 'pred=(' + predi.__str__() + ')' + 'obj=(' + obj.__str__() + ')')
    finally:
        nop =1
    #
    if (doagain == 1):
        predx = "(" + predi + '@' + time.time().__str__() + ")"
        print("new predx("+ predx + ")")
        spoPlus(sub,predx,obj)
    #endif    
#spoPlus 
def getspo():
    global SPO
    return(SPO)
#
