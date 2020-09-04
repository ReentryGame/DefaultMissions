import json, glob

for checklist in glob.glob('**/*.json', recursive=True):
#    if not checklist.endswith('checklist.json'): continue
    print(checklist)
    j = json.load(open(checklist))
    open(checklist, 'w').write(json.dumps(j, indent=4, sort_keys=True))
