import argparse
import ast
import json
from csv_handler import save_to_csv
from json_handler import save_to_json
from validator import validate_file_path, validate_file_extension, validate_array

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Save 2D integer list to CSV or JSON file.')
    parser.add_argument('path', help='Path to output file')
    parser.add_argument('list', help='2D integer list to save as a string')

    args = parser.parse_args()

    path = args.path
    input_list = args.list

    if validate_file_path(path) and validate_file_extension(path, ('.csv', '.json')) and validate_array(input_list):
        if isinstance(input_list, str):
            ast_input_list = ast.literal_eval(input_list)

        if path.endswith('.csv'):
            save_to_csv(path,  input_list)
            print(f'Successfully saved 2D integer list to CSV file at {path}')
        else:
            save_to_json(path, ast_input_list)
            print(f'Successfully saved 2D integer list to JSON file at {path}')
