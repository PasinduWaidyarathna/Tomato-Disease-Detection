import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from matplotlib.figure import Figure

# Function to generate the bar chart
def generate_bar_chart():
    mydb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="Pradeepa64@",
                                   database="agro")
    mycursor = mydb.cursor()

    # Fetching Data From MySQL to my Python program
    mycursor.execute("SELECT Name, Marks FROM student_marks")
    result = mycursor.fetchall()

    Names = []
    Marks = []

    for i in result:
        Names.append(i[0])
        Marks.append(i[1])

    print("Name of Students = ", Names)
    print("Marks of Students = ", Marks)

    # Generating random colors for each student
    num_students = len(Names)
    colors = np.random.rand(num_students, 3)

    # Create the bar chart
    fig = Figure(figsize=(300/80, 200/80), dpi=80)
    ax = fig.add_subplot(111)
    bars = ax.bar(Names, Marks, color=colors)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Name of Students")
    ax.set_ylabel("Marks of Students")
    ax.set_title("Student's Information")

    # Add the bar chart to the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Draw the canvas
    canvas.draw()

    # Add the closing event for the Matplotlib figure
    canvas_widget.get_tk_widget().bind("<Destroy>", lambda e: plt.close(fig))

# Create the main Tkinter window
main_window = tk.Tk()
main_window.title("Student Information App")
main_window.geometry("1200x720")

# Create a frame for the bar chart
main_frame = tk.Frame(main_window, width=300, height=200)
main_frame.pack(side=tk.LEFT, padx=20, pady=20)

# Button to generate the bar chart
generate_button = tk.Button(main_window, text="Generate Bar Chart", command=generate_bar_chart)
generate_button.pack(side=tk.TOP, pady=20)

# Run the Tkinter event loop
main_window.mainloop()
