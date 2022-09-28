# IclCV接口文档使用说明

## `Icl.CVImage`
### 图片格式
```python
class Format(enum.Enum):
    FORMAT_YUV420P = 0
    FORMAT_YUV422P = 1
    FORMAT_YUV444P = 2
    FORMAT_NV12 = 3
    FORMAT_NV21 = 4
    FORMAT_NV16 = 5
    FORMAT_NV61 = 6
    FORMAT_NV24 = 7
    FORMAT_RGB_PLANAR = 8
    FORMAT_BGR_PLANAR = 9
    FORMAT_RGB_PACKED = 10
    FORMAT_BGR_PACKED = 11
    FORMAT_RGBP_SEPARATE = 12
    FORMAT_BGRP_SEPARATE = 13
    FORMAT_GRAY = 14
    FORMAT_COMPRESSED = 15
```
各个格式说明:

* FORMAT_YUV420P

表示预创建一个 YUV420 格式的图片,有三个 plane

* FORMAT_YUV422P

表示预创建一个 YUV422 格式的图片,有三个 plane

* FORMAT_YUV444P

表示预创建一个 YUV444 格式的图片,有三个 plane

* FORMAT_NV12

表示预创建一个 NV12 格式的图片,有两个 plane

* FORMAT_NV21

表示预创建一个 NV21 格式的图片,有两个 plane

* FORMAT_NV16

表示预创建一个 NV16 格式的图片,有两个 plane

* FORMAT_NV61

表示预创建一个 NV61 格式的图片,有两个 plane

* FORMAT_RGB_PLANAR

表示预创建一个 RGB 格式的图片,RGB 分开排列,有一个 plane

* FORMAT_BGR_PLANAR

表示预创建一个 BGR 格式的图片,BGR 分开排列,有一个 plane

* FORMAT_RGB_PACKED

表示预创建一个 RGB 格式的图片,RGB 交错排列,有一个 plane

* FORMAT_BGR_PACKED

表示预创建一个 BGR 格式的图片,BGR 交错排列,有一个 plane

* FORMAT_RGBP_SEPARATE

表示预创建一个 RGB planar 格式的图片，RGB 分开排列并各占一个 plane，共有 3 个 plane

* FORMAT_BGRP_SEPARATE

表示预创建一个 BGR planar 格式的图片，BGR 分开排列并各占一个 plane，共有 3 个 plane

* FORMAT_GRAY

表示预创建一个灰度图格式的图片,有一个 plane

* FORMAT_COMPRESSED

表示预创建一个 VPU 内部压缩格式的图片，共有四个 plane，分别存放内容如下：

plane0: Y compressed table

plane1: Y compressed data

plane2: CbCr compressed table

plane3: CbCr compressed data

### 图片数据类型
```python
class ImgDtype(enum.Enum):
    DATA_TYPE_EXT_FLOAT32 = 0
    DATA_TYPE_EXT_1N_BYTE = 1
    DATA_TYPE_EXT_4N_BYTE = 2
    DATA_TYPE_EXT_1N_BYTE_SIGNED = 3
    DATA_TYPE_EXT_4N_BYTE_SIGNED = 4
```

各个格式说明:

* DATA_TYPE_EXT_FLOAT32

表示所创建的图片数据格式为单精度浮点数

* DATA_TYPE_EXT_1N_BYTE

表示所创建图片数据格式为普通无符号 1N UINT8

* DATA_TYPE_EXT_4N_BYTE

表示所创建图片数据格式为 4N UINT8,即四张无符号 INT8 图片数据交错排列，一个 bm_image 对象其实含有四张属性相同的图片

* DATA_TYPE_EXT_1N_BYTE_SIGNED

表示所创建图片数据格式为普通有符号 1N INT8

* DATA_TYPE_EXT_4N_BYTE_SIGNED

表示所创建图片数据格式为 4N INT8,即四张有符号 INT8 图片数据交错排列

* 其中，对于 4N 排列方式可参考下图：

![](data/4N%E5%9B%BE%E7%89%87%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F.png)
