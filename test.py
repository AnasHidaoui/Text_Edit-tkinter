
####################################
# import the requirements modules
###################################
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
import tkinter.font
from tkinter import simpledialog
from tkinter import filedialog # filedialog allows user to select where they want to save the file.
from PIL import Image, ImageTk
from tkinter import messagebox
###################################
# this part for the rootwindow:
#####################################"
root_master = Tk()
root_master.geometry('900x600')
root_master.title('Text Editor')
root_master.resizable(0,0)
#######################################
# all variables :
all_font = StringVar()
all_size  = StringVar() 
#######################################
#######################################
# default values
file_name = '' # Current file name.
current_font_family = "Liberation Mono"
current_font_size = 12
fontColor ='#FFF'
fontBackground= '#45596E'
#######################################"
###########################################################
# This part for coding
##########################################################
###########################################
# craet tag
############################################
def make_tag():
    try :
        current_tags = text.tag_names()
        if "bold" in current_tags:
            weight = "bold"
        else:
            weight = "normal"
        if "italic" in current_tags:
            slant = "italic"
        else:
            slant = "roman"

        if "underline" in current_tags:
            underline = 1
        else:
            underline = 0

        if "overstrike" in current_tags:
            overstrike = 1
        else:
            overstrike = 0
        big_font = tkinter.font.Font(text, text.cget("font"))
        big_font.configure(slant= slant ,
                           weight= weight ,
                            underline= underline ,
                            overstrike= overstrike ,
                            family= current_font_family ,
                            size= current_font_size )
        text.tag_config("BigTag", font=big_font , foreground= fontColor , background= fontBackground) 
        if "BigTag" in  current_tags:
            text.tag_remove("BigTag" , 1.0 , END)
            text.tag_add("BigTag" , 1.0 , END)

    except Exception as e :
        print(e)
        
        
########################################
# creat new file
########################################
def new(event=None):
    try :
        file_name = ''  # chage the name of file 
        ans = messagebox.askquestion(title="Save File" , message="Would you like to save this file?")
        if True:
            save()
        delete_all()
    except Exception :
        pass
##########################################
# open new file
###########################################
def open_file(event=None):
    try :
        new()
        file = filedialog.askopenfile()
        global file_name
        file_name = file.name
        text.insert(INSERT , file.read())
    except Exception :
        pass
###########################################
# save file
############################################
def save(event=None):
    try :
        global file_name
        file_name = ''
        if file_name == '':
            path = filedialog.asksaveasfilename()
            file_name = path
            root_master.title(file_name + " - Script Editor")
            with open(file_name,'w') as file :
                file.write(text.get('0.0',END))
    except Exception :
        massgaebox.showerror('Error','Cannot save this file !!')
################################################
# save as
#################################################
def save_as(event=None):
    try :
        if file_name == '':
            save()
            return "break"
        f = filedialog.asksaveasfile(mode='w')
        if f is None: 
                return
        text2save = str(text.get(1.0, END)) 
        f.write(text2save)
        f.close()
    except Exception :
        pass
#######################################################
#rename file
#####################################################
new_name = '' # Used for renaming the file

def rename(event=None):
    try :
        import os # import the os module to rename the file
        global file_name
        if file_name == '':
            open_file()
        arr = file_name.split('/')
        path = ''
        for i in range(0 , len(arr) -1):
            path = path + arr[i] + '/'
        new_name = simpledialog.askstring("Rename", "Enter new name:")
        os.rename(file_name ,path+new_name)
        file_name = str(path) + str(new_name)
        root_master.title(file_name + " - Script Editor")
    except Exception :
        pass
##############################################
# close 
##############################################
def close(event=None):
    try :
        save()
        master.quit()
    except Exception :
        massagebax.showerror('Error','Cannot close this widow !!')
#######################################
# cut 
######################################
def cut(event=None) :
    try :
        # first clear the previous text on the clipboard.
        root_master.clipboard_clear()
        text.clipboard_append(string=text.selection_get())
        #index of the first and yhe last letter of our selection.
        text.delete(SEL_FIRST,SEL_LAST)
    except Exception :
        text.clipboard_append(string='')
        
def copy(event=None):
    # first clear the previous text on the clipboard.
    try :
        print(text.index(SEL_FIRST))
        print(text.index(SEL_LAST))
        root_master.clipboard_clear()
        text.clipboard_append(string=text.selection_get())
    except Exception :
        text.clipboard_append(string='')
#####################################
# paste
#####################################

def paste(event=None):
    try :
		# get gives everyting from the clipboard and paste it on the current cursor position
        # it does'nt removes it from the clipboard.
        text.insert(INSERT, root_master.clipboard_get())
    except Exception :
        pass

##########################################
# delete
###########################################
def delete():
    try :
        text.delete(index1=SEL_FIRST, index2=SEL_LAST)
    except Exception :
        pass

def undo():
    try :
        text.edit_undo()
    except Exception :
        pass

def redo():
    try :
        text.edit_redo()
    except Exception :
        pass

def select_all(event=None):
    try :
        text.tag_add(SEL,'1.0',END)
    except Exception :
        pass

def delete_all():
    try :
        rext.delete(1.0,END)
    except Exception :
        pass
# implementation of search dialog box - calling the check method to search and find_text_cancel_button to close it
def find_text(event=None):
    search_toplevel = Toplevel(root_master)
    search_toplevel.title('Find Text')
    search_toplevel.transient(root_master)
    search_toplevel.resizable(False, False)
    Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')
    search_entry_widget = Entry(search_toplevel, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    search_entry_widget.focus_set()
    Button(search_toplevel, text="Ok",
           underline=0,
           command=lambda: check( search_entry_widget.get())).grid(row=0, column=2, sticky='e' +'w', padx=2, pady=5)
    Button(search_toplevel, text="Cancel", underline=0,
           command=lambda: find_text_cancel_button(search_toplevel)).grid(row=0, column=4, sticky='e' +'w', padx=2, pady=2)

# remove search tags and destroys the search box
def find_text_cancel_button(search_toplevel):
    try :
        text.tag_remove('found', '1.0', END)
        search_toplevel.destroy()
        return "break"
    except Exception :
        pass

# FORMAT BAR METHODS

def bold(event=None):
    try :
        current_tags = text.tag_names()
        if "bold" in current_tags:
        # first char is bold, so unbold the range
            text.tag_delete("bold",  1.0, END)
        else:
            # first char is normal, so bold the whole selection
            text.tag_add("bold", 1.0, END)
            make_tag()
    except Exception :
            pass

def italic(event=None):
    try :
        current_tags = text.tag_names()
        if "italic" in current_tags:
            ext.tag_add("roman",  1.0, END)
            ext.tag_delete("italic", 1.0, END)
        else:
            text.tag_add("italic",  1.0, END)
            make_tag()
    except Exception :
            pass

def underline(event=None):
    try :
        current_tags = text.tag_names()
        if "underline" in current_tags:
            text.tag_delete("underline",  1.0, END)
        else:
            text.tag_add("underline",  1.0, END)
            make_tag()
    except Exception :
            pass

def strike():
    try :
        current_tags = text.tag_names()
        if "overstrike" in current_tags:
            text.tag_delete("overstrike" ,"1.0", END)
        else:
            text.tag_add("overstrike" , 1.0, END)
            make_tag()
    except Exception :
            pass

def highlight():
    try :
        color = colorchooser.askcolor(initialcolor='white')
        color_rgb = color[1]
        global fontBackground
        fontBackground= color_rgb
        current_tags = text.tag_names()
        if "background_color_change" in current_tags:
            text.tag_delete("background_color_change", "1.0", END)
        else:
            text.tag_add("background_color_change", "1.0", END)
            make_tag()
    except Exception :
        pass


# To make align functions work properly
def remove_align_tags():
    try :
        all_tags = text.tag_names(index=None)
        if "center" in all_tags:
            text.tag_remove("center", "1.0", END)
        if "left" in all_tags:
            text.tag_remove("left", "1.0", END)
        if "right" in all_tags:
            text.tag_remove("right", "1.0", END)
    except Exception :
        pass
# align_center
def align_center(event=None):
    remove_align_tags()
    text.tag_configure("center", justify='center')
    text.tag_add("center", 1.0, "end")

# align_justify
def align_justify():
    remove_align_tags()

# align_left
def align_left(event=None):
    remove_align_tags()
    text.tag_configure("left", justify='left')
    text.tag_add("left", 1.0, "end")

# align_right
def align_right(event=None):
    remove_align_tags()
    text.tag_configure("right", justify='right')
    text.tag_add("right", 1.0, "end")

# Font and size change functions - BINDED WITH THE COMBOBOX SELECTION
# change font and size are methods binded with combobox, calling fontit and sizeit
# called when <<combobox>> event is called

def change_font(event):
    try :
        f = all_fonts.get()
        global current_font_family
        current_font_family = f
        make_tag()
    except Exception as e :
        print(e)

def change_size(event):
    sz = int(all_size.get())
    global current_font_size
    current_font_size = sz
    make_tag()

def change_color():
    color = colorchooser.askcolor(initialcolor='#ff0000')
    color_name = color[1]
    global fontColor
    fontColor = color_name
    current_tags = text.tag_names()
    if "font_color_change" in current_tags:
        # first char is bold, so unbold the range
        text.tag_delete("font_color_change", 1.0 , END)
    else:
        # first char is normal, so bold the whole selection
        text.tag_add("font_color_change", 1.0 , END)
        make_tag()

# Adding Search Functionality

def check(value):
    text.tag_remove('found', '1.0', END)
    text.tag_config('found', foreground='red')
    list_of_words = value.split(' ')
    for word in list_of_words:
        idx = '1.0'
        while idx:
            idx = text.search(word, idx, nocase=1, stopindex=END)
            if idx:
                lastidx = '%s+%dc' % (idx, len(word))
                text.tag_add('found', idx, lastidx)
                print(lastidx)
                idx = lastidx

###########################################
# this part for desinger:
###############################################
##############<! CREATING - MENUBAR AND ITS MENUS, TOOLS BAR, FORMAT BAR, STATUS BAR AND TEXT AREA !>##############
########################################<! Tool Bar!>################################
toolbar = Frame(root_master)
# the button toolbar
###########################################<!New!>##################################
photo_new = PhotoImage(file="icons/new.png")
bt_new = Button(toolbar,
             image=photo_new,
             command=new,
             width=27,
                )
######################################<!Save!>#######################################
photo_save = PhotoImage(file="icons/save.png")
bt_save = Button(toolbar,
                 image=photo_save,
                 command=save,
                 width=27)
#####################################<!open!>#################################
photo_open = PhotoImage(file="icons/open.png")
bt_open=Button(toolbar,
               image=photo_open,
               command=open_file,
               width=35)
######################################<!copy!>################################
photo_copy = PhotoImage(file='icons/copy.png')
bt_copy = Button(toolbar,
                 image=photo_copy,
                 command=copy,
                 width=35)
#######################################<!Cut!>###################################
photo_cut = PhotoImage(file='icons/cut.png')
bt_cut = Button(toolbar,
                image = photo_cut,
                command=cut,
                width = 35)
################################<!paste!>######################################
photo_paste = PhotoImage(file='icons/paste.png')
bt_paste = Button(toolbar,
                        image=photo_paste,
                        command=paste,
                        width=35)
################################"<!Redo!>##########################################
photo_redo = PhotoImage(file='icons/redo.png')
bt_redo = Button(toolbar,
                 image=photo_redo,
                 command=redo,
                 width=30)
####################################<!Undo!>###################################
photo_undo = PhotoImage(file='icons/undo.png')
bt_undo = Button(toolbar,
                 image=photo_undo,
                 command=undo,
                 width=30)
####################################<!Find!>###################################
photo_find = PhotoImage(file='icons/find.png')
bt_find = Button(toolbar,
                 image=photo_find,
                 command=undo,
                 width=30)
#################""<! Geometry management for toolbar items!>###################################
toolbar.pack(side='top',fill='x')
bt_new.pack(side='left',padx=4,pady=4)
bt_save.pack(side='left',padx=4,pady=4)
bt_open.pack(side='left',padx=4,pady=4)
bt_copy.pack(side='left',padx=4,pady=4)
bt_cut.pack(side='left',padx=4,pady=4)
bt_paste.pack(side='left',padx=4,pady=4)
bt_redo.pack(side='left',padx=4,pady=4)
bt_undo.pack(side='left',padx=4,pady=4)
bt_find.pack(side='left',padx=4,pady=4)
#####################################################<! Formating bar!>######################################################
formatingbar = Frame(root_master,padx=2,pady=2)

#####################################################<!Combobox<formating bar>!>#####################################################################
# combbox all font
combobox_font = ttk.Combobox(formatingbar,
                             height=60,
                             width=20,
                             textvariable=all_font,
                             state='readonly')
combobox_font['values'] = ( 'Courier',
                            'Helvetica',
                            'Liberation Mono',
                            'OpenSymbol',
                            'Century Schoolbook L',
                            'DejaVu Sans Mono',
                            'Ubuntu Condensed',
                            'Ubuntu Mono',
                            'Lohit Punjabi',
                            'Mukti Narrow',
                            'Meera', 'Symbola',
                            'Abyssinica SIL')
#combobox_font.bind('<<ComboboxSelected>>',change_font)
combobox_font.current(2)
# combobox size
combobox_size = ttk.Combobox(formatingbar,
                             state='readonly',
                             height=60,
                             textvariable=all_size,
                             width=5)
combobox_size['values'] = ('10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30','32','34','36','38','40')
#combobox_font.bind('<<ComboboxSelected>>',change_size)
combobox_size.current(1)
# FORMATBAR BUTTONS
#bold Button
photo_bold = PhotoImage(file='icons/bold.png')
bt_bold = Button(formatingbar,
                 image=photo_bold,
                 borderwidth=1,
                 command=bold,
                 width=28)
# italic Button
photo_italic = PhotoImage(file='icons/italic.png')

bt_italic = Button(formatingbar,
                   image=photo_italic,
                   borderwidth=1,
                   command=italic,
                   width=28)
# underline botton
photo_underline = PhotoImage(file='icons/underline.png')
bt_underline = Button(formatingbar,
                      image=photo_underline,
                      borderwidth=1,
                      command=underline,
                      width=28)
# strike button
photo_strike = PhotoImage(file='icons/strike.png')
bt_strike = Button(formatingbar,
                   image=photo_strike,
                   borderwidth=1,
                   command=strike,
                   width=28)
# font_colore
photo_font_color = PhotoImage(file='icons/font-color.png')
bt_font_color = Button(formatingbar,
                       image=photo_font_color,
                       borderwidth=1,
                       command=change_color,
                       width=28)
# highlight button

photo_highlight = PhotoImage(file='icons/highlight.png')
bt_highlight = Button(formatingbar,
                       image=photo_highlight ,
                       borderwidth=1,
                       command=highlight,
                       width=28)

#align_justify button
photo_align_justify = PhotoImage(file='icons/align-justify.png')
bt_align_justify = Button(formatingbar,
                          image=photo_align_justify,
                          borderwidth=1,
                          command=align_justify,
                          width=30)
# align_left button
photo_align_left = PhotoImage(file='icons/align-left.png')
bt_align_left = Button(formatingbar,
                       image=photo_align_left,
                       borderwidth=1,
                       width=28)
# align_right button
photo_align_right = PhotoImage(file='icons/align-right.png')
bt_align_right = Button(formatingbar,
                        image=photo_align_right,
                        borderwidth=1,
                        command=align_right,
                        width=28)
# STATUS BAR
status = Label(root_master, text="", bd=1, relief=SUNKEN,bg='blue')
status.pack(side="bottom",fill='x')
# CREATING TEXT AREA - FIRST CREATED A FRAME AND THEN APPLIED TEXT OBJECT TO IT.
text_frame = Frame(root_master)#borderwidth=1)#relief="sunken")
# #45596E
text = Text(text_frame,
            wrap="word",
            font=("Liberation Mono", 12),
            background='#11167b',
            insertwidth=3,
            fg='#FFF',
            insertbackground='#FFF',
            selectbackground = '#FFF',
            borderwidth=5,
            highlightthickness=5 ,
            pady=8,
            highlightcolor = '#ff06c9',
            highlightbackground='red',
            undo= True)
scrollbar_text = Scrollbar(text_frame,highlightbackground='red',
                           activebackground='#45596E',
                           bg='#45596E')
text.config(yscrollcommand=scrollbar_text.set)
scrollbar_text.config(command=text.yview)
###################################################<!Geometry management for part text!>###############################
text_frame.pack(side="bottom",fill="both", expand=True)
text.pack(side="left", fill="both", expand=True) # pack text object.
scrollbar_text.pack(side='left',fill='y')
#################################<!geometry management gor formatingbar!>###############################################
formatingbar.pack(side='top',fil='x')
combobox_font.pack(side='left',padx=4,pady=4)
combobox_size.pack(side='left',padx=4,pady=4)
bt_bold.pack(side='left',padx=4,pady=4)
bt_italic.pack(side='left',padx=4,pady=4)
bt_underline.pack(side='left',padx=4,pady=4)
bt_strike.pack(side='left',padx=4,pady=4)
bt_highlight.pack(side='left',padx=4,pady=4)
bt_font_color.pack(side='left',padx=4,pady=4)
bt_align_right.pack(side='left',padx=4,pady=4)
bt_align_left.pack(side='left',padx=4,pady=4)
bt_align_justify.pack(side='left',padx=4,pady=4) 
# the menu....##############################################################################################################
menu = Menu(root_master)
root_master.configure(menu=menu)
#######################################<!creat the princeplle menus!>##########################################################
file_menu = Menu(menu)
# Menu1: File
menu.add_cascade(label='File',menu=file_menu,underline=0)

file_menu.add_command(label="New File",
                      command=new,
                      compound='left',
                      accelerator='Ctrl+N',
                      underline=0)

file_menu.add_command(label='Open',
                      command=open_file,
                      accelerator='Ctrl+O',
                      compound='left',
                      underline = 0      
                      )

file_menu.add_command(label='Save',
                     compound='left',
                      accelerator='Ctrl+S',
                      underline=0
                      )

file_menu.add_command(label='Save as',
                      compound='left',
                      accelerator='Ctrl+shift+S',
                      underline=0
                      )

file_menu.add_command(label='Rename',
                      compound='left',
                      accelerator='Ctrl+R',
                      underline=0
                      )

file_menu.add_command(label='Close',
                      compound='left',
                      accelerator='Ctrl+f4',
                      underline=0
                      )
# Menu2; Edit
edit_menu = Menu(menu)
menu.add_cascade(label='Edit',menu=edit_menu,underline=0)

edit_menu.add_command(label='Undo',
                      accelerator='Ctrl+Z',
                      compound='left',
                      underline=0)

edit_menu.add_command(label='Redo',
                      compound='left',
                      underline=0,
                      accelerator='Ctrl+Y'
                      )

edit_menu.add_separator()  # add separator !

edit_menu.add_command(label='Cut',
                      compound='left',
                      accelerator='Ctrl+X',
                      underline=0)

edit_menu.add_command(label='Copy',
                      compound='left',
                      accelerator='Ctrl+C',
                      underline=0
                      )

edit_menu.add_command(label='Paste',
                      compound='left',
                      accelerator='Ctrl+P',
                      underline=0)

edit_menu.add_command(label='Delelte',
                      compound='left',
                      underline=0)

edit_menu.add_command(label='Select All',
                      compound='left',
                      accelerator='Ctrl+A',
                      underline=0)

edit_menu.add_command(label='Clear All',
                      compound='left',
                      underline=0)
#Menu3: Tool Menu
tool_menu = Menu(menu)
menu.add_cascade(label="Tools", menu=tool_menu, underline=0)

tool_menu.add_command(label="Change Color",
                      command=change_color,
                      underline=0
                      )
tool_menu.add_command(label="Search",
                      command=find_text,
                      compound='left',
                      #image=image_find,
                      accelerator='Ctrl+F',
                      underline=0
                      )
##############################################################################################
# command to add a abot meuny
def about(event=None):
    messagebox.showinfo("About", "Text Editor\nCreated in Python 3 using Tkinter\nCopyright with Anas Hidaoui  2020")
##############################################################################################
help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu, underline=0)
help_menu.add_command(label="About",
                      command=about,
                      accelerator='Ctrl+H',
                      underline=0)



#----- BINDING ALL KEYBOARD SHORTCUTS ---------- #
text.bind('<Control-n>', new)
text.bind('<Control-N>', new) 

text.bind('<Control-o>', open_file)
text.bind('<Control-O>', open_file)

text.bind('<Control-s>', save)
text.bind('<Control-S>', save)

text.bind('<Control-Shift-s>', save_as)
text.bind('<Control-Shift-S>', save_as)

text.bind('<Control-r>', rename)
text.bind('<Control-R>', rename)

text.bind('<Alt-F4>', close)
text.bind('<Alt-F4>', close)

text.bind('<Control-x>', cut)
text.bind('<Control-X>', cut)

text.bind('<Control-c>', copy)
text.bind('<Control-C>', copy)

text.bind('<Control-p>', paste)
text.bind('<Control-P>', paste)

text.bind('<Control-a>', select_all)
text.bind('<Control-A>', select_all)

text.bind('<Control-h>', about)
text.bind('<Control-H>', about)
'''
text.bind('<Control-f>', find_text)
text.bind('<Control-F>', find_text)

text.bind('<Control-Shift-i>', italic)
text.bind('<Control-Shift-I>', italic)

text.bind('<Control-b>', bold)
text.bind('<Control-B>', bold)

text.bind('<Control-u>', underline)
text.bind('<Control-U>', underline)

text.bind('<Control-Shift-l>', align_left)
text.bind('<Control-Shift-L>', align_left)

text.bind('<Control-Shift-r>', align_right)
text.bind('<Control-Shift-R>', align_right)

text.bind('<Control-Shift-c>', align_center)
text.bind('<Control-Shift-C>', align_center)
#----- END : BINDING ALL KEYBOARD SHORTCUTS ---------- #
'''

############################################<!Run the main window!>########################################################
root_master.mainloop()
