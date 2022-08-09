import os  # module to interact with the operating system (OS)

# Get current directory
pwd = os.getcwd()
print(f"Current working directory: {pwd}")

# List files and directories in current directory
files = os.listdir()

for file in files:
    print(file)
