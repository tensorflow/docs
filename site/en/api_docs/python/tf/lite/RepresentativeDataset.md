page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lite.RepresentativeDataset


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/lite/RepresentativeDataset">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/lite/python/lite.py#L112-L130">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `RepresentativeDataset`

Representative dataset to evaluate optimizations.



### Aliases:

* Class <a href="/api_docs/python/tf/lite/RepresentativeDataset"><code>tf.compat.v1.lite.RepresentativeDataset</code></a>
* Class <a href="/api_docs/python/tf/lite/RepresentativeDataset"><code>tf.compat.v2.lite.RepresentativeDataset</code></a>


<!-- Placeholder for "Used in" -->

A representative dataset that can be used to evaluate optimizations by the
converter. E.g. converter can use these examples to estimate (min, max) ranges
by calibrating the model on inputs. This can allow converter to quantize a
converted floating point model.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/lite/python/lite.py#L121-L130">View source</a>

``` python
__init__(input_gen)
```

Creates a representative dataset.


#### Args:


* <b>`input_gen`</b>: an input generator that can be used to generate input samples
  for the model. This must be a callable object that returns an object
  that supports the `iter()` protocol (e.g. a generator function). The
  elements generated must have same type and shape as inputs to the model.
