
from tkinter import *

from tkinter import *
from PIL import ImageTk,Image

root = Tk()

canvas = Canvas(root, width = 300, height = 300)      

canvas.pack()   


dictionary_for_areas_nodes = {
    'gulshan iqbal': ImageTk.PhotoImage(Image.open('Areas Nodes/IqbalLoc.png')),
    'gulistane johar': ImageTk.PhotoImage(Image.open('Areas Nodes/JoharLoc.png')),
    'Defence Phase4 5 and Gizri': ImageTk.PhotoImage(Image.open('Areas Nodes/D45GLoc.png')),
    'Clifton block 123': ImageTk.PhotoImage(Image.open('Areas Nodes/C123Loc.png')),
    'Saddar': ImageTk.PhotoImage(Image.open('Areas Nodes/SaddarLoc.png')),
    'Defence Phase 1 and 2': ImageTk.PhotoImage(Image.open('Areas Nodes/D12Loc.png')),
    'north nazimabad': ImageTk.PhotoImage(Image.open('Areas Nodes/NNLoc.png')),
    'garden': ImageTk.PhotoImage(Image.open('Areas Nodes/GardenLoc.png')),
    'Malir cant': ImageTk.PhotoImage(Image.open('Areas Nodes/MalirLoc.png')),
    'Defence Phase 6 7 8': ImageTk.PhotoImage(Image.open('Areas Nodes/D678Loc.png')),
    'Shaheed Milat': ImageTk.PhotoImage(Image.open('Areas Nodes/SeMLoc.png')),
    'Federal area': ImageTk.PhotoImage(Image.open('Areas Nodes/FBLoc.png')),
    'Clifton block 7 8 9': ImageTk.PhotoImage(Image.open('Areas Nodes/C789Loc.png')),
    'Bahadurabad': ImageTk.PhotoImage(Image.open('Areas Nodes/BahadurabadLoc.png')),
    'Clifton Cant': ImageTk.PhotoImage(Image.open('Areas Nodes/CCLoc.png')),
    'PECHS': ImageTk.PhotoImage(Image.open('Areas Nodes/PECHSLoc.png'))
}


canvas.create_image(20,20,anchor=NW, image=dictionary_for_areas_nodes['gulshan iqbal']) 

mainloop()