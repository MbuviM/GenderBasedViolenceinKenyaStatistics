import matplotlib.pyplot as plt
import pandas as pd

# Reading the database
data = pd.read_csv('main_GBV.csv')
print(data.head(7))

# Plot the graph
plt.bar(data['Counties'], data['GBV_Cases(%)'])

# Adding a title to the plot
plt.title('GBV cases per county')

# Setting the x and y labels
plt.xlabel('Counties')
plt.ylabel('GBV_Cases_Percentage')
plt.show()