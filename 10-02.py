with open('files/learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip().replace('Python', 'C'))
