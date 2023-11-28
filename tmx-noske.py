from xml.etree import ElementTree as gfg
from os.path import isfile


directory = "ItSr23"
filename_column = "id"
metadata_filename = "metadata.csv"
separator = "\t"

with open(directory + "/" + metadata_filename, "r", encoding="utf8") as md:
    metadata_lines = [[y.rstrip() for y in x.split(separator)] for x in md.readlines() if x]

filename_index = metadata_lines[0].index(filename_column)
info = metadata_lines[0]
del metadata_lines[0]


def GenerateXML(metadata, file_path):
    tmx = gfg.parse(file_path)
    global info

    root = gfg.Element("doc")
    for key, value in zip(info, metadata):
        root.set(key, value)

    tuples = [("1", "2"), ("3", "4")]
    n = len(tuples)

    roots = [root for x in range(n)]
    trees = []
    for index in range(n):
        trees.append(gfg.ElementTree(roots[index]))
    return trees


docs = [GenerateXML(x, directory + "/" + x[filename_index] + ".xml") for x in metadata_lines if isfile(directory + "/" + x[filename_index] + ".xml")]
docs = zip(*docs)

for i, doc in enumerate(docs):
    strings = [gfg.tostring(x.getroot(), encoding='utf8').decode("utf-8").split("<?xml version='1.0' encoding='utf8'?>")[1] for x in doc]
    with open("results/result" + str(i) + ".xml", "w", encoding="utf-8") as r:
        r.write("\n".join(strings))

