from collections import OrderedDict
import re
fa = open('data/values.csv', 'r')
fb = open('data/transformed_values.csv', 'w')

#create list containing all parameters 
parameters = []
header = fa.readline()
for line in fa :
    line = line.strip()
    ids = line.split(',')
    if ids[2] not in parameters:
        parameters.append(ids[2])

#sort parameters list (numerically and then alphabetically)
def key(s):
    num, letters = re.match(r'(\d*)(.*)', s).groups()
    return float(num or 'inf'), letters

parameters = sorted(parameters, key=key)

#create dictionary with each language id and its name as key:value pairs
language_names = {}
fd = open('data/language_names.csv', 'r')
header = fd.readline()
for line in fd :
    line = line.strip()
    if '"' in line :
        words=line.split('"')
        name = words[1].replace(",", "")
        (num, iden) = words[0][:-1].split(',')
        language_names[iden] = name
    else:
        words = line.split(',')
        language_names[words[1]] = words[2]
    
#create a dictionary with a key for each language, and the corresponding value as a list containing the value for each feature
languages = OrderedDict()
fa.seek(0)
header = fa.readline()
for line in fa :
    line = line.strip()
    ids = line.split(',')
    #137 of the languages are not present in the language names file, so add these to the dict as their language id instead
    if ids[1] not in language_names:
        language_names[ids[1]] = ids[1]
    if ids[1] not in languages:
        #create list of 192 (the number of features) empty elements for each language
        languages[ids[1]] = [''] * 192
        #the position of the specific feature within the list (parameters.index(ids[2])) equals the value for that feature
    languages[ids[1]][parameters.index(ids[2])] = ids[3]


#replace parameter names
fc = open('data/parameters.csv', 'r')
header = fc.readline()
for line in fc:
    line = line.strip()
    words = line.split(',')
    parameters = list(map(lambda x: x.replace(words[0], words[1]), parameters))

#write header of file
fb.write('Language,' + ','.join(parameters) + '\n')

#fill in every language
for language in languages :
    fb.write(language_names[language] + ',' + ','.join(languages[language]) + '\n')

    

