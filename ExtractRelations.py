from nltk.corpus import ieer
from nltk.sem import relextract
import re

docs = ieer.parsed_docs('NYT_19980315')
tree = docs[1].text

#print(tree)

# Converts chunk (NER is already done) into list of two-member lists. Each contains a string followed by a tree (named entity)
# Eg: "about first-level questions, said Ms."   => string
#     (PERSON Cohn)                             => named entity, which is a tree. Root is PERSON, and child node is Cohn
pairs = relextract.tree2semi_rel(tree)
""" for s, tree in pairs[:3]:
    print('*'*20)
    print(' '.join(s))
    print(tree) """

# Processes three of the above pairs at a time into a dictionary. Eg: (string1, tree1)    (string2, tree2)    (string3, tree3)
# string1 is stored as left context.
# tree1 is the subject, string2 is the filler, and tree2 is the object.
# string3 is stored as right context.
reldicts = relextract.semi_rel2reldict(pairs)
for r in reldicts:
    print('=' * 20)
    print(r['subjtext'])            # Print the subject text
    print(r['filler'])              # Print the filler information
    print(r['objtext'])             # Print the object text

# Matches any number of characters followed by the word "in" as long as "in" is not followed by a word ending in "ing"
IN = re.compile(r'.*\bin\b(?!\b.+ing\b)')

# Finds relationships of the form entity1 IN entity2, where entity1 is ORGANIZATION and entity2 is LOCATION
print('\nRelation of type ORGANIZATION in LOCATION: \n')
for relation in relextract.extract_rels('ORG', 'LOC', docs[1], corpus='ieer', pattern=IN):
    print(relextract.rtuple(relation))