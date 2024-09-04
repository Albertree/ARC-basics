import json
import os
from pathlib import Path
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from ARCLOADER import *

settings = json.load(open('settings.json', 'r'))
colors_rgb = settings['colors_rgb']

#############################################################################################
# plot thumbnail
def plot_thumbnail(datas, path = None):
    num_data = len(datas)
    color = '#AAB7B8'
    alpha = 1 
    linewidth = 1.5

    converted = []
    for pair in datas:
        result = []
        for data in pair:
            for line in data:
                d_input = [[colors_rgb[value] for value in line] for line in pair[0]]
                d_output = [[colors_rgb[value] for value in line] for line in pair[1]]
        result.append(d_input)
        result.append(d_output)
        converted.append(result)

    datas = converted
    
    fig, axs = plt.subplots(num_data, 2, figsize=(10, 5 * num_data))
    plt.tight_layout()
    if num_data == 1:
        datas = datas[0]
        for i in range(num_data):
            for j in range(2):
                axs[j].grid(True, which = 'both', color = color, alpha = alpha, linewidth = linewidth)    
                axs[j].xaxis.set_ticks_position('top')
                axs[j].set_xticks([x - 0.50 for x in range(1 + (np.array(datas[j]).shape[1]))])
                axs[j].yaxis.set_ticks_position('left')
                axs[j].set_yticks([x - 0.50 for x in range(1 + (np.array(datas[j]).shape[0]))])
                axs[j].tick_params(top = False, labeltop = False, left = False, labelleft = False)
                axs[j].imshow(datas[j])
    else:
        for i in range(num_data):
            for j in range(2):
                axs[i, j].grid(True, which = 'both', color = color, alpha = alpha, linewidth = linewidth)    
                axs[i, j].xaxis.set_ticks_position('top')
                axs[i, j].set_xticks([x - 0.50 for x in range(1 + (np.array(datas[i][j]).shape[1]))])
                axs[i, j].yaxis.set_ticks_position('left')
                axs[i, j].set_yticks([x - 0.50 for x in range(1 + (np.array(datas[i][j]).shape[0]))])
                axs[i, j].tick_params(top = False, labeltop = False, left = False, labelleft = False)
                axs[i, j].imshow(datas[i][j])

    plt.savefig(path)
    plt.close()


#############################################################################################
# plot full image
def plot_full(datas, path = None):
    num_train = len(datas[0])
    num_test = len(datas[1])
    num_data = num_train + num_test
    color1 = '#AAB7B8'
    color2 = 'purple'
    alpha = 1 
    linewidth = 1.5

    new = []
    for tr in datas[0]:
        new.append(tr)
    for te in datas[1]:
        new.append(te)
    datas = new

    converted = []
    for pair in datas:
        result = []
        for data in pair:
            for line in data:
                d_input = [[colors_rgb[value] for value in line] for line in pair[0]]
                d_output = [[colors_rgb[value] for value in line] for line in pair[1]]
        result.append(d_input)
        result.append(d_output)
        converted.append(result)

    datas = converted
    
    fig, axs = plt.subplots(num_data, 2, figsize=(10, 5 * num_data))
    plt.tight_layout()
    for i in range(num_data):
        for j in range(2):
            if i < num_train:
                axs[i, j].grid(True, which = 'both', color = color1, alpha = alpha, linewidth = linewidth)
                axs[i, j].xaxis.set_ticks_position('top')
                axs[i, j].set_xticks([x - 0.50 for x in range(1 + (np.array(datas[i][j]).shape[1]))])
                axs[i, j].yaxis.set_ticks_position('left')
                axs[i, j].set_yticks([x - 0.50 for x in range(1 + (np.array(datas[i][j]).shape[0]))])
                axs[i, j].tick_params(top = False, labeltop = False, left = False, labelleft = False)
                axs[i, j].imshow(datas[i][j])
            else:
                axs[i, j].grid(True, which = 'both', color = color2, alpha = alpha, linewidth = linewidth)
                axs[i, j].xaxis.set_ticks_position('top')
                axs[i, j].set_xticks([x - 0.50 for x in range(1 + (np.array(datas[i][j]).shape[1]))])
                axs[i, j].yaxis.set_ticks_position('left')
                axs[i, j].set_yticks([x - 0.50 for x in range(1 + (np.array(datas[i][j]).shape[0]))])
                axs[i, j].tick_params(top = False, labeltop = False, left = False, labelleft = False)
                axs[i, j].imshow(datas[i][j])

    plt.savefig(path)
    plt.close()


#############################################################################################
# plot full image without answer
def plot_without_answer(datas, path = None):
    num_train = len(datas[0])
    num_test = len(datas[1])
    num_data = num_train + num_test
    color1 = '#AAB7B8'
    color2 = 'purple'
    alpha = 1 
    linewidth = 1.5

    new = []
    for tr in datas[0]:
        new.append(tr)
    for te in datas[1]:
        new.append(te)
    datas = new

    converted = []
    for pair in datas:
        result = []
        for data in pair:
            for line in data:
                d_input = [[colors_rgb[value] for value in line] for line in pair[0]]
                d_output = [[colors_rgb[value] for value in line] for line in pair[1]]
        result.append(d_input)
        result.append(d_output)
        converted.append(result)

    datas = converted
    
    fig, axs = plt.subplots(num_data, 2, figsize=(10, 5 * num_data))
    plt.tight_layout()
    for i in range(num_data):
        for j in range(2):
            if i < num_train:
                axs[i, j].grid(True, which = 'both', color = color1, alpha = alpha, linewidth = linewidth)
                axs[i, j].xaxis.set_ticks_position('top')
                axs[i, j].set_xticks([x - 0.50 for x in range(1 + (np.array(datas[i][j]).shape[1]))])
                axs[i, j].yaxis.set_ticks_position('left')
                axs[i, j].set_yticks([x - 0.50 for x in range(1 + (np.array(datas[i][j]).shape[0]))])
                axs[i, j].tick_params(top = False, labeltop = False, left = False, labelleft = False)
                axs[i, j].imshow(datas[i][j])
            else:
                if j == 0:
                    axs[i, j].grid(True, which = 'both', color = color2, alpha = alpha, linewidth = linewidth)
                    axs[i, j].xaxis.set_ticks_position('top')
                    axs[i, j].set_xticks([x - 0.50 for x in range(1 + (np.array(datas[i][j]).shape[1]))])
                    axs[i, j].yaxis.set_ticks_position('left')
                    axs[i, j].set_yticks([x - 0.50 for x in range(1 + (np.array(datas[i][j]).shape[0]))])
                    axs[i, j].tick_params(top = False, labeltop = False, left = False, labelleft = False)
                    axs[i, j].imshow(datas[i][j])
                else:
                    axs[i, j].axis('off')

    plt.savefig(path)
    plt.close()
       

#############################################################################################
# image generator
def image_gen(type = 'train', mode = 'thumbnail'):
    assert type == 'train' or type == 'eval'
    path = './data/'

    arc = ARCDataset()
    tasks, j_codes = arc.load_data(type = type, form = 'list', shuffle = False, jcode = True)

    ######################################################
    # thumbnail mode
    if mode == 'thumbnail':
        mode_path = path + 'thumbnails/'
        mode_path_type = mode_path + type + '/'
        mode_path_test_and_answer = mode_path_type + 'test_and_answer/' # only form thumbnail mode

        # create folders for thumbnails
        if not os.path.exists(Path(mode_path)):
            os.mkdir(Path(mode_path))
        if not os.path.exists(Path(mode_path_type)):
            os.mkdir(Path(mode_path_type))
        if not os.path.exists(Path(mode_path_test_and_answer)):
            os.mkdir(Path(mode_path_test_and_answer))

        # image generation
        for i in tqdm(range(len(tasks)), desc = "Generating " + mode + " of " + type):
            plot_thumbnail(tasks[i][0], path = Path(mode_path_type + j_codes[i] + '.png'))
            plot_thumbnail(tasks[i][1], path = Path(mode_path_test_and_answer + j_codes[i] + '.png'))

    ######################################################
    # full mode
    elif mode == 'full':
        mode_path = path + 'full/'
        mode_path_type = mode_path + type + '/'

        # create folders for full images
        if not os.path.exists(Path(mode_path)):
            os.mkdir(Path(mode_path))
        if not os.path.exists(Path(mode_path_type)):
            os.mkdir(Path(mode_path_type))
        
        # image generation
        for i in tqdm(range(len(tasks)), desc = "Generating "+ mode + " of " + type):
            plot_full(tasks[i], path = Path(mode_path_type + j_codes[i] + '.png'))


    ######################################################
    # full without answer mode
    elif mode == 'full_without_answer':
        mode_path = path + 'without_answer/'
        mode_path_type = mode_path + type + '/'

        # create folders for full images without answer
        if not os.path.exists(Path(mode_path)):
            os.mkdir(Path(mode_path))
        if not os.path.exists(Path(mode_path_type)):
            os.mkdir(Path(mode_path_type))

        # image generation
        for i in tqdm(range(len(tasks)), desc = "Generating "+ mode + " of " + type):
            plot_without_answer(tasks[i], path = Path(mode_path_type + j_codes[i] + '.png')) # .split('\\')[-1]

    else:
        raise Exception("Invalid mode: ", mode)



#############################################################################################
#############################################################################################
if __name__ == "__main__":
    # type
    # 1. 'train'                : training data (400 tasks)
    # 2. 'eval'                 : evaluation data (400 tasks)

    # mode
    # 1. 'thumbnail'            : only example pairs + test input with the answer in the separate folder
    # 2. 'full'                 : entire task including the answer (test pairs have purple grid lines)
    # 3. 'full_wihout_answer'   : entire task without the answer (test grid have purple grid lines)


    image_gen(type = 'train', mode = 'thumbnail')
    image_gen(type = 'eval', mode = 'thumbnail')

    image_gen(type = 'train', mode = 'full')
    image_gen(type = 'eval', mode = 'full')

    image_gen(type = 'train', mode = 'full_without_answer')
    image_gen(type = 'eval', mode = 'full_without_answer')