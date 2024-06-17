import re

def split_para(para):
    return re.findall(r"[\w]+|[-.,\'!=?;/\(\)\[\]]", para)

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
        f.write("      color: white; \n")
        f.write("    }\n")
        f.write("    .button:hover {\n")
        f.write("      font-weight : bold; \n")
        f.write("    }\n")
        # Class buttons
        f.write("    .button_MATERIAL {\n")
        f.write("      background-color: red; \n")
        f.write("    }\n")
        f.write("    .button_MLIP {\n")
        f.write("      background-color: blue; \n")
        f.write("    }\n")
        f.write("    .button_PROPERTY {\n")
        f.write("      background-color: green; \n")
        f.write("    }\n")
        # f.write("    .button_SIMULATION {\n")
        # f.write("      background-color: magenta; \n")
        # f.write("    }\n")
        f.write("    .button_VALUE {\n")
        f.write("      background-color: teal; \n")
        f.write("    }\n")
        f.write("    .button_APPLICATION {\n")
        f.write("      background-color: orange; \n")
        f.write("    }\n")
        # Word buttons
        f.write("    .button_words {\n")
        f.write("      background-color: white; \n")
        f.write("      color: black; \n")
        f.write("    }\n")
        f.write("    .button_words:hover {\n")
        f.write("      background-color: yellow; \n")
        f.write("    }\n")
        
        f.write("    </style>\n")
        f.write("    <div> \n")
        f.write("      <b>Class:&nbsp;</b> \n")
        f.write("      <button type='button' class='button button_MATERIAL' onclick='Select_Func(\"MATERIAL\")'>MATERIAL</button>\n")
        f.write("      <button type='button' class='button button_MLIP' onclick='Select_Func(\"MLIP\")'>MLIP</button> \n")
        f.write("      <button type='button' class='button button_PROPERTY' onclick='Select_Func(\"PROPERTY\")'>PROPERTY</button> \n")
        # f.write("      <button type='button' class='button button_SIMULATION' onclick='Select_Func(\"SIMULATION\")'>SIMULATION</button> \n")
        f.write("      <button type='button' class='button button_VALUE' onclick='Select_Func(\"VALUE\")'>VALUE</button> \n")
        f.write("      <button type='button' class='button button_APPLICATION' onclick='Select_Func(\"APPLICATION\")'>APPLICATION</button> \n")
        f.write("    </div>\n")

        f.write("    <div>\n")
        for i, word in enumerate(text):
            f.write(f"      <button id='{i}' type='button' class='button button_words' onclick='F(\"{i}\")'>{word}</button> \n")
        f.write("    </div>\n")
        f.write("    <button type='button' style='width:200px;margin-top:20px;' onclick='saveAnnotation()'>Generate annotation</button>\n")
        f.write("    <input style='width:700px;margin-top:10px;' type='text' id='show' value=''/>\n")
        f.write("    <button type='button' onclick='copyAnnotation()' style='width:200px;'>Copy annotation</button>\n")
        f.write("    <a style='margin-top:20px;'class='action' href='{{ url_for(\"blog.update\", id=ID) }}'>Finish</a>\n")
        
        # ----------------------------
        # Script from here on
        # ----------------------------
        f.write("    <script>\n")
        f.write("    const annotation = {};\n")
        f.write("    function Select_Func(Class) {\n")
        f.write("      if  (Class === 'MATERIAL') F = Func_MATERIAL\n")
        f.write("      if  (Class === 'MLIP') F = Func_MLIP\n")
        f.write("      if  (Class === 'PROPERTY') F = Func_PROPERTY\n")
        # f.write("      if  (Class === 'SIMULATION') F = Func_SIMULATION\n")
        f.write("      if  (Class === 'PROPERTY') F = Func_PROPERTY\n")
        f.write("      if  (Class === 'VALUE') F = Func_VALUE\n")
        f.write("      if  (Class === 'APPLICATION') F = Func_APPLICATION\n")
        f.write("    }\n")
        f.write("    function Func_MATERIAL(id) {\n")
        f.write("      document.getElementById(id).style.backgroundColor = 'red';\n")
        f.write("      document.getElementById(id).style.color = 'white';\n")
        f.write("      annotation[id] = 'MATERIAL';\n")
        f.write("    }\n")
        f.write("    function Func_MLIP(id) {\n")
        f.write("      document.getElementById(id).style.backgroundColor = 'blue';\n")
        f.write("      document.getElementById(id).style.color = 'white';\n")
        f.write("      annotation[id] = 'MLIP';\n")
        f.write("    }\n")
        f.write("    function Func_PROPERTY(id) {\n")
        f.write("      document.getElementById(id).style.backgroundColor = 'green';\n")
        f.write("      document.getElementById(id).style.color = 'white';\n")
        f.write("      annotation[id] = 'PROPERTY';\n")
        f.write("    }\n")
        # f.write("    function Func_SIMULATION(id) {\n")
        # f.write("      document.getElementById(id).style.backgroundColor = 'magenta';\n")
        # f.write("      document.getElementById(id).style.color = 'white';\n")
        # f.write("      annotation[id] = 'SIMULATION';\n")
        # f.write("    }\n")
        f.write("    function Func_VALUE(id) {\n")
        f.write("      document.getElementById(id).style.backgroundColor = 'teal';\n")
        f.write("      document.getElementById(id).style.color = 'white';\n")
        f.write("      annotation[id] = 'VALUE';\n")
        f.write("    }\n")
        f.write("    function Func_APPLICATION(id) {\n")
        f.write("      document.getElementById(id).style.backgroundColor = 'orange';\n")
        f.write("      document.getElementById(id).style.color = 'white';\n")
        f.write("      annotation[id] = 'APPLICATION';\n")
        f.write("    }\n")
        f.write("    function saveAnnotation() {\n")
        f.write("      var anno = JSON.stringify(annotation);\n")
        f.write("      document.getElementById('show').value = anno;\n")
        f.write("    }\n")
        f.write("    function copyAnnotation() {\n")
        f.write("      var copyText = document.getElementById('show');\n")
        f.write("      copyText.select();\n")
        f.write("      navigator.clipboard.writeText(copyText.value);\n")
        f.write("    }\n")
        f.write("    </script>\n")
        
        f.write("  </form>\n")
        f.write("{% endblock %}\n")