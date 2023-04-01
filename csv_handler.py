import csv


def save_to_csv(file_path, data):
    """
    Save 2D list to CSV file

    Args:
        file_path (str): Path to the CSV file
        data (list): 2D list of data to be saved

    Returns:
        None
    """
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data])
