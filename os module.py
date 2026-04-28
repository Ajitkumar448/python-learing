import os
directory_path = r"C:\Users\AJIT KUMAR\Documents"
contents = os.listdir(directory_path)
print(f"Contents of directory {directory_path}:")
for item in contents:
    print(item)