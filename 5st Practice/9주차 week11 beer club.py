from tkinter import *

class App(Frame):
    def __init__(self,window):
        super().__init__(window)
        self.pack(padx=20,pady=20)
        self.create_widgets()

    def create_widgets(self):
        Label(self,text="Name").grid(row=0,column=0,sticky=E)
        self.name=Entry(self,width=10)
        self.name.grid(row=0,column=1)
        Label(self,text="Email").grid(row=1,column=0,sticky=E)
        self.email=Entry(self,width=10)
        self.name.grid(row=1,column=1)
        Label(self,text="@skku.edu").grid(row=1,column=2,sticky=W)
        self.sex=StringVar()
        self.sex.set(None)
        Label(self,text="Sex").grid(row=2,column=0,sticky=E)
        Radiobutton(self,text='male',variable=self.sex,value='male').grid(row=2,column=1)
        Radiobutton(self,text='female',variable=self.sex,value='female').grid(row=2,column=2,sticky=W)
        Label(self,text="Favorites").grid(row=3,column=1)
        self.largers=BooleanVar()
        Checkbutton(self,text="Larger",variable=self.largers).grid(row=4,column=0)
        self.wheetbeer=BooleanVar()
        Checkbutton(self,text="Wheet beer",variable=self.largers).grid(row=4,column=1)
        self.pilsners=BooleanVar()
        Checkbutton(self,text="Pilsners",variable=self.largers).grid(row=4,column=2)
        self.paleales=BooleanVar()
        Checkbutton(self,text="Pale Ale",variable=self.largers).grid(row=4,column=0)
        self.indiapaleales=BooleanVar()
        Checkbutton(self,text="India Pale Ale",variable=self.largers).grid(row=4,column=0)
        self.stouts=BooleanVar()
        Checkbutton(self,text="Stout",variable=self.largers).grid(row=4,column=0)

        Button(self,text="Register",command=self.write_summary).grid(row=6,column=0,columnspan=3,skicky=S)
        self.summary=Text(self,width=48,height=10,wrap=WROD)
        self.summary.grid(row=7,column=0,columnspan=3,sticky=S)
        Button(self,text="Quit",command=self.quit).grid(row=8,columnn=0,columnspan=3)

    def write_summary(self):
        summary="Name : "+self.name.get()+"\n"
        summary+="Email : "+self.email.get()+"@skku.edu\n"
        summary+="Sex : "+self.sex.get()+"\n"
        summary+="Favorites are :"
        if self.largers.get():
            summary+="Largers,"
        if self.wheetbeer.get():
            summary+="wheet beers,"
        if self.pilsners.get():
            summary+="pilsners,"
        if self.paleales.get():
            summary+="pale ales,"
        if self.indiapaleales.get():
            summary+="india pale ales,"
        if self.stouts.get():
            summary+="stouts,"
        summary+="..."
        self.summary.delete(0.0,END)
        self.summary.insert(0.0,summary)

window=Tk()
window.title("Beer club")
window.geometry("400x420")
App(window)
window.mainloop()
        
        
