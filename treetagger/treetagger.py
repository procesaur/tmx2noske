from os import name
from subprocess import check_output


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
