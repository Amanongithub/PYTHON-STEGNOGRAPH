# Python program implementing Image Steganography 

# PIL module is used to extract 
# pixels of image and modify it 
from PIL import Image 
import os
import sys
'''getpath=os.getcwd()
print (getpath)
os.chdir(getpath+"\Workplace2")'''
# Convert encoding data into 8-bit binary 
# form using ASCII value of characters
from tkinter import messagebox
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

import gidecode_support

def vp_start_gui():
    getpath=os.getcwd()
    print (getpath)
    os.chdir(getpath+"\Workplace2")
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gidecode_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    gidecode_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def funidecode(self):
        #sname="kkkl"
        sname=self.Text1.get("1.0",'end-1c');
        decode(sname)
        self.Label3.configure(text='''100% DONEE''')
        

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+359+211")
        top.title("IMAGE DECODER")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.15, rely=0.044, height=41, width=434)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 24 -weight bold -underline 1 -overstrike 1")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''IMAGE  STG DEC0DE''')

        self.HELP = tk.Button(top)
        self.HELP.place(relx=0.833, rely=0.156, height=25, width=50)
        self.HELP.configure(activebackground="#ececec")
        self.HELP.configure(activeforeground="#000000")
        self.HELP.configure(background="#d9d9d9")
        self.HELP.configure(disabledforeground="#a3a3a3")
        self.HELP.configure(foreground="#000000")
        self.HELP.configure(highlightbackground="#d9d9d9")
        self.HELP.configure(highlightcolor="black")
        self.HELP.configure(pady="0")
        self.HELP.configure(text='''HELP''')

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.483, rely=0.444, relheight=0.078, relwidth=0.283)

        self.Text1.configure(background="#ffffff")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=174)
        self.Text1.configure(wrap='word')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.133, rely=0.444, height=35, width=170)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''SOURCE FILE(.Extenstion)''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.45, rely=0.822, height=25, width=70)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''INITIATE''')
        self.Button1.configure(command=self.funidecode)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.333, rely=0.889, height=41, width=204)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#10d809")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''0%''')
'''
def genData(data): 
		
		# list of binary codes 
		# of given data 
		newd = [] 
		
		for i in data: 
			newd.append(format(ord(i), '08b')) 
		return newd 
		
# Pixels are modified according to the 
# 8-bit binary data and finally returned 
def modPix(pix, data): 
	
	datalist = genData(data) 
	lendata = len(datalist) 
	imdata = iter(pix) 

	for i in range(lendata): 
		
		# Extracting 3 pixels at a time 
		pix = [value for value in imdata.__next__()[:3] +
								imdata.__next__()[:3] +
								imdata.__next__()[:3]] 
									
		# Pixel value should be made 
		# odd for 1 and even for 0 
		for j in range(0, 8): 
			if (datalist[i][j]=='0') and (pix[j]% 2 != 0): 
				
				if (pix[j]% 2 != 0): 
					pix[j] -= 1
					
			elif (datalist[i][j] == '1') and (pix[j] % 2 == 0): 
				pix[j] -= 1
				
		# Eigh^th pixel of every set tells 
		# whether to stop ot read further. 
		# 0 means keep reading; 1 means the 
		# message is over. 
		if (i == lendata - 1): 
			if (pix[-1] % 2 == 0): 
				pix[-1] -= 1
		else: 
			if (pix[-1] % 2 != 0): 
				pix[-1] -= 1

		pix = tuple(pix) 
		yield pix[0:3] 
		yield pix[3:6] 
		yield pix[6:9] 

def encode_enc(newimg, data): 
	w = newimg.size[0] 
	(x, y) = (0, 0) 
	
	for pixel in modPix(newimg.getdata(), data): 
		
		# Putting modified pixels in the new image 
		newimg.putpixel((x, y), pixel) 
		if (x == w - 1): 
			x = 0
			y += 1
		else: 
			x += 1
			
# Encode data into image 
def encode(): 
	img = input("Enter image name(with extension): ") 
	image = Image.open(img, 'r')
	msgfile=input("file name (with extension):")
	f=open(msgfile,"r")
	data=f.read()
	#data = input("Enter data to be encoded : ") 
	if (len(data) == 0): 
		raise ValueError('Data is empty') 
		
	newimg = image.copy() 
	encode_enc(newimg, data) 
	
	new_img_name = input("Enter the name of new image(with extension): ") 
	newimg.save(new_img_name, str(new_img_name.split(".")[1].upper())) 
       '''
# Decode the data in the image 
def decode(img): 
	#img = input("Enter image name(with extension) :") 
	image = Image.open(img, 'r') 
	
	data = '' 
	imgdata = iter(image.getdata()) 
	
	while (True): 
		pixels = [value for value in imgdata.__next__()[:3] +
								imgdata.__next__()[:3] +
								imgdata.__next__()[:3]] 
		# string of binary data 
		binstr = '' 
		
		for i in pixels[:8]: 
			if (i % 2 == 0): 
				binstr += '0'
			else: 
				binstr += '1'
				
		data += chr(int(binstr, 2)) 
		if (pixels[-1] % 2 != 0): 
			#return data
                        textfile=open("output.txt","w")
                        textfile.write(data)
                        textfile.close()
                        return data
			
# Main Function		 S
'''def imgmain(para):
        getpath=os.getcwd()
        print (getpath)
        os.chdir(getpath+"/Workplace2")
        outputstring=decode(para)
        textfile=open("output.txt","w")
        textfile.write(outputstring)
        textfile.close()
    '''
             
		
# Driver Code 
if __name__ == '__main__' :
   
	
	# Calling main function 
    vp_start_gui() 
