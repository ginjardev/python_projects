from tkinter import *
from parse import *
from math import factorial


app = Tk()

app.title("Calculator")
# app.geometry('600x800')
Label(app, text="").grid(row=0)
display = Entry(app)
display.grid(rows=1, columnspan=6, sticky=N+E+W+S)

#buttons
Button(app, text=1, command=lambda:get_variable(1)).grid(row=2, column=0, sticky=N+S+E+W)
Button(app, text=2, command=lambda:get_variable(2)).grid(row=2, column=1, sticky=N+S+E+W)
Button(app, text=3, command=lambda:get_variable(3)).grid(row=2, column=2, sticky=N+S+E+W)

Button(app, text=4, command=lambda:get_variable(4)).grid(row=3, column=0, sticky=N+S+E+W)
Button(app, text=5, command=lambda:get_variable(5)).grid(row=3, column=1, sticky=N+S+E+W)
Button(app, text=6, command=lambda:get_variable(6)).grid(row=3, column=2, sticky=N+S+E+W)

Button(app, text=7, command=lambda:get_variable(7)).grid(row=4, column=0, sticky=N+S+E+W)
Button(app, text=8, command=lambda:get_variable(8)).grid(row=4, column=1, sticky=N+S+E+W)
Button(app, text=9, command=lambda:get_variable(9)).grid(row=4, column=2, sticky=N+S+E+W)

Button(app, text="AC", command=lambda:clear_all()).grid(row=5, column=0, sticky=N+S+E+W)
Button(app,text=" 0",command = lambda :get_variables(0)).grid(row=5,column=1, sticky=N+S+E+W)
Button(app,text=" .",command = lambda :get_variables(".")).grid(row=5,column=2, sticky=N+S+E+W)

Button(app,text="+", command = lambda :get_operation("+")).grid(row=2,column=3, sticky=N+S+E+W)
Button(app,text="-", command = lambda :get_operation("-")).grid(row=3,column=3, sticky=N+S+E+W)
Button(app,text="*", command = lambda :get_operation("*")).grid(row=4,column=3, sticky=N+S+E+W)
Button(app,text="/", command = lambda :get_operation("/")).grid(row=5,column=3, sticky=N+S+E+W)

Button(app,text="pi", command = lambda :get_operation("*3.14")).grid(row=2,column=4, sticky=N+S+E+W)
Button(app,text="%", command = lambda :get_operation("%")).grid(row=3,column=4, sticky=N+S+E+W)
Button(app,text="(", command = lambda :get_operation("(")).grid(row=4,column=4, sticky=N+S+E+W)
Button(app,text="exp", command = lambda :get_operation("**")).grid(row=5,column=4, sticky=N+S+E+W)

Button(app,text="<-",command= lambda :undo()).grid(row=2,column=5, sticky=N+S+E+W)
Button(app,text="x!", command= lambda: fact()).grid(row=3,column=5, sticky=N+S+E+W)
Button(app,text=")",command= lambda :get_operation(")")).grid(row=4,column=5, sticky=N+S+E+W)
Button(app,text="^2",command= lambda :get_operation("**2")).grid(row=5,column=5, sticky=N+S+E+W)
Button(app,text="^2",command= lambda :get_operation("**2")).grid(row=5,column=5, sticky=N+S+E+W)
Button(app,text="=",command= lambda :calculate()).grid(columnspan=6, sticky=N+S+E+W)


i = 0 
def get_variable(num):
    global i
    display.insert(i, num)
    i+=1


def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i+=length



app.mainloop()
