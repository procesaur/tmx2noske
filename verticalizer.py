from tokenizer import tokenize
from random import choices
from string import ascii_lowercase
from tqdm import tqdm


def get_rand():
    return ''.join(choices(ascii_lowercase, k=10))


def verticalize(file_path):
    print("verticalizing...")
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    pars = ["<doc " + x for x in text.split("<doc ")]
    del pars[0]
    chunk_names = []
    for par in tqdm(pars, total=len(pars)):
        name = "./tmp/" + get_rand()
        lines = tokenize(par)
        with open(name, "w", encoding="utf-8") as t:
            t.writelines('\n'.join(lines))
        chunk_names.append(name)
    return chunk_names
