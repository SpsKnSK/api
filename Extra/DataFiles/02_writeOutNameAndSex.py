import os
directory = os.path.dirname(__file__)
file_path = os.path.join(directory, '01_students.txt')
with open(file_path, 'r') as file:
    lines = file.readlines()
    for l in lines:
        columns = l.split(',')
        print(columns[0], "Girl" if columns[3]== 'F' else "Boy")