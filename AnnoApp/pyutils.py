import re

def split_para(para):
    return re.findall(r"[\w']+|[-.,!?;/\(\)\[\]]", para)