import pandas as pd

# Load data from a CSV file
data = pd.read_csv('data.csv')

# Display the first 5 rows of the data
print(data.head())

# Calculate some basic statistics
mean = data.mean()
median = data.median()
mode = data.mode()

print('Mean:', mean)
print('Median:', median)
print('Mode:', mode)

# Plot a histogram of the data
data.hist()

# Save the plot to a file
plt.savefig('histogram.png')

