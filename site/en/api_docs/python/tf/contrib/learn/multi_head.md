page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.multi_head

``` python
tf.contrib.learn.multi_head(
    heads,
    loss_weights=None
)
```



Defined in [`tensorflow/contrib/learn/python/learn/estimators/head.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/learn/python/learn/estimators/head.py).

Creates a MultiHead stemming from same logits/hidden layer. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
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