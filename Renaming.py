# import os
# import pandas as pd
#
# root_svn = r'D:\Test'
#
# print('Writing...Good things take time :)')
#
#
# def is_folder_empty(folder_path):
#     return len(os.listdir(folder_path)) == 0
#
#
# def is_python_file(folder_path):
#     return any(file.endswith('.py') for file in os.listdir(folder_path))
#
#
# def rename(entry_path):
#     source_path = os.path.join(entry_path, 'Source')
#     sourcecode_path = os.path.join(entry_path, 'SourceCode')
#
#     if os.path.exists(source_path):
#         os.rename(source_path, sourcecode_path)
#
#
# data = {'Folder': [],'SourceCode': [], 'Source': []}
#
# for entry in os.scandir(root_svn):
#     if entry.is_dir():
#         data['Folder'].append(os.path.basename(entry.path))
#         source_code_path = os.path.join(entry.path, 'SourceCode')
#         source_status = 'Missing' if not os.path.exists(source_code_path) else (
#             'No' if is_folder_empty(source_code_path) else 'Yes')
#         data['SourceCode'].append(source_status)
#
#         sourcepath = os.path.join(entry.path, 'Source')
#         source___ = 'Missing' if not os.path.exists(sourcepath) else (
#             'No' if is_folder_empty(sourcepath) else 'Yes')
#         data['Source'].append(source___)
#
#
#         rename(entry.path)
#
# df = pd.DataFrame(data)
# excel_file = 'Report.xlsx'
# df.to_excel(excel_file, index=False)
# print(f"Data written to {excel_file}")


import os
import pandas as pd
import re

root_svn = r'D:\Test'

print('Writing...Good things take time :)')


def is_folder_empty(folder_path):
    return len(os.listdir(folder_path)) == 0


def is_python_file(folder_path):
    return any(file.endswith('.py') for file in os.listdir(folder_path))


def rename(entry_path):
    for subdir in os.scandir(entry_path):
        if subdir.is_dir() and re.match(r'sou\w*\s*code', subdir.name, re.IGNORECASE):
            sourcecode_path = os.path.join(entry_path, 'SourceCode')
            os.rename(subdir.path, sourcecode_path)

def rename_source(entry_path):
    source_path = os.path.join(entry_path, 'Source')
    sourcecode_path = os.path.join(entry_path, 'SourceCode')

    if os.path.exists(source_path):
        os.rename(source_path, sourcecode_path)


data = {'Folder': [],'SourceCode': [], 'Source': []}


for entry in os.scandir(root_svn):
    if entry.is_dir():
        data['Folder'].append(os.path.basename(entry.path))
        source_code_path = os.path.join(entry.path, 'SourceCode')
        source_status = 'Missing' if not os.path.exists(source_code_path) else (
            'No' if is_folder_empty(source_code_path) else 'Yes')
        data['SourceCode'].append(source_status)

        sourcepath = os.path.join(entry.path, 'Source')
        source___ = 'Missing' if not os.path.exists(sourcepath) else (
            'No' if is_folder_empty(sourcepath) else 'Yes')
        data['Source'].append(source___)

        rename(entry.path)
        rename_source(entry.path)

df = pd.DataFrame(data)
excel_file = 'Report.xlsx'
df.to_excel(excel_file, index=False)
print(f"Data written to {excel_file}")