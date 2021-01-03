from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])


def view_command(): 
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get().strip().lower(), author_text.get().strip().lower(), genre_text.get().strip().lower(),status_text.get().strip().lower()):
        list1.insert(END, row)
        
def add_command():
    backend.insert(title_text.get().strip().lower(), author_text.get().strip().lower(), genre_text.get().strip().lower(),status_text.get().strip().lower())
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    #list1.delete(0,END)
    #list1.insert(END,(title_text.get(), author_text.get(), genre_text.get()))
    view_command()

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def delete_all_command():
    backend.delete_all()
    view_command()

def update_command():
    backend.update(selected_tuple[0],title_text.get(), author_text.get(), genre_text.get(), status_text.get())
    view_command()

window = Tk()

window.wm_title("Digital Library")

l1 = Label(window,text="Title")
l1.grid(row=0, column = 0)

l2 = Label(window,text="Author")
l2.grid(row=0, column = 2)

l3 = Label(window,text="Genre")
l3.grid(row=1, column = 0)

l4 = Label(window,text="Status")
l4.grid(row=1, column = 2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0,column=3)

genre_text = StringVar()
e3 = Entry(window, textvariable=genre_text)
e3.grid(row=1,column=1)

status_text = StringVar()
e4 = Entry(window, textvariable=status_text)
e4.grid(row=1,column=3)

list1 = Listbox(window, height=10, width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)


sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window, text="View all books",width=30, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window, text="Search the book",width=30, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window, text="Add to the library",width=30, command=add_command)
b3.grid(row=4,column=3)

b4=Button(window, text="Update the book info",width=30,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window, text="Delete the book from library",width=30, command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window, text="Delete everything from library",width=30, command=delete_all_command)
b6.grid(row=7,column=3)

b7=Button(window, text="Close the library",width=30, command=window.destroy)
b7.grid(row=8,column=3)


window.mainloop()