## Brain-Score of tested resnet50 training strategies:
Scores range from 0 to 1, higher is better. Currently best performing model on BrainScore achieves an average score of .465.
Highest score in each category is marked in ***bold italic***.

|training datasets used|Average|V1|V2|V4|IT|
|---	|---	|---	|---	|---	|---	|
|rwave-1024|.230|.437|.217|.252|.185|
|rwave-4096|.239|.434|.226|.279|.190|
|rwave-1024 -> CIFAR100|.269|.448|.276|.322|.262|
|rwave-4096 -> CIFAR100|.253|***.528***|.139|.319|.205|
|rwave-4096 -> ImageNet|***.385***|.455|***.288***|***.490***|***.394***|
|ImageNet|.376|.459|.283|.481|.370|


### Layer -> cortical region commitment
As the BrainScore Benchmark was done using the Base Model, Layers of the ANN are mapped to cortical regions automatically.
the available layers of resnet50 are:
|layer #|name|type|
|---	|---	|---	|
|0|conv1|Conv2d|
|1|bn1|BatchNorm2d|
|2|relu|ReLU|
|3|maxpool|MaxPool2d|
|4|layer1|Conv2d->BatchNorm2d|
|5|layer2|Conv2d->BatchNorm2d|
|6|layer3|Conv2d->BatchNorm2d|
|7|layer4|Conv2d->BatchNorm2d|
|8|avgpool|AvgPool2d|
|9|fc|Linear|


The table shows the mapping per model:
|training datasets used|layer V1|layer V2|layer V4|layer IT|
|---	|---	|---	|---	|---	|
|rwave-1024|maxpool|layer4|maxpool|layer3|
|rwave-4096|maxpool|layer3|maxpool|layer3|
|rwave-1024 -> CIFAR100|maxpool|layer3|maxpool|layer3|
|rwave-4096 -> CIFAR100|layer3|layer4|layer3|layer3|
|rwave-4096 -> ImageNet|maxpool|layer3|layer2|layer3|
|ImageNet|maxpool|layer3|layer2|layer3|
