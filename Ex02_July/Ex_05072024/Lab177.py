# # Walk into directory..

import os

for root, dir, files in os.walk("C:/Users/manib/PycharmProjects/PyLearning3xATB/Ex02_July/Ex_05072024"):
    print(f'Current directory {root}')
    print(f'Sub directory {dir}')
    print(f'files in the directory {files}')
#

# import os
# print(os.getcwd())