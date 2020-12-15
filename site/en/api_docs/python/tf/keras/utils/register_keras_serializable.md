description: Registers an object with the Keras serialization framework.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.utils.register_keras_serializable" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.utils.register_keras_serializable

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/utils/generic_utils.py#L118-L164">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Registers an object with the Keras serialization framework.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.utils.register_keras_serializable`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.utils.register_keras_serializable(
    package='Custom', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This decorator injects the decorated class or function into the Keras custom
object dictionary, so that it can be serialized and deserialized without
needing an entry in the user-provided custom object dict. It also injects a
function that Keras will call to get the object's serializable string key.

Note that to be serialized and deserialized, classes must implement the
`get_config()` method. Functions do not have this requirement.

The object will be registered under the key 'package>name' where `name`,
defaults to the object name if not passed.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`package`
</td>
<td>
The package that this class belongs to.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The name to serialize this class under in this package. If None, the
class' name will be used.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A decorator that registers the decorated class with the passed names.
</td>
</tr>

</table>

