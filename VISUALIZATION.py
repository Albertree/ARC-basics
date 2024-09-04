import json
import numpy as np
import matplotlib.pyplot as plt
from ARCLOADER import *

settings = json.load(open('settings.json', 'r'))
colors_rgb = settings['colors_rgb']

# convert color grid to rbg grid
def convert_data(datas, dim):
    result = []
    if dim == 2: # dim = (row, col)
        for line in datas:
            d_grid = [colors_rgb[value] for value in line]
            result.append(d_grid)

    elif dim == 3: # dim = (input & output(2), row, col)
        for data in datas:
            for line in data:
                d_input = [[colors_rgb[value] for value in line] for line in datas[0]]
                d_output = [[colors_rgb[value] for value in line] for line in datas[1]]
        result.append(d_input)
        result.append(d_output)

    elif dim == 4: # dim = (number of pairs(p), input & output(2), row, col)
        for pair in datas:
            resul = []
            for data in pair:
                for line in data:
                    d_input = [[colors_rgb[value] for value in line] for line in pair[0]]
                    d_output = [[colors_rgb[value] for value in line] for line in pair[1]]
            resul.append(d_input)
            resul.append(d_output)
            result.append(resul)

    elif dim == 10:
        result = [[], []]
        for line in datas[0][0]:
            d_grid = [colors_rgb[value] for value in line]
            result[0].append(d_grid)
        
        for data in datas[1]:
            resul = []
            for line in data:
                d_colors = [colors_rgb[value] for value in line]
                resul.append(d_colors)
            result[1].append(resul)

    else:
        raise Exception("Invalid data dimension: ")
    
    return result

# split grid into 10 colors
def spliter_full(grid):
    assert type(grid[0][0]) == int 
    dim1 = len(grid)
    dim2 = len(grid[0])

    result = [[grid], None] # [[[2d-ori]], [[2d-0], [2d-1], [2d-2], ... [2d-9]]]
    frame = [[[12 for _ in range(dim2)] for _ in range(dim1)] for _ in range(10)]

    for i in range(dim1):
        for j in range(dim2):
            frame[grid[i][j]][i][j] = grid[i][j]
    result[1] = frame

    return result


# plot grid
def plot_data(datas, tencolorsplit = False):
    if tencolorsplit == True:
        datas = spliter_full(datas)


    # check data dimension
    if type(datas[0]) == int:
        datas = [datas]
        dim = 2
    elif type(datas[0][0]) == int:
        dim = 2
    elif type(datas[0][0][0]) == int:
        assert len(datas) == 2
        dim = 3
    elif type(datas[0][0][0][0]) == int:
        # plot 10 color split (datas must be the output of spliter)
        if tencolorsplit == True:
            assert len(datas) == 2 # [original, ten splits]
            assert len(datas[0]) == 1
            assert type(datas[0][0][0][0]) == int # [0][0][dim1][dim2]
            assert len(datas[1]) == 10
            assert type(datas[1][9][0][0]) == int # [1][0 - 9][dim1][dim2]
            dim = 10
        else:
            dim = 4
    elif type(datas[0][0][0][0][0]) == int:
        assert len(datas) == 2
        new = []
        for tr in datas[0]:
            new.append(tr)
        for te in datas[1]:
            new.append(te)
        datas = new
        dim = 4
    else:
        raise Exception("Invalid data dimension")
    
    num_data = len(datas)
    datas = convert_data(datas, dim)
    color = '#AAB7B8' # 'purple'
    alpha = 1
    linewidth = 1.5

    # plot grids depending on the dimension
    if dim == 2: # dim = (row, col)
        fig, ax = plt.subplots(1, 1, figsize = (4, 4))
        plt.tight_layout()

        ax.grid(True, which = 'both', color = color, alpha = alpha, linewidth = linewidth) 
        ax.xaxis.set_ticks_position('top')
        ax.set_xticks([x - 0.50 for x in range(1 + (np.array(datas).shape[1]))])
        ax.yaxis.set_ticks_position('left')
        ax.set_yticks([x - 0.50 for x in range(1 + (np.array(datas).shape[0]))])
        ax.tick_params(top = False, labeltop = False, left = False, labelleft = False)
        ax.imshow(datas)

        plt.show()

    elif dim == 3: # dim = (input & output(2), row, col)
        fig, axs = plt.subplots(1, 2, figsize = (8, 4 * num_data))
        plt.tight_layout()
        
        for i in range(2):
            axs[i].grid(True, which = 'both', color = color, alpha = alpha, linewidth = linewidth) 
            axs[i].xaxis.set_ticks_position('top')
            axs[i].set_xticks([x - 0.50 for x in range(1 + (np.array(datas[i]).shape[1]))]) # atleast_2d
            axs[i].yaxis.set_ticks_position('left')
            axs[i].set_yticks([x - 0.50 for x in range(1 + (np.array(datas[i]).shape[0]))]) # atleast_2d
            axs[i].tick_params(top = False, labeltop = False, left = False, labelleft = False)
            axs[i].imshow(datas[i])

        plt.show()

    elif dim == 4: # dim = (number of pairs(p), input & output(2), row, col)
        fig, axs = plt.subplots(num_data, 2, figsize=(6, 3 * num_data))
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

        plt.show()

    elif dim == 10:
        fig, axs = plt.subplots(num_data, 10, figsize = (20, 4))
        plt.tight_layout()

        for i in range(num_data):                
            for j in range(10):
                if i == 0:
                    if j == 0:  
                        axs[i, j].grid(True, which = 'both', color = color, alpha = alpha, linewidth = linewidth) 
                        axs[i, j].xaxis.set_ticks_position('top')
                        axs[i, j].set_xticks([x - 0.50 for x in range(1 + (np.array(datas[i]).shape[1]))])
                        axs[i, j].yaxis.set_ticks_position('left')
                        axs[i, j].set_yticks([x - 0.50 for x in range(1 + (np.array(datas[i]).shape[1]))])
                        axs[i, j].tick_params(top = False, labeltop = False, left = False, labelleft = False)
                        axs[i, j].imshow(datas[i])

                    else:
                        axs[i, j].axis('off')
                        
                else:
                    axs[i, j].grid(True, which = 'both', color = color, alpha = alpha, linewidth = linewidth)    
                    axs[i, j].xaxis.set_ticks_position('top')
                    axs[i, j].set_xticks([x - 0.50 for x in range(1 + (np.array(datas[i]).shape[1]))])
                    axs[i, j].yaxis.set_ticks_position('left')
                    axs[i, j].set_yticks([x - 0.50 for x in range(1 + (np.array(datas[i]).shape[1]))])
                    axs[i, j].tick_params(top = False, labeltop = False, left = False, labelleft = False)
                    axs[i, j].imshow(datas[i][j])

        plt.show()

    else:
        raise Exception("Invalid data dimension: ", dim)



if __name__ == "__main__":
    color_pallette = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [-1,-1,-1,-1]] # 3 additional colors 10 and 11 and 12(-1) [12 means null]
    plot_data(color_pallette)

    arc = ARCDataset()
    tasks, j_codes = arc.load_data(type = 'train', form = 'list', shuffle = False, jcode = True)

    x = 14     # 0 - 399      (task number) 37
    tt = 1    # 0 or 1       (train or test)
    p = 0     # 0 - max pair (pair number)
    io = 0    # 0 or 1       (input or output)

    ex = tasks[x][tt][p][io]

    plot_data(ex)
    # plot_data(spliter_full(ex), tencolorsplit = True)
    plot_data(ex, tencolorsplit=True)