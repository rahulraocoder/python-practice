import os
import tempfile
import time
from backup import backup_file, restore_file, list_backups

def test_backup_and_restore():
    # Create test file
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"test content")
        test_file = tmp.name
    
    try:
        # Test backup
        backup_path = backup_file(test_file)
        assert backup_path is not None
        assert os.path.exists(backup_path)
        assert test_file in backup_path  # Verify original filename in backup
        
        # Test restore to new location
        restored_path = test_file + ".restored"
        assert restore_file(backup_path, restored_path) is True
        assert os.path.exists(restored_path)
        
        # Verify content
        with open(restored_path, 'rb') as f:
            assert f.read() == b"test content"
            
        # Test restore to original location
        os.remove(test_file)
        assert restore_file(backup_path, test_file) is True
        assert os.path.exists(test_file)
        
    finally:
        # Clean up
        for f in [test_file, backup_path, restored_path]:
            if f and os.path.exists(f):
                try:
                    os.remove(f)
                except:
                    pass

def test_list_backups():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        test_file = tmp.name
    
    try:
        # Create multiple backups
        backup1 = backup_file(test_file)
        time.sleep(1)  # Ensure different timestamps
        backup2 = backup_file(test_file)
        
        # Test listing
        backups = list_backups(test_file)
        assert len(backups) >= 2
        assert backup1 in backups
        assert backup2 in backups
        # Newest should be first
        assert backups.index(backup2) < backups.index(backup1)
        
    finally:
        for f in [test_file, backup1, backup2]:
            if f and os.path.exists(f):
                try:
                    os.remove(f)
                except:
                    pass
