page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.summarize_activation

``` python
tf.contrib.layers.summarize_activation(op)
```



Defined in [`tensorflow/contrib/layers/python/layers/summaries.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/layers/python/layers/summaries.py).

Summarize an activation.

This applies the given activation and adds useful summaries specific to the
activation.

#### Args:

* <b>`op`</b>: The tensor to summarize (assumed to be a layer activation).

#### Returns:

The summary op created to summarize `op`.