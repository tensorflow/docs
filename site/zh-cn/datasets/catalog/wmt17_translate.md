# `wmt17_translate`

注意：需要手动下载，详见如下教程。

* **描述**

该项目使用的数据集来自statmt.org。

在不同的年份，我们发布了不同的版本，数据集来源并不惟一。主项目`wmt_translate`允许使用者通过自定义`tfds.translate.wmt.WmtConfig`自行配置 data/language pair。

```
config = tfds.translate.wmt.WmtConfig(
    version="0.0.1",
    language_pair=("fr", "de"),
    subsets={
        tfds.分块.TRAIN: ["commoncrawl_frde"],
        tfds.分块.VALIDATION: ["euelections_dev2019"],
    },
)
builder = tfds.builder("wmt_translate", config=config)
```

* **主页**：

[http://www.statmt.org/wmt17/translation-task.html](http://www.statmt.org/wmt17/translation-task.html)

* **源代码**：

[`tfds.translate.wmt17.Wmt17Translate`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/wmt17.py)

* **版本**：
* **`1.0.0`** (默认)：没有发布文档。
    
* **数据集大小**：`未知`

*  **手动下载指南**：该数据集需要开发者手动将数据源导入 `download_config.manual_dir` （默认为 `~/tensorflow_datasets/manual/` ）：
    wmt 的部分配置如下，需要手动下载。
    开发者需在 `wmt.py` 中查看需要  下载的文件名和具体路径。

* **Auto-cached**([documentation](https://www.tensorflow.google.cn/datasets/performances#auto-caching))：否

* **引用**:

```
@InProceedings{bojar-EtAl:2017:WMT1,
  author    = {Bojar, Ond{r}ej  and  Chatterjee, Rajen  and  Federmann, Christian  and  Graham, Yvette  and  Haddow, Barry  and  Huang, Shujian  and  Huck, Matthias  and  Koehn, Philipp  and  Liu, Qun  and  Logacheva, Varvara  and  Monz, Christof  and  Negri, Matteo  and  Post, Matt  and  Rubino, Raphael  and  Specia, Lucia  and  Turchi, Marco},
  title     = {Findings of the 2017 Conference on Machine Translation (WMT17)},
  booktitle = {Proceedings of the Second Conference on Machine Translation, Volume 2: Shared Task Papers},
  month     = {September},
  year      = {2017},
  address   = {Copenhagen, Denmark},
  publisher = {Association for Computational Linguistics},
  pages     = {169--214},
  url       = {http://www.aclweb.org/anthology/W17-4717}
}
```

*  **可视化
([tfds.show_examples](https://www.tensorflow.google.cn/datasets/api_docs/python/tfds/visualization/show_examples))**：
    不支持。

## wmt17_translate/cs-en （默认配置）

*   **配置说明**: WMT 2017 cs-en 翻译任务数据集。

*   **下载大小**: `1.66 GiB`
*   **数据分块**:

分块        | 样本
:----------- | ---------:
'test'       | 3,005
'train'      | 15,851,649
'validation' | 2,999

*   **Features**：

```python
Translation({
    'cs': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```
*   **Supervised keys** （见
    [`as_supervised` doc](https://www.tensorflow.google.cn/datasets/api_docs/python/tfds/load#args)）：
    `('cs', 'en')`


## wmt17_translate/fi-en

*   **配置说明**: WMT 2017 fi-en translation task dataset.

*   **下载大小**: `414.10 MiB`
*   **数据分块**:

分块        | Examples
:----------- | --------:
'test'       | 6,004
'train'      | 2,656,542
'validation' | 6,000

*   **Features**:

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fi': Text(shape=(), dtype=tf.string),
})
```
*   **Supervised keys** （见
    [`as_supervised` doc](https://www.tensorflow.google.cn/datasets/api_docs/python/tfds/load#args)）：
    `('fi', 'en')`

## wmt17_translate/lv-en

*   **配置说明**: WMT 2017 lv-en translation task dataset.

*   **下载大小**: `161.69 MiB`
*   **数据分块**:

分块        | Examples
:----------- | --------:
'test'       | 2,001
'train'      | 3,567,528
'validation' | 2,003

*   **Features**:

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'lv': Text(shape=(), dtype=tf.string),
})
```
*   **Supervised keys** （见
    [`as_supervised` doc](https://www.tensorflow.google.cn/datasets/api_docs/python/tfds/load#args)）：
    `('lv', 'en')`

## wmt17_translate/ru-en

*   **配置说明**: WMT 2017 ru-en translation task dataset.

*   **下载大小**: `3.34 GiB`
*   **数据分块**:

分块        | Examples
:----------- | ---------:
'test'       | 3,001
'train'      | 25,782,720
'validation' | 2,998

*   **Features**:

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```
*   **Supervised keys** （见
    [`as_supervised` doc](https://www.tensorflow.google.cn/datasets/api_docs/python/tfds/load#args)）：
    `('ru', 'en')`

## wmt17_translate/tr-en

*   **配置说明**: WMT 2017 tr-en translation task dataset.

*   **下载大小**: `59.32 MiB`
*   **数据分块**:

分块        | Examples
:----------- | -------:
'test'       | 3,007
'train'      | 205,756
'validation' | 3,000

*   **Features**:

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'tr': Text(shape=(), dtype=tf.string),
})
```
*   **Supervised keys** （见
    [`as_supervised` doc](https://www.tensorflow.google.cn/datasets/api_docs/python/tfds/load#args)）：
    `('tr', 'en')`

## wmt17_translate/zh-en

*   **配置说明**: WMT 2017 zh-en translation task dataset.

*   **下载大小**: `2.16 GiB`
*   **数据分块**:

分块        | Examples
:----------- | ---------:
'test'       | 2,001
'train'      | 25,136,609
'validation' | 2,002

*   **Features**:

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'zh': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** （见
    [`as_supervised` doc](https://www.tensorflow.google.cn/datasets/api_docs/python/tfds/load#args)）：
    `('zh', 'en')`

