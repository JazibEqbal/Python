
import subprocess
import os
import re

# Define the SVN repository directory
svn_repo_dir = r'D:\ArchivingExe'

# Define the output folder for logs
output_folder = 'svn_logs'

# Function to run an SVN command and write the output to the log file
def run_svn_command(command, log_file):
    log_file.write(f"Running SVN command: {' '.join(command)}\n")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=svn_repo_dir, text=True)
    log_file.write(result.stdout)
    log_file.write(result.stderr)
    log_file.write("\n\n")

# Ensure the output folder exists or create it if not
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of subfolders in the SVN repository directory
subfolders = [f.name for f in os.scandir(svn_repo_dir) if f.is_dir()]

# Iterate through each subfolder and generate logs
for subfolder in subfolders:
    output_file = os.path.join(output_folder, f'{subfolder}_svn_logs.txt')
    with open(output_file, 'w') as log_file:
        log_file.write(f"Logs for {subfolder}:\n\n")

        # Run SVN log command to get commit history
        run_svn_command(['svn', 'log'], log_file)

        log_file.write("Actions on each commit:\n")
        log_file.write("------------------------\n")

        # Run SVN log command again to get commit messages
        run_svn_command(['svn', 'log', '--verbose'], log_file)

        # Read the log file contents and extract commit messages
        with open(output_file, 'r') as log_file_read:
            log_text = log_file_read.read()
            commit_messages = re.findall(r'(?<=\n\n)(r\d+.*?)(?=\n\n|$)', log_text, re.DOTALL)

            for i, message in enumerate(commit_messages, start=1):
                log_file.write(f"Commit {i}:\n{message}\n")

    print(f"Logs for {subfolder} have been saved to {output_file}")


#FINAL
import subprocess
import re
import os

svn_repo_dir = r'D:\BuildScripts'
output_file = 'svn_logs_bswm.txt'
current_folder = os.path.basename(svn_repo_dir)


def run_svn_command(command, log_file):
    # log_file.write(f"Running SVN command: {' '.join(command)}\n")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=svn_repo_dir, text=True)
    log_file.write(result.stdout)
    log_file.write(result.stderr)
    log_file.write("\n\n")


with open(output_file, 'w') as log_file:
    # run_svn_command(['svn', 'log'], log_file)

    log_file.write(f"Logs for {current_folder}\n")
    # log_file.write("------------------------\n")

    run_svn_command(['svn', 'log', '--verbose'], log_file)
    with open(output_file, 'r') as log_file_read:
        log_text = log_file_read.read()
        commit_messages = re.findall(r'(?<=\n\n)(r\d+.*?)(?=\n\n|$)', log_text, re.DOTALL)
        for i, message in enumerate(commit_messages, start=1):
            log_file.write(f"Commit {i}:\n{message}\n")

print(f"SVN logs have been saved to {output_file}")

import subprocess
import re
import os

svn_repo_dir = r'D:\Assign'
output_file = 'svn_logs_bswm.txt'
current_folder = os.path.basename(svn_repo_dir)


def run_svn_command(command, log_file):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=svn_repo_dir, text=True)
    log_file.write(result.stdout)
    log_file.write(result.stderr)
    log_file.write("\n\n")


with open(output_file, 'w') as log_file:
    log_file.write(f"Logs for {current_folder}\n")

    # Run 'svn log' with the repository path to capture only top-level logs
    run_svn_command(['svn', 'log', '--verbose', '-l', '1000', svn_repo_dir], log_file)

    with open(output_file, 'r') as log_file_read:
        log_text = log_file_read.read()
        commit_entries = re.split(r'\n\n', log_text)  # Split log entries by double newline
        #
        # for entry in commit_entries:
        #     lines = entry.strip().split('\n')
        #     if len(lines) >= 3:
        #         path_lines = '\n'.join(lines[:3])  # Capture the first 3 lines of each entry
        #         log_file.write(f"{path_lines}\n")

print(f"SVN logs for the top-level directory have been saved to {output_file}")