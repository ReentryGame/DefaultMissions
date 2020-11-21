import json
import glob

for checklist in glob.glob('**/*.json', recursive=True) + glob.glob('**/*.desc', recursive=True):
    print(checklist)
    j = json.load(open(checklist))
    open(checklist, 'w').write(json.dumps(j, ensure_ascii=False, indent=4, sort_keys=True))
