#!/usr/bin/python3
import os
import re

for page in os.listdir("."):
    if page.startswith("mint-page-") and page.endswith(".html"):
        new_page = page.replace("page-", "")
        with open(page,encoding='utf8') as source:
            with open(new_page, "w") as destination:
                print("Generating %s from %s" % (new_page, page))
                for line in source:
                    line=line.rstrip()
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
                        if src != None and os.path.exists(src):
                            print("  --> Adding content from %s" % src)
                            with open(src) as content:
                                for content_line in content:
                                    content_line = content_line.rstrip()
                                    for name in variables.keys():
                                        value = variables[name]
                                        content_line = content_line.replace("$%s" % name, value)
                                    print(content_line, file=destination)
                    else:
                        print(line, file=destination)
