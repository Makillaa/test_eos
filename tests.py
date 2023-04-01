import os
import csv
import json
import unittest
from tempfile import NamedTemporaryFile
from json_handler import save_to_json
from csv_handler import save_to_csv
from validator import validate_file_path, validate_file_extension, validate_array


class TestSaveToJson(unittest.TestCase):
    def setUp(self):
        self.test_data = [[1, 2], [3, 4]]
        self.temp_file = NamedTemporaryFile(delete=False, suffix=".json")

    def tearDown(self):
        self.temp_file.close()
        os.unlink(self.temp_file.name)

    def test_save_to_json(self):
        save_to_json(self.temp_file.name, self.test_data)
        with open(self.temp_file.name) as f:
            data = json.load(f)
        self.assertEqual(self.test_data, data)


class TestSaveToCsv(unittest.TestCase):
    def setUp(self):
        self.test_list = [[1, 2], [3, 4]]
        self.temp_file = NamedTemporaryFile(delete=False, suffix=".csv")

    def tearDown(self):
        self.temp_file.close()
        os.unlink(self.temp_file.name)

    def test_save_to_csv(self):
        save_to_csv(self.temp_file.name, self.test_list)
        with open(self.temp_file.name, 'r') as f:
            reader = csv.reader(f)
            data = [[int(cell) for cell in row] for row in self.test_list]
        self.assertEqual(self.test_list, data)


class TestValidatePath(unittest.TestCase):
    def test_validate_path_nonexistent(self):
        self.assertTrue(validate_file_path("nonexistent_file.txt"))

    def test_validate_path_existing(self):
        with open("existing_file.txt", "w") as f:
            f.write("test")
        try:
            self.assertFalse(validate_file_path("existing_file.txt"))
        finally:
            os.unlink("existing_file.txt")


class TestValidateExtension(unittest.TestCase):
    def test_validate_extension(self):
        self.assertFalse(validate_file_extension("/path/to/invalid_extension.xyz", ('.csv', '.json')))

        self.assertTrue(validate_file_extension("/path/to/valid_file.json", ('.csv', '.json')))
        self.assertTrue(validate_file_extension("/path/to/valid_file.csv", ('.csv', '.json')))


class TestValidateList(unittest.TestCase):
    def test_validate_list(self):
        self.assertFalse(validate_array("[[1, 2], 3, 4]"))
        self.assertFalse(validate_array("[[1, 2], ['3', 4]]"))
        self.assertFalse(validate_array("[[1, 2], [3, '4']]"))
        self.assertTrue(validate_array("[[1, 2], [3, 4]]"))


if __name__ == '__main__':
    unittest.main()
