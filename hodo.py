from tkinter import *

bor = int(input('Mennyi bor?'))

foablak = Tk()

foablak.geometry('250x200')

gomb3 = Button(foablak, text = "Kiszámít")

gomb3.pack(side=RIGHT)


mezo1 = Entry(foablak)


mezo1.pack(side=RIGHT)

mezo2 = Entry(foablak)


mezo2.pack

mezo3 = Entry(foablak)


mezo3.pack(side=RIGHT)

mezo4 = Entry(foablak)


mezo4.pack(side=RIGHT)

mezo5 = Entry(foablak)


mezo5.pack(side=RIGHT)

foablak.mainloop()