description: Exposes custom classes/functions to Keras deserialization internals.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.utils.CustomObjectScope" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__enter__"/>
<meta itemprop="property" content="__exit__"/>
<meta itemprop="property" content="__init__"/>
</div>

# tf.keras.utils.CustomObjectScope

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/utils/generic_utils.py#L52-L89">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Exposes custom classes/functions to Keras deserialization internals.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.utils.custom_object_scope`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.utils.CustomObjectScope`, `tf.compat.v1.keras.utils.custom_object_scope`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.utils.CustomObjectScope(
    *args
)
</code></pre>



<!-- Placeholder for "Used in" -->

Under a scope `with custom_object_scope(objects_dict)`, Keras methods such
as <a href="../../../tf/keras/models/load_model.md"><code>tf.keras.models.load_model</code></a> or <a href="../../../tf/keras/models/model_from_config.md"><code>tf.keras.models.model_from_config</code></a>
will be able to deserialize any custom object referenced by a
saved config (e.g. a custom layer or metric).

#### Example:



Consider a custom regularizer `my_regularizer`:

```python
layer = Dense(3, kernel_regularizer=my_regularizer)
config = layer.get_config()  # Config contains a reference to `my_regularizer`
...
# Later:
with custom_object_scope({'my_regularizer': my_regularizer}):
  layer = Dense.from_config(config)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`*args`
</td>
<td>
Dictionary or dictionaries of `{name: object}` pairs.
</td>
</tr>
</table>



## Methods

<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/utils/generic_utils.py#L81-L85">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__enter__()
</code></pre>




<h3 id="__exit__"><code>__exit__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/utils/generic_utils.py#L87-L89">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__exit__(
    *args, **kwargs
)
</code></pre>






