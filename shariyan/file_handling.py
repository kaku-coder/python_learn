import os 

current_directory = os.getcwd()
print(current_directory)

# Current folder (shariyan) ke bajaye main 'd:\python' folder ki files dekhne ke liye path pass karein:
files = os.listdir(r"d:\python")
print("Files in python folder:", files)