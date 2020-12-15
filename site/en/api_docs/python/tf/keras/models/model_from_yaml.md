description: Parses a yaml model configuration file and returns a model instance.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.models.model_from_yaml" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.models.model_from_yaml

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/saving/model_config.py#L67-L105">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Parses a yaml model configuration file and returns a model instance.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.models.model_from_yaml`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.models.model_from_yaml(
    yaml_string, custom_objects=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Usage:



```
>>> model = tf.keras.Sequential([
...     tf.keras.layers.Dense(5, input_shape=(3,)),
...     tf.keras.layers.Softmax()])
>>> try:
...   import yaml
...   config = model.to_yaml()
...   loaded_model = tf.keras.models.model_from_yaml(config)
... except ImportError:
...   pass
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`yaml_string`
</td>
<td>
YAML string or open file encoding a model configuration.
</td>
</tr><tr>
<td>
`custom_objects`
</td>
<td>
Optional dictionary mapping names
(strings) to custom classes or functions to be
considered during deserialization.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Keras model instance (uncompiled).
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ImportError`
</td>
<td>
if yaml module is not found.
</td>
</tr>
</table>

