import tkinter
import csv
import tkinter.messagebox
class CSVproject:
    def __init__(self):
        self.root=tkinter.Tk()
        b1=tkinter.Button(self.root,text='Add record',command=self.writerec,width=50)
        b2=tkinter.Button(self.root,text='Display record',command=self.readrec,width=50)
        b3=tkinter.Button(self.root,text='Search record',command=self.searchrec,width=50)
        b4=tkinter.Button(self.root,text='Delete record',command=self.delrec,width=50)
        b5=tkinter.Button(self.root,text='Modify record',command=self.modifyrec,width=50)
        b6=tkinter.Button(self.root,text='Exit',command=self.root.destroy,width=50)
        b1.pack()
        b2.pack()
        b3.pack()
        b4.pack()
        b5.pack()
        b6.pack()
        tkinter.mainloop()






        
    ##for adding records:
    def writerec(self):
        self.root.destroy()
        self.root1=tkinter.Tk()
        self.l1=tkinter.Label(self.root1,text='Enter the name:')
        self.e1=tkinter.Entry(self.root1,width=50)
        self.l1.pack()
        self.e1.pack()
        self.l2=tkinter.Label(self.root1,text='Enter the Class:')
        self.e2=tkinter.Entry(self.root1,width=50)
        self.l2.pack()
        self.e2.pack()
        self.l3=tkinter.Label(self.root1,text='Enter the Fees:')
        self.e3=tkinter.Entry(self.root1,width=50)
        self.l3.pack()
        self.e3.pack()
        self.b1=tkinter.Button(self.root1,text='SAVE RECORD',command=self.savedata,width=30)
        self.b1.pack()
        self.b2=tkinter.Button(self.root1,text='BACK',command=lambda:[self.root1.destroy(),self.__init__()],width=30)
        self.b2.pack()
    def savedata(self):
        rec=[]
        Name=self.e1.get()
        Class=self.e2.get()
        Fees=self.e3.get()
        rec.append([Name,Class,Fees])
        with open("record.csv",'a',newline='')as f:
            wr=csv.writer(f,delimiter=',')
            for row in rec:
                wr.writerow(row)
        
        #completed
        













    
    #for displaying records:
    def readrec(self):
        self.root.destroy()
        self.root2=tkinter.Tk()
        self.listbos=tkinter.Listbox(self.root2,width=50)
        self.listbos.pack(side='left',fill='both')
        self.scrolbar=tkinter.Scrollbar(self.root2)
        self.scrolbar.pack(side='right',fill='both')
        with open("record.csv",'r') as f:
            cr=csv.reader(f)
            for row in cr:
                self.listbos.insert('end',row)
        self.listbos.config(yscrollcommand=self.scrolbar.set)
        self.scrolbar.config(command=self.listbos.yview)
        self.b=tkinter.Button(self.root2,text='BACK',command=lambda:[self.root2.destroy(),self.__init__()])
        self.b.pack()
        #completed








        
    #for deleting records:
    def delrec(self):
        self.root.destroy()
        self.root3=tkinter.Tk()
        self.l1=tkinter.Label(self.root3,text='Enter the name(for delete the record):')
        self.l1.pack()
        self.e1=tkinter.Entry(self.root3,width=50)
        self.e1.pack()
        self.b1=tkinter.Button(self.root3,text='DELETE RECORD',command=self.deleterecord,width=30)
        self.b1.pack()
        self.b2=tkinter.Button(self.root3,text='BACK',command=lambda:[self.root3.destroy(),self.__init__()],width=30)
        self.b2.pack()
    def deleterecord(self):
        nm=str(self.e1.get())
        found=False
        with open("record.csv",'r') as f:
            cr=csv.reader(f)
            rec=[]
            for row in cr:
                if (nm!=row[0]):
                    rec.append(row)
                else:
                    found=True
        with open("record.csv",'w',newline='') as f:
            wr=csv.writer(f,delimiter=',')
            wr.writerows(rec)
            if found==True:
                tkinter.messagebox.showinfo('Result',"Record found and deleted")
            else:
                tkinter.messagebox.showinfo('Result',"Record not found and not deleted")
        #completed
    









    
    #for searching records:
    def searchrec(self):
        self.root.destroy()
        self.root4=tkinter.Tk()
        self.l1=tkinter.Label(self.root4,text='Enter the name to see his record:')
        self.e1=tkinter.Entry(self.root4,width=50)
        self.l1.pack()
        self.e1.pack()
        self.b1=tkinter.Button(self.root4,text='SEARCH RECORD',command=self.searchrecord,width=30)
        self.b2=tkinter.Button(self.root4,text='BACK',command=lambda:[self.root4.destroy(),self.__init__()],width=30)
        self.b1.pack()
        self.b2.pack()
    def searchrecord(self):
        nm=self.e1.get()
        Found=False
        with open("record.csv",'r') as f:
            cr=csv.reader(f)
            for row in cr:
                if (nm==row[0]):
                    tkinter.messagebox.showinfo('Result',row)
                    Found=True
            if Found==False:
                tkinter.messagebox.showinfo('Result',"Record not found...")
        #Completed











    
    #for modifying records:
    def modifyrec(self):
        self.root.destroy()
        self.root5=tkinter.Tk()
        self.l1=tkinter.Label(self.root5,text='Enter the name to modify his record:')
        self.en=tkinter.Entry(self.root5,width=50)
        self.l1.pack()
        self.en.pack()
        self.b1=tkinter.Button(self.root5,text='MODIFY RECORD',command=self.modifyrecord,width=30)
        self.b2=tkinter.Button(self.root5,text='BACK',command=lambda:[self.root5.destroy(),self.__init__()],width=30)
        self.b1.pack()
        self.b2.pack()
    def modifyrecord(self):
        nm=self.en.get()
        self.found=False
        with open("record.csv",'r') as f:
            cr=csv.reader(f)
            self.rec=[]
            for row in cr:
                if (nm==row[0]):
                    self.found=True
                    self.root5.destroy()
                    self.root6=tkinter.Tk()
                    label=tkinter.Label(self.root6,text='Old data:'+str(row))
                    label.pack()
                    self.l1=tkinter.Label(self.root6,text='Enter the name:')
                    self.e1=tkinter.Entry(self.root6,width=50)
                    self.l1.pack()
                    self.e1.pack()
                    self.l2=tkinter.Label(self.root6,text='Enter the Class:')
                    self.e2=tkinter.Entry(self.root6,width=50)
                    self.l2.pack()
                    self.e2.pack()
                    self.l3=tkinter.Label(self.root6,text='Enter the Fees:')
                    self.e3=tkinter.Entry(self.root6,width=50)
                    self.l3.pack()
                    self.e3.pack()
                    self.b1=tkinter.Button(self.root6,text='UPDATE RECORD',command=self.mr,width=30)
                    self.b1.pack()
                    self.b2=tkinter.Button(self.root6,text='BACK',command=lambda:[self.root6.destroy(),self.__init__()],width=30)
                    self.b2.pack()
                else:
                    self.rec.append(row)
            if self.found==False:
                tkinter.messagebox.showinfo('Result',"Record not found...")
                    
    def mr(self):
        Name=self.e1.get()
        Class=self.e2.get()
        Fees=self.e3.get()
        self.rec.append([Name,Class,Fees])
                
        with open("record.csv",'w',newline='') as f:
            wr=csv.writer(f,delimiter=',')
            wr.writerows(self.rec)
            if self.found==True:
                tkinter.messagebox.showinfo('Result',"Record has been updated..")

        #completed
            
                
        
    






myproject=CSVproject()








#This program is written by Muhammad Yasir Hussain
