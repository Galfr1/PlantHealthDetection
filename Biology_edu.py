import cv2
import numpy as np
from keras.models import load_model
import tkinter as tk
from tkinter import filedialog as fd
import xlsxwriter as xl

def getInputAsInt(input):
    return int(input.get(1.0, "end-1c"))

frm1 = tk.Tk()
frm1.geometry("600x600")
frm1.resizable(False, False)
frm1.title("Plant Amount")

lb1 = tk.Label(frm1, text="Please enter the amount of plants for your experiment:")
inp1 = tk.Text(frm1, height = 1, width = 3)

def btn1_action():
    plantAmount = getInputAsInt(inp1)
    frm1.withdraw()

    frm2 = tk.Toplevel()
    frm2.geometry("900x900")
    frm2.resizable(False, False)
    frm2.title("Image Loader")

    imagePaths = []

    def openImage():
        filetypes = (
            ('jpg Image File', '*.jpg'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        imagePaths.append(filename)

    x = 0
    while(x < plantAmount):
        lb2 = tk.Label(frm2, text=f"Front of plant {x + 1}:")
        btn2 = tk.Button(frm2, text="Open Image...", command=openImage)
        lb2.pack()
        btn2.pack()
        lb2_2 = tk.Label(frm2, text=f"Back of plant {x + 1}:")
        btn2_2 = tk.Button(frm2, text="Open Image...", command=openImage)
        lb2_2.pack()
        btn2_2.pack()
        x += 1

    rawResults = []

    def loadImages():
        def clr():
            global imagePaths
            global rawResults
            imagePaths = []
            rawResults = []
            lb3.destroy()
            clearBtn.destroy()

        clearBtn = tk.Button(frm2, text="Clear", command=clr)
        lb3 = tk.Label(frm2, text="The process of calculating results is long and might take a while, please wait...\nAfter this process, choose an empty folder to save the data in (as excel file).")
        lb3.pack()
        clearBtn.pack()

        model = load_model('keras_model.h5', compile=False)
        labels = open('labels.txt', 'r').readlines()
        a = 0
        while(a < len(imagePaths)):
            image = cv2.imread(imagePaths[a])
            image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
            image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
            image = (image / 127.5) - 1
            probabilities = model.predict(image)
            print(probabilities)
            rs = probabilities[0]
            print(rs[0], rs[1])
            rs0 = int(rs[0] * 100)
            rs1 = int(rs[1] * 100)
            print(labels[np.argmax(probabilities)])
            txt = str(rs0) + "," + str(rs1)
            rawResults.append(txt)
            a += 1

        output_folder = fd.askdirectory()
        output_excel_path = output_folder + "/output.xlsx"

        wb = xl.Workbook(output_excel_path)
        ws = wb.add_worksheet()
        ws.write(0, 0, 'ID')
        ws.write(0, 1, 'Front_Healthy_Percentage')
        ws.write(0, 2, 'Front_Unhealthy_Percentage')
        ws.write(0, 3, 'Back_Healthy_Percentage')
        ws.write(0, 4, 'Back_Unhealthy_Percentage')

        b = 0
        c = 0
        while(b < plantAmount):
            ws.write(b + 1, 0, b + 1)
            c1 = rawResults[c].split(',')
            c2 = rawResults[c + 1].split(',')
            ws.write(b + 1, 1, c1[0])
            ws.write(b + 1, 2, c1[1])
            ws.write(b + 1, 3, c2[0])
            ws.write(b + 1, 4, c2[1])
            b += 1
            c += 2

        wb.close()



    btn3 = tk.Button(frm2, text="Load", command=loadImages)
    btn3.pack()
    frm2.mainloop()


btn1 = tk.Button(frm1, text="OK", command=btn1_action)

lb1.pack()
inp1.pack()
btn1.pack(pady=10)

frm1.mainloop()