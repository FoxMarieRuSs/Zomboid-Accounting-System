import pytest
from src.inventory import Inventory

@pytest.fixture
def inventory():
    return Inventory('test_data.csv')

def test_get_item_by_id(inventory):
    item = inventory.get_item_by_id('1')
    assert item['Name'] == 'Hummer'

def test_search_by_name(inventory):
    results = inventory.search_by_name('Nails')
    assert len(results) == 2
