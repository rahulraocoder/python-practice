import os
import tempfile
from contact_book import ContactBook

def test_add_and_search_contacts():
    cb = ContactBook()
    # Test adding new contact
    assert cb.add_contact("John", "123", "john@test.com") is True
    # Test duplicate detection
    assert cb.add_contact("John", "123", "john@test.com") is False
    
    # Test searching
    results = cb.search("John")
    assert len(results) == 1
    assert results[0]["name"] == "John"
    assert results[0]["phone"] == "123"

    # Search by phone should also work
    results = cb.search("123")
    assert len(results) == 1

def test_file_operations():
    cb = ContactBook()
    cb.add_contact("Alice", "456", "alice@test.com")
    
    # Use temp file for testing
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        try:
            # Test save/load
            cb.save_to_file(tmp.name)
            
            new_cb = ContactBook()
            new_cb.load_from_file(tmp.name)
            results = new_cb.search("Alice")
            assert len(results) == 1
            assert results[0]["email"] == "alice@test.com"
        finally:
            os.unlink(tmp.name)  # Clean up
