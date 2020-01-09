page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.multi_head


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/head.py#L466-L496">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a MultiHead stemming from same logits/hidden layer. (deprecated)

``` python
tf.contrib.learn.multi_head(
    heads,
    loss_weights=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please switch to tf.contrib.estimator.*_head.

#### Args:


* <b>`heads`</b>: list of Head objects.
* <b>`loss_weights`</b>: optional list of weights to be used to merge losses from
    each head. All losses are weighted equally if not provided.


#### Returns:

A instance of `Head` that merges multiple heads.



#### Raises:


* <b>`ValueError`</b>: if heads and loss_weights have different size.
