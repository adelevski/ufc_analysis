# Import statements
import pandas as pd


# Reading in csv file and turning it into a Pandas DataFrame
df = pd.read_csv("data/data.csv")


# Printing all the columns 
for column in df.columns:
    print(column)


# # Printing all columns about the Red fighter
# for column in df.columns:
#     if column.startswith("R_"):
#         print(column)


# # Printing general columns (not about either fighter)
# for column in df.columns:
#     if not column.startswith("R_") and not column.startswith("B_"):
#         print(column)


