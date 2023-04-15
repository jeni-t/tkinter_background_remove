#NOTE: C:\Users\Jenifer\.u2net===> u2net.onnx- download 
from rembg import remove
from PIL import Image
import tkinter as tk
import easygui as eg
root = tk.Tk()
root.title("image resize")
root.geometry('320x100')

def call_result():
    input_path =  eg.fileopenbox(title='Select image file')
    output_path = 'output.png'
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)
    message_label = tk.Label(root, font=('arial',12,'bold'),text="background removed")
    message_label.grid(row=3, column=1)
    
buttonCal = tk.Button(root, text="process", width=10,command=call_result).grid(row=3, column=0)


