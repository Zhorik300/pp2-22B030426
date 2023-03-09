import os
path = 'C:\\Users\\user\\Documents\\pp2-22B030426\\tsis6'


for x in os.listdir():
    if x.endswith(".txt"):
        print("Only files :", x)

dir_list=os.listdir(path)
print("All directories:", dir_list)