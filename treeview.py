from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root, text='Treeview')
label.pack()

treeview = ttk.Treeview(root)
treeview.pack()

treeview.insert('', '0', 'item1', text='First Item')
treeview.insert('', '1', 'item2', text='Second Item')
treeview.insert('', 'end', 'item3', text='Third Item')


logo = PhotoImage(file='C:\\Users\\Paopao\\Pictures\\python.gif').subsample(10, 10)
treeview.insert('item2', 'end', 'python', text='Python', image = logo)

treeview.config(height=5)

treeview.move('item2', 'item1', 'end')

treeview.item('item1', open=True)


if __name__ == '__main__':
    mainloop()
