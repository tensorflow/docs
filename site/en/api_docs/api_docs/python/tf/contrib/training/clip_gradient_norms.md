

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.training.clip_gradient_norms

``` python
clip_gradient_norms(
    gradients_to_variables,
    max_norm
)
```



Defined in [`tensorflow/contrib/training/python/training/training.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/training/python/training/training.py).

Clips the gradients by the given value.

#### Args:

* <b>`gradients_to_variables`</b>: A list of gradient to variable pairs (tuples).
* <b>`max_norm`</b>: the maximum norm value.


#### Returns:

  A list of clipped gradient to variable pairs.