import os
import json


def validate_file_path(file_path: str) -> bool:
    if not os.path.exists(file_path):
        return True
    else:
        print(f'Error: File {file_path} already exists')
        return False


def validate_file_extension(file_path: str, extensions: tuple) -> bool:
    ext = os.path.splitext(file_path)[1]
    if ext in extensions:
        return True
    else:
        print(f"File extension '{ext}' is not supported")
        return False


def validate_array(array_str: str) -> bool:
    try:
        array = json.loads(array_str)
        if isinstance(array, list) and all(isinstance(row, list) and all(isinstance(val, int) for val in row) for row in array):
            if len(array) > 0 and all(len(row) == len(array[0]) for row in array):
                return True
            else:
                print("Error: The array must be two-dimensional and all rows must have the same length.")
        else:
            print("Error: The array must contain only integer values.")
    except json.JSONDecodeError:
        print('Error: input is not a valid JSON string')
    return False




