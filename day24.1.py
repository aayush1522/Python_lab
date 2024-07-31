import matplotlib.pyplot as plt

# Data input
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Monthly Income Distribution')
plt.show()


#Conclusion
#Salary: $5000 (62.5%)
#Freelance: $1500 (18.8%)
#Investments: $1000 (12.5%)
#Rental: $600 (7.5%)
#Other: $400 (5%)
#Analysis:

#The primary source of income is the salary, making up 62.5% of the total.
#Freelance work adds a substantial 18.8%.
#Investments contribute 12.5%, indicating a good return on investments.
#This diverse income distribution indicates a stable financial situation,
#with the majority coming from a steady salary and additional income from various other sources,
#providing financial security and potential growth.
