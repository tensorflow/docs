page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.constant


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/constant_op.py#L164-L227">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a constant tensor.

### Aliases:

* `tf.compat.v2.constant`


``` python
tf.constant(
    value,
    dtype=None,
    shape=None,
    name='Const'
)
```



### Used in the guide:

* [Better performance with tf.function and AutoGraph](https://www.tensorflow.org/guide/function)
* [Eager execution](https://www.tensorflow.org/guide/eager)
* [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)
* [Use a GPU](https://www.tensorflow.org/guide/gpu)
* [Using the SavedModel format](https://www.tensorflow.org/guide/saved_model)

### Used in the tutorials:

* [Automatic differentiation and gradient tape](https://www.tensorflow.org/tutorials/customization/autodiff)
* [Better performance with tf.function](https://www.tensorflow.org/tutorials/customization/performance)
* [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)
* [Load a pandas.DataFrame](https://www.tensorflow.org/tutorials/load_data/pandas_dataframe)
* [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)
* [TFRecord and tf.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord)
* [Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer)
* [Unicode strings](https://www.tensorflow.org/tutorials/load_data/unicode)



The resulting tensor is populated with values of type `dtype`, as
specified by arguments `value` and (optionally) `shape` (see examples
below).

The argument `value` can be a constant value, or a list of values of type
`dtype`. If `value` is a list, then the length of the list must be less
than or equal to the number of elements implied by the `shape` argument (if
specified). In the case where the list length is less than the number of
elements specified by `shape`, the last element in the list will be used
to fill the remaining entries.

The argument `shape` is optional. If present, it specifies the dimensions of
the resulting tensor. If not present, the shape of `value` is used.

If the argument `dtype` is not specified, then the type is inferred from
the type of `value`.

#### For example:



```python
# Constant 1-D Tensor populated with value list.
tensor = tf.constant([1, 2, 3, 4, 5, 6]) => [1 2 3 4 5 6]

# Constant 1-D Tensor populated with value list.
tensor = tf.constant([1, 2, 3, 4, 5, 6], shape=(2,3))
     => [[1 2 3], [4 5 6]]

# Constant 2-D tensor populated with scalar value -1.
tensor = tf.constant(-1.0, shape=[2, 3]) => [[-1. -1. -1.]
                                             [-1. -1. -1.]]
```

<a href="../tf/constant"><code>tf.constant</code></a> differs from <a href="../tf/fill"><code>tf.fill</code></a> in a few ways:

*   <a href="../tf/constant"><code>tf.constant</code></a> supports arbitrary constants, not just uniform scalar
    Tensors like <a href="../tf/fill"><code>tf.fill</code></a>.
*   <a href="../tf/constant"><code>tf.constant</code></a> creates a `Const` node in the computation graph with the
    exact value at graph construction time. On the other hand, <a href="../tf/fill"><code>tf.fill</code></a>
    creates an Op in the graph that is expanded at runtime.
*   Because <a href="../tf/constant"><code>tf.constant</code></a> only embeds constant values in the graph, it does
    not support dynamic shapes based on other runtime Tensors, whereas
    <a href="../tf/fill"><code>tf.fill</code></a> does.

#### Args:


* <b>`value`</b>:          A constant value (or list) of output type `dtype`.

* <b>`dtype`</b>:          The type of the elements of the resulting tensor.

* <b>`shape`</b>:          Optional dimensions of resulting tensor.

* <b>`name`</b>:           Optional name for the tensor.


#### Returns:

A Constant Tensor.



#### Raises:


* <b>`TypeError`</b>: if shape is incorrectly specified or unsupported.
