import matplotlib.pyplot as plt

# Data
labels = ['Safe Tomato', 'Unsafe Tomato']
sizes = [82, 10]
colors = ['#32a85c', '#dde810']  # Light Green for Safe, Light Yellow for Unsafe

# Plotting the pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)

# Draw a white circle in the center to create a doughnut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

plt.title('Scanned Tomato Percentage')

# Display the chart
plt.show()
