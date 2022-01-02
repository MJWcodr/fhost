import os
import pandoc
from datetime import date

def links(path, output_file_name="index.html"):
    header = f"""
---
author: Matthias Wünsch
date: {date.today()}
title: {os.path.basename(path)}
lang: de-de
keywords: []
---
"""
    out = ""
    for i in os.listdir(path):
        listitem = "- " + "[" + i + "]" + "(" + i + ")" + "\n"
        out = out + listitem
    out = header + out

    # turn the markdown list into an html file
    # and write it to "output_filename"

    file_list = pandoc.read(out, format="markdown")
    file_list_converted = pandoc.write(
        file_list, f"{path}/{output_file_name}", "html", ['--template', "links"])