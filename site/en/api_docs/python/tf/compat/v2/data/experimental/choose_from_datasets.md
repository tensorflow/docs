page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.data.experimental.choose_from_datasets


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/experimental/ops/interleave_ops.py#L234-L274">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a dataset that deterministically chooses elements from `datasets`.

``` python
tf.compat.v2.data.experimental.choose_from_datasets(
    datasets,
    choice_dataset
)
```



<!-- Placeholder for "Used in" -->

For example, given the following datasets:

```python
datasets = [tf.data.Dataset.from_tensors("foo").repeat(),
            tf.data.Dataset.from_tensors("bar").repeat(),
            tf.data.Dataset.from_tensors("baz").repeat()]

# Define a dataset containing `[0, 1, 2, 0, 1, 2, 0, 1, 2]`.
choice_dataset = tf.data.Dataset.range(3).repeat(3)

result = tf.data.experimental.choose_from_datasets(datasets, choice_dataset)
```

The elements of `result` will be:

```
"foo", "bar", "baz", "foo", "bar", "baz", "foo", "bar", "baz"
```

#### Args:


* <b>`datasets`</b>: A list of <a href="../../../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> objects with compatible structure.
* <b>`choice_dataset`</b>: A <a href="../../../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> of scalar <a href="../../../../../tf#int64"><code>tf.int64</code></a> tensors between
  `0` and `len(datasets) - 1`.


#### Returns:

A dataset that interleaves elements from `datasets` according to the values
of `choice_dataset`.



#### Raises:


* <b>`TypeError`</b>: If the `datasets` or `choice_dataset` arguments have the wrong
  type.
