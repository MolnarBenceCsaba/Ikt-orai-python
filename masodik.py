from tkinter import *
ablak1 = Tk()
gyoker = 'H:\\IKT python\\masodik feladat github'
ablak1.geometry('800x800')
ablak1.title('CSŐŐŐŐŐŐ')
icon = PhotoImage(file="H:\\IKT python\\masodik feladat github\\Ikt-orai-python\\owo.png")
elsokep = PhotoImage(file="H:\\IKT python\\masodik feladat github\\Ikt-orai-python\\owo.png")
ablak1.iconphoto(True,icon)
ablak1.config(background="pink")
cimke= Label(ablak1,
                text= "OwO",
                fg ="#eb34eb", 
                bg= "#c3cee0", 
               font=('Arial', 200, 'bold'),
               bd=10,
               relief = RAISED,
               padx=15,
               pady=20,
               image=elsokep,
               compound='center'
                ).pack()






ablak1.mainloop()