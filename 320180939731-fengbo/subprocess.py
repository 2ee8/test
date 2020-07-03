#!/usr/bin/env python3
__author__ == "Bo Feng"
__email__ == "bfeng18@lzu.edu.cn"
'''
This use subprocess to ouput a file's change history difference between commit bdfore and express in one line in kernel
'''
from subprocess import Popen, check_output

def gitFileDynamics(fileName, kernelRange, repo):
    cmd = ["git", "-stat", "--oneline", "--follow", kernelRange, fileName]
    result = check_output(cmd, cwd=repo).decode("utf-8")
    print(result)

