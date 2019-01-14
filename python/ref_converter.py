import json
import re
from collections import defaultdict


LABEL_REGEX = r'\\label\{([^}]+)\}'
REF_REGEX = r'\\ref\{([^}]+)\}'


def config_referencing_keys(config_file):
    with open(config_file, 'r') as f:
        valid_cross_refs = json.load(f)
    keys = list(valid_cross_refs.keys())
    long_names = list(valid_cross_refs.values())
    for key, long_name in zip(keys, long_names):
        valid_cross_refs['sup.{}'.format(
            key)] = 'Supplementary {}'.format(long_name)
    return valid_cross_refs


def build_label_index(valid_keys,
                      main_filepath='tex/main.tex',
                      sup_filepath='tex/sup.tex'):
    # Read in the tex from main and supp, combine into single string
    with open(main_filepath, 'r') as f:
        input_tex = f.read()
    with open(sup_filepath, 'r') as f:
        input_tex += f.read()
    matches = [m.span() for m in re.finditer(LABEL_REGEX, input_tex)]
    global_count_d = defaultdict(int)
    ref_to_string_d = {}
    for m in matches:
        # Each m contains the start and end index of a match (a label)
        label = input_tex[m[0]:m[1]]
        print(label)
        key = label[7:-1]  # Extracts the ... inside '\label{...}'
        print(key)
        key_type = key.split(':')[0]
        print(key_type)
        if key_type not in valid_keys:
            # If encounter a label that is not in set of valid keys, do nothing
            continue
        global_count_d[key_type] += 1
        ref_to_string_d[key] = '{} {}'.format(valid_keys[key_type],
                                              global_count_d[key_type])
    return global_count_d, ref_to_string_d


def convert_refs(in_filepath, out_filepath, ref_to_string_dict):
    with open(in_filepath, 'r') as f:
        tex = f.read()
    for key, converted_string in ref_to_string_d.items():
        old = r'\ref{' + key + '}'
        tex = tex.replace(old, converted_string)
    with open(out_filepath, 'w') as f:
        f.write(tex)


if __name__ == '__main__':
    valid_keys = config_referencing_keys('cross_refs.json')
    # First pass: build an index of all valid labels
    global_count_d, ref_to_string_d = build_label_index(valid_keys)

    convert_refs('tex/main.tex', 'processed_main.tex', ref_to_string_d)
    # Unlike the main manuscript, the supplement is written
    # to a file called 'submission_...' because it's ready
    # to be compiled and doesn't need anymore processing
    # (e.g. we don't need to add the BBL to the .tex to
    # make it a single file, we just need a pdf for the
    # supplement)
    convert_refs('tex/sup.tex', 'submission_sup.tex', ref_to_string_d)
