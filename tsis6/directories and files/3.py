import os

path = r'C:\\Users\\user\\Documents\\pp2-22B030426\\c.txt'
print(os.path.exists(path))
path = r'gC:\\Users\\user\\Documents\\pp2-22B030426\\c.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))