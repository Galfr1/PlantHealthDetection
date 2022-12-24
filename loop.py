import cv2
import numpy as np
from PIL import ImageTk, Image
from keras.models import load_model
import tkinter as tk

frame = tk.Tk()
frame.title("Plant Health Detection")
frame.geometry("400x400")
frame.resizable(False, False)

def main():
    vid.release()
    frame.destroy()

    model = load_model('keras_model.h5', compile=False)

    camera = cv2.VideoCapture(0)

    labels = open('labels.txt', 'r').readlines()

    window = tk.Tk()
    window.title("Information")
    window.geometry("400x400")
    window.resizable(False, False)

    label = tk.Label(window, text="Press 'esc' in the 'Webcam Image' window to exit.")
    label.pack()
    info = tk.Label(window, text="")
    info.pack()
    info.config(font=("Arial", 25))

    def capture():

        ret, image = camera.read()

        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        cv2.imshow('Webcam Image', image)

        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        image = (image / 127.5) - 1

        probabilities = model.predict(image)

        print(labels[np.argmax(probabilities)])

        info.config(text=labels[np.argmax(probabilities)])

        keyboard_input = cv2.waitKey(1)

        if keyboard_input == 27:
            camera.release()
            cv2.destroyAllWindows()
            window.destroy()

        window.after(10, capture)

    capture()
    window.mainloop()

start = tk.Button(frame, text="Begin Detection!", command=main)
start.pack()

label_widget = tk.Label(frame)
label_widget.pack()

vid = cv2.VideoCapture(0)

width, height = 800, 600

vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


def open_camera():
    _, vidframe = vid.read()

    opencv_image = cv2.cvtColor(vidframe, cv2.COLOR_BGR2RGBA)

    captured_image = Image.fromarray(opencv_image)

    photo_image = ImageTk.PhotoImage(image=captured_image)

    label_widget.photo_image = photo_image

    label_widget.configure(image=photo_image)

    label_widget.after(10, open_camera)

open_camera()
frame.mainloop()


