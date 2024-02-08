import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk

my_dict = {'NAME': ['Infant', 'Child', 'Young', 'Old'], 'Nos': [30, 40, 50, 50]}
df = pd.DataFrame(data=my_dict)
lbl = ['Infant', 'Child', 'Young', 'Old']
fig1 = df.plot.pie(title="Population", y='Nos', figsize=(3, 3), labels=lbl).get_figure()

my_w = tk.Tk()
my_w.geometry("1200x700")  # Size of the window
my_w.title('www.plus2net.com')

# Get the width and height of the Tkinter window
window_width = my_w.winfo_reqwidth()
window_height = my_w.winfo_reqheight()

# Calculate the position for the bottom-left corner
x_position = 10  # You can adjust this value based on your preferences
y_position = window_height - 10 - 3 * 80  # Adjusted to leave some space from the bottom

# Place the pie chart using absolute coordinates
plot1 = FigureCanvasTkAgg(fig1, master=my_w)
plot1.get_tk_widget().place(x=x_position, y=y_position)

my_w.mainloop()
