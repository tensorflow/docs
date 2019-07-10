page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.summarize_activation

Summarize an activation.

``` python
tf.contrib.layers.summarize_activation(op)
```



Defined in [`contrib/layers/python/layers/summaries.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/summaries.py).

<!-- Placeholder for "Used in" -->

This applies the given activation and adds useful summaries specific to the
activation.

#### Args:


* <b>`op`</b>: The tensor to summarize (assumed to be a layer activation).

#### Returns:

The summary op created to summarize `op`.
