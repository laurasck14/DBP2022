#!/usr/bin/env python3
''' Laura Santa Cruz Kaster
'''
import sys, os, re
import tkinter as tk
import tkinter.ttk as ttk
from GuiBaseClass import GuiBaseClass
import tkinter.filedialog as filedialog
import LauraSantaCruzUniProtParser2 as ProtParser2

class UniProtGui(GuiBaseClass):
    def __init__(self,root,dirname,args):
        super().__init__(root)
        mnu=self.getMenu('File')
        mnu.insert_command(0, label='Open dir...', command=self.fileOpen)
        mf = self.getFrame()

        # we create two frames one for the top and one for the bottom
        frtop = ttk.Frame(mf)
        frtext = ttk.Frame(mf)
        # create all the panedwindow,listbox,textbox stuff
        self.pw = ttk.PanedWindow(frtext, orient='horizontal')
        self.lb_files = tk.Listbox(self.pw, exportselection=False)
        self.text = tk.Text(frtext, wrap='word',undo=True)
        # for some reason you have to use this grid stuff
        self.pw.grid()
        self.lb_files.grid()
        self.pw.add(self.lb_files) #add lb and textbox to pw
        self.pw.add(self.text)
       
        # Combobox placed on the topframe, label for text description
        lab = ttk.Label(frtop, text='Select an option') #label on the main frame
        lab.grid(row = 0, column = 1)
        self.svar = tk.StringVar() # get the imput from selection
        combo = ttk.Combobox(frtop, width= 20,textvariable=self.svar)
        combo['values']=('GO','KEGG','DOI') #options where to chooose from
        combo.grid(column=1,row=5) # not sure
        #print(self.svar.get()) # get the imput from selection
        #test.current()

        frtop.pack(side='top')
        frtext.pack(side='top', fill='both', expand=True)
        self.pw.pack(side='top', fill='both', expand=True)

        self.addStatusBar() #status bar with filename

        def selection(event):
            if not self.svar.get():
                self.message("Please select an option")

            elif self.lb_files.curselection():
                filename = self.lb_files.get(self.lb_files.curselection())
                opt = self.svar.get()
                #print('file:',filename,'\n command:',opt)

                if 'GO' in opt:
                    sol = ProtParser2.get_go_ids(filename)
                    self.text.insert('1.0',sol)
                    
                elif 'KEGG' in opt:
                    sol = ProtParser2.get_keggs_ids(filename)
                    self.text.insert('1.0',sol)

                elif 'DOI' in opt:
                    sol = ProtParser2.get_doi_ids(filename)
                    self.text.insert('1.0',sol) 

        self.lb_files.bind('<Double-1>', selection)

        #open filedialog in case no dirname is given and see the files in the directory if given
        self.dirname = dirname
        if (dirname == "" or dirname == "-"):
            self.fileOpen()
        else:
            dirname = args[1]
            all_files = os.listdir(dirname)
            self.message("Directory searched: "+ os.path.basename(dirname))
            for filename in all_files:
                self.lb_files.insert('end',filename)

    def fileOpen (self,dirname=''):
        if dirname == "" or not(os.path.exists(dirname)):
            dirname=filedialog.askdirectory(
                title='Select a directory',
                initialdir=os.path.dirname(self.dirname))
            all_files = os.listdir(dirname)        

        if dirname != "":
            for filename in all_files:
                #self.lb_files.insert('end',filename)
                self.message("Directory searched: "+ os.path.basename(dirname))
               
                # We only include in the display the files that end in .dat or .dat.gz
                if re.search('.+(dat|dat.gz$)',filename):
                    self.lb_files.insert('end',filename)

def main (args):
    # if no filename is provided we open the gui app and the option to give a filename
    if len(args) == 1:
        dirname=''
        root=tk.Tk()
        root.geometry("700x500")
        root.title("UniprotParser3Combo")
        bapp = UniProtGui(root,dirname,args) 
        bapp.mainLoop()

    if len(args) > 1:
        dirname= args[1]
        root=tk.Tk()
        root.geometry("700x500")
        root.title("UniprotParser3Combo")
        bapp = UniProtGui(root,dirname,args) 
        bapp.mainLoop()

if __name__ == "__main__":
   main(sys.argv)