page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.apply_regularization


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/regularizers.py#L170-L209">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the summed penalty by applying `regularizer` to the `weights_list`.

``` python
tf.contrib.layers.apply_regularization(
    regularizer,
    weights_list=None
)
```



<!-- Placeholder for "Used in" -->

Adding a regularization penalty over the layer weights and embedding weights
can help prevent overfitting the training data. Regularization over layer
biases is less common/useful, but assuming proper data preprocessing/mean
subtraction, it usually shouldn't hurt much either.

#### Args:


* <b>`regularizer`</b>: A function that takes a single `Tensor` argument and returns
  a scalar `Tensor` output.
* <b>`weights_list`</b>: List of weights `Tensors` or `Variables` to apply
  `regularizer` over. Defaults to the <a href="/api_docs/python/tf/GraphKeys#WEIGHTS"><code>GraphKeys.WEIGHTS</code></a> collection if
  `None`.


#### Returns:

A scalar representing the overall regularization penalty.



#### Raises:


* <b>`ValueError`</b>: If `regularizer` does not return a scalar output, or if we find
    no weights.
