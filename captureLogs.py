# import subprocess
#
# svn_local_folder_path = r"D:\BuildScripts"
# output_file = "svn_logs_bswm.txt"
#
# try:
#     svn_log_output = subprocess.check_output(['svn', 'log', svn_local_folder_path], universal_newlines=True)
# except subprocess.CalledProcessError as e:
#     print("Error executing SVN log command:", e)
#     svn_log_output = ""
#
# print("SVN Log Output:")
# print(svn_log_output)
#
# with open(output_file, 'w') as file:
#     file.write(svn_log_output)
#
# print(f"SVN logs for folder '{svn_local_folder_path}' saved to {output_file}")

# import subprocess
#
# # Define the SVN repository directory
# svn_repo_dir = r'D:\BuildScripts'
#
# # Define the output file for logs
# output_file = 'svn_logs_bswm.txt'
#
# # Function to run an SVN command and write the output to the log file
# def run_svn_command(command):
#     with open(output_file, 'a') as log_file:
#         log_file.write(f"Running SVN command: {command}\n")
#         result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=svn_repo_dir, text=True)
#         log_file.write(result.stdout)
#         log_file.write(result.stderr)
#         log_file.write("\n\n")
#
# # Clear the existing log file if it exists
# with open(output_file, 'w') as log_file:
#     log_file.write("SVN Logs:\n\n")
#
# # Run SVN log command to get commit history
# run_svn_command(['svn', 'log'])
#
# # Run SVN status command to track file changes in each commit
# run_svn_command(['svn', 'status', '-v'])
#
# print(f"SVN logs have been saved to {output_file}")


#----------------------------------------FINAL

# import subprocess
# import re
# import os
#
# svn_repo_dir = r'D:\ArchivingExe'
# output_file = 'svn_logs_bswm.txt'
# current_folder = os.path.basename(svn_repo_dir)
#
#
# def run_svn_command(command, log_file):
#     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=svn_repo_dir, text=True)
#     log_file.write(result.stdout)
#     log_file.write(result.stderr)
#     log_file.write("\n\n")
#
#
# with open(output_file, 'w') as log_file:
#     log_file.write(f"Logs for {current_folder}\n")
#     run_svn_command(['svn', 'log', '--verbose'], log_file)
#     with open(output_file, 'r') as log_file_read:
#         log_text = log_file_read.read()
#         commit_messages = re.findall(r'(?<=\n\n)(r\d+.*?)(?=\n\n|$)', log_text, re.DOTALL)
#         for i, message in enumerate(commit_messages, start=1):
#             log_file.write(f"Commit {i}:\n{message}\n")
#
# print(f"SVN logs have been saved to {output_file}")


import subprocess
import re
import os

svn_repo_dir = r'D:\BswMProxyPNCCfgCreator'
output_file = 'svn_logs_bswm.txt'
current_folder = os.path.basename(svn_repo_dir)


def run_svn_command(command, log_file):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=svn_repo_dir, text=True)
    log_file.write(result.stdout)
    log_file.write(result.stderr)
    log_file.write("\n\n")


with open(output_file, 'w') as log_file:
    log_file.write(f"Logs for {current_folder}\n")
    run_svn_command(['svn', 'log', '--verbose', '-l', '1000', svn_repo_dir], log_file)
    with open(output_file, 'r') as log_file_read:
        log_text = log_file_read.read()
        commit_entries = re.split(r'\n\n', log_text)

print(f"SVN logs have been saved to {output_file}")