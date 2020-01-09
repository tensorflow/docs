page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.repeat


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L4893-L4927">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Repeat elements of `input`

### Aliases:

* <a href="/api_docs/python/tf/repeat"><code>tf.compat.v1.repeat</code></a>
* <a href="/api_docs/python/tf/repeat"><code>tf.compat.v2.repeat</code></a>


``` python
tf.repeat(
    input,
    repeats,
    axis=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`input`</b>: An `N`-dimensional Tensor.
* <b>`repeats`</b>: An 1-D `int` Tensor. The number of repetitions for each element.
  repeats is broadcasted to fit the shape of the given axis. `len(repeats)`
  must equal `input.shape[axis]` if axis is not None.
* <b>`axis`</b>: An int. The axis along which to repeat values. By default (axis=None),
  use the flattened input array, and return a flat output array.
* <b>`name`</b>: A name for the operation.


#### Returns:

A Tensor which has the same shape as `input`, except along the given axis.
  If axis is None then the output array is flattened to match the flattened
  input array.

#### Examples:

>     >>> repeat(['a', 'b', 'c'], repeats=[3, 0, 2], axis=0)
>     ['a', 'a', 'a', 'c', 'c']
>     >>> repeat([[1, 2], [3, 4]], repeats=[2, 3], axis=0)
>     [[1, 2], [1, 2], [3, 4], [3, 4], [3, 4]]
>     >>> repeat([[1, 2], [3, 4]], repeats=[2, 3], axis=1)
>     [[1, 1, 2, 2, 2], [3, 3, 4, 4, 4]]
>     >>> repeat(3, repeats=4)
>     [3, 3, 3, 3]
>     >>> repeat([[1,2], [3,4]], repeats=2)
>     [1, 1, 2, 2, 3, 3, 4, 4]
