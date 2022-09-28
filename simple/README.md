# simple 目录介绍

## 开发环境配置
* 由于比特大陆的`se5`盒子上默认提供的是`python3.5`的开发环境，`vscode`不支持`python3.5`的调试功能，因此对其进行升级到`python3.8`的开发环境，同时导入比特大陆`npu-sdk3.0`的`python3.8`环境的开发包路径

### 安装`python3.8`
* [安装`python3.8`](https://www.python.org/ftp/python/3.8.13/Python-3.8.13.tgz)
* 先安装[zlib](https://www.cyberithub.com/how-to-install-zlib-package-on-ubuntu-20-04-lts-focal-fossa/)
```shell
sudo apt update
# sudo apt install zlib1g
sudo apt install zlib1g-dev
```
* 再安装`python3.8`
```shell
tar xzvf Python-3.8.13.tgz
cd Python-3.8.13 
mkdir build && cd build
../configure 
make -j33
sudo make install #默认安装在/usr/local/bin以及/usr/local/lib目录下
```
* 导入比特大陆`npu-sdk3.0`的`python3.8`环境的开发包路径到系统启动加载配置文件`~/.bashrc`
```shell
sudo vim ~/.bashrc
export PYTHONPATH=/data/project/deploy/sophonsdk_v3.0.0_20220716/sophonsdk_v3.0.0/lib/opencv/soc/opencv-python:/data/project/deploy/sophonsdk_v3.0.0_20220716/sophonsdk_v3.0.0/lib/sail/python3/soc/py38:$PYTHONPATH
source ~/.bashrc
```
* 测试`python3.8`开发环境导入比特大陆提供的开发包
```shell
#python3.8
import sophon.sail as sail
import cv2
```
### 安装其他的`python`开发包
```shell
pip3.8 install numpy -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
pip3.8 install Pillow -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
pip3.8 install shapely -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
pip3.8 install pyclipper -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
pip3.8 install loguru -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
pip3.8 install prettytable -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```

基于BMCV/OpenCV做前后处理， BMRT做为推理引擎，提供基于单个模型的推理示例。

主要目录结构和模块说明：


| 样例名称 | 语言 | 适配BMNNSDK版本 | 简介 |
|---|---|---|---|
|[centernet](./simple/centernet) | c++/python | >=2.6.0 | CenterNet 推理示例，采用BMCV做前后处理。 |
|[LPRNet](./lprnet) | c++/python | >=2.6.0 | CenterNet 推理示例，采用BMCV做前后处理。 |
|[PP-OCRv2](./PP-OCRv2) | python | >=2.6.0 | PP-OCRv2 推理示例，采用OpenCV做前后处理。 |
|[Resnet_classify](./Resnet_classify) | c++ | >=2.6.0 | Resnet_classify 推理示例。 |
|[retinaface](./retinaface) | c++/python | >=2.6.0 | RetinaFace 推理示例，采用BMCV或OpenCV做前后处理。 |
|[ssd](./ssd) | c++/python | >=2.6.0 | ssd 推理示例，采用BMCV或OpenCV做前后处理。 |
|[yolact](./ssd) | python | >=2.6.0 | yolact 推理示例，采用BMCV或OpenCV做前后处理。 |
| [YOLOV5](./yolov5) |  c++/python | >=2.6.0 | 使用bmcv/opencv做前处理，BMRT推理的示例程序 |
|[YOLOv34](./yolov34) | c++/python | >=2.6.0 | YOLOV3/YOLOV4 推理示例，采用BMCV做前后处理。 |
|[YOLOX](./yolox) | c++/python | >=2.6.0 | YOLOX 推理示例，采用BMCV做前后处理。 |


> 已经转换好的bmodel文件可从以下百度网盘下载：
> 链接: https://pan.baidu.com/s/1d3f8CjzC3BF2-2I2OF0q1g 提取码: lt59 