import os

base_dir = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions"
search_str = "www.mysticdigitalsolutions.com"
replace_str = "mysticdigitalsolutions.com"

for root, dirs, files in os.walk(base_dir):
    if "node_modules" in dirs:
        dirs.remove("node_modules")
    if ".git" in dirs:
        dirs.remove(".git")
        
    for file in files:
        if file.endswith(".html") or file.endswith(".xml") or file.endswith(".txt") or file.endswith(".js"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if search_str in content:
                    new_content = content.replace(search_str, replace_str)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

print("Global replacement finished.")
