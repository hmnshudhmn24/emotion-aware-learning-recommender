import re
def clean_text(t): return ' '.join(re.sub(r'[^a-zA-Z ]',' ',t).lower().split())
