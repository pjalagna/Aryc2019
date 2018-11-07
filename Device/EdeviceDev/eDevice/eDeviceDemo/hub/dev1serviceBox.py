#file dev1service
def main(ffile): 
    """ service for dev1 records \n
        passes message to service port
    """
    # send to hub viz "hubaddrSvc.txt.txt"
    fx = open('hubaddrSvc.txt', 'r')
    fx1 = fx.readline()
    fx1 = fx1[:-1]
    ans = ffile  
    import sr232
    sr232.send(fx1, ans )
#end main
