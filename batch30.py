import os

# Define the base directory where folders will be created
base_dir = r"C:\Users\PC 1\Pyths\30DaysofPython"

# Define the number of folders to create
num_folders = 30

# Loop to create folders
for i in range(1, num_folders + 1):
    folder_name = f"Day_{i}"
    folder_path = os.path.join(base_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created folder: {folder_path}")

print("All folders created.")
