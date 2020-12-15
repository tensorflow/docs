description: Applies cosine decay to the learning rate.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.cosine_decay" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.cosine_decay

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/optimizer_v2/legacy_learning_rate_decay.py#L457-L517">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Applies cosine decay to the learning rate.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.cosine_decay(
    learning_rate, global_step, decay_steps, alpha=0.0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`learning_rate`
</td>
<td>
A scalar `float32` or `float64` Tensor or a Python number.
The initial learning rate.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
A scalar `int32` or `int64` `Tensor` or a Python number. Global
step to use for the decay computation.
</td>
</tr><tr>
<td>
`decay_steps`
</td>
<td>
A scalar `int32` or `int64` `Tensor` or a Python number. Number
of steps to decay over.
</td>
</tr><tr>
<td>
`alpha`
</td>
<td>
A scalar `float32` or `float64` Tensor or a Python number. Minimum
learning rate value as a fraction of learning_rate.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
String. Optional name of the operation.  Defaults to 'CosineDecay'.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A scalar `Tensor` of the same type as `learning_rate`.  The decayed
learning rate.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if `global_step` is not supplied.
</td>
</tr>
</table>



#### References:

Stochastic Gradient Descent with Warm Restarts:
  [Loshchilov et al., 2017]
  (https://openreview.net/forum?id=Skq89Scxx&noteId=Skq89Scxx)
  ([pdf](https://openreview.net/pdf?id=Skq89Scxx))




#### Eager Compatibility
When eager execution is enabled, this function returns a function which in
turn returns the decayed learning rate Tensor. This can be useful for changing
the learning rate value across different invocations of optimizer functions.

