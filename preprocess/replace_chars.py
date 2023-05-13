import os
  
charmap = {"~": "č", "{": "š", "}" : "ć", "|" : "đ", "`": "ž", "[": "Š", "@" : "Ž", "^" : "Č", "]" : "Ć", "\\": "Đ"}

def replace_chars(file_path, dest_path):
    with open(file_path, 'r') as f:
        try:
            text = f.read()
        except UnicodeDecodeError:
            print("Decode error, skipping file!")
            return
    for char, replacement in charmap.items():
        text = text.replace(char, replacement)
    with open(dest_path, 'w') as f:
        f.write(text)

script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
years = ["2020"]
months = ["01", "02"]

for y in years:
    for m in months:
        try:
            path = f"./COVIDdataset/{y}-{m}"
            path_result = f"./charreplace/{y}-{m}"
            path = os.path.join(script_dir, path)
            os.chdir(path)
            path_result = os.path.join(script_dir, path_result)

            for date in os.listdir():
                curr_path = os.path.join(path, date)
                curr_path_result = os.path.join(path_result, date)
                os.chdir(curr_path)
                os.makedirs(curr_path_result, exist_ok=True)

                cnt = 0
                for file in os.listdir():
                    file_path = f"{curr_path}/{file}"
                    dest_path = f"{curr_path_result}/file{cnt}.txt"
                    replace_chars(file_path, dest_path)
                    cnt += 1
        except FileNotFoundError:
            print(f"{y}-{m} not found")
