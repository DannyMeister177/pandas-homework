import pandas as pd

# Load the data
df = pd.read_csv('data/WA_Fn-UseC_-HR-Employee-Attrition.csv')
df.drop('EmployeeCount', axis=1, inplace=True)        # Column has no relevant info

# Print info and summary stats
print(f'Info and description of dataset:\n')
print(df.info())
print(f'------------------------------------------------------------\n\n')
print(f'Print descriptive statistics. There are two many columns to fit on the screen so will temporarily remove\n'
      f'limits to pandas display settings.\n')

# Reset limits in pandas.options.display so that all data prints to the console output window
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Actual Printing
print(df.describe().dropna(how='all'))
print(f'------------------------------------------------------------\n\n')

# Print correlations
print(f'Printing the correlations. There are two many columns to fit on the screen so will temporarily remove limits\n'
      f'to pandas display settings.\n')
print(df.corr().dropna(how='all'))
print(f'------------------------------------------------------------\n\n')
