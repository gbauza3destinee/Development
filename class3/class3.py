import pandas as pd 

# Pandas is a library that provides data structures and functions needed to efficiently manipulate large datasets.

# My  Student Dictionary 
cooking_class_dict = {"Name": ["Sarah", "Joe", "Alice"],
                      "Favorite Food":[ "Pizza", "Ice Cream", "Mango"]
                      }


students_df = pd.DataFrame(cooking_class_dict)
print(students_df)


## Output this data as a file
students_df.to_excel("output.xlsx", index=false)