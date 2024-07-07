import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="your password",
                               database="database name")
mycursor = mydb.cursor()

# Fetching Data From mysql to my python program
mycursor.execute("select Name, Marks from student_marks")
result = mycursor.fetchall

Names = []
Marks = []

for i in mycursor:
    Names.append(i[0])
    Marks.append(i[1])

"""print("Name of Students = ", Names)
print("Marks of Students = ", Marks)"""
#bar_color = 'skyblue'
# Visualizing Data using Matplotlib
num_students = len(Names)
colors = np.random.rand(num_students, 3)
plt.bar(Names, Marks,color=colors)
plt.ylim(0, 100)
plt.xlabel("Name of Students")
plt.ylabel("Marks of Students")
plt.title("Student's Information")
plt.show()
