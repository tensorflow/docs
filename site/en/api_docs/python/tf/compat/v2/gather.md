page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.gather


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L3959-L3973">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Gather slices from params axis axis according to indices.

``` python
tf.compat.v2.gather(
    params,
    indices,
    validate_indices=None,
    axis=None,
    batch_dims=0,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Gather slices from params axis `axis` according to `indices`.  `indices` must
be an integer tensor of any dimension (usually 0-D or 1-D).

For 0-D (scalar) `indices`:

> `output`<div> $$[p_0,          ..., p_{axis-1},        \hspace{5.1em}
>            p_{axis + 1}, ..., p_{N-1}]$$ </div> =\
> `params`<div> $$[p_0,          ..., p_{axis-1},        \hspace{1em}
>            indices,                              \hspace{1em}
>            p_{axis + 1}, ..., p_{N-1}]$$ </div>.

For 1-D (vector) `indices` with `batch_dims=0`:

> `output`<div> $$[p_0,          ..., p_{axis-1},        \hspace{2.6em}
>            i,                                    \hspace{2.6em}
>            p_{axis + 1}, ..., p_{N-1}]$$ </div> =\
> `params`<div> $$[p_0,          ..., p_{axis-1},        \hspace{1em}
>            indices[i],                           \hspace{1em}
>            p_{axis + 1}, ..., p_{N-1}]$$ </div>.

In the general case, produces an output tensor where:

<div> $$\begin{align*}
output[p_0,             &..., p_{axis-1},                       &
     &i_{B},           ..., i_{M-1},                          &
     p_{axis + 1},    &..., p_{N-1}]                          = \\
params[p_0,             &..., p_{axis-1},                       &
     indices[p_0, ..., p_{B-1}, &i_{B}, ..., i_{M-1}],        &
     p_{axis + 1},    &..., p_{N-1}]
\end{align*}$$ </div>

Where <div> $$N$$ </div>=`ndims(params)`, <div> $$M$$ </div>=`ndims(indices)`, and <div> $$B$$ </div>=`batch_dims`.
Note that params.shape[:batch_dims] must be identical to
indices.shape[:batch_dims].

The shape of the output tensor is:

> `output.shape = params.shape[:axis] + indices.shape[batch_dims:] +
> params.shape[axis + 1:]`.

Note that on CPU, if an out of bound index is found, an error is returned.
On GPU, if an out of bound index is found, a 0 is stored in the corresponding
output value.

See also <a href="../../../tf/gather_nd"><code>tf.gather_nd</code></a>.

<div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src="https://www.tensorflow.org/images/Gather.png"
alt>
</div>

#### Args:


* <b>`params`</b>: The `Tensor` from which to gather values. Must be at least rank
  `axis + 1`.
* <b>`indices`</b>: The index `Tensor`.  Must be one of the following types: `int32`,
  `int64`. Must be in range `[0, params.shape[axis])`.
* <b>`validate_indices`</b>: Deprecated, does nothing.
* <b>`axis`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`. The
  `axis` in `params` to gather `indices` from. Must be greater than or equal
  to `batch_dims`.  Defaults to the first non-batch dimension. Supports
  negative indexes.
* <b>`batch_dims`</b>: An `integer`.  The number of batch dimensions.  Must be less
  than `rank(indices)`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `params`.
