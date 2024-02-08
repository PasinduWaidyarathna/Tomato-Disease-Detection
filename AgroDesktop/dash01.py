import tkinter
from tkinter import *
# from tkinter import messagebox
import mysql.connector
import cv2
from PIL import Image, ImageTk
#from ml_module import MLModel  # Import the MLModel class
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import testZ as db
# import numpy as np
# import tensorflow as tf
# from keras.preprocessing import image
# from keras.applications.resnet50 import preprocess_input
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


root = Tk()
root.title("AGRODIAGNOBOT System")
root.geometry("1250x700+210+100")

# icon image
image_icon = PhotoImage(file="image/icon.png")
root.iconphoto(False, image_icon)

camera_label = None


def home_page():
    global camera_label
    home_frame = Frame(main_frame)

    lb = tkinter.Label(home_frame, text='Home Page : Camera Output ', font=('Bold', 15))
    lb.pack()



    # OpenCV code to capture webcam feed
    cap = cv2.VideoCapture(0)

    # Create a label for displaying the camera feed
    camera_label = Label(home_frame)

    def update_camera():
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (360, 250))

            # Convert the OpenCV image to Tkinter PhotoImage
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(img)

            # Update label with the new image
            camera_label.config(image=img)
            camera_label.image = img

            # Call itself after 10 milliseconds
            root.after(10, update_camera)

    # Create a label for displaying the camera feed

    camera_label = tkinter.Label(home_frame)
    camera_label.pack()

    # Start updating the camera feed
    update_camera()

    prediction_class_lb = tkinter.Label(home_frame, text='Prediction Class name : late-blight ')
    prediction_class_lb.pack()
    percentage_class_lb = tkinter.Label(home_frame, text='Percentage  : 96.46% ')
    percentage_class_lb.pack()

    # Bar chart plotting code
    mydb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="Pradeepa64@",
                                   database="agro")
    mycursor = mydb.cursor()
    mycursor.execute("select Name, Marks from student_marks")
    result = mycursor.fetchall()

    Names = []
    Marks = []

    for i in result:
        Names.append(i[0])
        Marks.append(i[1])

    # Matplotlib bar chart
    fig, ax = plt.subplots(figsize=(10,6))
    colors = np.random.rand(len(Names), 3)
    ax.bar(Names, Marks, color=colors)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Name of Students")
    ax.set_ylabel("Marks of Students")
    ax.set_title("Student's Information")

    # Embedding Matplotlib plot in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=home_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Pie chart plotting code
    my_dict = {'NAME': ['Infant', 'Child', 'Young', 'Old'], 'Nos': [30, 40, 50, 50]}
    df = pd.DataFrame(data=my_dict)
    lbl = ['Infant', 'Child', 'Young', 'Old']
    fig1, ax1 = plt.subplots(figsize=(3, 3))
    ax1.pie(df['Nos'], labels=lbl, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Embedding Matplotlib pie chart in Tkinter
    pie_canvas = FigureCanvasTkAgg(fig1, master=home_frame)
    pie_widget = pie_canvas.get_tk_widget()
    pie_widget.pack()

    home_frame.pack(padx=20)


def menu_page():
    menu_frame = Frame(main_frame)

    lb = tkinter.Label(menu_frame, text='Menu Page\n\nPage:2', font=('Bold', 30))
    lb.pack()

    menu_frame.pack(padx=20)


def contact_page():
    contact_frame = Frame(main_frame)

    lb = tkinter.Label(contact_frame, text='Contact Page\n\nPAge:3', font=('Bold', 30))
    lb.pack()

    contact_frame.pack(padx=20)


def about_page():
    about_frame = Frame(main_frame)

    lb = tkinter.Label(about_frame, text='About Page\n\nPAge:4', font=('Bold', 30))
    lb.pack()

    about_frame.pack(padx=20)


def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    menu_indicate.config(bg='#c3c3c3')
    contact_indicate.config(bg='#c3c3c3')
    about_indicate.config(bg='#c3c3c3')


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()


def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()


options_frame = tkinter.Frame(root, bg='#c3c3c3')

##home button
home_button = tkinter.Button(options_frame, text='Home', font=('Bold', 15),
                             fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(home_indicate, home_page))

home_button.place(x=80, y=70)

home_indicate = tkinter.Label(options_frame, text='', bg='#c3c3c3')
home_indicate.place(x=60, y=74, width=5, height=30)

##menu button
menu_button = tkinter.Button(options_frame, text='Menu', font=('Bold', 15),
                             fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(menu_indicate, menu_page))

menu_button.place(x=80, y=120)

menu_indicate = tkinter.Label(options_frame, text='', bg='#c3c3c3')
menu_indicate.place(x=60, y=124, width=5, height=30)

##contact button
contact_button = tkinter.Button(options_frame, text='Contact', font=('Bold', 15),
                                fg='#158aff', bd=0, bg='#c3c3c3',
                                command=lambda: indicate(contact_indicate, contact_page))

contact_button.place(x=80, y=170)

contact_indicate = tkinter.Label(options_frame, text='', bg='#c3c3c3')
contact_indicate.place(x=60, y=174, width=5, height=30)

##about button
about_button = tkinter.Button(options_frame, text='About', font=('Bold', 15),
                              fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(about_indicate, about_page))

about_button.place(x=80, y=220)

about_indicate = tkinter.Label(options_frame, text='', bg='#c3c3c3')
about_indicate.place(x=60, y=224, width=5, height=30)

options_frame.pack(side=tkinter.LEFT)
options_frame.pack_propagate(False)
options_frame.config(width=240, height=700)

main_frame = tkinter.Frame(root, highlightbackground='black', highlightthickness=2)

main_frame.pack(side=tkinter.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=1010, height=700)

root.mainloop()
