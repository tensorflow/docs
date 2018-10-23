

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.SparseFeature

## Class `SparseFeature`





Defined in [`tensorflow/python/ops/parsing_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/ops/parsing_ops.py).

See the guide: [Inputs and Readers > Converting](../../../api_guides/python/io_ops#Converting)

Configuration for parsing a sparse input feature from an `Example`.

Note, preferably use `VarLenFeature` (possibly in combination with a
`SequenceExample`) in order to parse out `SparseTensor`s instead of
`SparseFeature` due to its simplicity.

Closely mimicking the `SparseTensor` that will be obtained by parsing an
`Example` with a `SparseFeature` config, a `SparseFeature` contains a

* `value_key`: The name of key for a `Feature` in the `Example` whose parsed
  `Tensor` will be the resulting `SparseTensor.values`.

* `index_key`: A list of names - one for each dimension in the resulting
  `SparseTensor` whose `indices[i][dim]` indicating the position of
  the `i`-th value in the `dim` dimension will be equal to the `i`-th value in
  the Feature with key named `index_key[dim]` in the `Example`.

* `size`: A list of ints for the resulting `SparseTensor.dense_shape`.

For example, we can represent the following 2D `SparseTensor`

```python
SparseTensor(indices=[[3, 1], [20, 0]],
             values=[0.5, -1.0]
             dense_shape=[100, 3])
```

with an `Example` input proto

```python
features {
  feature { key: "val" value { float_list { value: [ 0.5, -1.0 ] } } }
  feature { key: "ix0" value { int64_list { value: [ 3, 20 ] } } }
  feature { key: "ix1" value { int64_list { value: [ 1, 0 ] } } }
}
```

and `SparseFeature` config with 2 `index_key`s

```python
SparseFeature(index_key=["ix0", "ix1"],
              value_key="val",
              dtype=tf.float32,
              size=[100, 3])
```

#### Fields:

* <b>`index_key`</b>: A single string name or a list of string names of index features.
    For each key the underlying feature's type must be `int64` and its length
    must always match that of the `value_key` feature.
    To represent `SparseTensor`s with a `dense_shape` of `rank` higher than 1
    a list of length `rank` should be used.
* <b>`value_key`</b>: Name of value feature.  The underlying feature's type must
    be `dtype` and its length must always match that of all the `index_key`s'
    features.
* <b>`dtype`</b>: Data type of the `value_key` feature.
* <b>`size`</b>: A Python int or list thereof specifying the dense shape. Should be a
    list if and only if `index_key` is a list. In that case the list must be
    equal to the length of `index_key`. Each for each entry `i` all values in
    the `index_key`[i] feature must be in `[0, size[i])`.
* <b>`already_sorted`</b>: A Python boolean to specify whether the values in
    `value_key` are already sorted by their index position. If so skip
    sorting. False by default (optional).

## Properties

<h3 id="already_sorted"><code>already_sorted</code></h3>

Alias for field number 4

<h3 id="dtype"><code>dtype</code></h3>

Alias for field number 2

<h3 id="index_key"><code>index_key</code></h3>

Alias for field number 0

<h3 id="size"><code>size</code></h3>

Alias for field number 3

<h3 id="value_key"><code>value_key</code></h3>

Alias for field number 1



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
@staticmethod
__new__(
    cls,
    index_key,
    value_key,
    dtype,
    size,
    already_sorted=False
)
```





