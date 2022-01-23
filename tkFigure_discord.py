from tkinter import *
from PIL import Image, ImageTk, ImageOps
from itertools import cycle
import socket
import threading

#Hyper params
socket_toggle = False
toggle = False
HOST = '127.0.0.1'
PORT = 1338
SPEAKING = "f"



#init util functions
def input_images(img_string, ratio):
    img = Image.open(img_string)
    width, height = img.size
    img = img.resize((int(width/ratio), int(height/ratio)))
    img = ImageTk.PhotoImage(img)
    return img


def socket_listen():
	global conn
	global SPEAKING
	while True:
		try:
			data = conn.recv(1024)
			SPEAKING = data.decode("utf-8")[0]
		except:
			pass

#animations
def stop_animation(*event):
    global C
    global after_id
    C.delete("all")
    root.after_cancel(after_id)


def show_animation():
    global after_id
    global C
    global frames_sequence
    after_id = root.after(300, show_animation)
    img = next(frames_sequence)
    C.delete("all")
    C.create_image(300,300,image = img)


def mouth_track():
    global C
    global toggle
    global figure_shade
    global root
    global s
    global conn

    if SPEAKING == 't':
        if not toggle:
            show_animation()
            toggle = True
        else:
            pass
    else:
        if toggle:
            stop_animation()
            C.create_image(300,320,image = figure_shade)
            toggle = False
        else:
            pass

    root.after(60,mouth_track)



#GUI
root = Tk()
root.title("Colbert's Figure")
root.geometry("600x600")
root.iconbitmap('icon256.ico')

#init images
figure_shade = input_images("colbert_imgs/4.png", 6)
figure_m_1 = input_images("colbert_imgs/1.png", 5)
figure_m_2 = input_images("colbert_imgs/2.png", 5)
figure_m_3 = input_images("colbert_imgs/3.png", 5)

frames = [figure_m_1, figure_m_2, figure_m_3]
frames_sequence = cycle(frames)
frames_itr = iter(frames)

if socket_toggle == False:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	socket_toggle = True


#Canvas
C = Canvas(root, bg="white", height=600,width=600)
C.configure(bg='green2')
C.pack()
C.create_image(300,320,image = figure_shade)


root.after(60,mouth_track)
socekt_listener = threading.Thread(target = socket_listen)
socekt_listener.daemon = True
socekt_listener.start()

root.mainloop()
