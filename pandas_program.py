import os
os.system('cls' if os.name == 'nt' else 'clear')
import pandas as pd
import numpy as np


months = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                   index=['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                          'August', 'September', 'October', 'November', 'December'])
print("Month Series:")
print(months)

students_dict = {'MATMIE': 42, 'MATDAIS': 36, 'COMIE': 41, 'COMEC': 37}
students_series = pd.Series(students_dict)
print("\nStudents Series:")
print(students_series)

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
exam_df = pd.DataFrame(exam_data, index=labels)
print("\nExam DataFrame:")
print(exam_df)

filtered_df = exam_df[exam_df['attempts'] > 2]
print("\nRows where number of attempts is greater than 2:")
print(filtered_df)
