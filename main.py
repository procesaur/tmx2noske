from os import listdir, remove
from tqdm import tqdm
from split_tmx import generate_split_files
from treetagger.treetagger import tag_treetagger
from verticalizer import verticalize


files_dir = "ItSr23"
split_tmx = False
tag = True

if split_tmx:
    generate_split_files(files_dir)

if tag:
    files = [x for x in listdir("results") if files_dir in x and ".vert" not in x]
    for x in files:
        file_path = "results/" + x
        lang = x.split(".xml")[0].split("_")[1]
        input_files = verticalize(file_path)
        with open(file_path + ".vert", "a+", encoding="utf-8") as rf:
            for input_file in tqdm(input_files, total=len(input_files)):
                rf.write(tag_treetagger(lang, input_file) + "\n")
                try:
                    remove(input_file)
                except:
                    pass
