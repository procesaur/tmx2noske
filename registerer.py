lang_map = {
        "sr": "Srpski",
        "en": "English",
        "fr": "French",
        "de": "German",
        "it": "Italian"
    }


def generate_registry(name, information, lang, atts, struct, pair_element):

    info = {
        "path": "/home/noske/data/corpora/" + name,
        "vertical": "/home/noske/data/verticals/" + name,
        "encoding": "UTF-8",
        "info": information,
        "maintainer": "JeRTeh",
        "language": lang_map[lang],
        "infohref.path": "",
        "tagsetdoc.path": "",
        "doc_attributes": atts,
        }

    data_str = '''PATH %s
VERTICAL %s
ENCODING %s
INFO "%s"
MAINTAINER "%s"
LANGUAGE "%s"
INFOHREF "%s"
TAGSETDOC "%s"

ATTRIBUTE lc {
    LABEL "word (lowercase)"
    DYNAMIC utf8lowercase
    DYNLIB internal
    ARG1 "C"
    FUNTYPE s
    FROMATTR word
    TYPE index
    TRANSQUERY yes
}

ATTRIBUTE lemma_lc {
    LABEL "lemma (lowercase)"
    DYNAMIC utf8lowercase
    DYNLIB internal
    ARG1 "C"
    FUNTYPE s
    FROMATTR lemma
    TYPE index
    TRANSQUERY yes
}

ATTRIBUTE word
ATTRIBUTE tag
ATTRIBUTE lemma

STRUCTURE doc {
    ATTRIBUTE %s
}

''' % (info["path"], info["vertical"], info["encoding"], info["info"], info["maintainer"], info["language"],
       info["infohref.path"], info["tagsetdoc.path"], make_nrattributes_str(info["doc_attributes"]))

    for s in struct:
        data_str += "\nSTRUCTURE " + s

    data_str += "\nALIGNSTRUCT " + pair_element

    with open("registry/" + name, "w", encoding="utf-8") as r:
        r.write(data_str)


def make_nrattributes_str(att_list):
    return '\n\tATTRIBUTE '.join(att_list)
