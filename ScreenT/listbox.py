"""
File listbox.py
Pja 02-24-2020

Creates, fills, and retains selected item value

test as
import listbox
m = listbox.main()
# make selection and exit window
# refocus onto python
m

"""
def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    ws = w.__str__()
    index = int(w.curselection()[0])
    value = w.get(index)
    print 'You selected item %d: "%s"' % (index, value)
    global n
    n.set(ws[1:]+"::" +value)
    print(ws[1:]+"::" +value)
    
#

def main():
    import Tkinter
    tt = Tkinter
    page = tt.Tk()

    # set up storage
    global m,n
    m = tt.StringVar() # listset
    n = tt.StringVar() # selected value

    # setup listbox on page
    Lb1 = tt.Listbox(page,listvariable=m,name='eLb1')
    Lb1.grid(row=7,column=7)

    #add some values
    Lb1.insert("end", "(no selection)")
    Lb1.insert("end", "Python")
    Lb1.insert("end", "Perl")
    Lb1.insert("end", "C")
    Lb1.insert("end","PHP")
    Lb1.insert("end", "JSP")
    Lb1.insert("end", "Ruby")

    # bind to event
    Lb1.bind('<<ListboxSelect>>', onselect)

    # execute page
    page.mainloop()

    # on exit n.get() will expose selected value
    return(n.get())
#






