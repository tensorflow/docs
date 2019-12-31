# 增加数据集

按照本指南将数据集添加到 TFDS。

请参阅我们的[数据集列表](catalog/overview.md)来查看您所需的数据集是否尚未添加。

*   [总览](#总览)
*   [编写 `my_dataset.py`](#编写-my-datasetpy)
    *   [使用默认模版](#使用默认模版)
    *   [DatasetBuilder](#datasetbuilde)
    *   [my_dataset.py](#my-datasetpy)
*   [指定 `DatasetInfo`](#指定-datasetinfo)
    *   [`FeatureConnector`s](#featureconnectors)
*   [下载和提取源数据](#下载和提取源数据)
    *   [手动下载和提取](#手动下载和提取)
*   [指定数据集分割](#指定数据集分割)
*   [编写样本生成器](#编写样本生成器)
    *   [文件存取及 `tf.io.gfile`](#文件存取及-tfiogfile)
    *   [额外的依赖](#额外的依赖)
    *   [数据损坏](#数据损坏)
    *   [数据不一致](#数据不一致)
*   [数据集配置](#数据集配置)
    *   [使用 `BuilderConfig` 进行重型配置](#使用-builderconfig-进行重型配置)
    *   [使用构造函数参数进行轻型配置](#使用构造函数参数进行轻型配置)
*   [创建您自己的 `FeatureConnector`](#创建您自己的-featureconnector)
*   [添加数据集到 `tensorflow/datasets`](#添加数据集到-tensorflowdatasets)
    *   [1. 为注册添加导入](#1-为注册添加导入)
    *   [2. 本地运行 `download_and_prepare`](#2-本地运行-download_and_prepare)
    *   [3. 仔细检查引文](#3-仔细检查引文)
    *   [4. 添加测试](#4-添加测试)
    *   [5. 检查您的代码样式](#5-检查您的代码样式)
    *   [6. 添加发行说明](#6-添加发行说明)
    *   [7. 提交以供审阅!](#7-提交以供审阅)
*   [在 TFDS 之外定义数据集](#在-tfds-之外定义数据集)
*   [大型数据集和分布式生成](#大型数据集和分布式生成)
*   [测试 `MyDataset`](#测试-mydataset)

## 总览

数据集以各种格式分布于各个角落，它们并不总是以可以立即送入机器学习流水线的格式进行存储。

TFDS 提供了一种将所有数据集转换成一种标准格式的方法，进行必要的预处理，以使数据集为机器学习流水线做好准备，并通过 `tf.data` 提供了一种标准的输入流水线。

为了实现这一点，每个数据集都实现了 `DatasetBuilder` 的子类，该子类指定了：

* 数据从何处来（例如它的 URL）；
* 数据集看起来像什么（例如它的特征）；
* 数据应该如何划分（例如 `训练` 与 `测试`）；
* 以及数据集中的各条记录（records）。

首次使用数据集时，将下载，准备好数据集，并以标准格式写入磁盘。后续访问将直接从这些预处理后的文件中读取。

**Note**: 目前我们不支持在一台机器上需要超过 1 天才能生成的数据集。请参看[下面有关大型数据集的部分](#大型数据集和分布式生成)。

## 编写 `my_dataset.py`

### 使用默认模版

如果您想要[为我们的资源库做贡献](https://github.com/tensorflow/datasets/blob/master/CONTRIBUTING.md)并添加新数据集，以下脚本将通过生成所需的 python 文件等方式帮助您入门。要使用它们，请克隆 `tfds` 资源库并运行以下命令：

```
python tensorflow_datasets/scripts/create_new_dataset.py \
  --dataset my_dataset \
  --type image  # text, audio, translation,...
```


然后在生成的文件中搜索 `TODO(my_dataset)` 去做修改。

### `DatasetBuilder`

每个数据集都被定义为 
[`tfds.core.DatasetBuilder`](api_docs/python/tfds/core/DatasetBuilder.md) 的一个子类，实现了以下的方法：

* `_info`：建立描述数据集的 [`DatasetInfo`](api_docs/python/tfds/core/DatasetInfo.md) 对象
* `_download_and_prepare`：将源数据下载并序列化到磁盘
* `_as_dataset`：从序列化数据中产生一个 `tf.data.Dataset`

大多数数据集是 [`tfds.core.GeneratorBasedBuilder`](api_docs/python/tfds/core/GeneratorBasedBuilder.md) 的子类，该类是 `tfds.core.DatasetBuilder` 的子类，可简化定义数据集。它适用于能在单个机器上生成的数据集。该类的子类实现了：

* `_info`: 建立描述数据集的 [`DatasetInfo`](api_docs/python/tfds/core/DatasetInfo.md) 对象
* `_split_generators`: 下载源数据并定义数据分割
* `_generate_examples`: 从源数据中产生 `(key, example)` 元组

本指南将使用 `GeneratorBasedBuilder`。

### `my_dataset.py`

`my_dataset.py` 首先看起来像这样：

```python
import tensorflow_datasets.public_api as tfds

class MyDataset(tfds.core.GeneratorBasedBuilder):
  """对我的数据集的简短描述。"""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # 指定 tfds.core.DatasetInfo 对象
    pass # TODO

  def _split_generators(self, dl_manager):
    # 下载数据并定义划分
    # dl_manager 是一个 tfds.download.DownloadManager，其能够被用于
    # 下载并提取 URLs
    pass  # TODO

  def _generate_examples(self):
    # 从数据集中产生样本
    yield 'key', {}
```

如果您想要遵循测试驱动的开发工作流程，这可以帮助您更快迭代，那么请先跳到下面的[测试说明](#测试-mydataset)，添加测试，然后回到这里。

有关版本说明，请阅读[数据集版本](datasets_versioning.md)。

## 指定 `DatasetInfo`

[`DatasetInfo`](api_docs/python/tfds/core/DatasetInfo.md) 描述了数据集。

```python
class MyDataset(tfds.core.GeneratorBasedBuilder):

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # 这是将在数据集页面上显示的描述。
        description=("This is the dataset for xxx. It contains yyy. The "
                     "images are kept at their original dimensions."),
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            "image_description": tfds.features.Text(),
            "image": tfds.features.Image(),
            # 在这里，标签可以是5个不同的值。
            "label": tfds.features.ClassLabel(num_classes=5),
        }),
        # 如果特征中有一个通用的（输入，目标）元组，
        # 请在此处指定它们。它们将会在
        # builder.as_dataset 中的 
        # as_supervised=True 时被使用。
        supervised_keys=("image", "label"),
        # 用于文档的数据集主页
        homepage="https://dataset-homepage.org",
        # 数据集的 Bibtex 引用
        citation=r"""@article{my-awesome-dataset-2020,
                              author = {Smith, John},"}""",
    )
```

### `FeatureConnector`s

每种特征都在 `DatasetInfo` 中指定为 [`tfds.features.FeatureConnector`](api_docs/python/tfds/features.md)。
`FeatureConnector`记录了每种特征，提供了形状和类型检查，并对串行写入及读取磁盘进行了抽象。有许多的特征种类已经被定义，您也可以[添加一个新的特征](#创建您自己的-featureconnector)。

如果您已经实现了测试工具，那么 `test_info` 现在应该通过了测试。

## 下载和提取源数据

大多数数据集都需要从网络下载数据。所有下载和提取必须经过
[`tfds.download.DownloadManager`](api_docs/python/tfds/download/DownloadManager.md)。
`DownloadManager` 当前支持提取 `.zip`， `.gz` 和 `.tar` 文件。

例如，使用 `download_and_extract` 可以下载和提取 URLs：

```python
def _split_generators(self, dl_manager):
  # 相当于 dl_manager.extract(dl_manager.download(urls))
  dl_paths = dl_manager.download_and_extract({
      'foo': 'https://example.com/foo.zip',
      'bar': 'https://example.com/bar.zip',
  })
  dl_paths['foo'], dl_paths['bar']
```

### 手动下载和提取

对于不能自动下载的源数据（例如，下载可能需要登陆），用户将手动下载源数据并将其放在 `manual_dir` 中，您可以通过 `dl_manager.manual_dir` 访问该文件夹（默认为 `~/tensorflow_datasets/manual/my_dataset`）。

## 指定数据集分割

如果数据集带有预定义的分割（例如，MNSIT 有训练和测试分割），那么就在 `DatasetBuilder` 中保留那些分割。如果这是您自己的数据，并且您可以决定您自己的分割，那么我们建议使用 `(训练：80%，验证：10%，测试：10%)` 的分割。用户总是可以通过 [`tfds.Split.subsplit`](splits.md#subsplit) 得到子分割。

```python
  def _split_generators(self, dl_manager):
    # 下载源数据
    extracted_path = dl_manager.download_and_extract(...)

    # 指定分割
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "images_dir_path": os.path.join(extracted_path, "train"),
                "labels": os.path.join(extracted_path, "train_labels.csv"),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "images_dir_path": os.path.join(extracted_path, "test"),
                "labels": os.path.join(extracted_path, "test_labels.csv"),
            },
        ),
    ]
```

`SplitGenerator` 描述了一个分割应该如何生成。`gen_kwargs` 将作为关键字参数传递到 `_generate_examples`，我们将在后续定义。

## 编写样本生成器

`_generate_examples` 从源数据的每种分割中生成样本。对于上述定义的有着 `gen_kwargs` 的 `TRAIN` 分割，`_generate_examples` 将被调用成：

```python
builder._generate_examples(
    images_dir_path="{extracted_path}/train",
    labels="{extracted_path}/train_labels.csv",
)
```

该方法通常将读取源数据集加工件（如 CSV 文件）并产生（键值，特征字典）元组，对应于在 `DatasetInfo` 中指定的特征。

```python
def _generate_examples(self, images_dir_path, labels):
  # 从源文件中读取输入数据
  for image_file in tf.io.gfile.listdir(images_dir_path):
    ...
  with tf.io.gfile.GFile(labels) as f:
    ...

  # 并以特征字典的方式生成样本
  for image_id, description, label in data:
    yield image_id, {
        "image_description": description,
        "image": "%s/%s.jpeg" % (images_dir_path, image_id),
        "label": label,
    }
```

`DatasetInfo.features.encode_example` 将把这些字典编码成适于写到磁盘中的格式（当前我们使用 `tf.train.Example` 协议缓冲区（protocol buffers）格式）。例如，`tfds.features.Image` 将自动复制出传递的图像文件的 JPEG 内容。

键值（此处：`image_id`）应该唯一地标识记录。它用于全局数据集顺序随机化。如果生成的两条记录使用了相同的键值，那么在准备数据集期间将会引发异常。

如果您已经实现了测试工具，那么您的构建器测试现在应该通过了。

### 文件存取及 `tf.io.gfile`

为了支持云存储系统，对所有文件系统的访问，请使用 `tf.io.gfile` 或者其他 TensorFlow 文件 APIs（例如，`tf.python_io`）。避免使用 Python 内置的文件操作（如 `open`，`os.rename`，`gzip` 等）。

### 额外的依赖

一些数据集在数据生成过程中需要额外的 Python 依赖。例如，SVHN 数据集使用 `scipy` 来导入一些数据。为了保证 `tensorflow-datasets` 包较小，并允许用户仅在需要时才安装额外依赖，请使用 `tfds.core.lazy_imports`。

要使用 `lazy_imports`：

*   将数据集的条目添加到 [`setup.py`](https://github.com/tensorflow/datasets/tree/master/setup.py) 里的 `DATASET_EXTRAS` 中。这样一来，用户就可以执行诸如 `pip install 'tensorflow-datasets[svhn]'` 来安装额外的依赖。
*   将要导入的条目添加到 [`LazyImporter`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/lazy_imports_lib.py) 和 [`LazyImportsTest`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/lazy_imports_lib_test.py)。
*   使用 `tfds.core.lazy_imports` 在您的 `DatasetBuilder` 中访问依赖（例如，`tfds.core.lazy_imports.scipy`）。


### 数据损坏

一些数据集不是完全干净，包含了一些损坏的数据（例如，图像在 JPEG 文件中，但有些是无效的 JPEG）。应该跳过这些样本，但在数据集描述中要注明删除了多少条样本及其原因。

### 数据不一致

一些数据集为单个记录或特征，提供了可能存在或者可能不再存在的一组 URLs（例如，网上各种图片的 URLs）。这些数据集很难正确版本化，因为源数据不稳定（URLs 来来去去）。

如果数据集本来就不稳定（也就是说，如果长时间运行多次可能不会产生相同的数据），通过向 `DatasetBuilder` 添加一个类常量，将数据集标记为不稳定：`UNSTABLE = "<为什么这个数据集不稳定>"`。例如，`UNSTABLE = "来源于网络的下载 URLs。"`

## 数据集配置

某些数据集可能具有应公开的变体，或有关如何预处理数据的选项。这些配置可以分为两类：

1. “重型”：影响数据如何写入磁盘的配置。我们将其称为“重型”配置。
2. “轻型”：影响运行时预处理的配置（即可以在 `tf.data` 输入流水线中完成的配置）。我们将其称为“轻型”配置。

### 使用 `BuilderConfig` 进行重型配置

重型配置影响数据如何写入磁盘。例如，对于文本数据集，不同的 `TextEncoder` 和词汇表影响写入磁盘的单词 id。

重型配置通过 [`tfds.core.BuilderConfig`](https://tensorflow.google.cn/datasets/api_docs/python/tfds/core/BuilderConfig.md) 完成：

1. 将配置对象定义为 `tfds.core.BuilderConfig` 的子类。例如，`MyDatasetConfig`。
2. 在 `MyDataset` 中定义 `BUILDER_CONFIGS` 类成员，该成员列出了数据集公开的 `MyDatasetConfig`。
3. 使用 `MyDataset` 中的 `self.builder_config` 来配置数据生成。这可能包括在 `_info()` 中设置不同的值，或更改下载数据的访问权限。

有 `BuilderConfig` 的数据集，对每种配置都有一个名称和版本号与之对应，因此数据集特定变体的完全合格的名称为`数据集名称/配置名称`（例如，`"lm1b/bytes"`）。配置默认为 `BUILDER_CONFIGS` 中的第一个（例如，"`lm1b`" 默认为 `"lm1b/plain_text"`）。

有关使用 `BuilderConfig` 的数据集的示例，请参阅 [`Lm1b`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/lm1b.py)。

### 使用构造函数参数进行轻型配置

对于可以在 `tf.data` 输入流水线中即时更改的情况，可在 `MyDataset` 构造函数中添加关键字参数，将值存储在成员变量中，并在后续使用它们。例如，重载 `_as_dataset()`，调用 `super()` 得到 `tf.data.Dataset`，然后依据成员变量进行额外的转换。

## 创建您自己的 `FeatureConnector`

请注意，大多数数据集[当前一系列的 `tfds.features.FeatureConnector`](api_docs/python/tfds/features.md)已足够，但有时可能需要定义一个新的。

Note: 如果您需要一个新的不在默认设置中出现的 `FeatureConnector`，并计划将其提交到 `tensorflow/datasets`，请根据您的建议在 GitHub 上开启一个
[新问题](https://github.com/tensorflow/datasets/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=)。

`DatasetInfo` 中的 [`tfds.features.FeatureConnector`](api_docs/python/tfds/features/FeatureConnector.md) 对应着 `tf.data.Dataset` 对象返回的元素。例如：

```
tfds.DatasetInfo(features=tfds.features.FeatureDict({
    'input': tfds.features.Image(),
    'output': tfds.features.Text(encoder=tfds.text.ByteEncoder()),
    'metadata': {
        'description': tfds.features.Text(),
        'img_id': tf.int32,
    },
}))
```

`tf.data.Dataset` 对象中的项看起来像：

```
{
    'input': tf.Tensor(shape=(None, None, 3), dtype=tf.uint8),
    'output': tf.Tensor(shape=(None,), dtype=tf.int32),  # 词 id 序列
    'metadata': {
        'description': tf.Tensor(shape=(), dtype=tf.string),
        'img_id': tf.Tensor(shape=(), dtype=tf.int32),
    },
}
```

`tfds.features.FeatureConnector` 对象，将特征如何在磁盘中编码，从特征如何呈现给用户中抽象了出来。下图显示了数据集的抽象层，以及从原始数据集文件到 `tf.data.Dataset` 对象的转换。

<p align="center">
  <img src="dataset_layers.png" alt="DatasetBuilder abstraction layers" width="700"/>
</p>

要创建自己的特征连接器（feature connector），请继承 `tfds.features.FeatureConnector` 并实现抽象方法：

*   `get_tensor_info()`：指定 `tf.data.Dataset` 返回的张量形状/类型。
*   `encode_example(input_data)`：定义了如何将在生成器 `_generate_examples()` 中给定的数据编码成兼容 `tf.train.Example` 的数据。
*   `decode_example`：定义了如何将从 `tf.train.Example` 读取的张量中的数据解码成 `tf.data.Dataset` 返回的用户张量。
*   （可选）`get_serialized_info()`：如果 `get_tensor_info()` 返回的信息与实际将数据写入磁盘的方式不同，那么您需要重载 `get_serialized_info()` 以匹配 `tf.train.Example` 的规范。

1.  如果您的连接器仅含一个数值，那么 `get_tensor_info`、`encode_example` 和 `decode_example` 方法能直接返回单个数值（不需要将数值包装在字典中）。

2.  如果您的连接器是多个子特征的容器，那么最简单的方式是继承 `tfds.features.FeaturesDict` 并使用 `super()` 方法自动编码/解码子连接器。

请参看 [`tfds.features.FeatureConnector`](api_docs/python/tfds/features/FeatureConnector.md) 了解更多详细信息，参看 [特征软件包](api_docs/python/tfds/features.md) 了解更多示例。

## 添加数据集到 `tensorflow/datasets`

如果您想与社区共享您的工作，则可以将您的数据实现录入到 `tensorflow/datasets`中。感谢您的贡献！

在发送拉取请求（pull request）之前，请遵循以下最后几个步骤：

### 1. 为注册添加导入

所有 `tfds.core.DatasetBuilder` 的子类在它们的模块被导入时，会自动注册，这样它们可以通过 `tfds.builder` 和 `tfds.load` 进行访问。

如果您为 `tensorflow/datasets` 贡献数据集，则请在其子文件夹的 `__init__.py`（如 [`image/__init__.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/__init__.py)）添加模块导入。

### 2. 本地运行 `download_and_prepare`

如果您为 `tensorflow/datasets` 贡献数据集，则请为数据集添加一个校验和文件。在第一次下载时，`DownloadManager` 将自动将所有下载 URLs 的大小和校验和添加到该文件中。这样可以确保在后续数据生成中，下载的文件符合预期。

```sh
touch tensorflow_datasets/url_checksums/my_new_dataset.txt
```

本地运行 `download_and_prepare` 确保数据生成有效：

```
# 默认的 data_dir 为 ~/tensorflow_datasets
python -m tensorflow_datasets.scripts.download_and_prepare \
  --register_checksums \
  --datasets=my_new_dataset
```

注意 `--register_checksums` 标志只能在开发中使用。

将 `dataset_info.json` 文件中的内容复制到 [GitHub gist](https://gist.github.com/)，并在您的拉取请求中链接至该文件。


### 3. 仔细检查引文

在 `DatasetInfo.citation` 中包含数据集的引文很重要。向社区贡献数据集是一项艰巨而重要的工作，我们希望简化数据集用户引用该工作的过程。

如果数据集的网站有特别要求的引用，请使用该引用（以 BibTex 格式）。

如果论文在 [arXiv](https://arxiv.org/) 上，在 arXiv 找到该论文，并在右侧点击 `bibtex` 链接。

如果论文不在 arXiv上，在 [Google Scholar](https://scholar.google.com) 上找到该篇论文，并点击标题下方的双引号标志，在弹出框中点击 `BibTeX`。

如果没有相关的论文（例如，只有一个网站），您可以使用 [BibTeX 在线编辑器](https://truben.no/latex/bibtex/) 创建一个自定义的 BibTeX 条目（下拉菜单有一个 `Online` 输入类型）。

### 4. 添加测试

TFDS 中的大多数数据集应该有一个单元测试，并且您的审阅人可能会要求您添加一个（如果您还没有的话）。请参阅下方的[测试部分](#测试-mydataset)。

### 5. 检查您的代码样式

除了 TensorFlow 使用 2 个空格而非 4 个空格外，请遵循 [PEP 8 Python 样式指南](https://www.python.org/dev/peps/pep-0008)。请遵守 [Google Python 样式指南](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)。

最重要的是，使用 [`tensorflow_datasets/oss_scripts/lint.sh`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/oss_scripts/lint.sh) 确保您的代码格式正确。例如，检查 `image` 目录：

```sh
./oss_scripts/lint.sh tensorflow_datasets/image
```

参看 [TensorFlow 代码样式指南](https://tensorflow.google.cn/community/contribute/code_style)了解更多信息。

### 6. 添加发行说明

将数据集添加到[发行说明](https://github.com/tensorflow/datasets/tree/master/docs/release_notes.md)。
该发行说明将在下一个发行版中发布。

### 7. 提交以供审阅!

发送拉取请求以供审阅。


## 在 TFDS 之外定义数据集

您可以使用 `tfds` API 在 `tfds` 库之外，定义自己的自定义的数据集。这些说明与上面的内容基本相同，但有一些细微的调整，请参见下文。

### 1. 调整校验和文件夹

为了确保重新分发数据集时的安全性和可重复性，`tfds` 在 [`tensorflow_datasets/url_checksums`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/url_checksums) 中包含了全部数据集下载的 URL 校验和。

您可以在您的代码中调用 `tfds.download.add_checksums_dir('/path/to/checksums_dir')` 注册一个外部的校验和文件夹，这样您的数据集的用户会自动使用您的校验和。

首次创建此校验和文件，您可以使用 `tensorflow_datasets.scripts.download_and_prepare` 脚本并给出 `--register_checksums --checksums_dir=/path/to/checksums_dir` 标志。

### 2. 调整伪造样本文件夹

为了进行测试，您可以通过设定 `tfds.testing.DatasetBuilderTestCase` 中的 `EXAMPLE_DIR` 属性，定义您自己的伪造样本文件夹，而不是使用默认的[伪造样本文件夹](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/testing/test_data/fake_examples)：

```
class MyDatasetTest(tfds.testing.DatasetBuilderTestCase):
  EXAMPLE_DIR = 'path/to/fakedata'`
```

## 大型数据集和分布式生成

一些数据集非常大，以至于需要多台计算机来下载和生成。我们使用 Apache Beam 支持此用例。请阅读 [Beam 数据集指南](beam_datasets.md)以开始使用。

## 测试 `MyDataset`

`tfds.testing.DatasetBuilderTestCase` 是一个基本的 `TestCase`，用于完全测试一个数据集。它使用“伪造样本”作为模拟源数据集结构的测试数据。

测试数据应该放在 `my_dataset` 文件夹下的 [`testing/test_data/fake_examples/`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/testing/test_data/fake_examples/) 中，并且应该在下载和提取时模拟源数据集加工件。它可以手工创建，也可以用一个脚本自动创建（[示例脚本](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/testing/cifar.py)）。

确保在测试数据分割中使用不同的数据，因为如果数据集分割重叠，则测试将失败。

**测试数据不应包含任何受版权保护的材料**。如有疑问，请勿使用原始数据集中的材料创建数据。

```python
import tensorflow as tf
from tensorflow_datasets import my_dataset
import tensorflow_datasets.testing as tfds_test


class MyDatasetTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = my_dataset.MyDataset
  SPLITS = {  # 伪造样本中每种分割的期望样本量。
      "train": 12,
      "test": 12,
  }
  # 如果数据集 `download_and_extract` 有多种来源：
  DL_EXTRACT_RESULT = {
      "name1": "path/to/file1",  # 相对于 fake_examples/my_dataset 文件夹的路径。
      "name2": "file2",
  }

if __name__ == "__main__":
  tfds_test.test_main()
```

您可以在继续实现 `MyDataset` 的同时运行测试。
如果您完成了上述所有步骤，则应该可以通过测试。
