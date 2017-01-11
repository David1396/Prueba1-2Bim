
from tkinter import *
y=750

ventana = Tk()
ventana.title("Prueba1 --- David Saldaña")
canvas= Canvas(ventana, width=1100, height=600)
canvas.pack()

img1= PhotoImage(file="nave.png")
img= PhotoImage(file="planeta.png")

canvas.create_image(750,50,anchor=NW, image=img1)
canvas.create_image(10,50,anchor=NW, image=img)

def viaje(event):
    global y
    if event.keysym == 'Left':
        canvas.move(1,-15,0)
        y=y-3
        print("coor x: ",1,"y: ",y)
        if y==633:
            print("HAZ ATERRIZADO EXITOSAMENTE!!!!")
      
    else:
        canvas.move(1,3,0)


canvas.bind_all('<KeyPress-Left>',viaje)
canvas.bind_all('<KeyPress-Right>',viaje)


ventana.mainloop()
