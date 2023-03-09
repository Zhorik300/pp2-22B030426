import os
with open("C.txt") as f:
    with open("D.txt", "w") as f1:
        for line in f:
            f1.write(line)