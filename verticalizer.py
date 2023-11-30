from tokenizer import tokenize
from random import choices
from string import ascii_lowercase
from tqdm import tqdm
from os import listdir, mkdir
from os.path import splitext, isdir


ini_dir = "data/source/"
target_dir = "data/verticals/"


def get_rand():
    return ''.join(choices(ascii_lowercase, k=10))


def verticalize(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    lines = tokenize(text)
    save_path = file_path.replace(ini_dir, target_dir)
    save_path = splitext(save_path)[0] + ".vert"
    with open(save_path, "w", encoding="utf-8") as t:
        t.writelines('\n'.join(lines).replace("<seg>\n</seg>", "<seg>\n*\n</seg>"))


def verticalize_multiple(directory):
    print("verticalizing...")

    if not isdir(target_dir + directory):
        mkdir(target_dir + directory)

    files = listdir(ini_dir + directory)
    for x in tqdm(files, total=len(files)):
        verticalize(ini_dir + directory + "/" + x)
