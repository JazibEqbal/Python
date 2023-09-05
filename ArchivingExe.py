import os
import pandas as pd
import subprocess
import re

root_svn = r'E:\BuildScripts'

print('Writing...Good things take time :)')

def is_folder_empty(folder_path):
    return len(os.listdir(folder_path)) == 0

def has_exe(folder_path):
    return any(file.endswith('.exe') for file in os.listdir(folder_path))

def get_revision_log(path):
    cmd = ['svn', 'log', '--stop-on-copy', path]
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
        'SourceCode Revision Log': [], 'Source': [], 'Source Revision Log': [], 'Execute': [], 'Execute Revision Log': []}

# pattern = re.compile(r'sou\w*code', re.IGNORECASE)
pattern = re.compile(r'sou\w*\s*code', re.IGNORECASE)

for entry in os.scandir(root_svn):
    if entry.is_dir() and entry.name not in ['.svn', 'venv', '.idea']:
        directory_name = os.path.basename(entry.path)
        data['Directory'].append(directory_name)

        doc_path = os.path.join(entry.path, 'Doc')
        doc_status = 'Missing' if not os.path.exists(doc_path) else ('No' if is_folder_empty(doc_path) else 'Yes')
        data['DOC'].append(doc_status)

        input_path = os.path.join(entry.path, 'Inputs')
        input_status = 'Missing' if not os.path.exists(input_path) else ('No' if is_folder_empty(input_path) else 'Yes')
        data['Inputs'].append(input_status)

        result_path = os.path.join(entry.path, 'Results')
        result_status = 'Missing' if not os.path.exists(result_path) else ('No' if is_folder_empty(result_path) else 'Yes')
        data['Results'].append(result_status)

        data['EXE'].append('Yes' if has_exe(entry.path) else 'Missing')

        source_status = 'Missing'
        for foldername in os.listdir(entry.path):
            if pattern.search(foldername):
                source_code_folder = os.path.join(entry.path, foldername)
                if any(file.endswith('.py') for file in os.listdir(source_code_folder)):
                    source_status = 'Yes'
                else:
                    source_status = 'No'
                break
        data['SourceCode'].append(source_status)

        source_code_path = os.path.join(entry.path, 'SourceCode')
        data['SourceCode Revision Log'].append(get_revision_log(source_code_path))

        source_path = os.path.join(entry.path, 'Source')
        source_status_ = 'Missing' if not os.path.exists(source_path) else ('No' if is_folder_empty(source_path) else 'Yes')
        data['Source'].append(source_status_)
        data['Source Revision Log'].append(get_revision_log(source_path))

        execute_path = os.path.join(entry.path, 'Execute')
        execute_status = 'Missing' if not os.path.exists(execute_path) else ('No' if is_folder_empty(execute_path) else 'Yes')
        data['Execute'].append(execute_status)
        data['Execute Revision Log'].append(get_revision_log(execute_path))

df = pd.DataFrame(data)

excel_file = 'Report.xlsx'
df.to_excel(excel_file, index=False)

print(f"Data written to {excel_file}")

