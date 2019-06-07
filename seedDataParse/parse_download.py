import os
import requests

def main():
    fp = open("collage_parsed.json", 'r')
    dir = "issues/"

    done = False
    for line in fp:
        if "title" in line:
            title = line.strip()[10:-2]
        if "image" in line:
            image = line.strip()[10:-2]
        if "issue" and "pdf" in line:
            issue = line.strip()[10:-2]
            done = True
        if done:
            name = title.replace(' ', '_').lower()
            location = dir + name
            os.makedirs(location)

            if image is not "":
                response = requests.get(image)
                if response.status_code == 200:
                    with open(location + "/" +name + ".jpg", 'wb') as f:
                        f.write(response.content)
                del response

            if issue is not "":
                response = requests.get(issue)
                if response.status_code == 200:
                    with open(location + "/" +name + ".pdf", 'wb') as f:
                        f.write(response.content)
                del response 
                
            done = False

main()