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
        f.write("      font-weight : bold; \n")
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
        # <a href="destination.html">
        #     <button>Click Me!</button>
        # </a>
        f.write("    <div> \n")
        f.write("      <b>Class:&nbsp;</b> \n")
        f.write("      <a href='https://08lkabe82u4c-496ff2e9c6d22116-5000-colab.googleusercontent.com/'> <button type='button' class='button button_MATERIAL'>MATERIAL</button> </a>\n")
        f.write("      <button type='button' class='button button_MLIP'>MLIP</button> \n")
        f.write("      <button type='button' class='button button_PROPERTY'>PROPERTY</button> \n")
        f.write("      <button type='button' class='button button_SIMULATION'>SIMULATION</button> \n")
        f.write("      <button type='button' class='button button_VALUE'>VALUE</button> \n")
        f.write("      <button type='button' class='button button_APPLICATION'>APPLICATION</button> \n")
        f.write("      <button type='button' class='button button_OTHER'>OTHER</button> \n")
        f.write("    </div>\n")

        f.write("    <div>\n")
        for word in text:
            f.write(f"      <button  type='button' class='button button_words'>{word}</button> \n")
        f.write("    </div>\n")
        
        f.write("  </form>\n")
        f.write("{% endblock %}\n")