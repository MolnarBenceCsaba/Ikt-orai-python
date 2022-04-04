from tkinter import *



foablak = Tk()

foablak.geometry('550x200')

gomb3 = Button(foablak, text = "Kiszámít")

gomb3.pack(side=RIGHT)


mezo1 = Entry(foablak)

cimke2 = Label(foablak, text="Mennyiség ")

cimke2.pack(side=RIGHT)
mezo1.pack(side=RIGHT)

mezo2 = Entry(foablak)

cimke3 = Label(foablak, text="hány cm")

cimke3.pack(side=RIGHT)
mezo2.pack

mezo3 = Entry(foablak)


mezo3.pack(side=RIGHT)
cimke1 = Label(foablak, text="Dolgok")

cimke1.pack(side=RIGHT)
mezo4 = Entry(foablak)

mezo4.pack(side=RIGHT)


mezo5 = Entry(foablak)

mezo5.pack(side=RIGHT)

foablak.mainloop()