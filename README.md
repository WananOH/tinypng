![](http://ww4.sinaimg.cn/large/005Xtdi2gw1f4kksnoy72j313y07yjuk.jpg)

## 前言
我们在写文章或者建网站时，经常需要对图片压缩处理，以便帮助用户节省流量和提升网站加载速度。

图片压缩有很多方法，这里推荐的是[TinyPNG](https://tinypng.com/)。TinyPNG 是一个在线压缩工具，主要优点是在视觉上没有明显变化的情况下达到很高的压缩比(如我手机截屏图片大小一般为110k，压缩后能达到30k左右)。

TinyPNG官网: https://tinypng.com/

>
TinyPNG支持一次最多上传20张图片，图片最大5M。

如果处理的图片比较少则使用在线压缩即可，非常方便，但如果图片处理量比较大，使用在线压缩一次一次的上传下载则显得有些麻烦了，因此用Python写了一个简单的脚本，用于批量压缩图片。

## 使用方法

### 一.配置环境

**Python:** 保证电脑中存在 Python 环境。

**Tinify:** 导入Tinify
```
  pip install --upgrade tinify
```

### 二.申请 API key

到此处申请 API key: https://tinypng.com/developers

>
一个 key 每个月可以免费压缩500张图片，可以申请多个 key。

### 三.配置脚本并运行
下载完该脚本后，你需要简单编辑一下该脚本，将申请到到API key 填写进去。

```
online_key_list = [
    "sq5RzZVjHxVKRN0CHSBn659XPb67PyMl",
    "rcj2WmWcPZGMDbmwDXJ69XQKGhyr6mCw", # 可以继续添加  防止一个key不够
]
```

之后你可以将该脚本放入到需要压缩的图片的文件夹下，然后在命令行(终端)中进入到该文件夹

执行如下命令批量压缩指定文件夹下大于1000的图片:
```
python tinypng.py -d /wwwroot/swdz -s 1000k
```
或以下命令压缩指定图片：
```
python tinypng.py -f /wwwroot/swdz/icon1.png 
```

### 四.支持参数

参数  | 参数类型 | 摘要                               | 示例
:----:|----------|------------------------------------|-----------------------------
 无参 |          | 压缩根目录下所有图片文件       | `tinypng.py` 
`－f` | 图像文件 | 压缩指定的单个文件                 | `tinypng.py -f /User/GcsSloop/demo.jpg`
`－d` | 文件夹   | 压缩指定文件夹下所有图片文件       | `tinypng.py -d /User/GcsSloop/DemoDir`
`－s` | 图像大小   | 压缩指定大小的图片       | `tinypng.py -s 1000K`
 `-w` | 整型数字 | 压缩后图片的宽度，不指定则宽度不变 | `tinypng.py -w 300`

**参数优先级:**
```
  －f > －d > 无参
```
如果指定了 `－f` 则只会压缩指定文件，即使后续跟了 `－d` 也不会压缩指定的文件夹

```
 －w 无冲突，均可使用
```

```
-s 用于压缩指定文件夹下大于指定大小的图片，对-f指定图片无效
```








