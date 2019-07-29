import getopt, os, sys, math, struct, wave
import sys

num_lsb = 2
'''getpath=os.getcwd()
print (getpath)
#os.chdir(getpath+"\workplace2")
print (getpath)'''
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

import gsencode_support

def vp_start_gui():
    getpath=os.getcwd()
    print (getpath)
    os.chdir(getpath+"\workplace2")
    print (getpath)
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gsencode_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    gsencode_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def funsencode(self):
        #sname="kkkl"
        sname=self.sourcetext.get("1.0",'end-1c');
        dname=self.datatext.get("1.0",'end-1c');
        oname=self.outputtext.get("1.0",'end-1c');
        hide_data(sname,dname,oname)
        self.Label5.configure(text='''100% DONEE''')

    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 24 -weight bold -underline 1"  \
            " -overstrike 1"

        top.geometry("600x450+341+154")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.SOUND_STG_ENCODE = tk.Label(top)
        self.SOUND_STG_ENCODE.place(relx=0.25, rely=0.044, height=51, width=325)
        self.SOUND_STG_ENCODE.configure(background="#d9d9d9")
        self.SOUND_STG_ENCODE.configure(disabledforeground="#a3a3a3")
        self.SOUND_STG_ENCODE.configure(font=font9)
        self.SOUND_STG_ENCODE.configure(foreground="#000000")
        self.SOUND_STG_ENCODE.configure(text='''SOUND STG ENCODE''')

        self.sourcetext = tk.Text(top)
        self.sourcetext.place(relx=0.55, rely=0.422, relheight=0.067
                , relwidth=0.283)
        self.sourcetext.configure(background="white")
        self.sourcetext.configure(font="TkTextFont")
        self.sourcetext.configure(foreground="black")
        self.sourcetext.configure(highlightbackground="#d9d9d9")
        self.sourcetext.configure(highlightcolor="black")
        self.sourcetext.configure(insertbackground="black")
        self.sourcetext.configure(selectbackground="#c4c4c4")
        self.sourcetext.configure(selectforeground="black")
        self.sourcetext.configure(width=10)
        self.sourcetext.configure(wrap='word')

        self.datatext = tk.Text(top)
        self.datatext.place(relx=0.55, rely=0.511, relheight=0.067
                , relwidth=0.283)
        self.datatext.configure(background="white")
        self.datatext.configure(font="TkTextFont")
        self.datatext.configure(foreground="black")
        self.datatext.configure(highlightbackground="#d9d9d9")
        self.datatext.configure(highlightcolor="black")
        self.datatext.configure(insertbackground="black")
        self.datatext.configure(selectbackground="#c4c4c4")
        self.datatext.configure(selectforeground="black")
        self.datatext.configure(width=10)
        self.datatext.configure(wrap='word')

        self.outputtext = tk.Text(top)
        self.outputtext.place(relx=0.55, rely=0.6, relheight=0.067
                , relwidth=0.283)
        self.outputtext.configure(background="white")
        self.outputtext.configure(font="TkTextFont")
        self.outputtext.configure(foreground="black")
        self.outputtext.configure(highlightbackground="#d9d9d9")
        self.outputtext.configure(highlightcolor="black")
        self.outputtext.configure(insertbackground="black")
        self.outputtext.configure(selectbackground="#c4c4c4")
        self.outputtext.configure(selectforeground="black")
        self.outputtext.configure(width=10)
        self.outputtext.configure(wrap='word')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.3, rely=0.422, height=21, width=134)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''SOURCE FILE(.Extention)''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.317, rely=0.533, height=21, width=121)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''DATA FILE(.Extention)''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.167, rely=0.622, height=21, width=216)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''NAME OUTPUT SOUND FILE(.Extention)''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.467, rely=0.733, height=25, width=55)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''INITIATE''')
        self.Button1.configure(command=self.funsencode)

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.35, rely=0.844, height=41, width=202)
        self.Label5.configure(background="#0fd837")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''0%''')
        self.Label5.configure(width=202)











def print_usage():
    print("\nUsage options:\n",
        "-h, --hide     If present, the script runs to hide data\n",
        "-r, --recover  If present, the script runs to recover data\n",
        "-s, --sound    What follows is the name of carrier wav file\n",
        "-d, --data     What follows is the file name having data to hide\n",
        "-o, --output   Output filename of choice\n",
        "-n, --nlsb     Number of LSBs to use\n",
        "-b, --bytes    Number of bytes to recover\n"
        " --help         Display help\n")

def prepare(sound_path):
    global sound, params, n_frames, n_samples, fmt, mask, smallest_byte
    sound = wave.open(sound_path, "r")
    
    params = sound.getparams()
    num_channels = sound.getnchannels()
    sample_width = sound.getsampwidth()
    n_frames = sound.getnframes()
    n_samples = n_frames * num_channels

    if (sample_width == 1):  # samples are unsigned 8-bit integers
        fmt = "{}B".format(n_samples)
        # Used to set the least significant num_lsb bits of an integer to zero
        mask = (1 << 8) - (1 << num_lsb)
        # The least possible value for a sample in the sound file is actually
        # zero, but we don't skip any samples for 8 bit depth wav files.
        smallest_byte = -(1 << 8)
    elif (sample_width == 2):  # samples are signed 16-bit integers
        fmt = "{}h".format(n_samples)
        # Used to set the least significant num_lsb bits of an integer to zero
        mask = (1 << 15) - (1 << num_lsb)
        # The least possible value for a sample in the sound file
        smallest_byte = -(1 << 15)
    else:
        # Python's wave module doesn't support higher sample widths
        raise ValueError("File has an unsupported bit-depth")

def hide_data(sound_path,file_path,output_path):
    global sound, params, n_frames, n_samples, fmt, mask, smallest_byte
    #sound_path =input("SOUND FILE(with extension):")
    #file_path =input("SOURCE MESSAGE FILE (with extension):")
#output_path =input(" OUTPUT SOUND FILE (with extension):")
    prepare(sound_path)
    # We can hide up to num_lsb bits in each sample of the sound file
    max_bytes_to_hide = (n_samples * num_lsb) // 8
    filesize = os.stat(file_path).st_size
    
    if (filesize > max_bytes_to_hide):
        required_LSBs = math.ceil(filesize * 8 / n_samples)
        raise ValueError("Input file too large to hide, "
                         "requires {} LSBs, using {}"
                         .format(required_LSBs, num_lsb))
    
    print("Using {} B out of {} B".format(filesize, max_bytes_to_hide))
    
    
    # Put all the samples from the sound file into a list
    raw_data = list(struct.unpack(fmt, sound.readframes(n_frames)))
    sound.close()
    
    input_data = memoryview(open(file_path, "rb").read())
    
    # The number of bits we've processed from the input file
    data_index = 0
    sound_index = 0
    
    # values will hold the altered sound data
    values = []
    buffer = 0
    buffer_length = 0
    done = False
    
    while(not done):
        while (buffer_length < num_lsb and data_index // 8 < len(input_data)):
            # If we don't have enough data in the buffer, add the
            # rest of the next byte from the file to it.
            buffer += (input_data[data_index // 8] >> (data_index % 8)
                        ) << buffer_length
            bits_added = 8 - (data_index % 8)
            buffer_length += bits_added
            data_index += bits_added
            
        # Retrieve the next num_lsb bits from the buffer for use later
        current_data = buffer % (1 << num_lsb)
        buffer >>= num_lsb
        buffer_length -= num_lsb

        while (sound_index < len(raw_data) and
               raw_data[sound_index] == smallest_byte):
            # If the next sample from the sound file is the smallest possible
            # value, we skip it. Changing the LSB of such a value could cause
            # an overflow and drastically change the sample in the output.
            values.append(struct.pack(fmt[-1], raw_data[sound_index]))
            sound_index += 1

        if (sound_index < len(raw_data)):
            current_sample = raw_data[sound_index]
            sound_index += 1

            sign = 1
            if (current_sample < 0):
                # We alter the LSBs of the absolute value of the sample to
                # avoid problems with two's complement. This also avoids
                # changing a sample to the smallest possible value, which we
                # would skip when attempting to recover data.
                current_sample = -current_sample
                sign = -1

            # Bitwise AND with mask turns the num_lsb least significant bits
            # of current_sample to zero. Bitwise OR with current_data replaces
            # these least significant bits with the next num_lsb bits of data.
            altered_sample = sign * ((current_sample & mask) | current_data)

            values.append(struct.pack(fmt[-1], altered_sample))

        if (data_index // 8 >= len(input_data) and buffer_length <= 0):
            done = True
        
    while(sound_index < len(raw_data)):
        # At this point, there's no more data to hide. So we append the rest of
        # the samples from the original sound file.
        values.append(struct.pack(fmt[-1], raw_data[sound_index]))
        sound_index += 1
    
    sound_steg = wave.open(output_path, "w")
    sound_steg.setparams(params)
    sound_steg.writeframes(b"".join(values))
    sound_steg.close()
    print("Data hidden over {} audio file".format(output_path))

def recover_data(sound_path, output_path, num_lsb, bytes_to_recover):
    # Recover data from the file at sound_path to the file at output_path
    global sound, n_frames, n_samples, fmt, smallest_byte
    prepare(sound_path)

    # Put all the samples from the sound file into a list
    raw_data = list(struct.unpack(fmt, sound.readframes(n_frames)))
    # Used to extract the least significant num_lsb bits of an integer
    mask = (1 << num_lsb) - 1
    output_file = open(output_path, "wb+")
    
    data = bytearray()
    sound_index = 0 
    buffer = 0
    buffer_length = 0
    sound.close()

    while (bytes_to_recover > 0):
        
        next_sample = raw_data[sound_index]
        if (next_sample != smallest_byte):
            # Since we skipped samples with the minimum possible value when
            # hiding data, we do the same here.
            buffer += (abs(next_sample) & mask) << buffer_length
            buffer_length += num_lsb
        sound_index += 1
        
        while (buffer_length >= 8 and bytes_to_recover > 0):
            # If we have more than a byte in the buffer, add it to data
            # and decrement the number of bytes left to recover.
            current_data = buffer % (1 << 8)
            buffer >>= 8
            buffer_length -= 8
            data += struct.pack('1B', current_data)
            bytes_to_recover -= 1

    output_file.write(bytes(data))
    output_file.close()
    print("Data recovered to {} text file".format(output_path))

'''def audmain():
    getpath=os.getcwd()
    print (getpath)
    os.chdir(getpath+"/workplace2")
    print("1.ENCODE")
    
    hide_data()'''
        

if __name__ == "__main__":
    ''' getpath=os.getcwd()
    print (getpath)
    os.chdir(getpath+"/workplace")'''
    vp_start_gui()

'''try:
    opts, args = getopt.getopt(sys.argv[1:], 'hrs:d:o:n:b:',
                              ['hide', 'recover', 'sound=', 'data=',
                               'output=', 'nlsb=', 'bytes=', 'help'])
except getopt.GetoptError:
    print_usage()
    sys.exit(1)

hiding_data = False
recovering_data = False

for opt, arg in opts:
    if opt in ("-h", "--hide"):
        hiding_data = True
    elif opt in ("-r", "--recover"):
        recovering_data = True
    elif opt in ("-s", "--sound"):
        sound_path = arg
    elif opt in ("-d", "--data"):
        file_path = arg
    elif opt in ("-o", "--output"):
        output_path = arg
    elif opt in ("-n", "--nlsb"):
        num_lsb = int(arg)
    elif opt in ("-b", "--bytes"):
        bytes_to_recover = int(arg)
    elif opt in ("--help"):
        print_usage()
        sys.exit(1)
    else:
        print("Invalid argument {}".format(opt))

try:
    if (hiding_data):
        hide_data(sound_path, file_path, output_path, num_lsb)
    if (recovering_data):
        recover_data(sound_path, output_path, num_lsb, bytes_to_recover)
except Exception as e:
    print("Ran into an error during execution. Check input and try again.\n")
    print(e)
    print_usage()
    sys.exit(1)
'''
