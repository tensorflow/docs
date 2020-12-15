description: Splits an RNG seed into num new seeds by adding a leading axis.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.experimental.stateless_split" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.experimental.stateless_split

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/stateless_random_ops.py#L53-L84">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Splits an RNG seed into `num` new seeds by adding a leading axis.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.random.experimental.stateless_split`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.experimental.stateless_split(
    seed, num=2
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example:



```
>>> seed = [1, 2]
>>> new_seeds = tf.random.experimental.stateless_split(seed, num=3)
>>> print(new_seeds)
tf.Tensor(
[[1105988140 1738052849]
 [-335576002  370444179]
 [  10670227 -246211131]], shape=(3, 2), dtype=int32)
>>> tf.random.stateless_normal(shape=[3], seed=new_seeds[0, :])
<tf.Tensor: shape=(3,), dtype=float32, numpy=array([-0.59835213, -0.9578608 ,
0.9002807 ], dtype=float32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`seed`
</td>
<td>
an RNG seed (a tensor with shape [2] and dtype `int32` or
`int64`). (When using XLA, only `int32` is allowed.)
</td>
</tr><tr>
<td>
`num`
</td>
<td>
optional, a positive integer or scalar tensor indicating the number of
seeds to produce (default 2).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor with shape [num, 2] representing `num` new seeds. It will have the
same dtype as `seed` (if `seed` doesn't have an explict dtype, the dtype
will be determined by <a href="../../../tf/convert_to_tensor.md"><code>tf.convert_to_tensor</code></a>).
</td>
</tr>

</table>

