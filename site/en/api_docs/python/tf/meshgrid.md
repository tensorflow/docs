page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.meshgrid


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/meshgrid">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L2871-L2944">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Broadcasts parameters for evaluation on an N-D grid.

### Aliases:

* <a href="/api_docs/python/tf/meshgrid"><code>tf.compat.v1.meshgrid</code></a>
* <a href="/api_docs/python/tf/meshgrid"><code>tf.compat.v2.meshgrid</code></a>


``` python
tf.meshgrid(
    *args,
    **kwargs
)
```



<!-- Placeholder for "Used in" -->

Given N one-dimensional coordinate arrays `*args`, returns a list `outputs`
of N-D coordinate arrays for evaluating expressions on an N-D grid.

#### Notes:



`meshgrid` supports cartesian ('xy') and matrix ('ij') indexing conventions.
When the `indexing` argument is set to 'xy' (the default), the broadcasting
instructions for the first two dimensions are swapped.

#### Examples:



Calling `X, Y = meshgrid(x, y)` with the tensors

```python
x = [1, 2, 3]
y = [4, 5, 6]
X, Y = tf.meshgrid(x, y)
# X = [[1, 2, 3],
#      [1, 2, 3],
#      [1, 2, 3]]
# Y = [[4, 4, 4],
#      [5, 5, 5],
#      [6, 6, 6]]
```

#### Args:


* <b>`*args`</b>: `Tensor`s with rank 1.
* <b>`**kwargs`</b>:   - indexing: Either 'xy' or 'ij' (optional, default: 'xy').
  - name: A name for the operation (optional).


#### Returns:


* <b>`outputs`</b>: A list of N `Tensor`s with rank N.


#### Raises:


* <b>`TypeError`</b>: When no keyword arguments (kwargs) are passed.
* <b>`ValueError`</b>: When indexing keyword argument is not one of `xy` or `ij`.
