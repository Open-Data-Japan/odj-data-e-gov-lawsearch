import os
import xml.etree.ElementTree as ET
#import xml.etree.ElementTree as Element

path_script_folder = os.path.dirname(os.path.realpath((__file__)))
path_input_files = path_script_folder + '/all_xml/'
path_processed_file = path_script_folder + "/" + "processed/japanese_law_text.txt"

input_file_sample = path_input_files + "108DF0000000103_20150801_000000000000000/108DF0000000103_20150801_000000000000000.xml" 


def format_tag(tag: type(ET.Element)) -> str:
    """
Law
LawNum
LawBody
LawTitle
Preamble
Paragraph
ParagraphNum
ParagraphSentence
Sentence
MainProvision
Article
ArticleTitle
Paragraph
ParagraphNum
ParagraphSentence
Sentence
Article
ArticleTitle
Paragraph
ParagraphNum
ParagraphSentence
Sentence
Article
ArticleTitle
Paragraph
ParagraphNum
ParagraphSentence
Sentence
    """
    return ""

def extract_text_from_xml(filepath: str) -> str:
    formatted_file = ""

    tree = ET.parse(filepath)
    
    root = tree.getroot()
    for item in root.iter():
        formatted_file += format_tag(item)

    return formatted_file


print(extract_text_from_xml(input_file_sample))
