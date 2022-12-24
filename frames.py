import cv2
import numpy as np
from keras.models import load_model
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Plant Health Check")
window.geometry("800x900")
window.resizable(False, False)

resultLabel = tk.Label(window, text="")
resultLabel.config(font=("Arial", 25))


def checkPlant():
    model = load_model('keras_model.h5', compile=False)
    camera = vid
    labels = open('labels.txt', 'r').readlines()
    ret, image = camera.read()
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image / 127.5) - 1
    probabilities = model.predict(image)
    print(labels[np.argmax(probabilities)])
    resultLabel.config(text=labels[np.argmax(probabilities)])


def exit():
    window.destroy()


frameBtn = tk.Button(window, text="Check 1 Frame", command=checkPlant)
exitBtn = tk.Button(window, text="Exit", command=exit)
frameBtn.pack()
exitBtn.pack()

vid = cv2.VideoCapture(0)

width, height = 800, 600

vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

label_widget = tk.Label(window)
label_widget.pack()

resultLabel.pack()


def open_camera():
    _, frame = vid.read()

    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    captured_image = Image.fromarray(opencv_image)

    photo_image = ImageTk.PhotoImage(image=captured_image)

    label_widget.photo_image = photo_image

    label_widget.configure(image=photo_image)
    label_widget.after(10, open_camera)


open_camera()

window.mainloop()