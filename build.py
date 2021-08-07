#!/usr/bin/python3
import os
import re
import shutil

template_directory = 'wizixo/template/'
dist_directory = 'wizixo/dist/'

# Delete dist directory if exists and create it again
if os.path.exists(dist_directory):
    shutil.rmtree(dist_directory)
os.mkdir(dist_directory)

for page in os.listdir(template_directory):
    if page.startswith("mint-page-") and page.endswith(".html"):
        shutil.copy2(template_directory + page, dist_directory + page)
        new_page = page.replace("page-", "")
        with open(template_directory + page) as source:
            with open(dist_directory + new_page, "w") as destination:
                print("Generating %s from %s" % (new_page, page))
                for line in source:
                    line = line.rstrip()
                    if "<include" in line:
                        attributes = re.findall(r'(\S+)=["\']?((?:.(?!["\']?\s+(?:\S+)=|[>"\']))+.)["\']?', line, re.I)
                        variables = {}
                        src = None
                        for attribute in attributes:
                            name, value = attribute
                            if name == "src":
                                src = value
                            else:
                                variables[name] = value
                        if src != None and os.path.exists(template_directory + src):
                            print("  --> Adding content from %s" % src)
                            with open(template_directory + src) as content:
                                for content_line in content:
                                    content_line = content_line.rstrip()
                                    for name in variables.keys():
                                        value = variables[name]
                                        content_line = content_line.replace("$%s" % name, value)
                                    print(content_line, file=destination)
                    else:
                        print(line, file=destination)
    else:
        source = template_directory + page
        destination = dist_directory + page
        if os.path.isdir(source):
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)
