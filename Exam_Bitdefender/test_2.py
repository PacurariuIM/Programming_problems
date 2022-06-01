import time
import webbrowser
import json

start = time.time()

url = 'https://google.com'
webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)

end = time.time()
result = end - start
print(result)

with open("data.txt", "w") as outfile:
    json.dump(result, outfile)
