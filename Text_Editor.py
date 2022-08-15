!pip install tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# Defining TextEditor class
class TextEditor:
    
    #defining consturctor
    def __init__(self, root):
        
        #assigning root
        self.root = root
        
        #title of the window
        self.root.title("TEXT EDITOR")
        
        #Window size or geometery
        self.root.geometry("1200x700+200+150")
        
        #Initializing filename
        self.filename = None
        
        #Declaring Title variable
        self.title = StringVar()
        
        #Declaring Status variable
        self.status = StringVar()
        
        #Creating titlebar
        self.titlebar = Label(self.root, textvariable = self.title, font = ('times new roman', 15, 'bold'), bd = 2, relief = GROOVE)
        #Packing titlebar to root window
        self.titlebar.pack(side = TOP, fill = BOTH)
        #Calling set title function
        self.settitle()
        
        #Creating Statusbar
        self.statusbar = Label(self.root, textvariable = self.status, font = ('times new roman', 15, 'bold'), bd = 2, relief = GROOVE)
        #Packing statusbar to root window
        self.statusbar.pack(side = BOTTOM, fill = BOTH)
        # Initializing Status
        self.status.set('Welcome to Text Editor')
        
        # Creating Menubar
        self.menubar = Menu(self.root, font = ('times new roman', 12, 'bold'), activebackground = 'skyblue')
        # Configuring menubar on root window
        self.root.config(menu = self.menubar)
        
        # Creating filemenu
        self.filemenu = Menu(self.menubar, font = ('times new roman', 12, 'bold'), activebackground = 'skyblue', tearoff = 0)
        # Adding New file command
        self.filemenu.add_command(label = 'New', accelerator = 'Ctrl+N', command = self.newfile)
        # Adding Open file command
        self.filemenu.add_command(label = 'Open', accelerator = 'Ctrl+O', command = self.openfile)
        # Adding Save file command
        self.filemenu.add_command(label = 'Save', accelerator = 'Ctrl+S', command = self.savefile)
        # Adding Save As file command
        self.filemenu.add_command(label = 'Save As', accelerator = 'Ctrl+A', command = self.saveasfile)
        # Adding Separator
        self.filemenu.add_separator()
        # Adding Exit window command
        self.filemenu.add_command(label = 'Exit', accelerator = 'Ctrl+E', command = self.exit)
        # Cascading file menu to menubar
        self.menubar.add_cascade(label = 'File', menu = self.filemenu)
        
        # Creating Edit menu
        self.editmenu = Menu(self.menubar, font = ('times new roman', 12, 'bold'), activebackground = 'skyblue', tearoff = 0)
        # Adding Cut text command
        self.editmenu.add_command(label = 'Cut', accelerator = 'Ctrl+X', command = self.cut)
        # Adding Copy text command
        self.editmenu.add_command(label = 'Copy', accelerator = 'Ctrl+C', command = self.copy)
        # Adding Paste text command
        self.editmenu.add_command(label = 'Paste', accelerator = 'Ctrl+V', command = self.paste)
        # Adding Separator
        self.filemenu.add_separator()
        # Adding Undo text command
        self.editmenu.add_command(label = 'Undo', accelerator = 'Ctrl+U', command = self.undo)
        # Cascading editmenu to menubar
        self.menubar.add_cascade(label = 'Edit', menu = self.editmenu)
        
        #Creating Help menu
        self.helpmenu = Menu(self.menubar, font = ('times new roman', 12, 'bold'), activebackground = 'skyblue', tearoff = 0)
        # Adding About text command
        self.editmenu.add_command(label = 'About', command = self.infoabout)
        # Cascading editmenu to menubar
        self.menubar.add_cascade(label = 'Help', menu = self.helpmenu)
        
        # Creating Scrollbar
        scrol_y = Scrollbar(self.root, orient = VERTICAL)
        # Creating Text area
        self.txtarea = Text(self.root, yscrollcommand = scrol_y.set, font = ('times new roman', 15, 'bold'), state = 'normal', relief = GROOVE)
        # Packing Scrollbar to root window
        scrol_y.pack(side = RIGHT, fill = Y)
        # Adding Scrollbar to text area
        scrol_y.config(command = self.txtarea.yview)
        # Packing Text Area to root window
        self.txtarea.pack(fill = BOTH, expand = 1)
        # Calling shortcuts function
        self.shortcuts()
        
    # Defining set title function
    def settitle(self):
        # Checking if file name is not None
        if self.filename:
            # Updating Title as filename
            self.title.set(self.filename)
        else:
            # Updating Title as Untitled
            self.title.set('Untitled')
    
    # Defining New file Function
    def newfile(self, *args):
        # Clearing the Text Area
        self.txtarea.delete('1.0', END)
        # Updating filename as None
        self.filename = None
        # Calling settitle function
        self.settitle()
        # Updating status
        self.status.set('New File Created')
        
    # Defining Open File Function
    def openfile(self, *args):
        # Exception Handling
        try:
            # Asking for file to open
            self.filename = filedialog.askopenfilename(title = 'Select file', filetypes = (("All Files", '*.*'), ('Text Files', '*.txt'), ('Python Files', '*.py')))
            # Checking if filename not none
            if self.filename:
                # Opening file in readmode
                infile = open(self.filename, 'r')
                # Clearing text area
                self.txtarea.delete('1.0', END)
                # Inserting data line by line into text area
                for line in infile:
                    self.txtarea.insert(END, line)
                # Closing the file
                infile.close()
                # Calling Set title
                self.settitle()
                # Updating Status
                self.status.set('Opened file successfully')
        except Exception as e:
            messagebox.showerror('Exception', e)
            
    # Defining Save File Fuction
    def savefile(self, *args):
        # Exception Handling
        try:
            # checking if filename not none
            if self.filename:
                # Reading the data from text area
                data = self.txtarea.get('1.0', END)
                # Opening file in writemode
                outfile = open(self.filename, 'w')
                # Writing data into file
                outfile.write(data)
                # Closing file
                outfile.close()
                # Calling set title
                self.settitle()
                # Updating status
                self.status.set('Saved Successfully')
            else:
                self.saveasfile()
        except Exception as e:
            messagebox.showerror('Exception', e)
            
    # Defining Save As File function
    def saveasfile(self, *args):
        # Exception Handling
        try:
            # Asking for filename and type to save
            untitledfile = filedialog.asksaveasfilename(title = 'Save file As', defaultextension = '.txt', initialfile = 'Untitled.txt', filetypes = (('AllFiles', '*.*'), ('Text Files', '.txt'), ('Python Files', '.py')))
            # Reading the data from text area
            data = self.txtarea.get('1.0', END)
            # Opening file in writemode
            outfile = open(untitledfile, 'w')
            # Writing data into file
            outfile.write(data)
            # Closing file
            outfile.close()
            # Updating filename as Untitled
            self.filename = untitledfile
            # Calling set title
            self.settitle()
            # Updating status
            self.status.set('Saved Successfully')
        except Exception as e:
            messagebox.showerror('Exception', e)
            
    # Defining Exit function
    def exit(self, *args):
        op = messagebox.askyesno('WARNING', 'You may loose unsaved data')
        if op > 0:
            self.root.destroy()
        else:
            return
    
    # Defining Cut Function
    def cut(self, *args):
        self.txtarea.event_generate('<<CUT>>')
        
    # Defining Copy Function
    def copy(self, *args):
        self.txtarea.event_generate('<<COPY>>')
        
    # Defining Paste Function
    def paste(self, *args):
        self.txtarea.event_generate('<<PASTE>>')
        
    # Defining Undo function
    def undo(self, *args):
        # Exception Handling
        try:
            # Checking if filename is none
            if self.filename:
                # Clearing Text Area
                self.txtarea.delete('1.0', END)
                # Opening file in read mode
                infile = open(self.filename, 'r')
                # Inserting data Line by line into text area
                for line in infile:
                    self.txtarea.insert(END, line)
                # Closing File
                infile.close()
                # Calling Set title
                self.settitle()
                # Updating Status
                self.status.set('Undone Successfully')
            else:
                # Clearing Text Area
                self.txtarea.delete('1.0', END)
                # Updating filename as None
                self.filename = None
                # Calling set title
                self.settitle()
                # Updating status
                self.status.set('Undone Successfully')
        except Exception as e:
            messagebox.showerror('Exception', e)
            
    # Defining About function
    def infoabout(self):
        messagebox.showinfo('About Text Editor', 'A Simple Text Editor\nCreated using Python.')
        
    # Defining Shortcuts Function
    def shortcuts(self):
        # Binding Ctrl+n to newfile function
        self.txtarea.bind('<Control-n>', self.newfile)
        # Binding Ctrl+o to openfile function
        self.txtarea.bind('<Control-o>', self.openfile)
        # Binding Ctrl+s to savefile function
        self.txtarea.bind('<Control-s>', self.savefile)
        # Binding Ctrl+a to saveasfile function
        self.txtarea.bind('<Control-a>', self.saveasfile)
        # Binding Ctrl+e to exit function
        self.txtarea.bind('<Control-e>', self.exit)
        # Binding Ctrl+x to cut function
        self.txtarea.bind('<Control-x>', self.cut)
        # Binding Ctrl+c to copy function
        self.txtarea.bind('<Control-c>', self.copy)
        # Binding Ctrl+v to paste function
        self.txtarea.bind('<Control-v>', self.paste)
        # Binding Ctrl+u to undo function
        self.txtarea.bind('<Control-u>', self.undo)
        
# Creating TK Container
root = Tk()
# Passing root to TextEditor Class
TextEditor(root)
# Root Window looping
root.mainloop()
