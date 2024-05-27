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

#Let change it
INPUT_FILE_NAME = "res/example.tsv"

line_header = None
line_content = []
keys = []
PASS_COLUMN = ['Text Key',]
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

#Let change it
directoryParent = 'results/'

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

    with codecs.open(directory + '/' + 'Localizable.xcstrings', 'w', 'utf-8') as outfile:
        outfile.write('{\n')
        outfile.write('"sourceLanguage" : "en",\n')
        outfile.write('"strings" : {\n')

        for i in range(len(line_content)):
            content = line_content[i]

            if idx >= len(content) or content[idx] == '#VALUE!' or content[idx] == '' or content[0] == '':
                continue

            outfile.write('"' + content[0] + '": {\n')
            outfile.write('"extractionState" : "manual",\n')
            outfile.write('"localizations" : {\n')

            value = content[idx]

            for indexLang in range(len(language_type_array)):
                if indexLang < 1:
                    continue
                outfile.write('"' + language_type_array[indexLang] + '" : {\n')
                outfile.write('"stringUnit" : {\n')
                outfile.write('"state" : "translated",\n')

                text: str = content[indexLang]

                text = text.replace(' ______ ', ' & ')
                text = text.replace(' ______', ' & ')
                text = text.replace('______', ' & ')

                text = text.replace(' _____ ', '\\n')
                text = text.replace(' _____', '\\n')
                text = text.replace('_____', '\\n')

                text = text.replace('____', '%@')

                text = text.replace(' ___', '\\\"')
                text = text.replace('___', '\\\"')

                text = text.replace('__ ', '\\\"')
                text = text.replace('__', '\\\"')

                outfile.write('"value" : "' + text + '"\n')
                outfile.write('}\n')
                if indexLang == len(language_type_array) - 1:
                    outfile.write('}\n')
                else:
                    outfile.write('},\n')

            outfile.write('\n}')

            if i == len(line_content) - 1:
                outfile.write('\n}')
            else:
                outfile.write('\n},')

        outfile.write('\n},')
        outfile.write('\n"version" : "1.0"')
        outfile.write('\n}')

        outfile.close()

# Create enum file
allCases = '\n'
for i in range(len(line_content)):
    for caseIndex in range(len(line_content[i])):
        case = line_content[i][caseIndex]
        if caseIndex == 0:
            allCases += '   case ' + case + '\n'
        else:
            break

with codecs.open(directoryParent + '/' + 'MTText.swift', 'w', 'utf-8') as mtutext:
    mtutext.write('''//
//  MTText.swift
//
        
import UIKit
        
enum MTText: String {
        ''')

    mtutext.write(allCases)
    mtutext.write('''
}

extension MTText {
    var text: String {
        return rawValue
    }

    var localized: String {
        let language = Locale.preferredLanguages.first ?? "en"
        if let path = Bundle.main.path(forResource: language, ofType: "lproj") {
            let bundle = Bundle(path: path)
            if let string = bundle?.localizedString(forKey: text, value: nil, table: nil) {
                return string.capFirstLetter()
            }
        }
        
        return NSLocalizedString(text, comment: "").capFirstLetter()
    }
    
    func format(_ arguments: CVarArg...) -> String {
        let value = NSLocalizedString(text, comment: "")
        return String(format: value, arguments: arguments)
    }
    
    static func updateLocalize(_ lang: String) {
        UserDefaults.standard.setValue([lang], forKey: "AppleLanguages")
    }
}

extension String {
    func capFirstLetter() -> String {
        return self.isEmpty ? self : prefix(1).capitalized + dropFirst()
    }

    mutating func capitalizeFirstLetter() {
        self = self.capitalizingFirstLetter()
    }
}''')

    outfile.close()
