import os
import hashlib
from pathlib import Path
  

script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
years = ["2019", "2020", "2021"]
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

for y in years:
    for m in months:
        try:
            path = f"./charreplace/{y}-{m}"
            list_of_files = os.walk(path)
            unique_files = dict()
            for root, folders, files in list_of_files:
                for file in files:
                    file_path = Path(os.path.join(root, file))
                    Hash_file = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
                    if Hash_file not in unique_files:
                        unique_files[Hash_file] = file_path
                    else:
                        os.remove(file_path)
                        print(f"{file_path} has been deleted")
        except FileNotFoundError:
            print(f"{y}-{m} not found")