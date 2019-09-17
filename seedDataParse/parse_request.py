import substring
import requests
from lxml import etree, html
import uuid
import os
import re
from bs4 import BeautifulSoup



dir = "issues/"


def main():
    URL = "https://www.mtsu.edu/collage/issues.php"
    r = requests.get(url=URL)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    samples = soup.findAll("div", {"class": "grid-item-container"})


    write_file = open('collage_parsed.json', 'w')
    write_file.write("[\n")

    is_first = True
    count = 78

    for sample in samples[:-1]:
        text = str(sample.findAll("div"))
        try:
            image = "https://mtsu.edu" + substring.substringByChar(text[text.index("src"):], startChar="/", endChar="\"")[:-1]
        except:
            image = ""
        try: 
            title = substring.substringByChar(text[text.index("h3>"):], startChar=">", endChar="<")[1:-1]
        except:
            title = ""
        try:
            pdf = "https://mtsu.edu" + substring.substringByChar(text[text.index("href=\"/coll"):], startChar="/", endChar="\"")[:-1]
        except:
            pdf = ""
        try: 
            youtube = substring.substringByChar(text[text.index("ref=\"https://www.youtube.com"):], startChar="h", endChar="\"")[:-1]
        except:
            youtube = ""
        try: 
            soundcloud = substring.substringByChar(text[text.index("ref=\"https://soundcloud.com/"):], startChar="h", endChar="\"")[:-1]
        except:
            soundcloud = ""


        if pdf == "https://mtsu.edu/collage/docs/Fall-1993.pdf":
            title = "Fall 1993"

        if pdf == "https://mtsu.edu/collage/docs/1982.pdf":
            title = "1982"

        writeToFile(is_first, count, write_file, title, image, pdf, youtube, soundcloud)

        count -= 1
        is_first = False

    write_file.write("\n]")
    write_file.close()


def writeToFile(is_first, count, write_file, title, img_link, issue_link, youtube, soundcloud):

    print("Working on", title)
    img, issue = get_issues(dir, title, img_link, issue_link)

    if is_first:
        write_file.write("\t{\n")
    else:
        write_file.write(",\n\t{\n")
    
    write_file.write("\t\t\"model\": \"issues.issue\", \n")

    # Write unique pk to file
    write_file.write("\t\t\"pk\":" + " \"" + str(count) + "\",")
    write_file.write('\n')

    write_file.write("\t\t\"fields\": { \n")

    # Write title to file in JSON format
    try:
        write_file.write("\t\t\t\"title\":" + " \"" + title + "\",")
    except:
        write_file.write("\t\t\t\"title\": \"\",")
    finally:
        write_file.write('\n')

    # Write image to file in JSON format
    try:
        write_file.write("\t\t\t\"image\":" + " \"" + img + "\",")
    except:
        write_file.write("\t\t\t\"image\": \"\",")
    finally:
        write_file.write('\n')

    # Write image link to file in JSON format
    try:
        write_file.write("\t\t\t\"image_link\":" + " \"" + img_link + "\",")
    except:
        write_file.write("\t\t\t\"image_link\": \"\",")
    finally:
        write_file.write('\n')

    # Write issue pdf link to file in JSON format
    try:
        write_file.write("\t\t\t\"issue\":" + " \"" + issue + "\",")
    except:
        write_file.write("\t\t\t\"issue\": \"\",")
    finally:
        write_file.write('\n')

    # Write issue link to file in JSON format
    try:
        write_file.write("\t\t\t\"issue_link\":" + " \"" + issue_link + "\",")
    except:
        write_file.write("\t\t\t\"issue_link\": \"\",")
    finally:
        write_file.write('\n')

    # Write youtube link to file in JSON format
    try:
        write_file.write("\t\t\t\"youtube\":" + " \"" + youtube + "\",")
    except:
        write_file.write("\t\t\t\"youtube\": \"\",")
    finally:
        write_file.write('\n')

    # Write soundcloud link to file in JSON format
    try:
        write_file.write("\t\t\t\"soundcloud\":" + " \"" + soundcloud + "\",")
    except:
        write_file.write("\t\t\t\"soundcloud\": \"\",")
    finally:
        write_file.write('\n')

    # Write created at to file in JSON format
    try:
        write_file.write("\t\t\t\"created_at\":" + " \"2019-06-01 00:00:00\"")
    finally:
        write_file.write('\n')

    write_file.write("\t\t}\n\t}")


def get_issues(dir, title, image, issue):

    name = title.replace(' ', '_').lower()
    location = dir + name
    os.makedirs(location)

    img_path = ""
    if image is not "":
        response = requests.get(image)
        if response.status_code == 200:
            file_name = location + "/" +name + ".jpg"
            with open(file_name, 'wb') as f:
                f.write(response.content)
                img_path = file_name.replace('\\', '\\\\')
        del response

    issue_path = ""
    if issue is not "":
        response = requests.get(issue)
        if response.status_code == 200:
            file_name = location + "/" +name + ".pdf"
            with open(file_name, 'wb') as f:
                f.write(response.content)
                issue_path = file_name.replace('\\', '\\\\')
        del response 

    return img_path, issue_path


main()