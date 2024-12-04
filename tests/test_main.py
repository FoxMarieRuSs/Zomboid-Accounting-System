import pytest
from services import FileReader, DataProcessor, FileWriter

def test_read_csv():
    reader = FileReader()
    data = reader.read_csv('test_data.csv')
    assert len(data) > 0

def test_sort():
    processor = DataProcessor()
    data = [{'name': 'Alice'}, {'name': 'Bob'}]
    sorted_data = processor.sort(data, 'name')
    assert sorted_data[0]['name'] == 'Alice'
