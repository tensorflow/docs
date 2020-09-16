description: LeCun normal initializer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.initializers.lecun_normal" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.initializers.lecun_normal

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/init_ops_v2.py#L823-L865">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



LeCun normal initializer.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.initializers.lecun_normal`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.initializers.lecun_normal(
    seed=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Initializers allow you to pre-specify an initialization strategy, encoded in
the Initializer object, without knowing the shape and dtype of the variable
being initialized.

Draws samples from a truncated normal distribution centered on 0 with `stddev
= sqrt(1 / fan_in)` where `fan_in` is the number of input units in the weight
tensor.

#### Examples:



```
>>> def make_variables(k, initializer):
...   return (tf.Variable(initializer(shape=[k, k], dtype=tf.float32)),
...           tf.Variable(initializer(shape=[k, k, k], dtype=tf.float32)))
>>> v1, v2 = make_variables(3, tf.initializers.lecun_normal())
>>> v1
<tf.Variable ... shape=(3, 3) ...
>>> v2
<tf.Variable ... shape=(3, 3, 3) ...
>>> make_variables(4, tf.initializers.RandomNormal())
(<tf.Variable ... shape=(4, 4) dtype=float32...
 <tf.Variable ... shape=(4, 4, 4) dtype=float32...
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`seed`
</td>
<td>
A Python integer. Used to seed the random generator.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A callable Initializer with `shape` and `dtype` arguments which generates a
tensor.
</td>
</tr>

</table>



#### References:

- Self-Normalizing Neural Networks,
[Klambauer et al., 2017]
(https://papers.nips.cc/paper/6698-self-normalizing-neural-networks)
([pdf]
(https://papers.nips.cc/paper/6698-self-normalizing-neural-networks.pdf))
- Efficient Backprop,
[Lecun et al., 1998](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)
