import tkinter as tk

window = tk.Tk()
var = tk.IntVar()
var.set(0)
f = open("solvent.txt","w")
window.title("Choose the Solvent")
dict={0:"chloroform",1:"CH2Cl2",2:"water",3:"methanol",4:"acetonitrile",5:"dmso",6:"thf",7:"pyridine",8:"acetone",9:"benzene"}
checkboxs = {}
def change_state():
    f.write(dict[var.get()])
    window.quit()
for x,y in dict.items():
    tk.Radiobutton(window,text = y,indicatoron = 0,variable = var,value = x,width = 30).pack()
tk.Button(window,text = "OK",command = change_state).pack()
window.mainloop()
f.close()