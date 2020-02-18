import pandas as pd

# 2. Load the insurance.csv in a DataFrame using pandas. Explore the dataset using functions like to_string(), columns,
# index, dtypes, shape, info() and describe(). Use this DataFrame for the following exercises.
df = pd.read_csv('winter2020-code/4-python-advanced-notebook/data/insurance.csv', header=0)

print(df.to_string())
print()
print(df.columns)
print()
print(df.index)
print()
print(df.dtypes)
print()
print(df.shape)
print()
print(df.info())
print()
print(df.describe())
print()

# 3. Print only the column age
print(df.age)
print()

# 4. Print only the columns age,children and charges
print(df[['age', 'children', 'charges']])
print()

# 5. Print only the first 5 lines and only the columns age,children and charges
print(df[['age', 'children', 'charges']].iloc[:5])
print()

# 6. What is the average, minimum and maximum charges ?
print(df['charges'].mean())
print()
print(df['charges'].min())
print()
print(df['charges'].max())
print()

# 7. What is the age and sex of the person that paid 10797.3362. Was he/she a smoker?
person = df[df["charges"] == 10797.3362].index[0]
print(f'The age of the person is {df.at[person, "age"]} and the sex is {df.at[person, "sex"]}.\n')
print(f'Is this person a smoker: {df.at[person, "smoker"]}\n\n')

# 8. What is the age of the person who paid the maximum charge?
person2 = df[df['charges'] == df['charges'].max()].index[0]
print(f'The age of the oldest person is {df.at[person2, "age"]}.\n\n')

# 9. How many insured people do we have for each region?
print('How many insured people do we have for each region?\n')
for name, group in df.groupby('region'):
    print(f'Group: {name}')
    print(f'Size: {len(group)} insured')
    print('------------------------\n')

# 10. How many insured people are children?
print(f'Total number of insured children: {df["children"].sum()}\n')

# 11. What do you expect to be the correlation between charges and age, bmi and children?
print(f'I expect the correlation between charges and age to be positive as health risks increase with age so \n'
      f'insurers will raise premiums to older people and depending on the plan, using the insurance will involve\n'
      f'deductibles or other out of pocket expenses which may be included in this dataset.\n'
      f'I expect the correlation between bmi and children to be positive as bmi and age are positively correlated\n'
      f'and age and children should also be positively correlated.\n')

# 12. Using the method corr(), check if your assumptions were correct.
print(f'Correlation between charges and age: {df["charges"].corr(df["age"])}')
print(f'Correlation between bmi and children: {df["bmi"].corr(df["children"])}\n')
