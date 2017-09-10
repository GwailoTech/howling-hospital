'''
    Name:         CHEO_02.py
    Created:      2017-08-27 20:54
    Creator:      Craig Davis
    Last Updated: 2017-09-02
------------------------------------------------------------------------------------------------------------------------
--   Date  | Developer   | Procedure            | Comments
------------------------------------------------------------------------------------------------------------------------
--  170827 | DavisC      | CHEO_BCMA_KIOSK      | Added Additional UTL_FILE calls for exceptions
--  170902 | DavisC      | CHEO_BCMA_KIOSK      | Corrected button issue (outside of class)
--         |             |                      | Updated the frame size and added widgets
--         |             |                      | Replaced referential version with older style for personal clarity
--  170903 | DavisC      | ZPLII.aztec          | Created class ZPLII
--         |             |                      | Created function aztec
--         |             | CHEOBCMAKiosk        | Changed class name to CamelCase
--  170904 | DavisC      |                      | Replaced Canvas object with Message Object
--         |             |                      | Replaced import tkinter * with specific list
--  170905 | DavisC      |                      | Working on Radio Group - INCOMPLETE
--  170907 | DavisC      |                      | Replaced MessageBox with Text
--         |             |                      | Added mouse click events to the text box
--         |             |                      |
--         |             |                      |
--         |             |                      |
------------------------------------------------------------------------------------------------------------------------

STILL TO DO !!!
    Enhance button click based on WHICH mouse button was clicked
    Add <Enter> and <Leave> event handling
    REF: http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm

'''

# Don't use! Poor form:
# from tkinter import *

try:
    from Tkinter import Tk, Button, Entry, Label, Message, Radiobutton, IntVar, END, N, E, W, S, Canvas, RIDGE, SUNKEN, \
        LEFT, RIGHT, TOP, BOTTOM, X, Y, StringVar, Text, Scrollbar, scrolledtext, DISABLED, NORMAL
except ImportError:
    from tkinter import Tk, Button, Entry, Label, Message, Radiobutton, IntVar, END, N, E, W, S, Canvas, RIDGE, SUNKEN, \
        LEFT, RIGHT, TOP, BOTTOM, X, Y, StringVar, Text, Scrollbar, scrolledtext, DISABLED, NORMAL

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = CHEOBCMAKiosk(root)
    ' Change Program Icon '
    root.iconbitmap('CHEOBear.ico')
    root.mainloop()
    #root.rdo


' @@@ ??? '
w = None


def create_CHEOBCMAKiosk(root, *args, **kwargs):
    ' Starting point when module is imported by another program. '
    global w, w_win, rt
    rt = root
    # w = Toplevel(root)
    top = CHEOBCMAKiosk(w)
    return w, top

'''==================================================================================================================---
--- Main class ... encapsulates all GUI objects
---=================================================================================================================='''


class CHEOBCMAKiosk:
    def __init__(self, top=None):
        ' "It is a good habit, when building any type of GUI component, to keep a reference to our parent" '
        self.top = top
        top.geometry("600x450+525+240")
        top.title("CHEO BCMA KIOSK")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        '''------------------------------------------------------------------------------------------------------
        Begin Build Text Box '''
        self.TextBox = Text(top)
        self.TextBox.place(relx=0.2, rely=0.15, relheight=0.34, relwidth=0.64)
        self.TextBox.configure(background="white")
        self.TextBox.configure(borderwidth="2")
        self.TextBox.configure(highlightbackground="#d9d9d9")
        self.TextBox.configure(highlightcolor="black")
        self.TextBox.configure(relief=RIDGE)
        self.TextBox.configure(takefocus="no")
        ' Bind mouse clicks '
        self.TextBox.bind("<Button-1>",self.textbox_text)
        self.TextBox.bind("<Button-2>",self.textbox_text)
        self.TextBox.bind("<Button-3>",self.textbox_text)
        ' Initial value '
        self.TextBox.insert(END, "This is the initial text.")
        ' Disable content from user entry '
        self.TextBox.config(state=DISABLED)

        self.LabelTitle = Label(top)
        self.LabelTitle.place(relx=0.03, rely=0.03, height=19, width=311)
        self.LabelTitle.configure(activebackground="#f9f9f9")
        self.LabelTitle.configure(activeforeground="black")
        self.LabelTitle.configure(background="#d9d9d9")
        self.LabelTitle.configure(disabledforeground="#a3a3a3")
        self.LabelTitle.configure(foreground="#000000")
        self.LabelTitle.configure(highlightbackground="#d9d9d9")
        self.LabelTitle.configure(highlightcolor="black")
        self.LabelTitle.configure(text='''Welcome to the CHEO self-serve BCMA employee barcode kiosk''')
        ''' End Build Canvas
        ------------------------------------------------------------------------------------------------------'''

        ''' Build Buttons
        ------------------------------------------------------------------------------------------------------'''
        # Print Button
        self.ButtonPrint = Button(top)
        self.ButtonPrint.configure(command=self.printBut)
        self.ButtonPrint.place(relx=0.42, rely=0.89, height=21, width=31)
        self.ButtonPrint.configure(text='''Print''')
        self.ButtonPrint.configure(underline="0")
        self.ButtonPrint.configure(default='active')
        self.ButtonPrint.configure(takefocus='Yes')
        # Close Button
        self.ButtonClose = Button(top)
        self.ButtonClose.configure(command=quit)
        self.ButtonClose.place(relx=0.55, rely=0.89, height=21, width=35)
        self.ButtonClose.configure(activebackground="#d9d9d9")
        self.ButtonClose.configure(activeforeground="#000000")
        self.ButtonClose.configure(background="#d9d9d9")
        self.ButtonClose.configure(disabledforeground="#a3a3a3")
        self.ButtonClose.configure(foreground="#000000")
        self.ButtonClose.configure(highlightbackground="#d9d9d9")
        self.ButtonClose.configure(highlightcolor="black")
        self.ButtonClose.configure(pady="0")
        self.ButtonClose.configure(text='''Close''')
        self.ButtonClose.configure(underline="0")
        ''' End Build Buttons
        ------------------------------------------------------------------------------------------------------'''

        ''' Begin Build Radio Group
        ------------------------------------------------------------------------------------------------------'''
        # Default Radio Button Source to TAP
        self.input_source = StringVar()
        self.input_source.set('TAP')

        # Tap Data Entry Radio
        self.rdo_TAP = Radiobutton(top)
        self.rdo_TAP.place(relx=0.8, rely=0.82, relheight=0.05, relwidth=0.14)
        self.rdo_TAP.configure(activebackground="#d9d9d9")
        self.rdo_TAP.configure(activeforeground="#000000")
        self.rdo_TAP.configure(background="#d9d9d9")
        self.rdo_TAP.configure(disabledforeground="#a3a3a3")
        self.rdo_TAP.configure(foreground="#000000")
        self.rdo_TAP.configure(highlightbackground="#d9d9d9")
        self.rdo_TAP.configure(highlightcolor="black")
        self.rdo_TAP.configure(justify=LEFT)
        self.rdo_TAP.configure(text='Tap Reader')
        self.rdo_TAP.configure(underline="0")
        self.rdo_TAP.configure(value='TAP')
        self.rdo_TAP.configure(variable=self.input_source)
        self.rdo_TAP.configure(command= self.radio_toggle)
        # Manual Data Entry Radio
        self.rdo_MAN = Radiobutton(top)
        self.rdo_MAN.place(relx=0.8, rely=0.89, relheight=0.05, relwidth=0.15)
        self.rdo_MAN.configure(activebackground="#d9d9d9")
        self.rdo_MAN.configure(activeforeground="#000000")
        self.rdo_MAN.configure(background="#d9d9d9")
        self.rdo_MAN.configure(disabledforeground="#a3a3a3")
        self.rdo_MAN.configure(foreground="#000000")
        self.rdo_MAN.configure(highlightbackground="#d9d9d9")
        self.rdo_MAN.configure(highlightcolor="black")
        self.rdo_MAN.configure(justify=LEFT)
        self.rdo_MAN.configure(text='Manual Entry')
        self.rdo_MAN.configure(underline="0")
        self.rdo_MAN.configure(value="MAN")
        self.rdo_MAN.configure(variable=self.input_source)
        self.rdo_MAN.configure(command=self.radio_toggle)
        ''' End Build Radio Group
        ------------------------------------------------------------------------------------------------------'''

        ''' Begin Fixed Labels
        ------------------------------------------------------------------------------------------------------'''
        # Last Name
        self.LabelLastName = Label(top)
        self.LabelLastName.place(relx=0.1, rely=0.56, height=19, width=56)
        self.LabelLastName.configure(activebackground="#f9f9f9")
        self.LabelLastName.configure(activeforeground="black")
        self.LabelLastName.configure(background="#d9d9d9")
        self.LabelLastName.configure(disabledforeground="#a3a3a3")
        self.LabelLastName.configure(foreground="#000000")
        self.LabelLastName.configure(highlightbackground="#d9d9d9")
        self.LabelLastName.configure(highlightcolor="black")
        self.LabelLastName.configure(text='''Last Name''')
        # First Name
        self.LabelFirstName = Label(top)
        self.LabelFirstName.place(relx=0.1, rely=0.62, height=19, width=57)
        self.LabelFirstName.configure(activebackground="#f9f9f9")
        self.LabelFirstName.configure(activeforeground="black")
        self.LabelFirstName.configure(background="#d9d9d9")
        self.LabelFirstName.configure(disabledforeground="#a3a3a3")
        self.LabelFirstName.configure(foreground="#000000")
        self.LabelFirstName.configure(highlightbackground="#d9d9d9")
        self.LabelFirstName.configure(highlightcolor="black")
        self.LabelFirstName.configure(text='''First Name''')
        # AD User Name
        self.LabelADUserName = Label(top)
        self.LabelADUserName.place(relx=0.07, rely=0.69, height=19, width=75)
        self.LabelADUserName.configure(activebackground="#f9f9f9")
        self.LabelADUserName.configure(activeforeground="black")
        self.LabelADUserName.configure(background="#d9d9d9")
        self.LabelADUserName.configure(disabledforeground="#a3a3a3")
        self.LabelADUserName.configure(foreground="#000000")
        self.LabelADUserName.configure(highlightbackground="#d9d9d9")
        self.LabelADUserName.configure(highlightcolor="black")
        self.LabelADUserName.configure(text='''AD User Name''')
        # AD Password
        self.LabelADPassword = Label(top)
        self.LabelADPassword.place(relx=0.08, rely=0.76, height=19, width=70)
        self.LabelADPassword.configure(activebackground="#f9f9f9")
        self.LabelADPassword.configure(activeforeground="black")
        self.LabelADPassword.configure(background="#d9d9d9")
        self.LabelADPassword.configure(disabledforeground="#a3a3a3")
        self.LabelADPassword.configure(foreground="#000000")
        self.LabelADPassword.configure(highlightbackground="#d9d9d9")
        self.LabelADPassword.configure(highlightcolor="black")
        self.LabelADPassword.configure(text='''AD Password''')
        ''' End Fixed Labels
        ------------------------------------------------------------------------------------------------------'''

        ''' Begin Data Entry
        ------------------------------------------------------------------------------------------------------'''
        # Last Name
        self.EntryLastName = Entry(top)
        self.EntryLastName.place(relx=0.2, rely=0.56, relheight=0.04, relwidth=0.34)
        self.EntryLastName.configure(background="white")
        self.EntryLastName.configure(disabledforeground="#a3a3a3")
        self.EntryLastName.configure(font="TkFixedFont")
        self.EntryLastName.configure(foreground="#000000")
        self.EntryLastName.configure(highlightbackground="#d9d9d9")
        self.EntryLastName.configure(highlightcolor="black")
        self.EntryLastName.configure(insertbackground="black")
        self.EntryLastName.configure(selectbackground="#c4c4c4")
        self.EntryLastName.configure(selectforeground="black")
        ' Bind mouse clicks '
        self.EntryLastName.bind("<Button-1>",self.lastname_text)
        self.EntryLastName.bind("<Button-2>",self.lastname_text)
        self.EntryLastName.bind("<Button-3>",self.lastname_text)
        'self.EntryLastName.configure(state=readonly)'
        ' First Name '
        self.EntryFirstName = Entry(top)
        self.EntryFirstName.place(relx=0.2, rely=0.62, relheight=0.04, relwidth=0.34)
        self.EntryFirstName.configure(background="white")
        self.EntryFirstName.configure(disabledforeground="#a3a3a3")
        self.EntryFirstName.configure(font="TkFixedFont")
        self.EntryFirstName.configure(foreground="#000000")
        self.EntryFirstName.configure(highlightbackground="#d9d9d9")
        self.EntryFirstName.configure(highlightcolor="black")
        self.EntryFirstName.configure(insertbackground="black")
        self.EntryFirstName.configure(selectbackground="#c4c4c4")
        self.EntryFirstName.configure(selectforeground="black")
        '''self.EntryFirstName.configure(label="Hi There")
        readonly = 'readonly'
        self.EntryFirstName.configure(state=readonly)'''
        ' AD User Name '
        self.EntryADUserName = Entry(top)
        self.EntryADUserName.place(relx=0.2, rely=0.69, relheight=0.04, relwidth=0.34)
        self.EntryADUserName.configure(background="white")
        self.EntryADUserName.configure(disabledforeground="#a3a3a3")
        self.EntryADUserName.configure(font="TkFixedFont")
        self.EntryADUserName.configure(foreground="#000000")
        self.EntryADUserName.configure(highlightbackground="#d9d9d9")
        self.EntryADUserName.configure(highlightcolor="black")
        self.EntryADUserName.configure(insertbackground="black")
        self.EntryADUserName.configure(selectbackground="#c4c4c4")
        self.EntryADUserName.configure(selectforeground="black")
        readonly = 'readonly'
        self.EntryADUserName.configure(state=readonly)
        ' Data Payload '
        self.EntryADPassword = Entry(top)
        self.EntryADPassword.place(relx=0.2, rely=0.76, relheight=0.04, relwidth=0.34)
        self.EntryADPassword.configure(background="white")
        self.EntryADPassword.configure(disabledforeground="#a3a3a3")
        self.EntryADPassword.configure(font="TkFixedFont")
        self.EntryADPassword.configure(foreground="#000000")
        self.EntryADPassword.configure(highlightbackground="#d9d9d9")
        self.EntryADPassword.configure(highlightcolor="black")
        self.EntryADPassword.configure(insertbackground="black")
        self.EntryADPassword.configure(selectbackground="#c4c4c4")
        self.EntryADPassword.configure(selectforeground="black")
        '''readonly = 'readonly'
        self.EntryADPassword.configure(state=readonly)'''
        ''' End Data Entry Fields
        ------------------------------------------------------------------------------------------------------'''

        ''' Begin Status Bar
        ------------------------------------------------------------------------------------------------------'''
        # Create a sunken status bar in the root object with a border
        self.status_text = StringVar()   # Displays live status
        self.status_text.set("Hello")
        self.status = Label(root, textvariable=self.status_text, bd=1, relief=SUNKEN, anchor=W)  # anchor to the West (Left)
        self.status.pack(side=BOTTOM, fill=X)  # display
        ''' End Status Bar
        ------------------------------------------------------------------------------------------------------'''

    ' Print Button Function'

    def printBut(self):
        ' Instantiate ZPLII Class '
        ' ??? @@@ '
        print('Print button has been pressed')
        print('Current values... ' + str(self.EntryFirstName))
        self.status = "Q"
        # self.input_source.set(_self.input_source.Get)


    def radio_toggle(self):
        ' @@@ '
        selection = self.input_source.get()
        print('Radio button is ' + selection)
        self.status_text.set("Radio toggled to " + selection)


    def textbox_text(self, event):
        print('Text Box Event - ' + str(event))
        ' Enable before insert '
        if self.TextBox["state"] == DISABLED:
            self.TextBox.config(state=NORMAL)
        self.TextBox.insert(END,"\nMouse click in TextBox")
        ' Disable after insert '
        self.TextBox.config(state=DISABLED)

    def lastname_text(self, event):
        print('LastName Entry Event - ' + str(event))
        ' Enable before insert '
        if self.TextBox["state"] == DISABLED:
            self.TextBox.config(state=NORMAL)
        self.TextBox.insert(END,"\nMouse click in Last Name field")
        ' Disable after insert '
        self.TextBox.config(state=DISABLED)
        ' Update status depending on which button pressed '
        if event.num == 1:
            self.status_text.set("Left button clicked")
        elif event.num == 2:
            self.status_text.set("Middle button clicked")
        elif event.num == 3:
            self.status_text.set("Right button clicked")
        else:
            self.status_text.set("*** The " + str(event.num) + " button pressed ***")

class ZPLII:
    def __init__(self):
        ' Placeholder '
        ''' Function calling order should be...
                1. top
                2. circle (optional)
                3. rectangle (optional)
                4. aztec
                5. boxtext
                    a. Line 1
                    b. Line 2
                    c. Line 3
                6. bottom
        '''

    ' Function will build and return BCMA ZPL '
    def democode(self, debug=1):
        ' Top '
        zpl = ZPLII.top('self')
        if debug == 1:
            ' Append Circle '
            zpl += ZPLII.circle('self')
            ' Append Rectangle '
            # zpl += ZPLII.rectangle('self')
        ' Append Aztec barcode '
        zpl += ZPLII.aztec('self', "MGarcia", 430, 50)
        ' Append Box Text Line 1 '
        zpl += ZPLII.zpltext('self', "UNSCHEDULED", 100, 20, 35, 30)
        ' Append Box Text Line 2 '
        zpl += ZPLII.zpltext('self', "MGarcia", 100, 60, 30, 28)
        ' Append Box Text Line 3 '
        zpl += ZPLII.zpltext('self', "Garcia,", 100, 90, 35, 30)
        ' Append Box Text Line 4 '
        zpl += ZPLII.zpltext('self', "Meghan", 120, 125, 35, 30)
        ' Append Bottom'
        zpl += ZPLII.bottom('self')


    ' Function will return BCMA ZPL Initialization string '
    def top(self, length=305, width=600):
        ' Start Format '
        zpl = "^XA^MMT"
        ' Add Media Width '
        zpl += "^PW" + width.__str__()
        ' Add Media Length'
        zpl += "^LL" + length.__str__()
        ' Add start coordinate '
        zpl += "^LS0"
        ' Output for debugging '
        print('top......... ' + zpl)
        ' Return zpl '
        return zpl

    ' Function will return BCMA Target Rectangle string '
    def rectangle(self):
        ' Top '
        zpl = "^FO13,109^GB183,0,1^FS"
        ' Bottom '
        zpl += "^FO12,17^GB183,0,1^FS"
        ' Left'
        zpl += "^FO195,18^GB0,91,1^FS"
        ' Right '
        zpl += "^FO12,17^GB0,91,1^FS"
        ' Output for debugging '
        print('rectangle... ' + zpl)
        ' Return zpl '
        return zpl

    ' Function will return ZPL string for text '

    def zpltext(self, payload, x, y, height, width, rotation="N"):
        ' Set geometry, rotation, and stretch '
        zpl = "^FO" + str(x) + "," + str(y) + "^AO" + rotation + "," + str(height) + "," + str(width) + "^FD"
        zpl += payload + "^FS"
        ' Output for debugging '
        print('zpltext..... ' + zpl)
        return zpl

    ' Function will return BCMA Target Circle string '

    def circle(self):
        ' Circle '
        zpl = "^FO223,17^GE91,92,^FS"
        ' Output for debugging '
        print('circle...... ' + zpl)
        ' Return zpl '
        return zpl

    ' Function will return ZPL string for Aztec encapsulated payload '

    def aztec(self, payload, x, y, w=3, r=0, prefix='IE', rotation="N", magnification=4, ecl=60):
        ' Set bar code default '
        zpl = "^BY" + str(w) + "," + str(r)
        ' Set Geometry '
        zpl += "^FO" + str(x) + "," + str(y)
        ' Set symbology, orientation, magnification, and error correction'
        zpl += "^BO" + rotation + "," + str(magnification) + ",N," + str(ecl) + ",N,1,^FD"
        ' Add Application Identifier Prefix '
        zpl += prefix
        ' Present Payload as UPPERCASE '
        zpl += payload.upper()
        ' Close '
        zpl += "^FS"
        ' Output for debugging '
        print('aztec....... ' + zpl)
        return zpl

    def bottom(self, copies=1):
        ' Bottom '
        zpl = "^PQ"
        ' Add Copies '
        zpl += copies.__str__()
        ' Continue (no incrementation) '
        zpl += ",0,1,Y^XZ"
        ' Output for debugging '
        print('bottom...... ' + zpl)
        ' Return zpl '
        return zpl


' Call Function '
if __name__ == '__main__':
    vp_start_gui()
