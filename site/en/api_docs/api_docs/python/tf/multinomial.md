

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.multinomial

``` python
multinomial(
    logits,
    num_samples,
    seed=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/random_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/ops/random_ops.py).

See the guide: [Constants, Sequences, and Random Values > Random Tensors](../../../api_guides/python/constant_op#Random_Tensors)

Draws samples from a multinomial distribution.

Example:

```python
# samples has shape [1, 5], where each value is either 0 or 1 with equal
# probability.
samples = tf.multinomial(tf.log([[10., 10.]]), 5)
```

#### Args:

* <b>`logits`</b>: 2-D Tensor with shape `[batch_size, num_classes]`.  Each slice
    `[i, :]` represents the unnormalized log-probabilities for all classes.
* <b>`num_samples`</b>: 0-D.  Number of independent samples to draw for each row slice.
* <b>`seed`</b>: A Python integer. Used to create a random seed for the distribution.
    See
    [`tf.set_random_seed`](../tf/set_random_seed)
    for behavior.
* <b>`name`</b>: Optional name for the operation.


#### Returns:

The drawn samples of shape `[batch_size, num_samples]`.