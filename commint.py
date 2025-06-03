import os
import datetime

file_path = "daily_update.txt"

for i in range(100): 
    with open(file_path, "a") as file:
        file.write(f"Commit {i+1}: Updated on {datetime.datetime.now()}\n")

    os.system("git add .")
    os.system(f'git commit -m "Auto commit {i+1}: {datetime.datetime.now()}"')

os.system("git push origin main")  # শেষে সব কমিট GitHub-এ পুশ করবে