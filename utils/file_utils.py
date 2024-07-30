import xml.etree.ElementTree as ET

def read_sql_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    sql_command = root.find('sql').text.strip()
    return sql_command
