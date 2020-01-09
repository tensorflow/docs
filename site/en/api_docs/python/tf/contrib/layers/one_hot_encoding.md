page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.one_hot_encoding


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/layers.py#L2540-L2566">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Transform numeric labels into onehot_labels using <a href="../../../tf/one_hot"><code>tf.one_hot</code></a>.

``` python
tf.contrib.layers.one_hot_encoding(
    labels,
    num_classes,
    on_value=1.0,
    off_value=0.0,
    outputs_collections=None,
    scope=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`labels`</b>: [batch_size] target labels.
* <b>`num_classes`</b>: Total number of classes.
* <b>`on_value`</b>: A scalar defining the on-value.
* <b>`off_value`</b>: A scalar defining the off-value.
* <b>`outputs_collections`</b>: Collection to add the outputs.
* <b>`scope`</b>: Optional scope for name_scope.


#### Returns:

One-hot encoding of the labels.
