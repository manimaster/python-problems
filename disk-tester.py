import os
import time
import subprocess

def test_write_speed(directory, file_size_mb=100):
    """
    Test write speed by writing random bytes to a temporary file.
    
    Args:
    - directory (str): The directory where the test file will be created.
    - file_size_mb (int): The size of the file to be written in MB.
    
    Returns:
    - float: Write speed in MB/s.
    """
    test_file = os.path.join(directory, "temp_speedtest_file")
    with open(test_file, "wb") as f:
        start_time = time.time()
        for _ in range(file_size_mb):
            f.write(os.urandom(1024 * 1024))  # write 1MB data
        f.flush()
        os.fsync(f.fileno())  # ensure it's written to disk
    duration = time.time() - start_time
    os.remove(test_file)
    return file_size_mb / duration  # MB/s

def test_read_speed(directory, file_size_mb=100):
    """
    Test read speed by reading a previously written file.
    
    Args:
    - directory (str): The directory where the test file will be created.
    - file_size_mb (int): The size of the file to be read in MB.
    
    Returns:
    - float: Read speed in MB/s.
    """
    test_file = os.path.join(directory, "temp_speedtest_file")
    with open(test_file, "wb") as f:
        f.write(os.urandom(file_size_mb * 1024 * 1024))
    
    with open(test_file, "rb") as f:
        start_time = time.time()
        while f.read(1024 * 1024):  # read 1MB data
            pass
    duration = time.time() - start_time
    os.remove(test_file)
    return file_size_mb / duration  # MB/s

def test_iops(directory, num_operations=1000):
    """
    Test IOPS (Input/Output Operations Per Second) by doing random read and write operations.
    
    Args:
    - directory (str): The directory where the test file will be created.
    - num_operations (int): The number of read/write operations.
    
    Returns:
    - float: Number of operations per second.
    """
    test_file = os.path.join(directory, "temp_speedtest_file")
    with open(test_file, "wb") as f:
        f.write(os.urandom(4 * 1024 * 1024))  # 4MB of data

    start_time = time.time()
    with open(test_file, "rb+") as f:
        for _ in range(num_operations):
            position = int(f.tell() * os.urandom(1)[0] / 256)
            f.seek(position)
            f.write(os.urandom(1024))  # random write of 1KB
            f.seek(position)
            f.read(1024)  # random read of 1KB
    duration = time.time() - start_time
    os.remove(test_file)
    return num_operations / duration  # operations per second

def shred_file(filepath):
    """
    Securely delete a file using the 'shred' utility (Linux only).
    
    Args:
    - filepath (str): The path of the file to be shredded.
    
    Returns:
    - str: Outcome message.
    """
    try:
        subprocess.run(['shred', '-u', filepath], check=True)
        return f"File {filepath} shredded successfully."
    except subprocess.CalledProcessError:
        return f"Failed to shred {filepath}. Ensure you have the required permissions and the 'shred' utility installed."

def wipe_disk(disk_path):
    """
    Wipe a disk using the 'dd' utility (Linux only).
    
    Args:
    - disk_path (str): The path to the disk (e.g., /dev/sda).
    
    Returns:
    - str: Outcome message.
    """
    try:
        subprocess.run(['dd', 'if=/dev/zero', f'of={disk_path}', 'bs=1M'], check=True)
        return f"Disk {disk_path} wiped successfully."
    except subprocess.CalledProcessError:
        return f"Failed to wipe {disk_path}. Ensure you have the required permissions and the 'dd' utility installed."

def check_disk_errors(disk_path):
    """
    Check a disk for errors using the 'fsck' utility (Linux only).
    
    Args:
    - disk_path (str): The path to the disk (e.g., /dev/sda).
    
    Returns:
    - str: Outcome message or errors found.
    """
    try:
        result = subprocess.run(['fsck', '-n', disk_path], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.output

# You can create a main() function to call these functions based on user input for a full-fledged tool.
