import os
print('Exist:', os.access('C:\\Users\\user\\Documents\\pp2-22B030426\\tsis6\\directories and files\\message.txt', os.F_OK))
print('Readable:', os.access('C:\\Users\\user\\Documents\\pp2-22B030426\\tsis6\\directories and files\\message.txt', os.R_OK))
print('Writable:', os.access('C:\\Users\\user\\Documents\\pp2-22B030426\\tsis6\\directories and files\\message.txt', os.W_OK))
print('Executable:', os.access('C:\\Users\\user\\Documents\\pp2-22B030426\\tsis6\\directories and files\\message.txt', os.X_OK))