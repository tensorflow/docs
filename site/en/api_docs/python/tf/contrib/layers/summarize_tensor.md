page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.summarize_tensor

Summarize a tensor using a suitable summary type.

``` python
tf.contrib.layers.summarize_tensor(
    tensor,
    tag=None
)
```



Defined in [`contrib/layers/python/layers/summaries.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/summaries.py).

<!-- Placeholder for "Used in" -->

This function adds a summary op for `tensor`. The type of summary depends on
the shape of `tensor`. For scalars, a `scalar_summary` is created, for all
other tensors, `histogram_summary` is used.

#### Args:


* <b>`tensor`</b>: The tensor to summarize
* <b>`tag`</b>: The tag to use, if None then use tensor's op's name.


#### Returns:

The summary op created or None for string tensors.
