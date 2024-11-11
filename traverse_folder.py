import os

def traverse_directory(file_folder):
    result = []
    skip_first_iteration = True
    for root, dirs, files in os.walk(file_folder):
        if skip_first_iteration:
            skip_first_iteration = False
        else:
            file_txt = os.path.join(root, 'stdout.txt')
            result.append(file_txt)
    return result

