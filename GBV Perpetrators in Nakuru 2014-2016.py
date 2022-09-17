# Pandas is a library used in datasets.
# Matplotlib is a python library used in the plotting of graphs.
import pandas as pd
import matplotlib.pyplot as plt

# Reading the database

cases = pd.read_csv('sexual_and_gender_based_violence_cases_from_january_2014_to_september_2016_in_nakuru_county.csv')
print(cases.head(6))

# Plot a graph
plt.scatter(cases['OBJECTID'], cases['No_of_perpetrators'])

# Adding the graph title
plt.title('GBV Perpetrators in Nakuru from January 2014 to September 2016')

# x and y labels
plt.xlabel('OBJECTID(Each month had a unique id from 0-32)')
plt.ylabel('Number of perpetrators')

# Used to output the graph
plt.show()
