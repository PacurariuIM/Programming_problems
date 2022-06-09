import time
import os
import shutil
import json


source_folder = "D:/Old_dir//"
dest_folder = "D:/New_dir//"
# os.mkdir(dest_folder)
start = time.time()

for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = dest_folder + file_name
    # copy only files
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('Files copied: ', file_name)

end = time.time()
interval = end - start
print(interval)

file = open("data.json", "r")
data = json.load(file)
file = open("data.json", "w")
data["results"].append(interval)
json.dump(data, file, indent=4)














