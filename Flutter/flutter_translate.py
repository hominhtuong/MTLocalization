import codecs
import os
import csv
import re
from shutil import rmtree

# __ (2 underscores)	left apostrophe (\")
# ___ (3 underscores)	right apostrophe  (\")
# ____ (4 underscores)	format string ("the number is \(x)")
# _____ (5 underscores)	Down the line (\n)
# ______ (6 underscores) -> &

# Let change it
INPUT_FILE_NAME = "res/example.tsv"
directoryParent = 'results/'


line_header = None
line_content = []
keys = []
PASS_COLUMN = ['Text Key', ]
language_type_array = PASS_COLUMN.copy()

with open(INPUT_FILE_NAME, encoding="utf8") as file:
    tsv_file = csv.reader(file, delimiter="\t")

    # printing data line by line
    for line in tsv_file:
        if line_header is None:
            line_header = line
        else:
            line_content.append(line)

for lang in line_header:
    res = re.findall(r'\(.*?\)', lang)
    if len(res) < 1:
        continue
    res = res[0]
    res = res.replace('(', '').replace(')', '')
    language_type_array.append(res)

print(language_type_array)

if os.path.exists(directoryParent):
    rmtree(directoryParent)

if not os.path.exists(directoryParent):
    os.makedirs(directoryParent)

for idx, lang in enumerate(language_type_array):
    if lang in PASS_COLUMN:
        continue
    directory = directoryParent
    if not os.path.exists(directory):
        os.makedirs(directory)

    with codecs.open(directory + '/intl_' + lang + '.arb', 'w', 'utf-8') as outfile:
        outfile.write('{\n')
        outfile.write('\t"@@locale": "' + lang + '"')

        for i in range(len(line_content)):
            content = line_content[i]

            if idx >= len(content) or content[idx] == '#VALUE!' or content[idx] == '' or content[0] == '':
                continue
            outfile.write(',\n')
            key = content[0]
            text: str = content[idx]
            text = text.replace(' ______ ', ' &amp; ')
            text = text.replace(' ______', ' &amp; ')
            text = text.replace('______', ' &amp; ')

            text = text.replace(' _____ ', '\\n')
            text = text.replace(' _____', '\\n')
            text = text.replace('_____', '\\n')

            text = text.replace('____', '%@')

            text = text.replace(' ___', '\\\"')
            text = text.replace('___', '\\\"')

            text = text.replace('__ ', '\\\"')
            text = text.replace('__', '\\\"')
            text = text.replace('\'', '\\\'')

            outfile.write('\t"' + content[0] + '": "' + text + '"')

        outfile.write('\n}')

        outfile.close()

