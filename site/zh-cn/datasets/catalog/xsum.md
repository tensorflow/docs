# `xsum`

Extreme Summarization (XSum) Dataset.

数据集中包含两部分特征: - document: 作为输入的新闻报道。 - summary: 输入的新闻报道所对应的一句话总结。

该数据需要手动下载及提取，参照链接
https://github.com/EdinburghNLP/XSum/blob/master/XSum-Dataset/README.md。
压缩'xsum-extracts-from-downloads'文件夹并命名为
'xsum-extracts-from-downloads.tar.gz'，之后放置于用于下载的文件夹中。

*   链接:
    [https://github.com/EdinburghNLP/XSum/tree/master/XSum-Dataset](https://github.com/EdinburghNLP/XSum/tree/master/XSum-Dataset)
*   `DatasetBuilder`:
    [`tfds.summarization.xsum.Xsum`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/xsum.py)
*   版本: `v1.1.0`
*   版本历史:

    *   **`1.1.0`** (默认版本):
    *   `1.0.0`: 数据未清洗的版本。

*   大小: `2.59 MiB`

## 特征
```python
FeaturesDict({
    'document': Text(shape=(), dtype=tf.string),
    'summary': Text(shape=(), dtype=tf.string),
})
```

## 统计数据

样本类别    | 样本数量
:--------- | -------:
全部        | 226,183
训练集      | 203,577
验证集      | 11,305
测试集      | 11,301

## 主页

*   [https://github.com/EdinburghNLP/XSum/tree/master/XSum-Dataset](https://github.com/EdinburghNLP/XSum/tree/master/XSum-Dataset)

## 控制键 (用于 `as_supervised=True`)
`(u'document', u'summary')`

## 参考
```
@article{Narayan2018DontGM,
  title={Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization},
  author={Shashi Narayan and Shay B. Cohen and Mirella Lapata},
  journal={ArXiv},
  year={2018},
  volume={abs/1808.08745}
}
```

--------------------------------------------------------------------------------