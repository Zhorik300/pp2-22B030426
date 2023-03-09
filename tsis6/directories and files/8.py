import os
if os.path.exists("out.txt"):
  os.remove("out.txt")
else:
  print("The file does not exist")