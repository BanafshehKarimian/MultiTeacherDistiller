# MultiTeacherDistiller
The extended version of [mdistiller](<https://github.com/megvii-research/mdistiller>) to multi-teacher, multi-student setting. 
## Multi Teacher Config
Simply add  'MULTITEACHER: True' to the distiller config and define other teachers. For example see [this](https://github.com/BanafshehKarimian/MultiTeacherDistiller/blob/main/configs/cifar100/multi_kd/resnet8x4.yaml) config.
## Guide
- tools/train.py: the main file
- configs/: contains the config files needed for running. 
- mdistiller/dataset/: add your data loader here with editing the get_dataset function of __init__. For using MLDK you need to also update the get_dataset_strong function. cifar100 and imagenet data loaders are already supported.
- mdistiller/distillers/: the knowledge distillation algorithms are coded here. To add a new algorithm, add the class and then add the name mapping to the distiller_dict of __init__.
- mdistiller/engine: has the main training epochs coded.
- mdistiller/models: has different model, i.e. mobilenet, resnet, shufflenet, VGG.
## How to Run
Use the main file, tools/train.py, with the address of the config file:
```bash
 python tools/train.py --cfg configs/cifar100/kd/resnet32x4_resnet8x4.yaml
  ```
If you want to use [Logit Standardization](https://github.com/sunshangquan/logit-standardization-KD/tree/master), use the following:
 ```bash
 python tools/train.py --cfg configs/cifar100/kd/resnet32x4_resnet8x4.yaml --logit-stand --base-temp 2 --kd-weight 9
  ```
Supported Algorithms:
|Method|Paper Link|
|:---:|:---:|
|KD| <https://arxiv.org/abs/1503.02531> |
|AT| <https://arxiv.org/abs/1612.03928> |
|NST| <https://arxiv.org/abs/1707.01219> |
|PKT| <https://arxiv.org/abs/1803.10837> |
|KDSVD| <https://arxiv.org/abs/1807.06819> |
|OFD| <https://arxiv.org/abs/1904.01866> |
|RKD| <https://arxiv.org/abs/1904.05068> |
|VID| <https://arxiv.org/abs/1904.05835> |
|SP| <https://arxiv.org/abs/1907.09682> |
|CRD| <https://arxiv.org/abs/1910.10699> |
|ReviewKD| <https://arxiv.org/abs/2104.09044> |
|DKD| <https://arxiv.org/abs/2203.08679> |
