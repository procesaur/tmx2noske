from os import name, listdir, mkdir
from os.path import splitext, isdir
from subprocess import check_output
from tqdm import tqdm


ini_dir = "data/verticals/"
target_dir = "data/tagged/"


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


def tag_multiple(directory):
    print("tagging...")

    if not isdir(target_dir + directory):
        mkdir(target_dir + directory)

    files = listdir(ini_dir + directory)
    for x in tqdm(files, total=len(files)):
        file_path = ini_dir + directory + "/" + x
        lang = x.split(".vert")[0].rsplit("_", 1)[1]

        save_path = file_path.replace(ini_dir, target_dir)
        save_path = splitext(save_path)[0] + ".tt"
        with open(save_path, "w", encoding="utf-8") as sf:
            sf.write(tag_treetagger(lang, file_path))
