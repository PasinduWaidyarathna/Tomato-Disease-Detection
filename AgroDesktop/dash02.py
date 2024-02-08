import tkinter as tk
from tkinter import PhotoImage
import mysql.connector
import cv2
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

root = tk.Tk()
root.title("AGRODIAGNOBOT System")
root.geometry("1250x700+210+100")

# Icon image
image_icon = PhotoImage(file="image/icon.png")
root.iconphoto(False, image_icon)

camera_label = None


def home_page():
    global camera_label
    home_frame = tk.Frame(main_frame)

    lb = tk.Label(home_frame, text='Home Page : Camera Output ', font=('Bold', 15))
    lb.pack()

    cap = cv2.VideoCapture(0)
    camera_label = tk.Label(home_frame)

    def update_camera():
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (360, 250))
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(img)
            camera_label.config(image=img)
            camera_label.image = img
            root.after(10, update_camera)

    camera_label = tk.Label(home_frame)
    camera_label.pack()
    update_camera()

    prediction_class_lb = tk.Label(home_frame, text='Prediction Class name : late-blight ')
    prediction_class_lb.pack()
    percentage_class_lb = tk.Label(home_frame, text='Percentage  : 96.46% ')
    percentage_class_lb.pack()

    mydb = mysql.connector.connect(host="localhost", user="root", password="Pradeepa64@", database="agro")
    mycursor = mydb.cursor()
   # mycursor.execute("select Name, Marks from student_marks")
    mycursor.execute("select category,value from summary ORDER BY category DESC;")
    result = mycursor.fetchall()

    category = []
    value = []

    for i in result:
        category.append(i[0])
        value.append(i[1])

    # Initialize DataFrame for the pie chart
    df = pd.DataFrame(data={'NAME': ['Day 01', 'Day 02', 'Day 03', 'Day 04'], 'Nos': [30, 40, 50, 50]})

    # Create a single figure for both bar chart and pie chart
    fig = plt.Figure(figsize=(15, 5))

    # Subplot for the bar chart
    ax_bar = fig.add_subplot(121)
    #colors = ['green', 'brown', 'yellow', 'red']
    rgb_values = [
        (50, 168, 92),  # Green
        (191, 149, 113),  # Brown
        (221, 232, 16),  # Yellow
        (214, 29, 9)  # Red
    ]

    colors = [(r / 255, g / 255, b / 255) for r, g, b in rgb_values]
    #colors = np.random.rand(len(category), 3)
    category2 = ('Healthy\nTomato','Not\nRecognized','Leaves\nDiseases','Insect\nDamage')
    ax_bar.bar(category2,value, color=colors)
    ax_bar.set_ylim(0,50)
    ax_bar.set_xlabel("Category")
    ax_bar.set_ylabel("Percentage (%)")
    ax_bar.set_title("Summary")

    # Subplot for the pie chart
    ax_pie = fig.add_subplot(122)
    ax_pie.pie(df['Nos'], labels=df['NAME'], autopct='%1.1f%%', startangle=90)
    ax_pie.axis('equal')

    # Embed the single figure in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=home_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    home_frame.pack(padx=20)



def menu_page():
    menu_frame = tk.Frame(main_frame)
    lb = tk.Label(menu_frame, text='Menu Page\n\nPage:2', font=('Bold', 30))
    lb.pack()
    menu_frame.pack(padx=20)


def contact_page():
    contact_frame = tk.Frame(main_frame)
    lb = tk.Label(contact_frame, text='Contact Page\n\nPage:3', font=('Bold', 30))
    lb.pack()
    contact_frame.pack(padx=20)


def about_page():
    about_frame = tk.Frame(main_frame)
    lb = tk.Label(about_frame, text='About Page\n\nPage:4', font=('Bold', 30))
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


options_frame = tk.Frame(root, bg='#c3c3c3')

home_button = tk.Button(options_frame, text='Dashboard', font=('Bold', 15),
                        fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(home_indicate, home_page))
home_button.place(x=70, y=70)

home_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home_indicate.place(x=60, y=74, width=5, height=30)

menu_button = tk.Button(options_frame, text='Schedule', font=('Bold', 15),
                        fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(menu_indicate, menu_page))
menu_button.place(x=70, y=120)

menu_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
menu_indicate.place(x=60, y=124, width=5, height=30)

contact_button = tk.Button(options_frame, text='History', font=('Bold', 15),
                           fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(contact_indicate, contact_page))
contact_button.place(x=70, y=170)

contact_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
contact_indicate.place(x=60, y=174, width=5, height=30)

about_button = tk.Button(options_frame, text='Settings', font=('Bold', 15),
                         fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(about_indicate, about_page))
about_button.place(x=70, y=220)

logout_button = tk.Button(options_frame, text='Logout', font=('Bold', 15),
                         fg='#158aff', bd=0, bg='#c3c3c3')
logout_button.place(x=70, y=270)

about_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
about_indicate.place(x=60, y=224, width=5, height=30)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.config(width=240, height=700)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=1010, height=700)

root.mainloop()
