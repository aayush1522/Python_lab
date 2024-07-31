import matplotlib.pyplot as plt

# Data
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, expenses, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel('Spending Categories')
plt.ylabel('Monthly Expenses (in dollars)')
plt.title('Monthly Expenses by Category')
plt.grid(True, linestyle='--', alpha=0.6)

# Display the chart
plt.show()


#Conclusion
#The code creates a bar chart to show how much money is spent in different categories each month.
#It uses colors to differentiate the categories and includes labels and a title for clarity.
#The chart helps to easily compare expenses across categories.
