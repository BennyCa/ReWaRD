## Brain-Score of tested resnet50 training strategies:
Scores range from 0 to 1, higher is better. Currently best performing model on BrainScore achieves an average score of .465.
Highest score in each category is marked in ***bold italic***.

|training datasets used|Average|V1|V2|V4|IT|Behavior|
|---	|---	|---	|---	|---	|---	|---  |
|rwave-1024|.230|.437|.217|.252|.185|.059|
|rwave-4096|.239|.434|***.226***|***.279***|***.190***|.065|
|FractalDB1k|***.267***|***.572***|.222|.250|***.190***|***.101***|
|---	|---	|---	|---	|---	|---	|---  |
|CIFAR100[^1]|.216|.389|.154|.305|.225|.010|
|rwave-1024 -> CIFAR100[^1]|***.290***|.455|***.267***|.392|***.276***|.060|
|rwave-4096 -> CIFAR100[^1]|.282|.444|.236|***.399***|.266|.067|
|FractalDB1k -> CIFAR100[^1]|.285|***.506***|.222|.372|.251|***.073***|
|---	|---	|---	|---	|---	|---	|---  |
|ImageNet1k -> CIFAR100[^1]|***.313***|.458|***.277***|***.437***|***.296***|***.097***|
|---	|---	|---	|---	|---	|---	|---  |
|ImageNet1k[^2]|***.414***|***.538***|.315|***.497***|.378|.342|
|rwave-1024 -> ImageNet1k[^2]|.399|.524|.314|.491|***.390***|.277|
|rwave-4096 -> ImageNet1k[^2]|.411|.517|.308|.488|.383|***.361***|
|FractalDB1k -> ImageNet1k[^2]|.407|.525|***.324***|.489|***.390***|.306 |

[^1]: The default configuration of the FractalDB pipeline was used for the fine-tuning step. (initial learning rate of 0.01)
[^2]: The default configuration of the FractalDB pipeline was altered for the fine-tuning step: the initial learning rate was set to 0.1.


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
|FractalDB1k|layer2|layer3|layer3|layer3|
|---	|---	|---	|---	|---	|
|CIFAR100[^1]|maxpool|layer3|maxpool|layer3|
|rwave-1024 -> CIFAR100[^1]|maxpool|layer3|layer2|layer3|
|rwave-4096 -> CIFAR100[^1]|maxpool|layer3|layer3|layer3|
|FractalDB1k -> CIFAR100[^1]|layer3|layer3|layer3|layer3|
|---	|---	|---	|---	|---	|
|ImageNet1k -> CIFAR100[^1]|maxpool|layer3|layer2|layer3|
|---	|---	|---	|---	|---	|
|ImageNet1k[^2]|layer2|layer2|layer2|layer3|
|rwave-1024 -> ImageNet1k[^2]|layer2|layer3|layer2|layer3|
|rwave-4096 -> ImageNet1k[^2]|layer2|layer2|layer2|layer3|
|FractalDB1k -> ImageNet1k[^2]|layer2|layer3|layer2|layer3|
