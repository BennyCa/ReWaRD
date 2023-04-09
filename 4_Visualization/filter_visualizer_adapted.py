import matplotlib.pyplot as plt
import numpy as np
import torch
import math
import torch.nn as nn
from nets.resnet import resnet50, resnet34
from nets.alex import bn_alexnet
from nets.vgg import vgg16
import os
import sys

def runSim(weight_name, model_type, numof_classes, max_layer):
    #### Load correct model
    if "resnet50" in model_type:
        model = resnet50(pretrained=False, num_classes=numof_classes)
    elif "resnet34" in model_type:
        model = resnet34(pretrained=False, num_classes=numof_classes)
    elif "bn_alexnet" in model_type:
        model = bn_alexnet(pretrained=False, num_classes=numof_classes)
        if "_ft" in model_type:
            removed = list(model.classifier.children())[:-1]
            model.classifier = torch.nn.Sequential(*removed)
            model.classifier = torch.nn.Sequential(model.classifier, nn.Linear(4096, numof_classes))
    elif "vgg16" in model_type:
        model = vgg16(pretrained=False, num_classes=numof_classes)
    else:
        print("Error, model not implemented")
        sys.exit()

    # load pre-trained model
    if os.path.exists(weight_name):
        print ("use pretrained model : %s" % weight_name)
        checkpoint = torch.load(weight_name, map_location=lambda storage, loc: storage)
        model.load_state_dict(checkpoint)
    #elif dataset == "imagenet":
    #    print ("use imagenet pretrained model")
    #    model = resnet50(pretrained=True)
    else:
        print("no weights found")


    #### Visualize Filters
    model_weights = [] 
    conv_layers = [] 
    model_children = list(model.modules())

    # counter to keep count of the conv layers
    counter = 0 
    # append all the conv layers and their respective weights to the list
    for i in range(len(model_children)):
        if type(model_children[i]) == nn.Conv2d:
            counter += 1
            model_weights.append(model_children[i].weight)
            conv_layers.append(model_children[i])
        elif type(model_children[i]) == nn.Sequential:
            pass
            #for j in range(len(model_children[i])):
            #    for child in model_children[i][j].modules():
            #        if type(child) == nn.Conv2d:
            #            counter += 1
            #            model_weights.append(child.weight)
            #            conv_layers.append(child)
    print(f"Total convolutional layers: {counter}")



    layer = 0
    # visualize the first conv layer filters
    #plt.figure(figsize=(16, 16))
    #for i, filter in enumerate(model_weights[layer]):
    #    if i>63: #limit to max 64 filters
    #        continue
    #    plt.subplot(8, 8, i+1) # we have 7x7 filters and total of 64 (see printed shapes)
    #    plt.imshow(filter[0, :, :].detach().cpu().numpy(), cmap='viridis')
    #    plt.axis('off')
    #plt.savefig(weight_name[:-4]+'_firstlayer_features.png')

    # visualize all conv layer filters
    for m in model_weights:
        if layer > max_layer:
            break
        plt.figure(figsize=(16, 16))
        for i, filter in enumerate(m):
            #if i>63: #limit to max 64 filters
                #continue
            plt.subplot(int(math.ceil(math.sqrt(len(m)))), int(math.ceil(math.sqrt(len(m)))), i+1) # we have ? filters and total of ? (see printed shapes)
            plt.imshow(filter[0, :, :].detach().cpu().numpy(), cmap='viridis')
            plt.axis('off')
        plt.savefig("imgs/" + weight_name[:-4]+'_' + str(layer)+ '_layer_features.png')
        layer +=1
        plt.close()
        





if len(sys.argv) != 5:
    print("usage: filter_visualizer path_to/net.pth|folder model_type(resnet50||resnet34||bn_alexnet||vgg16) class_count max_layer")
    sys.exit()

in_path = sys.argv[1]
model = sys.argv[2]
classes = int(sys.argv[3])
max_layer = int(sys.argv[4])


if in_path[-4:] == ".pth":
    file = in_path
    runSim(file, model, classes, max_layer)
else:
    for file in os.listdir(in_path):
        filepath = os.path.join(in_path, file)
        if os.path.isfile(filepath) and str(filepath)[-4:] == ".pth":
            runSim(str(filepath), str(filepath), classes, max_layer)

