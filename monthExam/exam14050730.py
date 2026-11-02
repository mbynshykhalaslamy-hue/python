import tkinter as tk
from tkinter import messagebox
import random
# import string


n="abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ0123456789"



def bedast_avardan():


    numRandom=int(add_Entry.get().strip())


    reshteh=''
    for i in range(numRandom):

        numRandom=random.randint(0,len(n)-1)
        charectr=n[numRandom]
        reshteh=reshteh+charectr
        # print(charectr,end='')
    label_result.configure(text=reshteh)






root=tk.Tk()
root.title('برنامه ی  به دست اوردن اعداد و کلمات تصادفی')

tk.Label(root, text="عدد اولی").grid(row=0,column=0,pady=5,padx=5)
add_Entry=tk.Entry(root)
add_Entry.grid(row=0,column=1,pady=5,padx=5)

label_result=tk.Label(root, text="")
label_result.grid(row=4,column=0,pady=5,padx=5)


bedastavardn=tk.Button(root, text='تولید تصادفی', command=bedast_avardan)
bedastavardn.grid(row=2,column=2,pady=5,padx=5)

bedastavardn=tk.Button(root, text='تولید اتوماتیک', command=bedast_avardan2)
bedastavardn.grid(row=2,column=1,pady=5,padx=5)

root.mainloop()


