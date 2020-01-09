page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.summary.scalar


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/summary/summary.py#L57-L84">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Outputs a `Summary` protocol buffer containing a single scalar value.

``` python
tf.compat.v1.summary.scalar(
    name,
    tensor,
    collections=None,
    family=None
)
```



<!-- Placeholder for "Used in" -->

The generated Summary has a Tensor.proto containing the input Tensor.

#### Args:


* <b>`name`</b>: A name for the generated node. Will also serve as the series name in
  TensorBoard.
* <b>`tensor`</b>: A real numeric Tensor containing a single value.
* <b>`collections`</b>: Optional list of graph collections keys. The new summary op is
  added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
* <b>`family`</b>: Optional; if provided, used as the prefix of the summary tag name,
  which controls the tab name used for display on Tensorboard.


#### Returns:

A scalar `Tensor` of type `string`. Which contains a `Summary` protobuf.



#### Raises:


* <b>`ValueError`</b>: If tensor has the wrong shape or type.
