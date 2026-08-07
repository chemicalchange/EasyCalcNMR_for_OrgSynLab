import tkinter as tk
import tkinter.filedialog as fd

f = open("info.txt","w")
dirname = fd.askdirectory(initialdir = "/home/dinglab/calculation/temp",title = "Select the Output Directory")
f.write(dirname + '\n')
window = tk.Tk()
window.title("Enter the Filename of the Output zip File and Your Email Address")
task = tk.Entry(window,width = 80)
email = tk.Entry(window,width = 80)
tk.Label(window,text = "Filename").grid(row = 0,column = 0)
tk.Label(window,text = "Email address").grid(row = 1,column = 0)
task.grid(row = 0,column = 1)
email.grid(row = 1,column = 1)
def change_state():
    f.write(task.get()+"\n")
    f.write(email.get()+"\n")
    window.quit()
tk.Button(window,text="Start Calculation",command=change_state).grid(row = 2,columnspan = 2)
window.mainloop()
f.close()