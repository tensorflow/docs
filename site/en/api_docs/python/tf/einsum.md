page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.einsum


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/special_math_ops.py#L170-L308">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A generalized contraction between tensors of arbitrary dimension.

### Aliases:

* `tf.compat.v1.einsum`
* `tf.compat.v1.linalg.einsum`
* `tf.compat.v2.einsum`
* `tf.compat.v2.linalg.einsum`
* `tf.linalg.einsum`


``` python
tf.einsum(
    equation,
    *inputs,
    **kwargs
)
```



### Used in the guide:

* [Recurrent Neural Networks (RNN) with Keras](https://www.tensorflow.org/guide/keras/rnn)

### Used in the tutorials:

* [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)



This function returns a tensor whose elements are defined by `equation`,
which is written in a shorthand form inspired by the Einstein summation
convention.  As an example, consider multiplying two matrices
A and B to form a matrix C.  The elements of C are given by:

```
  C[i,k] = sum_j A[i,j] * B[j,k]
```

The corresponding `equation` is:

```
  ij,jk->ik
```

In general, the `equation` is obtained from the more familiar element-wise
equation by
  1. removing variable names, brackets, and commas,
  2. replacing "*" with ",",
  3. dropping summation signs, and
  4. moving the output to the right, and replacing "=" with "->".

Many common operations can be expressed in this way.  For example:

```python
# Matrix multiplication
>>> einsum('ij,jk->ik', m0, m1)  # output[i,k] = sum_j m0[i,j] * m1[j, k]

# Dot product
>>> einsum('i,i->', u, v)  # output = sum_i u[i]*v[i]

# Outer product
>>> einsum('i,j->ij', u, v)  # output[i,j] = u[i]*v[j]

# Transpose
>>> einsum('ij->ji', m)  # output[j,i] = m[i,j]

# Trace
>>> einsum('ii', m)  # output[j,i] = trace(m) = sum_i m[i, i]

# Batch matrix multiplication
>>> einsum('aij,ajk->aik', s, t)  # out[a,i,k] = sum_j s[a,i,j] * t[a, j, k]
```

To enable and control broadcasting, use an ellipsis.  For example, to do
batch matrix multiplication, you could use:

<pre class="devsite-click-to-copy prettyprint lang-py">
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}einsum('...ij,...jk->...ik', u, v){% endhtmlescape %}</code>
</pre>

This function behaves like `numpy.einsum`, but does not support:

* Subscripts where an axis appears more than once for a single input
  (e.g. `ijj,k->ik`) unless it is a trace (e.g. `ijji`).

#### Args:


* <b>`equation`</b>: a `str` describing the contraction, in the same format as
  `numpy.einsum`.
* <b>`*inputs`</b>: the inputs to contract (each one a `Tensor`), whose shapes should
  be consistent with `equation`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The contracted `Tensor`, with shape determined by `equation`.



#### Raises:


* <b>`ValueError`</b>: If
  - the format of `equation` is incorrect,
  - the number of inputs implied by `equation` does not match `len(inputs)`,
  - an axis appears in the output subscripts but not in any of the inputs,
  - the number of dimensions of an input differs from the number of
    indices in its subscript, or
  - the input shapes are inconsistent along a particular axis.
