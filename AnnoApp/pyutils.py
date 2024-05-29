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
        f.write("    <style>\n")
        f.write("    .button {\n")
        f.write("      padding: 4px 8px;\n")
        f.write("      margin: 4px 2px;\n")
        f.write("      border-color: gray;\n")
        f.write("    }\n")
        f.write("    .button:hover {\n")
        f.write("      background-color: gray; \n")
        f.write("    }\n")
        
        f.write("    .button_MATERIAL {\n")
        f.write("      background-color: red; \n")
        f.write("      color: white; \n")
        f.write("    }\n")
        
        f.write("    .button_MLIP {\n")
        f.write("      background-color: blue; \n")
        f.write("      color: white; \n")
        f.write("    }\n")
        
        f.write("    .button_PROPERTY {\n")
        f.write("      background-color: green; \n")
        f.write("      color: white; \n")
        f.write("    }\n")
        
        f.write("    .button_SIMULATION {\n")
        f.write("      background-color: magenta; \n")
        f.write("      color: white; \n")
        f.write("    }\n")
        
        f.write("    .button_VALUE {\n")
        f.write("      background-color: teal; \n")
        f.write("      color: white; \n")
        f.write("    }\n")
        
        f.write("    .button_APPLICATION {\n")
        f.write("      background-color: orange; \n")
        f.write("      color: white; \n")
        f.write("    }\n")
        
        f.write("    .button_OTHER {\n")
        f.write("      background-color: lightgray; \n")
        f.write("      color: white; \n")
        f.write("    }\n")
        
        f.write("    .button_words {\n")
        f.write("      background-color: white; \n")
        f.write("    }\n")
        f.write("    .button_words:hover {\n")
        f.write("      background-color: yellow; \n")
        f.write("    }\n")
        
        f.write("    </style>\n")
        
        f.write("    <div> \n")
        f.write("      <b>Class:&nbsp;</b> \n")
        f.write("      <button class='button button_MATERIAL'>MATERIAL</button> \n")
        f.write("      <button class='button button_MLIP'>MLIP</button> \n")
        f.write("      <button class='button button_PROPERTY'>PROPERTY</button> \n")
        f.write("      <button class='button button_SIMULATION'>SIMULATION</button> \n")
        f.write("      <button class='button button_VALUE'>VALUE</button> \n")
        f.write("      <button class='button button_APPLICATION'>APPLICATION</button> \n")
        f.write("      <button class='button button_OTHER'>OTHER</button> \n")
        # f.write("      <span style='background-color:red;color:white;'>&nbsp;MATERIAL&nbsp;</span> \n")
        # f.write("      <span style='background-color:blue;color:white;'>&nbsp;MLIP&nbsp;</span> \n")
        # f.write("      <span style='background-color:green;color:white;'>&nbsp;PROPERTY&nbsp;</span> \n")
        # f.write("      <span style='background-color:magenta;color:white;'>&nbsp;SIMULATION&nbsp;</span> \n")
        # f.write("      <span style='background-color:teal;color:white;'>&nbsp;VALUE&nbsp;</span> \n")
        # f.write("      <span style='background-color:orange;color:white;'>&nbsp;APPLICATION&nbsp;</span> \n")
        # f.write("      <span style='background-color:lightgray;color:white;'>&nbsp;OTHER&nbsp;</span> \n")
        f.write("    </div>\n")

        f.write("    <div>\n")
        for word in text:
            f.write(f"      <button class='button button_words'>{word}</button> \n")
        f.write("    </div>\n")
        
        f.write("  </form>\n")
        f.write("{% endblock %}\n")