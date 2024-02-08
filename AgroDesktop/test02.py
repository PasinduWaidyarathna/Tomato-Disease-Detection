import matplotlib.pyplot as plt

# Data
categories = ['Quality Tomato', 'Leaves Diseases', 'Insect Damage', 'Not Recognized']
percentages = [40, 12, 5, 10]
colors = ['#32a85c', '#dde810', '#d61d09', '#bf9571']

# Plotting the bar chart
plt.bar(categories, percentages, color=colors)

# Adding labels and title
#plt.xlabel('Categories')
plt.ylabel('Percentage (%)')
plt.title('Summary')

# Display the chart
plt.show()
