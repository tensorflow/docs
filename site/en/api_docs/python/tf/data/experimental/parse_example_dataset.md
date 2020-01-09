page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.parse_example_dataset


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/experimental/ops/parsing_ops.py#L101-L146">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A transformation that parses `Example` protos into a `dict` of tensors.

### Aliases:

* `tf.compat.v1.data.experimental.parse_example_dataset`
* `tf.compat.v2.data.experimental.parse_example_dataset`


``` python
tf.data.experimental.parse_example_dataset(
    features,
    num_parallel_calls=1
)
```



<!-- Placeholder for "Used in" -->

Parses a number of serialized `Example` protos given in `serialized`. We refer
to `serialized` as a batch with `batch_size` many entries of individual
`Example` protos.

This op parses serialized examples into a dictionary mapping keys to `Tensor`
and `SparseTensor` objects. `features` is a dict from keys to `VarLenFeature`,
`SparseFeature`, and `FixedLenFeature` objects. Each `VarLenFeature`
and `SparseFeature` is mapped to a `SparseTensor`, and each
`FixedLenFeature` is mapped to a `Tensor`. See <a href="../../../tf/io/parse_example"><code>tf.io.parse_example</code></a> for more
details about feature dictionaries.

#### Args:


* <b>`features`</b>: A `dict` mapping feature keys to `FixedLenFeature`,
  `VarLenFeature`, and `SparseFeature` values.
* <b>`num_parallel_calls`</b>: (Optional.) A <a href="../../../tf#int32"><code>tf.int32</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>,
   representing the number of parsing processes to call in parallel.


#### Returns:

A dataset transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.



#### Raises:


* <b>`ValueError`</b>: if features argument is None.
