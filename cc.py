#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    May 23, 2019 11:15:32 AM IST  platform: Windows NT

import sys
import idecode
import iencode
import sdecode
import sencode

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import cc_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    cc_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    cc_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def goie(self):
        iencode.vp_start_gui() 
        
        
    def goid(self):
        idecode.vp_start_gui() 
    def gose(self):
        sencode.vp_start_gui() 
    def gosd(self):
        sdecode.vp_start_gui() 
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+327+163")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.IMAGE_ENCODER = tk.Button(top)
        self.IMAGE_ENCODER.place(relx=0.017, rely=0.289, height=74, width=277)
        self.IMAGE_ENCODER.configure(activebackground="#ececec")
        self.IMAGE_ENCODER.configure(activeforeground="#000000")
        self.IMAGE_ENCODER.configure(background="#d9d9d9")
        self.IMAGE_ENCODER.configure(disabledforeground="#a3a3a3")
        self.IMAGE_ENCODER.configure(foreground="#000000")
        self.IMAGE_ENCODER.configure(highlightbackground="#d9d9d9")
        self.IMAGE_ENCODER.configure(highlightcolor="black")
        self.IMAGE_ENCODER.configure(pady="0")
        self.IMAGE_ENCODER.configure(text='''IMAGE ENCODER''')
        self.IMAGE_ENCODER.configure(width=277)
        self.IMAGE_ENCODER.configure(command=self.goie)
        

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.517, rely=0.289, height=74, width=267)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''IMAGE DECODER''')
        self.Button2.configure(width=267)
        self.Button2.configure(command=self.goid)

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.017, rely=0.489, height=74, width=277)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''SOUND ENCODER''')
        self.Button3.configure(width=277)
        self.Button3.configure(command=self.gose)

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.517, rely=0.489, height=74, width=267)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''SOUND DECODER''')
        self.Button4.configure(width=267)
        self.Button4.configure(command=self.gosd)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.417, rely=0.089, height=21, width=90)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''STEGNOGRAPH''')

if __name__ == '__main__':
    vp_start_gui()




