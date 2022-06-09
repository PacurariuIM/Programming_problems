import time
import webbrowser
import json
import os

start = time.time()

url = 'https://google.com'
webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)
# os.system("taskkill /im chrome.exe /f")
end = time.time()
interval = end - start
print(interval)

file = open("data2.json", "r")
data = json.load(file)
file = open("data2.json", "w")
data["results"].append(interval)
json.dump(data, file, indent=4)
