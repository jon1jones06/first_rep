import os

os.makedirs("test_folder/sub_folder", exist_ok=True)

files = os.listdir(".")
print(files)