description: Indicates how a distributed variable will be aggregated.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.VariableAggregation" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="MEAN"/>
<meta itemprop="property" content="NONE"/>
<meta itemprop="property" content="ONLY_FIRST_REPLICA"/>
<meta itemprop="property" content="SUM"/>
</div>

# tf.compat.v1.VariableAggregation

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variables.py#L130-L138">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Indicates how a distributed variable will be aggregated.

<!-- Placeholder for "Used in" -->

<a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> distributes a model by making multiple copies
(called "replicas") acting data-parallel on different elements of the input
batch. When performing some variable-update operation, say
`var.assign_add(x)`, in a model, we need to resolve how to combine the
different values for `x` computed in the different replicas.

* `NONE`: This is the default, giving an error if you use a
  variable-update operation with multiple replicas.
* `SUM`: Add the updates across replicas.
* `MEAN`: Take the arithmetic mean ("average") of the updates across replicas.
* `ONLY_FIRST_REPLICA`: This is for when every replica is performing the same
  update, but we only want to perform the update once. Used, e.g., for the
  global step counter.
* `ONLY_FIRST_TOWER`: Deprecated alias for `ONLY_FIRST_REPLICA`.

## Class Variables

* `MEAN` <a id="MEAN"></a>
* `NONE` <a id="NONE"></a>
* `ONLY_FIRST_REPLICA` <a id="ONLY_FIRST_REPLICA"></a>
* `SUM` <a id="SUM"></a>
