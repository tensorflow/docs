page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.best_effort_input_batch_size


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/rnn.py#L69-L93">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Get static input batch size if available, with fallback to the dynamic one.

``` python
tf.contrib.rnn.best_effort_input_batch_size(flat_input)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`flat_input`</b>: An iterable of time major input Tensors of shape `[max_time,
  batch_size, ...]`. All inputs should have compatible batch sizes.


#### Returns:

The batch size in Python integer if available, or a scalar Tensor otherwise.



#### Raises:


* <b>`ValueError`</b>: if there is any input with an invalid shape.
