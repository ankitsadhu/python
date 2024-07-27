# create a Dataframe(Table) from a 2D list called student_data.
# Types: Dataframe, Series

import pandas as pd

student_data = [
    [1, 15],
    [2, 11],
    [3, 5]
]

df = pd.DataFrame(student_data, columns=['student_id', 'age'])
print(df, f"\n no of rows x cols: {df.shape}")
print(f"First 2 rows: {df.head(2)}")
print(f"Print age column: {df[['age']]}")


students = pd.DataFrame([
    [101, 'Ulysses', 13],
    [53, 'William', 10],
    [128, 'Henry', 6],
    [2, None, 19]
], columns=['student_id', 'name', 'age'])

# Q. Select the name & age of student with student_id = 101
print(students.loc[students['student_id'] == 101, ['name', 'age']]) # query, row, col

# Q. Create a new Column called bonus, with salary is doubled 
students['bonus'] = students['age'] * 2
print(students)


# Q. Drop duplicate rows, there are some duplicate rows in df based on the email column, pick the first occurance
students['email'] = students['name'] + '@gmail.com'
students.drop_duplicates(subset='email', keep='first', inplace=True)


# Q. Drop Missing Data row
students.dropna(subset=['name'])


# Rename Columns
students = students.rename(
    columns = {
        "id" :"student_id"
    }
)
print(students)

# Change Data Type
students.astype({"age": float})
