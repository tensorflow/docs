

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.cosine_decay

``` python
cosine_decay(
    learning_rate,
    global_step,
    decay_steps,
    name=None
)
```



Defined in [`tensorflow/python/training/learning_rate_decay.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/training/learning_rate_decay.py).

Applies cosine decay to the learning rate.

See [Loshchilov & Hutter, ICLR2016], SGDR: Stochastic Gradient Descent
with Warm Restarts.

When training a model, it is often recommended to lower the learning rate as
the training progresses.  This function applies a cosine decay function
to a provided initial learning rate.  It requires a `global_step` value to
compute the decayed learning rate.  You can just pass a TensorFlow variable
that you increment at each training step.

The function returns the decayed learning rate.  It is computed as:

```python
global_step = min(global_step, decay_steps)
decayed = 0.5 * (1 + cos(pi * global_step / decay_steps))
decayed_learning_rate = learning_rate * decayed
```

Example usage:

```python
decay_steps = 1000
lr_decayed = cosine_decay(learning_rate, global_step, decay_steps)
```

#### Args:

* <b>`learning_rate`</b>: A scalar `float32` or `float64` Tensor or a Python number.
    The initial learning rate.
* <b>`global_step`</b>: A scalar `int32` or `int64` `Tensor` or a Python number.
    Global step to use for the decay computation.
* <b>`decay_steps`</b>: A scalar `int32` or `int64` `Tensor` or a Python number.
    Number of steps to decay over.
* <b>`name`</b>: String. Optional name of the operation.  Defaults to 'CosineDecay'.

#### Returns:

A scalar `Tensor` of the same type as `learning_rate`.  The decayed
learning rate.

#### Raises:

* <b>`ValueError`</b>: if `global_step` is not supplied.