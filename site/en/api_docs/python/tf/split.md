page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.split


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/array_ops.py#L1642-L1710">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Splits a tensor into sub tensors.

### Aliases:

* `tf.compat.v1.split`
* `tf.compat.v2.split`


``` python
tf.split(
    value,
    num_or_size_splits,
    axis=0,
    num=None,
    name='split'
)
```



### Used in the guide:

* [Masking and padding with Keras](https://www.tensorflow.org/guide/keras/masking_and_padding)

### Used in the tutorials:

* [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)



If `num_or_size_splits` is an integer, then `value` is split along dimension
`axis` into `num_split` smaller tensors. This requires that `num_split` evenly
divides `value.shape[axis]`.

If `num_or_size_splits` is a 1-D Tensor (or list), we call it `size_splits`
and `value` is split into `len(size_splits)` elements. The shape of the `i`-th
element has the same size as the `value` except along dimension `axis` where
the size is `size_splits[i]`.

#### For example:



```python
# 'value' is a tensor with shape [5, 30]
# Split 'value' into 3 tensors with sizes [4, 15, 11] along dimension 1
split0, split1, split2 = tf.split(value, [4, 15, 11], 1)
tf.shape(split0)  # [5, 4]
tf.shape(split1)  # [5, 15]
tf.shape(split2)  # [5, 11]
# Split 'value' into 3 tensors along dimension 1
split0, split1, split2 = tf.split(value, num_or_size_splits=3, axis=1)
tf.shape(split0)  # [5, 10]
```

#### Args:


* <b>`value`</b>: The `Tensor` to split.
* <b>`num_or_size_splits`</b>: Either an integer indicating the number of splits along
  split_dim or a 1-D integer `Tensor` or Python list containing the sizes of
  each output tensor along split_dim. If a scalar then it must evenly divide
  `value.shape[axis]`; otherwise the sum of sizes along the split dimension
  must match that of the `value`.
* <b>`axis`</b>: An integer or scalar `int32` `Tensor`. The dimension along which to
  split. Must be in the range `[-rank(value), rank(value))`. Defaults to 0.
* <b>`num`</b>: Optional, used to specify the number of outputs when it cannot be
  inferred from the shape of `size_splits`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

if `num_or_size_splits` is a scalar returns `num_or_size_splits` `Tensor`
objects; if `num_or_size_splits` is a 1-D Tensor returns
`num_or_size_splits.get_shape[0]` `Tensor` objects resulting from splitting
`value`.



#### Raises:


* <b>`ValueError`</b>: If `num` is unspecified and cannot be inferred.
