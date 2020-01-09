page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.cosine_decay


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/learning_rate_decay.py#L454-L511">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Applies cosine decay to the learning rate.

### Aliases:

* <a href="/api_docs/python/tf/train/cosine_decay"><code>tf.compat.v1.train.cosine_decay</code></a>


``` python
tf.train.cosine_decay(
    learning_rate,
    global_step,
    decay_steps,
    alpha=0.0,
    name=None
)
```



<!-- Placeholder for "Used in" -->

See [Loshchilov & Hutter, ICLR2016], SGDR: Stochastic Gradient Descent
with Warm Restarts. https://arxiv.org/abs/1608.03983

When training a model, it is often recommended to lower the learning rate as
the training progresses.  This function applies a cosine decay function
to a provided initial learning rate.  It requires a `global_step` value to
compute the decayed learning rate.  You can just pass a TensorFlow variable
that you increment at each training step.

The function returns the decayed learning rate.  It is computed as:

```python
global_step = min(global_step, decay_steps)
cosine_decay = 0.5 * (1 + cos(pi * global_step / decay_steps))
decayed = (1 - alpha) * cosine_decay + alpha
decayed_learning_rate = learning_rate * decayed
```

#### Example usage:


```python
decay_steps = 1000
lr_decayed = cosine_decay(learning_rate, global_step, decay_steps)
```

#### Args:


* <b>`learning_rate`</b>: A scalar `float32` or `float64` Tensor or a Python number.
  The initial learning rate.
* <b>`global_step`</b>: A scalar `int32` or `int64` `Tensor` or a Python number. Global
  step to use for the decay computation.
* <b>`decay_steps`</b>: A scalar `int32` or `int64` `Tensor` or a Python number. Number
  of steps to decay over.
* <b>`alpha`</b>: A scalar `float32` or `float64` Tensor or a Python number. Minimum
  learning rate value as a fraction of learning_rate.
* <b>`name`</b>: String. Optional name of the operation.  Defaults to 'CosineDecay'.


#### Returns:

A scalar `Tensor` of the same type as `learning_rate`.  The decayed
learning rate.


#### Raises:


* <b>`ValueError`</b>: if `global_step` is not supplied.



#### Eager Compatibility
When eager execution is enabled, this function returns a function which in
turn returns the decayed learning rate Tensor. This can be useful for changing
the learning rate value across different invocations of optimizer functions.
