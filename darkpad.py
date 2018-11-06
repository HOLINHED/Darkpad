from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.filedialog import *
import tkinter.font as tkfont
 
#preferences
window = Tk()
window.title("Darkpad [Hacker mode]")
window.geometry("740x563")
window.resizable(width=False, height=False)
window.config(bg="black")
imgicon = PhotoImage(file="icon.png")
window.tk.call("wm", "iconphoto", window._w, imgicon)  

#functionality
def clearText():
	txt.delete('1.0', END)
	
def openFile():
	name = askopenfilename(initialdir="/",filetypes =(("Hack", "*.bat"),("All Files","*.*")),title = "Choose a file")
	
	try:
		file = open(name,"r")
		content = file.read()
		txt.insert("insert", content)
		file.close()
	except:
		messagebox.showinfo("Error", "There was an error reading that file.")

def saveFile():

	content = txt.get("1.0", "end-1c")

	file = asksaveasfilename(initialdir="/", filetypes =(("Hack", "*.bat"),("All Files","*.*")), title = "Choose save location")
	
	try:	
		save = open(file,"w")
		save.write(content)
		save.close()
	except:
		messagebox.showinfo("Error", "There was an error saving that file.")
		
#menu	
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New Hack", command=clearText)
filemenu.add_command(label="Open Hack", command=openFile)
filemenu.add_command(label="Save Hack", command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

#gui items
txt = scrolledtext.ScrolledText(window,width=72,height=28,bg="black",foreground="lime")

#textbox config
txt.config(font=("hack", 13, "normal"))
txt.config(insertbackground="lime")
font = tkfont.Font(font=txt["font"])
tab_width = font.measure(" " * 4)
txt.config(tabs=(tab_width,))

#layout
txt.grid(column=0,row=0)

#display window
window.mainloop()