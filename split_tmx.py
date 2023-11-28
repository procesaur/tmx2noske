from xml.etree import ElementTree
from os.path import isfile


filename_column = "id"
metadata_filename = "metadata.csv"
separator = "\t"
lang_attr = '{http://www.w3.org/XML/1998/namespace}lang'
xml_head = "<?xml version='1.0' encoding='utf8'?>"


def create_root(info, metadata):
    root = ElementTree.Element("doc")
    for key, value in zip(info, metadata):
        root.set(key, value)
    return root


def GenerateXML(metadata, file_path, info, pair_element):
    tmx = ElementTree.parse(file_path)
    langs = [x.attrib[lang_attr] for x in tmx.find('.//tu').findall('tuv')]

    roots = {lang: create_root(info, metadata) for lang in langs}
    trees = {}

    def get_segs(lang):
        segs = [x.find(pair_element) for x in tmx.findall('.//tuv') if x.attrib[lang_attr] == lang]
        return segs

    for lang in langs:
        for x in get_segs(lang):
            roots[lang].append(x)
        trees[lang] = ElementTree.ElementTree(roots[lang])

    return trees


def generate_split_files(directory, pair):

    with open(directory + "/" + metadata_filename, "r", encoding="utf8") as md:
        metadata_lines = [[y.rstrip() for y in x.split(separator)] for x in md.readlines() if x]

    fn_index = metadata_lines[0].index(filename_column)
    info = metadata_lines[0]
    del metadata_lines[0]

    file_paths = [(x, directory + "/" + x[fn_index] + ".xml") for x in metadata_lines]
    temp_docs = [GenerateXML(meta, file_path, info, pair) for meta, file_path in file_paths if isfile(file_path)]
    docs = {}
    for lang in temp_docs[0].keys():
        docs[lang] = [x[lang] for x in temp_docs]

    for lang, doc in docs.items():
        strings = [ElementTree.tostring(x.getroot(), encoding='utf8').decode("utf-8").split(xml_head)[1] for x in doc]
        new_file_name = "results/" + directory + "_" + lang + ".xml"
        with open(new_file_name, "w", encoding="utf-8") as r:
            r.write("\n".join(strings).replace('<seg>', '\n<seg>'))


def get_info(directory):
    with open(directory + "/" + metadata_filename, "r", encoding="utf8") as md:
        metadata_lines = [[y.rstrip() for y in x.split(separator)] for x in md.readlines() if x]
    info = metadata_lines[0]

    return info
