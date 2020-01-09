page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.parse_single_example


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/parsing_ops.py#L1025-L1072">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Parses a single `Example` proto.

### Aliases:

* `tf.compat.v2.io.parse_single_example`


``` python
tf.io.parse_single_example(
    serialized,
    features,
    example_names=None,
    name=None
)
```



### Used in the tutorials:

* [TFRecord and tf.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord)



Similar to `parse_example`, except:

For dense tensors, the returned `Tensor` is identical to the output of
`parse_example`, except there is no batch dimension, the output shape is the
same as the shape given in `dense_shape`.

For `SparseTensor`s, the first (batch) column of the indices matrix is removed
(the indices matrix is a column vector), the values vector is unchanged, and
the first (`batch_size`) entry of the shape vector is removed (it is now a
single element vector).

One might see performance advantages by batching `Example` protos with
`parse_example` instead of using this function directly.

#### Args:


* <b>`serialized`</b>: A scalar string Tensor, a single serialized Example.
  See `_parse_single_example_raw` documentation for more details.
* <b>`features`</b>: A `dict` mapping feature keys to `FixedLenFeature` or
  `VarLenFeature` values.
* <b>`example_names`</b>: (Optional) A scalar string Tensor, the associated name.
  See `_parse_single_example_raw` documentation for more details.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

A `dict` mapping feature keys to `Tensor` and `SparseTensor` values.



#### Raises:


* <b>`ValueError`</b>: if any feature is invalid.
