#!/usr/bin/python3
import os
import re

os.chdir("wizixo/template/")
for page in os.listdir("."):
    if page.startswith("mint-page-") and page.endswith(".html"):
        new_page = page.replace("page-", "")
        with open(page) as source:
            with open(new_page, "w") as destination:
                print("Generating %s from %s" % (new_page, page))
                for line in source:
                    line=line.rstrip()
                    if "<include" in line:
                        srcs = re.findall(r'<include[^<>]+src=["\']([^"\'<>]+\.(?:html|png|jpe?g))["\']', line, re.I)
                        for src in srcs:
                            if os.path.exists(src):
                                print("  --> Adding content from %s" % src)
                                with open(src) as content:
                                    for content_line in content:
                                        print(content_line.rstrip(), file=destination)
                    else:
                        print(line, file=destination)
