

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.cosine_decay_restarts

``` python
tf.train.cosine_decay_restarts(
    learning_rate,
    global_step,
    first_decay_steps,
    t_mul=2.0,
    m_mul=1.0,
    alpha=0.0,
    name=None
)
```



Defined in [`tensorflow/python/training/learning_rate_decay.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/training/learning_rate_decay.py).

Applies cosine decay with restarts to the learning rate.

See [Loshchilov & Hutter, ICLR2016], SGDR: Stochastic Gradient Descent
with Warm Restarts. https://arxiv.org/abs/1608.03983

When training a model, it is often recommended to lower the learning rate as
the training progresses.  This function applies a cosine decay function with
restarts to a provided initial learning rate.  It requires a `global_step`
value to compute the decayed learning rate.  You can just pass a TensorFlow
variable that you increment at each training step.

The function returns the decayed learning rate while taking into account
possible warm restarts. The learning rate multiplier first decays
from 1 to `alpha` for `first_decay_steps` steps. Then, a warm
restart is performed. Each new warm restart runs for `t_mul` times more steps
and with `m_mul` times smaller initial learning rate.

Example usage:

```python
first_decay_steps = 1000
lr_decayed = cosine_decay_restarts(learning_rate, global_step,
                                   first_decay_steps)
```

#### Args:

* <b>`learning_rate`</b>: A scalar `float32` or `float64` Tensor or a Python number.
    The initial learning rate.
* <b>`global_step`</b>: A scalar `int32` or `int64` `Tensor` or a Python number.
    Global step to use for the decay computation.
* <b>`first_decay_steps`</b>: A scalar `int32` or `int64` `Tensor` or a Python number.
    Number of steps to decay over.
* <b>`t_mul`</b>: A scalar `float32` or `float64` `Tensor` or a Python number.
    Used to derive the number of iterations in the i-th period
* <b>`m_mul`</b>: A scalar `float32` or `float64` `Tensor` or a Python number.
    Used to derive the initial learning rate of the i-th period:
* <b>`alpha`</b>: A scalar `float32` or `float64` Tensor or a Python number.
    Minimum learning rate value as a fraction of the learning_rate.
* <b>`name`</b>: String. Optional name of the operation.  Defaults to 'SGDRDecay'.

#### Returns:

A scalar `Tensor` of the same type as `learning_rate`.  The decayed
learning rate.

#### Raises:

* <b>`ValueError`</b>: if `global_step` is not supplied.