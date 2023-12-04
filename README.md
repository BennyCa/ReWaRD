# ReWaRD
Retinal Waves for Pre-Training Artificial Neural Networks Mimicking Real Prenatal Development

![ReWaRD Overview Figure](https://github.com/BennyCa/ReWaRD/blob/main/ReWaRD_Overview.png?raw=true)

If you use our code, please cite the following paper:
```
@inproceedings{cappell2023reward,
      title={ReWaRD: Retinal Waves for Pre-Training Artificial Neural Networks Mimicking Real Prenatal Development}, 
      author={Benjamin Cappell and Andreas Stoll and Williams Chukwudi Umah and Bernhard Egger},
      year={2023},
  booktitle={Proceedings of the Workshop on Unifying Representations in Neural Models (UniReps 2023) at NeurIPS 2023}
}
```
# Structure
This project provides different steps to make generation of retinal waves, pretraining a neural network and training it on image data easily accessible.\
[Step 1](/1_Generate-Retinal-Waves) - Generate retinal waves (pre-training data)\
[Step 2](/2_Dataset-Preparation) - Prepare the retinal wave dataset for pre-training (train/val/test split), download fine-tuning dataset\
[Step 3](/3_Pretraining-and-Finetuning)a - Pretrain the network on retinal waves\
[Step 3](/3_Pretraining-and-Finetuning)b - Fine-Tune = Train the network for a specific task on the fine-tuning dataset\
[Step 4](/4_Visualization) - Visualize filters on saved checkpoints\
[Step 5](/5_BrainScore) - Evaluate on BrainScore

# Publicly released retinal wave datasets and ANNs
retinal wave datasets and ANN intermediate results are released to the public:
- rwave1024 dataset: https://zenodo.org/record/7811859
- rwave4096 dataset: https://zenodo.org/record/7779498
- pre-trained and fine-tuned artificial neural networks: https://zenodo.org/record/7779519

# Quick Start
## Complete ReWaRD pipeline
Start from step 1 and execute each step consequently.

## Pre-train on an existing dataset
Get the intermediate result (rwave-4096 dataset, prepared for pre-training) from https://zenodo.org/record/7779498 and start with step 3a).

## Fine-tune a already pre-trained network
Get a pre-trained .pth from https://zenodo.org/record/7779519 (one starting with rwave...) and start with step 3b).

## Analyze emerging features
Get a fine-tuned .pth from https://zenodo.org/record/7779519 (pt-rwave...-ft-....pth) and start with step 4). 

# Prerequisites
1 - gcc, Java\
2 - python\
3 - python3.7, GPU\
4 - python\
5 - python3.7

for exact prerequisites see subfolders.

# License
This project is licensed under the MIT License. See [LICENSE](/LICENSE) for details.
The license does not apply to submodule repositories. See these repositories for their license.
