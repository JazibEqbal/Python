import os
import pandas as pd
import subprocess
from pathlib import Path

root_svn = r'E:\BuildScripts'
root_path = Path(root_svn)

print('Writing...Good things take time :)')


def is_folder_empty(folder_path):
    return len(list(folder_path.iterdir())) == 0


def has_exe(folder_path):
    return any(file.name.endswith('.exe') for file in folder_path.iterdir())


def get_revision_log(path):
    cmd = ['svn', 'log', '--stop-on-copy', str(path)]
    try:
        output = subprocess.check_output(cmd, universal_newlines=True, stderr=subprocess.DEVNULL)
        revisions = []

        for line in output.strip().split('\n'):
            if line.strip().startswith("r"):
                parts = line.split('|')
                if len(parts) >= 2:
                    revision = parts[0].strip()[1:]
                    revisions.append(revision)
                else:
                    print("Unexpected log format:", line)
            else:
                print("Skipping line:", line)

        return ', '.join(revisions)
    except subprocess.CalledProcessError:
        return ''


data = {'Directory': [], 'DOC': [], 'Inputs': [], 'Results': [], 'EXE': [], 'SourceCode': [],
        'SourceCode Revision Log': [], 'Source': [], 'Source Revision Log': [], 'Execute': [],
        'Execute Revision Log': []}

for entry in root_path.iterdir():
    if entry.is_dir() and entry.name not in ['.svn', 'venv', '.idea']:
        directory_name = entry.name
        data['Directory'].append(directory_name)

        for attribute in ['Doc', 'Inputs', 'Results', 'SourceCode', 'Source', 'Execute']:
            attribute_path = entry / attribute
            attribute_status = 'Missing' if not attribute_path.exists() else (
                'No' if is_folder_empty(attribute_path) else 'Yes')
            data[attribute].append(attribute_status)

            if attribute in ['SourceCode', 'Source', 'Execute']:
                data[f'{attribute} Revision Log'].append(get_revision_log(attribute_path))

        data['EXE'].append('Yes' if has_exe(entry) else 'Missing')

df = pd.DataFrame(data)

excel_file = 'Report.xlsx'
df.to_excel(excel_file, index=False)

print(f"Data written to {excel_file}")
