from xml.etree.ElementTree import Element, SubElement, ElementTree
import os

def parse_ls():
    root = Element('tree')
    items = {
        '.': root
    }
    
    current_folder = '.'
    for line in open('ls_output.txt'):
        current_folder = process_line(line[:-1], current_folder, items)

    ElementTree(root).write('ls_output.xml')

def process_line(line, current_folder, items):
    if not line:
        return current_folder

    is_directory_header = line.startswith('./')
    if is_directory_header:
        # Remove trailing colon
        current_folder = line[:-1]
        items[current_folder].tag = 'folder'
    else:
        file_name = line
        full_path = os.path.join(current_folder, file_name)
        items[full_path] = SubElement(items[current_folder], 'file', {'name': file_name})

    return current_folder


if __name__ == '__main__':
    parse_ls()