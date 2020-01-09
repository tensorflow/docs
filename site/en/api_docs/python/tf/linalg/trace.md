page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.trace


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/linalg/trace">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L2521-L2562">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Compute the trace of a tensor `x`.

### Aliases:

* <a href="/api_docs/python/tf/linalg/trace"><code>tf.compat.v1.linalg.trace</code></a>
* <a href="/api_docs/python/tf/linalg/trace"><code>tf.compat.v1.trace</code></a>
* <a href="/api_docs/python/tf/linalg/trace"><code>tf.compat.v2.linalg.trace</code></a>
* <a href="/api_docs/python/tf/linalg/trace"><code>tf.trace</code></a>


``` python
tf.linalg.trace(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

`trace(x)` returns the sum along the main diagonal of each inner-most matrix
in x. If x is of rank `k` with shape `[I, J, K, ..., L, M, N]`, then output
is a tensor of rank `k-2` with dimensions `[I, J, K, ..., L]` where

`output[i, j, k, ..., l] = trace(x[i, j, i, ..., l, :, :])`

#### For example:



```python
x = tf.constant([[1, 2], [3, 4]])
tf.linalg.trace(x)  # 5

x = tf.constant([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
tf.linalg.trace(x)  # 15

x = tf.constant([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],
                 [[-1, -2, -3],
                  [-4, -5, -6],
                  [-7, -8, -9]]])
tf.linalg.trace(x)  # [15, -15]
```

#### Args:


* <b>`x`</b>: tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The trace of input tensor.
