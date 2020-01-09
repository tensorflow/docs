page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.matrix_rank


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linalg_impl.py#L659-L694">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Compute the matrix rank of one or more matrices.

### Aliases:

* <a href="/api_docs/python/tf/linalg/matrix_rank"><code>tf.compat.v1.linalg.matrix_rank</code></a>
* <a href="/api_docs/python/tf/linalg/matrix_rank"><code>tf.compat.v2.linalg.matrix_rank</code></a>


``` python
tf.linalg.matrix_rank(
    a,
    tol=None,
    validate_args=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`a`</b>: (Batch of) `float`-like matrix-shaped `Tensor`(s) which are to be
  pseudo-inverted.
* <b>`tol`</b>: Threshold below which the singular value is counted as 'zero'.
  Default value: `None` (i.e., `eps * max(rows, cols) * max(singular_val)`).
* <b>`validate_args`</b>: When `True`, additional assertions might be embedded in the
  graph.
  Default value: `False` (i.e., no graph assertions are added).
* <b>`name`</b>: Python `str` prefixed to ops created by this function.
  Default value: 'matrix_rank'.


#### Returns:


* <b>`matrix_rank`</b>: (Batch of) `int32` scalars representing the number of non-zero
  singular values.
