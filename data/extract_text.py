import os
import xml.etree.ElementTree as ET
import warnings
import glob

path_script_folder = os.path.dirname(os.path.realpath((__file__)))
path_input_files = path_script_folder + '/all_xml/'
path_processed_file = path_script_folder + "/" + "processed/japanese_law_text.txt"

#input_file_sample = path_input_files + "108DF0000000103_20150801_000000000000000/108DF0000000103_20150801_000000000000000.xml" 
input_file_sample = path_input_files + '501AC0000000015_20230401_503AC0000000024/501AC0000000015_20230401_503AC0000000024.xml'

tag_format = {
    'Law' : None,
    'LawNum' : None,
    'LawBody' : None,
    'LawTitle' : None,
    'Preamble' : None,
    'Paragraph' : None,
    'ParagraphNum' : None
}

def format_tag(tag: type(ET.Element)) -> str:
    if tag.text is None:
        ret = ""
    else:
        ret = "" + tag.text
  
    format = tag_format.get(tag.tag, None)
    if format =='space':
        ret += ' '
    elif format =='newline':
        ret += '\n'
    elif format == 'skip':
        pass
    else: 
        warnings.warn("Tag " + tag.tag + " has no formatting")
        pass
    return ret

def extract_text_from_xml(filepath: str) -> str:
    formatted_file = ""

    tree = ET.parse(filepath)
    
    root = tree.getroot()
    for item in root.iter():
        formatted_file += format_tag(item)

    return formatted_file



#print(extract_text_from_xml(input_file_sample))
files = glob.glob(path_input_files + '/*/*xml')

with open(path_processed_file, "a") as outfile:
    for f in files:
        outfile.write(extract_text_from_xml(f))
