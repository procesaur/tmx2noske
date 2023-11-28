from os import name, remove
from subprocess import check_output
from tqdm import tqdm


def isWindows():
    return name == 'nt'


def tag_treetagger(lang, file_path, lemmatize=True):
    args = ([])
    ext = ""
    if isWindows():
        ext = ".exe"

    par_path = "./treetagger/par/" + lang + ".par"
    treetagger_path = "./treetagger/bin/tree-tagger" + ext

    args.append(treetagger_path)
    args.append(par_path)
    args.append(file_path)

    if lemmatize:
        args.append("-lemma")

    args.append("-token")
    args.append("-sgml")
    args.append("-no-unknown")
    args.append("-quiet")

    r = check_output(args)
    r = r.decode('utf-8')
    r = r.replace('\r\n', '\n')
    return r


def tag_multiple(file_path, input_files, lang):
    print("tagging...")
    with open(file_path + ".vert", "a+", encoding="utf-8") as rf:
        for input_file in tqdm(input_files, total=len(input_files)):
            rf.write(tag_treetagger(lang, input_file) + "\n")
            try:
                remove(input_file)
            except:
                pass