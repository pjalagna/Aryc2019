#file hubStart.py
""" load and go agent to spawn processes of hub """
import thread
import sr232
import Hub
r1 = thread.start_new_thread(sr232.listenStart,('dev1',5,))
r2 = thread.start_new_thread(sr232.listenStart,('svc1',5,))
r3 = thread.start_new_thread(sr232.listenStart,('disp1',5,))
h1 = thread.start_new_thread(Hub.main,('dev1',))
h1 = thread.start_new_thread(Hub.main,('svc1',))
h1 = thread.start_new_thread(Hub.main,('disp1',))
print( 'hub started - ctl-c to stop')
c = 1
while(c==1):
    pass
#wend
