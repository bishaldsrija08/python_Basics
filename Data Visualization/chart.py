import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 200, 250, 300, 350, 400]

# create bar diagram
plt.bar(months, sales, color='skyblue')

# create pie chart
plt.pie(sales, labels=months, autopct='%1.1f%%', startangle=140)

plt.title('Monthly Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales')

plt.show()