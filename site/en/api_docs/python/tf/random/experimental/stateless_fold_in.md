description: Folds in data to an RNG seed to form a new RNG seed.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.experimental.stateless_fold_in" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.experimental.stateless_fold_in

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateless_random_ops.py#L77-L113">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Folds in data to an RNG seed to form a new RNG seed.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.random.experimental.stateless_fold_in`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.experimental.stateless_fold_in(
    seed, data
)
</code></pre>



<!-- Placeholder for "Used in" -->

For example, in a distributed-training setting, suppose we have a master seed
and a replica ID. We want to fold the replica ID into the master seed to
form a "replica seed" to be used by that replica later on, so that different
replicas will generate different random numbers but the reproducibility of the
whole system can still be controlled by the master seed:

```
>>> master_seed = [1, 2]
>>> replica_id = 3
>>> replica_seed = tf.random.experimental.stateless_fold_in(
...   master_seed, replica_id)
>>> print(replica_seed)
tf.Tensor([1105988140          3], shape=(2,), dtype=int32)
>>> tf.random.stateless_normal(shape=[3], seed=replica_seed)
<tf.Tensor: shape=(3,), dtype=float32, numpy=array([0.03197195, 0.8979765 ,
0.13253039], dtype=float32)>
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
`data`
</td>
<td>
an `int32` or `int64` scalar representing data to be folded in to the
seed.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A new RNG seed that is a deterministic function of the inputs and is
statistically safe for producing a stream of new pseudo-random values. It
will have the same dtype as `data` (if `data` doesn't have an explict dtype,
the dtype will be determined by <a href="../../../tf/convert_to_tensor.md"><code>tf.convert_to_tensor</code></a>).
</td>
</tr>

</table>

