import substring
import requests
from lxml import etree, html
import uuid

def main():

    # Potential get request and clean up 
    # URL = "https://www.mtsu.edu/collage/issues.php"
    # r = requests.get(url=URL)
    # fp3 = open('test.txt', 'w')
    # document_root = html.fromstring(r.text)
    # fp3.write(etree.tostring(document_root, encoding='unicode', pretty_print=True))

    # From files for now
    collage_1 = open('collage_1.txt', 'r')
    collage_2 = open('collage_2.txt', 'r')
    write_file = open('collage_parsed.json', 'w')

    # Start JSON format
    write_file.write("[\n")

    # To identify is in <a> block
    search = False

    is_first = True

    for line in collage_1:

        # Start of html tag
        if "<a" in line:

            # Link for the image of the issue
            img = substring.substringByChar(line[line.index("href") + 4:], startChar="h", endChar="\"")[:-1]

            # Title of the issue
            title = substring.substringByChar(line[line.index("title") + 6:], startChar=line[line.index("title") + 6:][1], endChar="\"")[:-1]

            search = True

        # Search inside <a> tag
        if search:
            # Links
            if "window.open" in line:
                link = substring.substringByChar(line[line.index("window.open") + 1:], startChar="(", endChar=")")[2:-2]
                if "soundcloud" in link:
                    soundcloud = link
                elif "youtube" in link:
                    youtube = link
                else:
                    issue = link

        # End of html tag
        if "</a>" in line:

            writeToFile(is_first, write_file, title, img, issue, youtube, soundcloud)
            is_first = False
            title = None
            img = None
            issue = None
            youtube = None
            soundcloud = None

            # Out of tag
            search = False
    
    # File 1 done
    collage_1.close()

    # Parse through second file
    for line in collage_2:
        if "<a" in line:
            # Get title and issue pdf link
            title = substring.substringByChar(line[line.index(">"):], startChar=">", endChar="<")[1:-1]
            issue = "https://www.mtsu.edu" + substring.substringByChar(line[line.index("href") + 4:], startChar="/", endChar="\"")[:-1] 
            img = None
            youtube = None
            soundcloud = None
        writeToFile(is_first, write_file, title, img, issue, youtube, soundcloud)

    write_file.write("\n]")

    collage_2.close()
    write_file.close()

def writeToFile(is_first, write_file, title, img, issue, youtube, soundcloud):

    if is_first:
        write_file.write("\t{\n")
    else:
        write_file.write(",\n\t{\n")
    
    write_file.write("\t\t\"model\": \"issues.issuse\", \n")

    # Write unique pk to file
    write_file.write("\t\t\"pk\":" + " \"" + str(uuid.uuid4()) + "\",")
    write_file.write('\n')

    write_file.write("\t\t\"fields\": { \n")

    # Write title to file in JSON format
    try:
        write_file.write("\t\t\t\"Title\":" + " \"" + title + "\",")
    except:
        write_file.write("\t\t\t\"Title\": \"No title\",")
    finally:
        write_file.write('\n')

    # Write image to file in JSON format
    try:
        write_file.write("\t\t\t\"Image\":" + " \"" + img + "\",")
    except:
        write_file.write("\t\t\t\"Image\": \"No link\",")
    finally:
        write_file.write('\n')

    # Write issue pdf link to file in JSON format
    try:
        write_file.write("\t\t\t\"Issue\":" + " \"" + issue + "\",")
    except:
        write_file.write("\t\t\t\"Issue\": \"No link\",")
    finally:
        write_file.write('\n')

    # Write youtube link to file in JSON format
    try:
        write_file.write("\t\t\t\"Youtube\":" + " \"" + youtube + "\",")
    except:
        write_file.write("\t\t\t\"Youtube\": \"No link\",")
    finally:
        write_file.write('\n')

    # Write soundcloud link to file in JSON format
    try:
        write_file.write("\t\t\t\"Soundcloud\":" + " \"" + soundcloud + "\"")
    except:
        write_file.write("\t\t\t\"Soundcloud\": \"No link\"")
    finally:
        write_file.write('\n')
    write_file.write("\t\t}\n\t}")

main()