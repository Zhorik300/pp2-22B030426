import os
if os.path.exists("A.txt"):
  os.remove("A.txt")
else:
  print("The file does not exist")