import tkinter as tk


class riaze:
    def zarb(self):

        self.add*self.add1



    def taksim(self):

        self.add/self.add1



    def game(self):

        self.add+self.add1
        
        


    def menha(self):

        self.add-self.add1
        
       
        

    def __init__(self):

        if self.op=='*':
            self.zarb()

        if self.op=='/':
            self.taksim()

        if self.op=='+':
            self.game()

        if self.op=='-':
            self.menha()
        


root=tk.Tk()
tk.title('برنامه ی حل بعضی از مسال ریاضی')

tk.Label(root, text="عدد اولی").grid(row=0,column=0,pady=5,padx=5)
add_Entry=tk.Entry(root)
add_Entry.grid(row=0,column=1,pady=5,padx=5)

tk.Label(root, text="عدد اولی").grid(row=1,column=0,pady=5,padx=5)
add_Entry=tk.Entry(root)
add_Entry.grid(row=1,column=1,pady=5,padx=5)

bedastavardn=tk.Button(root, taxt='حل کردن', command="zarb")
bedastavardn.grid(row=2,column=2,pady=5,padx=5)

bedastavardn=tk.Button(root, taxt='حل کردن', command="taksim")
bedastavardn.grid(row=3,column=2,pady=5,padx=5)

bedastavardn=tk.Button(root, taxt='حل کردن', command="game")
bedastavardn.grid(row=4,column=2,pady=5,padx=5)

bedastavardn=tk.Button(root, taxt='حل کردن', command="menha")
bedastavardn.grid(row=5,column=2,pady=5,padx=5)

root.mainloop()