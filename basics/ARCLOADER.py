import os
import json
import glob
from pathlib import Path
import numpy as np

class ARCDataset:
    # load training data
    def load_data(self, type = 'train', form = 'list', shuffle = False, jcode = True):
        if type == 'train':
            path = Path('./data/training/')
        elif type == 'eval':
            path = Path('./data/evaluation/')
        else:
            raise ValueError("Invalid arg 'type'. Please use 'train' or 'eval'.")

        tasks = []
        j_codes = []

        json_files = glob.glob(os.path.join(path, '*.json'))

        # load json file with corresponding form (dict or list)
        if form == 'list':
            for file in json_files:
                task = []
                with open(file, 'r') as f:
                    data = json.load(f)
                    task.append(data['train'])
                    ttrain = []
                    for i in range(len(data['train'])):
                        ttrain.append(list(data['train'][i].values()))
                    ttest = []
                    for i in range(len(data['test'])):
                        ttest.append(list(data['test'][i].values()))
                    task = [ttrain, ttest]                    
                tasks.append(task)
                
        elif form == 'dict':
            for file in json_files:
                with open(file, 'r') as f:
                    data = json.load(f)
                tasks.append(data)

        else:
            raise ValueError("Invalid arg 'form'. Please use 'dict' or 'list'.")
        
        # suffle tasks
        if shuffle:
            np.random.seed = 777
            np.random.shuffle(tasks)  

        # make j_codes list
        for i in range(len(json_files)):
            jcode = (json_files[i].split('.json')[0])[-8:]
            j_codes.append(jcode)
        
        if jcode:
            return tasks, j_codes
        else:
            return tasks
    
    # jcode to index
    def jtoi(self, jcode, j_codes):
        if jcode in j_codes:
            return j_codes.index(jcode)
        else: 
            return None
        
    # index to jcode
    def itoj(self, index, j_codes):
        if index < len(j_codes):
            return j_codes[index]
        else:
            return None
    

if __name__ == "__main__":
    arc = ARCDataset()
    ## list format (recommended) #########################################################################################
    # type = 'train' or 'eval' / form = 'dict' or 'list' / shuffle = True or False / jcode = True or False
    tasks, j_codes = arc.load_data(type = 'train', form = 'list', shuffle = False, jcode = True)

    x = 0     # 0 - 399      (task number)
    tt = 0    # 0 or 1       (train or test)
    p = 0     # 0 - max pair (pair number)
    io = 0    # 0 or 1       (input or output)

    # print(tasks) - if form = 'list' / [x][0 or 1][p][0 or 1][row][col]
    print(tasks[x][tt][p][io])



    ## dict format #######################################################################################################
    # type = 'train' or 'eval' / form = 'dict' or 'list' / shuffle = True or False / jcode = True or False
    tasks, j_codes = arc.load_data(type = 'train', form = 'dict', shuffle = False, jcode = True)

    # print(tasks) / [x]['train' or 'test'][p]['input' or 'output'][row][col]
    print(tasks[x]['train'][p]['input'])

    ## json codes #########################################################################################
    # print(j_codes) # list of json codes (len = 400)
    print(arc.itoj(0, j_codes))
    print(arc.jtoi('5c2c9af4', j_codes))