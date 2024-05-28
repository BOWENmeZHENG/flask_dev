import re

def split_para(para):
    return re.findall(r"[\w']+|[-.,!?;/\(\)\[\]]", para)

def write_anno(name, text):
    with open(f'AnnoApp/templates/blog/{name}.html', 'w') as f:
        f.write("{% extends 'base.html' %}\n")
        f.write("{% block header %}\n")
        f.write("  <h1>{% block title %}Annotate{% endblock %}</h1>\n")
        f.write("{% endblock %}\n")
        f.write("{% block content %}\n")
        f.write("  <form method='post'>\n")
        f.write("    <p> \n")
        f.write("      <b>Class:&nbsp;</b> \n")
        f.write("      <span style='background-color:red;color:white;'>&nbsp;MATERIAL&nbsp;</span> \n")
        f.write("      <span style='background-color:blue;color:white;'>&nbsp;MLIP&nbsp;</span> \n")
        f.write("      <span style='background-color:green;color:white;'>&nbsp;PROPERTY&nbsp;</span> \n")
        f.write("      <span style='background-color:magenta;color:white;'>&nbsp;SIMULATION&nbsp;</span> \n")
        f.write("      <span style='background-color:teal;color:white;'>&nbsp;VALUE&nbsp;</span> \n")
        f.write("      <span style='background-color:orange;color:white;'>&nbsp;APPLICATION&nbsp;</span> \n")
        f.write("      <span style='background-color:lightgray;color:white;'>&nbsp;OTHER&nbsp;</span> \n")
        f.write("    </p>\n")
        f.write("    <style>\n")
        f.write("    .tooltip {\n")
        f.write("      position: relative;\n")
        f.write("      display: inline-block;\n")
        f.write("    }\n")
        f.write("    .tooltip .tooltiptext {\n")
        f.write("      visibility: hidden;\n")
        f.write("      background-color: black;\n")
        f.write("      color: #fff;\n")
        f.write("      text-align: center;\n")
        f.write("      position: absolute;\n")
        f.write("      z-index: 1;\n")
        f.write("    }\n")
        f.write("    .tooltip:hover .tooltiptext {\n")
        f.write("      visibility: visible;\n")
        f.write("    }\n")
        f.write("    </style>\n")
        f.write("    <div>\n")
        for word in text:
            f.write(f"      <span class='tooltip'>{word} <span class='tooltiptext'>{word}</span> </span> \n")
            
            # f.write(f"      <span class='tooltiptext'>{word}</span>\n")
        f.write("    </div>\n")
        
        f.write("  </form>\n")
        f.write("{% endblock %}\n")