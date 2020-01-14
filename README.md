# py-keras-train

## 简述

---
使用keras训练模型，保存成h5文件，转成pb文件，用于线上部署，
转换脚本[h5-to-pb](https://github.com/amir-abdi/keras_to_tensorflow)
线上部署使用golang，实现高并发[tfgo](https://github.com/galeone/tfgo)

---
近期在总结这一年来的项目，回头过往，发现总有些事情能做的更完美，只是曾经脑洞不够，现如今回补，提高自己也方便他人。

---
项目落地代码：
[go-mnist-service](https://github.com/atlantiswqq/go-keras-servcie.git)

# 本项目执行步骤

1. 执行train.py 

2.`python3 ./utils/keras_to_tensorflow.py --input_model="./output/h5/model.h5" --output_model="./output/pb/model.pb"`

正常提示如下：
```buildoutcfg
Using TensorFlow backend.
2020-01-14 18:11:52.052856: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
I0114 18:11:52.417983 4544931264 keras_to_tensorflow.py:145] Converted output node names are: ['dense_3/Softmax']
INFO:tensorflow:Froze 6 variables.
I0114 18:11:52.431236 4544931264 tf_logging.py:115] Froze 6 variables.
INFO:tensorflow:Converted 6 variables to const ops.
I0114 18:11:52.437839 4544931264 tf_logging.py:115] Converted 6 variables to const ops.
I0114 18:11:52.451970 4544931264 keras_to_tensorflow.py:177] Saved the freezed graph at output/pb/model.pb
```