"""
cleans up given bib file from attributes set in JabRef
"""
with open("bib.bib", 'r', encoding= 'utf-8') as old_bib:
    lines = old_bib.readlines()

remove = False
idx_remove = list()
for idx, line in enumerate(lines):
    if remove == True:
        idx_remove.append(idx)
    if 'abstract' in line:
        remove = True
        idx_remove.append(idx)
    if remove == True and '},' in line:
        remove = False

remove2 = False
for idx, line in enumerate(lines):
    if remove2 == True:
        idx_remove.append(idx)
    if 'comment' in line:
        remove2 = True
        idx_remove.append(idx)
    if remove2 == True and '},' in line:
        remove2 = False


with open("bib.bib", 'w', encoding= 'utf-8') as new_bib:
    for idx, line in enumerate(lines):
        if 'file' not in line and 'groups' not in line and 'keywords' not in line and 'priority' not in line and 'readstatus' not in line and idx not in idx_remove:
            new_bib.write(line)
        
