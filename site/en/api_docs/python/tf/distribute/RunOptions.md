description: Run options for strategy.run.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.RunOptions" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="experimental_bucketizing_dynamic_shape"/>
<meta itemprop="property" content="experimental_enable_dynamic_batch_size"/>
</div>

# tf.distribute.RunOptions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L593-L619">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Run options for `strategy.run`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.RunOptions`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.RunOptions(
    experimental_enable_dynamic_batch_size=(True),
    experimental_bucketizing_dynamic_shape=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

This can be used to hold some strategy specific configs.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`experimental_enable_dynamic_batch_size`
</td>
<td>
Boolean. Only applies to
TPUStrategy. Default to True. If True, TPUStrategy will enable dynamic
padder to support dynamic batch size for the inputs. Otherwise only static
shape inputs are allowed.
</td>
</tr><tr>
<td>
`experimental_bucketizing_dynamic_shape`
</td>
<td>
Boolean. Only applies to
TPUStrategy. Default to False. If True, TPUStrategy will automatic
bucketize inputs passed into `run` if the input shape is
dynamic. This is a performance optimization to reduce XLA recompilation,
which should not have impact on correctness.
</td>
</tr>
</table>



## Class Variables

* `experimental_bucketizing_dynamic_shape` <a id="experimental_bucketizing_dynamic_shape"></a>
* `experimental_enable_dynamic_batch_size` <a id="experimental_enable_dynamic_batch_size"></a>
