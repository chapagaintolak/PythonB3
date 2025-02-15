import os
# To create 
for i in range(1,101):
     #os.mkdir(f"Photos{i}")
     os.rmdir(f"Photos{i}")
# To delete
for i in range(1,101):
     os.rmdir(f"Photos{i}")
