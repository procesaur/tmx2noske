from os import listdir
from split_tmx import generate_split_files, get_info
from treetagger.treetagger import tag_multiple
from verticalizer import verticalize
from registerer import generate_registry


files_dir = "ItSr23"
information = "Parallel Serbian-Italian Corpus"
struct = ["seg"]
pair_element = "seg"


split_tmx = True
tag = True
registry = True

if split_tmx:
    generate_split_files(files_dir, pair_element)

if tag:
    files = [x for x in listdir("results") if files_dir in x and ".vert" not in x]
    for x in files:
        file_path = "results/" + x
        lang = x.split(".xml")[0].split("_")[1]
        input_files = verticalize(file_path)
        tag_multiple(file_path, input_files, lang)

if registry:
    files = [x for x in listdir("results") if files_dir in x and ".vert" in x]
    for x in files:
        name = x.split(".xml")[0]
        lang = x.split(".xml")[0].split("_")[1]
        generate_registry(name, information, lang, get_info(files_dir), struct, pair_element)
