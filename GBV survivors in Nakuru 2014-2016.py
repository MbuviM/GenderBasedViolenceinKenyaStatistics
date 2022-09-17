import pandas as pd
import matplotlib.pyplot as plt

# Obtaining the dataframe
survivors = pd.read_csv('sexual_and_gender_based_violence_cases_from_january_2014_to_september_2016_in_nakuru_county.csv')
print(survivors.head(6))

# Plotting the graph
plt.bar(survivors['OBJECTID'], survivors['No_of_rape_survivors'])

# Title of the graph
plt.title('GBV Survivors in Nakuru from January 2014 to September 2016')

#Labeling of graphs
plt.xlabel('OBJECTID(Each month had a unique id from 0-32)')
plt.ylabel('Number of survivors')

# Output the graph
plt.show()