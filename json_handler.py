import json


def save_to_json(file_path, data):
    """
    Save a list of data to a JSON file.

    Args:
        data (list): The list of data to save.
        file_path (str): The file path where the JSON file will be saved.

    Returns:
        None
    """
    with open(file_path, 'w') as f:
        json.dump(data, f)

