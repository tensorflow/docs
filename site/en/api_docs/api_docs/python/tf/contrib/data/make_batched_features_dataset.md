

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.make_batched_features_dataset

``` python
tf.contrib.data.make_batched_features_dataset(
    file_pattern,
    batch_size,
    features,
    reader=tf.data.TFRecordDataset,
    reader_args=None,
    num_epochs=None,
    shuffle=True,
    shuffle_buffer_size=10000,
    shuffle_seed=None,
    prefetch_buffer_size=1,
    reader_num_threads=1,
    parser_num_threads=2,
    sloppy_ordering=False,
    drop_final_batch=False
)
```



Defined in [`tensorflow/contrib/data/python/ops/readers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/data/python/ops/readers.py).

Returns a `Dataset` of feature dictionaries from `Example` protos.

Example:

```
serialized_examples = [
  features {
    feature { key: "age" value { int64_list { value: [ 0 ] } } }
    feature { key: "gender" value { bytes_list { value: [ "f" ] } } }
    feature { key: "kws" value { bytes_list { value: [ "code", "art" ] } } }
  },
  features {
    feature { key: "age" value { int64_list { value: [] } } }
    feature { key: "gender" value { bytes_list { value: [ "f" ] } } }
    feature { key: "kws" value { bytes_list { value: [ "sports" ] } } }
  }
]
```

We can use arguments:

```
features: {
  "age": FixedLenFeature([], dtype=tf.int64, default_value=-1),
  "gender": FixedLenFeature([], dtype=tf.string),
  "kws": VarLenFeature(dtype=tf.string),
}
```

And the expected output is:

```python
{
  "age": [[0], [-1]],
  "gender": [["f"], ["f"]],
  "kws": SparseTensor(
    indices=[[0, 0], [0, 1], [1, 0]],
    values=["code", "art", "sports"]
    dense_shape=[2, 2]),
}
```

#### Args:

* <b>`file_pattern`</b>: List of files or patterns of file paths containing
    `Example` records. See <a href="../../../tf/gfile/Glob"><code>tf.gfile.Glob</code></a> for pattern rules.
* <b>`batch_size`</b>: An int representing the number of records to combine
    in a single batch.
* <b>`features`</b>: A `dict` mapping feature keys to `FixedLenFeature` or
    `VarLenFeature` values. See <a href="../../../tf/parse_example"><code>tf.parse_example</code></a>.
* <b>`reader`</b>: A function or class that can be
    called with a `filenames` tensor and (optional) `reader_args` and returns
    a `Dataset` of `Example` tensors. Defaults to <a href="../../../tf/data/TFRecordDataset"><code>tf.data.TFRecordDataset</code></a>.
* <b>`reader_args`</b>: Additional arguments to pass to the reader class.
* <b>`num_epochs`</b>: Integer specifying the number of times to read through the
    dataset. If None, cycles through the dataset forever. Defaults to `None`.
* <b>`shuffle`</b>: A boolean, indicates whether the input should be shuffled. Defaults
    to `True`.
* <b>`shuffle_buffer_size`</b>: Buffer size of the ShuffleDataset. A large capacity
    ensures better shuffling but would increase memory usage and startup time.
* <b>`shuffle_seed`</b>: Randomization seed to use for shuffling.
* <b>`prefetch_buffer_size`</b>: Number of feature batches to prefetch in order to
    improve performance. Recommended value is the number of batches consumed
    per training step (default is 1).
* <b>`reader_num_threads`</b>: Number of threads used to read `Example` records. If >1,
    the results will be interleaved.
* <b>`parser_num_threads`</b>: Number of threads to use for parsing `Example` tensors
    into a dictionary of `Feature` tensors.
* <b>`sloppy_ordering`</b>: If `True`, reading performance will be improved at
    the cost of non-deterministic ordering. If `False`, the order of elements
    produced is deterministic prior to shuffling (elements are still
    randomized if `shuffle=True`. Note that if the seed is set, then order
    of elements after shuffling is deterministic). Defaults to `False`.
* <b>`drop_final_batch`</b>: If `True`, and the batch size does not evenly divide the
    input dataset size, the final smaller batch will be dropped. Defaults to
    `False`.


#### Returns:

A dataset of `dict` elements. Each `dict` maps feature keys to
`Tensor` or `SparseTensor` objects.