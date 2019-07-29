# Python program implementing Image Steganography 

# PIL module is used to extract 
# pixels of image and modify it 
from PIL import Image 
import os
import sys
# Convert encoding data into 8-bit binary 
# form using ASCII value of characters
#getpath=os.getcwd()
# print (getpath)
#os.chdir(getpath+"/Workplace2")
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

import giencode_support

def vp_start_gui():
    getpath=os.getcwd()
    print (getpath+"invp")
    os.chdir(getpath+"\Workplace2")
    print (getpath)
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = IMAGE_ENCODE (root)
    giencode_support.init(root, top)
    root.mainloop()

w = None
def create_IMAGE_ENCODE(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = IMAGE_ENCODE (w)
    giencode_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_IMAGE_ENCODE():
    global w
    w.destroy()
    w = None

class IMAGE_ENCODE:
    def funiencode(self):
        sname=self.sourcefilebutton.get("1.0",'end-1c');
        fname=self.filenamebutton.get("1.0",'end-1c');
        nfname=self.newfilebutton.get("1.0",'end-1c');
        encode(sname,fname,nfname)
        self.Label3.configure(text='''100% DONEE''')


        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 24 -weight bold -underline "  \
            "1 -overstrike 1"
        font13 = "-family {Segoe UI} -size 10 -weight bold"

        top.geometry("600x450+353+150")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.05, rely=0.067, height=51, width=534)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''IMAGE STG ENCODER''')
        self.Label1.configure(width=534)

        self.sourcefilebutton = tk.Text(top)
        self.sourcefilebutton.place(relx=0.5, rely=0.4, relheight=0.067
                , relwidth=0.283)
        self.sourcefilebutton.configure(background="white")
        self.sourcefilebutton.configure(font="TkTextFont")
        self.sourcefilebutton.configure(foreground="black")
        self.sourcefilebutton.configure(highlightbackground="#d9d9d9")
        self.sourcefilebutton.configure(highlightcolor="black")
        self.sourcefilebutton.configure(insertbackground="black")
        self.sourcefilebutton.configure(selectbackground="#c4c4c4")
        self.sourcefilebutton.configure(selectforeground="black")
        self.sourcefilebutton.configure(width=10)
        self.sourcefilebutton.configure(wrap='word')

        self.filenamebutton = tk.Text(top)
        self.filenamebutton.place(relx=0.5, rely=0.489, relheight=0.067
                , relwidth=0.283)
        self.filenamebutton.configure(background="white")
        self.filenamebutton.configure(font="TkTextFont")
        self.filenamebutton.configure(foreground="black")
        self.filenamebutton.configure(highlightbackground="#d9d9d9")
        self.filenamebutton.configure(highlightcolor="black")
        self.filenamebutton.configure(insertbackground="black")
        self.filenamebutton.configure(selectbackground="#c4c4c4")
        self.filenamebutton.configure(selectforeground="black")
        self.filenamebutton.configure(width=10)
        self.filenamebutton.configure(wrap='word')

        self.newfilebutton = tk.Text(top)
        self.newfilebutton.place(relx=0.5, rely=0.578, relheight=0.067
                , relwidth=0.283)
        self.newfilebutton.configure(background="white")
        self.newfilebutton.configure(font="TkTextFont")
        self.newfilebutton.configure(foreground="black")
        self.newfilebutton.configure(highlightbackground="#d9d9d9")
        self.newfilebutton.configure(highlightcolor="black")
        self.newfilebutton.configure(insertbackground="black")
        self.newfilebutton.configure(selectbackground="#c4c4c4")
        self.newfilebutton.configure(selectforeground="black")
        self.newfilebutton.configure(width=10)
        self.newfilebutton.configure(wrap='word')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.183, rely=0.422, height=21, width=164)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font13)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''SOURCE FILE(.Extension)''')
        self.Label2.configure(width=164)

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.217, rely=0.6, height=21, width=144)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=font13)
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''NEW FILE(.Extension)''')

        self.Label2_2 = tk.Label(top)
        self.Label2_2.place(relx=0.217, rely=0.511, height=21, width=144)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#d9d9d9")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font13)
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''DATA FILE(.Extension)''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.467, rely=0.733, height=24, width=60)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''INITIATE''')
        self.Button1.configure(command=self.funiencode)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.35, rely=0.844, height=41, width=194)
        self.Label3.configure(background="#2ad80f")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''0%''')
        self.Label3.configure(width=194)




###########################################

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
def encode(img,msgfile,new_img_name): 
	#img = input("Enter image name(with extension): ") 
	image = Image.open(img, 'r')
	#msgfile=input("file name (with extension):")
	f=open(msgfile,"r")
	data=f.read()
	#data = input("Enter data to be encoded : ") 
	if (len(data) == 0): 
		raise ValueError('Data is empty') 
		
	newimg = image.copy() 
	encode_enc(newimg, data) 
	
	#new_img_name = input("Enter the name of new image(with extension): ") 
	newimg.save(new_img_name, str(new_img_name.split(".")[1].upper())) 
       
# Decode the data in the image 
'''def decode(): 
	img = input("Enter image name(with extension) :") 
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
			return data '''
			
# Main Function		 
'''def imgmain():
        getpath=os.getcwd()
       # print (getpath)
        os.chdir(getpath+"/Workplace2")
        encode()
       
            #raise Exception("correct")
             
	'''	
# Driver Code 
if __name__ == '__main__' :
   
	
	# Calling main function 
    vp_start_gui() 
