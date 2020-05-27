# transfer-learning-for-segmentation-of-intestinal-glands
This code is a modified version of the DeepDIVA framework taken from:

https://github.com/DIVA-DIA/DeepDIVA

## Content
The goal of this project was to perform segmentation of intestinal glands from hematoxylin and eosin stained Whole Slide Images derived from a local dataset. To accomplish this task I pre-trained a Unet on the publicy available GlaS dataset and fine-tune it on our local dataset. 


## Getting started

In order to get the framework up and running it is only necessary to clone the latest version of the repository:

``` shell
git clone https://github.com/Sven-Wa/transfer-learning-for-segmentation-of-intestinal-glands.git
```

Run the script:

``` shell
bash setup_environment.sh
```

Reload your environment variables from `.bashrc` with: `source ~/.bashrc`

## Verifying Everything Works

To verify the correctness of the procecdure you can run a small experiment. Activate the DeepDIVA python environment:

``` shell
source activate deepdiva
```

## 1. Download the GlaS dataset (dataset for pre-training)
``` shell
python util/data/get_a_dataset.py --dataset glas --output-folder ./
```
## 2. Download the pT1-gland-mask-dataset  (dataset for fine-tuning)

https://github.com/Sven-Wa/pT1-gland-mask-dataset


## 3. Train a Unet on the GlaS dataset in order to perform semantic segmentation on intestinal glands.

``` shell
python /template/RunMe.py --runner-class semantic_segmentation --output-folder ./output --dataset-folder /path/to/GlaS/ --ignoregit --experiment-name pre-train-unet-with-glas --normalize --model-name unet --epochs 60 --crop-size 256 --imgs-in-memory 5 --crops-per-image 10 --momentum 0.9 --lr 0.01 --decay-lr 10 -j 10 --batch-size 32 --disable-databalancing
```

you can additionally set the following data augmentation options:
``` shell
--rotation
--flip
--stain_augmentation
--elastic_transformation

```

## 4. Test the trained model on a new gland dataset (pT1-gland-mask-dataset):
```
python /template/RunMe.py --runner-class semantic_segmentation --output-folder ./output --dataset-folder /path/to/pT1-gland-mask-dataset --ignoregit --experiment-name  test-performance-on-new-dataset --model-name unet --epochs 0 --crop-size 256 --imgs-in-memory 5 --crops-per-image 10 --momentum 0.9 --lr 0.01 --decay-lr 10 -j 10 --batch-size 32 --disable-databalancing --load-model /path/to/model/trained/on/Glas/model_best.pth.tar
```
You will see that the performance on the new dataset is not as good as on the  GlaS dataset. This is probably due to different color distribution between the two datasets. But we can improve the performance by fine-tuning our pre-trained model on images from the pT1-gland-mask-dataset

## 5. Fine-tune the model with new images from the pT1-gland-mask-dataset.
Inside the pT1-gland-mask-dataset Repository you can find a folder named subset. This folder contains subset of images from the pT1-gland-mask-dataset. Select one of this subsets to fine-tune your model. I experimented with this subsets to figure out how many images are needed for fine-tuning. It turned out that the performance for the our pre-trained Unet reaches saturation when fine-tuning with 18-24 images (without any data augmentation). 

```
python /template/RunMe.py --runner-class semantic_segmentation --output-folder ./output --dataset-folder /path/to/pT1-gland-mask-dataset/s1_24_images --ignoregit --experiment-name  fine-tuning --model-name unet --epochs 60 --crop-size 256 --imgs-in-memory 5 --crops-per-image 10 --momentum 0.9 --lr 0.01 --decay-lr 10 -j 10 --batch-size 32 --disable-databalancing --load-model /path/to/pre-trained-model/model_best.pth.ta
```



