from xml.etree import ElementTree
from os.path import isfile, splitext, isdir
from os import mkdir


filename_column = "id"
metadata_filename = "metadata.csv"
separator = "\t"
lang_attr = '{http://www.w3.org/XML/1998/namespace}lang'
xml_head = "<?xml version='1.0' encoding='utf8'?>"

ini_dir = "data/tmx/"
target_dir = "data/source/"


def create_root(info, metadata):
    root = ElementTree.Element("doc")
    for key, value in zip(info, metadata):
        root.set(key, value)
    return root


def GenerateXML(metadata, file_path, info, pair_element):
    tmx = ElementTree.parse(file_path)
    langs = [x.attrib[lang_attr] for x in tmx.find('.//tu').findall('tuv')]

    def get_segs(language):
        segs = [x.find(pair_element) for x in tmx.findall('.//tuv') if x.attrib[lang_attr] == language]
        return segs

    for lang in langs:
        root = create_root(info, metadata)
        for x in get_segs(lang):
            root.append(x)
        xml_string = ElementTree.tostring(root, encoding='utf8').decode("utf-8").split(xml_head)[1]
        save_path = file_path.replace(ini_dir, target_dir)
        save_path = splitext(save_path)[0] + "_" + lang + ".xml"
        with open(save_path, "w", encoding="utf-8") as xf:
            xf.write(xml_string.replace('<seg>', '\n<seg>'))


def generate_split_files(directory, pair):
    print("splitting TMXs...")

    if not isdir(target_dir + directory):
        mkdir(target_dir + directory)

    with open(ini_dir + directory + "/" + metadata_filename, "r", encoding="utf8") as md:
        metadata_lines = [[y.rstrip() for y in x.split(separator)] for x in md.readlines() if x]

    fn_index = metadata_lines[0].index(filename_column)
    info = metadata_lines[0]
    del metadata_lines[0]

    file_paths = [(x, ini_dir + directory + "/" + x[fn_index] + ".xml") for x in metadata_lines]
    for meta, file_path in file_paths:
        if isfile(file_path):
            GenerateXML(meta, file_path, info, pair)
        else:
            print(file_path)


def get_info(directory):
    with open(ini_dir + directory + "/" + metadata_filename, "r", encoding="utf8") as md:
        metadata_lines = [[y.rstrip() for y in x.split(separator)] for x in md.readlines() if x]
    info = metadata_lines[0]

    return info
