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

results = [interval]
with open("data.json", "w") as filehandle:
    dic = {"results": results}
    # data = json.load(filehandle)
    # filehandle.seek(0)
    json.dump(dic, filehandle, indent=4)
    filehandle.close()






# file = open("data.json", "w")
# file.read()
#
# dic = {"results": results}
# list_json = json.dumps(dic)
# file.close()
# print(dic)






