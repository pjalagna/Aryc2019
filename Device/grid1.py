from Tkinter import *

# callback
def act1():
    global e1
    print("e1=" + e1.get())
#end act1

# paint
master = Tk()
#master.geometry('200x210+350+70')
master.geometry('400x210+350+70')


Label(master, text="First").grid(row=0, sticky=W)
Label(master, text="Second").grid(row=1, sticky=W)

global e1
e1 = Entry(master)
e2 = Entry(master)

e3 = Button(master, text="b" , command=act1)
ROW = 0
e1.grid(row=ROW, column=1)
ROW = 1
e2.grid(row=ROW, column=1)
e3.grid(row=4, column=3)

master.mainloop()

"""
test 2 :- Blood_Pressure is Pressure_normal / test 2 ;

bundle b1 :-
    Rule 6 :-
          test1 : temp is Temp_normal              ( Y N )
          test2 :                                  ( Y Y )
          test3 : lung_sounds are clear_LungSounds ( Y Y )
          end
          act1 :                                   ( X )
          act2 :                                   ( - x )
          otherwise : act4 .
    / Rule 6 ;
/ Bundle b1 ;

"""
