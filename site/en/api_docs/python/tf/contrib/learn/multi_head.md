

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.learn.multi_head

### `tf.contrib.learn.multi_head`

``` python
multi_head(
    heads,
    loss_weights=None
)
```



Defined in [`tensorflow/contrib/learn/python/learn/estimators/head.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/learn/python/learn/estimators/head.py).

Creates a MultiHead stemming from same logits/hidden layer.

#### Args:

* <b>`heads`</b>: list of Head objects.
* <b>`loss_weights`</b>: optional list of weights to be used to merge losses from
      each head. All losses are weighted equally if not provided.


#### Returns:

  A instance of `Head` that merges multiple heads.


#### Raises:

* <b>`ValueError`</b>: if heads and loss_weights have different size.