page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.byte_size_load_fn


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/training/python/training/device_setter.py#L105-L136">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Load function that computes the byte size of a single-output `Operation`.

``` python
tf.contrib.training.byte_size_load_fn(op)
```



<!-- Placeholder for "Used in" -->

This is intended to be used with `"Variable"` ops, which have a single
`Tensor` output with the contents of the variable.  However, it can also be
used for calculating the size of any op that has a single output.

Intended to be used with `GreedyLoadBalancingStrategy`.

#### Args:


* <b>`op`</b>: An `Operation` with a single output, typically a "Variable" op.


#### Returns:

The number of bytes in the output `Tensor`.



#### Raises:


* <b>`ValueError`</b>: if `op` does not have a single output, or if the shape of the
  single output is not fully-defined.
