import pandas as pd
import os

# Create a sample DataFrame with column names
data={'Name':["Alice","Bob","charlie"],
      "Age":[25,30,35],
      "city":["New York","Los angeles","Chicago"]}

df=pd.DataFrame(data)

# Adding new row to df for V2
new_row_loc ={"Name":"Anshu","Age":23,"city":"Pune"}
df.loc[len(df.index)]=new_row_loc

# Adding new row to df for V3
# new_row_loc2={"Name":"v3","age": 33,"city":"deoghar"}
# df.loc2[len(df.index)]=new_row_loc2

# Ensure the "data" directory exits at the root level

data_dir="data"
os.makedirs(data_dir,exist_ok=True)

# Define the file path 
file_path=os.path.join(data_dir,"sample_data.csv")

# save the DataFrame to a CSV file, including columns names
df.to_csv(file_path,index=False)
  
print(f"Csv file saved to {file_path}")