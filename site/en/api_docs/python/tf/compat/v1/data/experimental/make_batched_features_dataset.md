page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.data.experimental.make_batched_features_dataset


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/experimental/ops/readers.py#L890-L910">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>





``` python
tf.compat.v1.data.experimental.make_batched_features_dataset(
    file_pattern,
    batch_size,
    features,
    reader=tf.compat.v1.data.TFRecordDataset,
    label_key=None,
    reader_args=None,
    num_epochs=None,
    shuffle=True,
    shuffle_buffer_size=10000,
    shuffle_seed=None,
    prefetch_buffer_size=dataset_ops.AUTOTUNE,
    reader_num_threads=1,
    parser_num_threads=2,
    sloppy_ordering=False,
    drop_final_batch=False
)
```



<!-- Placeholder for "Used in" -->
