from split_tmx import generate_split_files
from treetagger.treetagger import tag_multiple
from verticalizer import verticalize_multiple
from registerer import generate_registries


files_dir = "SerbItaCor3"
information = "Parallel Serbian-Italian Corpus"
struct = ["seg"]
pair_element = "seg"

split_tmx = True
vert = True
tag = True
registry = True

if split_tmx:
    generate_split_files(files_dir, pair_element)

if vert:
    verticalize_multiple(files_dir)

if tag:
    tag_multiple(files_dir)

if registry:
    generate_registries(files_dir, information, struct, pair_element)
