from pathlib import Path
def generate_report(e,p): Path('data/reports').mkdir(parents=True,exist_ok=True); open('data/reports/recommendation.txt','w').write(f'Emotion: {e}\n'+''.join([f'{k}: {v}\n' for k,v in p.items()]))
