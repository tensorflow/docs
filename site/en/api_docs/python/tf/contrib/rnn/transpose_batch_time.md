page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.transpose_batch_time


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/rnn.py#L43-L66">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Transposes the batch and time dimensions of a Tensor.

``` python
tf.contrib.rnn.transpose_batch_time(x)
```



<!-- Placeholder for "Used in" -->

If the input tensor has rank < 2 it returns the original tensor. Retains as
much of the static shape information as possible.

#### Args:


* <b>`x`</b>: A Tensor.


#### Returns:

x transposed along the first two dimensions.
