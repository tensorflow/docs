description: Run options for experimental_distribute_dataset(s_from_function).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.InputOptions" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="experimental_place_dataset_on_device"/>
<meta itemprop="property" content="experimental_prefetch_to_device"/>
<meta itemprop="property" content="experimental_replication_mode"/>
</div>

# tf.distribute.InputOptions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L623-L674">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Run options for `experimental_distribute_dataset(s_from_function)`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.InputOptions(
    experimental_prefetch_to_device=(True),
    experimental_replication_mode=tf.distribute.InputReplicationMode.PER_WORKER,
    experimental_place_dataset_on_device=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

This can be used to hold some strategy specific configs.

```python
# Setup TPUStrategy
resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
tf.config.experimental_connect_to_cluster(resolver)
tf.tpu.experimental.initialize_tpu_system(resolver)
strategy = tf.distribute.TPUStrategy(resolver)

dataset = tf.data.Dataset.range(16)
distributed_dataset_on_host = (
    strategy.experimental_distribute_dataset(
        dataset,
        tf.distribute.InputOptions(
            experimental_replication_mode=
            experimental_replication_mode.PER_WORKER,
            experimental_place_dataset_on_device=False)))
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`experimental_prefetch_to_device`
</td>
<td>
Boolean. Defaults to True. If True, dataset
elements will be prefetched to accelerator device memory. When False,
dataset elements are prefetched to host device memory. Must be False when
using TPUEmbedding API. experimental_prefetch_to_device can only be used
with experimental_replication_mode=PER_WORKER
</td>
</tr><tr>
<td>
`experimental_replication_mode`
</td>
<td>
Replication mode for the input function.
Currently, the InputReplicationMode.PER_REPLICA is only supported with
tf.distribute.MirroredStrategy.
experimental_distribute_datasets_from_function.
The default value is InputReplicationMode.PER_WORKER.
</td>
</tr><tr>
<td>
`experimental_place_dataset_on_device`
</td>
<td>
Boolean. Default to False. When True,
dataset will be placed on the device, otherwise it will remain on the
host. experimental_place_dataset_on_device=True can only be used with
experimental_replication_mode=PER_REPLICA
</td>
</tr>
</table>



## Class Variables

* `experimental_place_dataset_on_device` <a id="experimental_place_dataset_on_device"></a>
* `experimental_prefetch_to_device` <a id="experimental_prefetch_to_device"></a>
* `experimental_replication_mode` <a id="experimental_replication_mode"></a>
