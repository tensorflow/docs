description: Bidirectional wrapper for RNNs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Bidirectional" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="reset_states"/>
</div>

# tf.keras.layers.Bidirectional

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/wrappers.py#L325-L745">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Bidirectional wrapper for RNNs.

Inherits From: [`Wrapper`](../../../tf/keras/layers/Wrapper.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Bidirectional`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Bidirectional(
    layer, merge_mode='concat', weights=None, backward_layer=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`layer`
</td>
<td>
<a href="../../../tf/keras/layers/RNN.md"><code>keras.layers.RNN</code></a> instance, such as <a href="../../../tf/keras/layers/LSTM.md"><code>keras.layers.LSTM</code></a> or
<a href="../../../tf/keras/layers/GRU.md"><code>keras.layers.GRU</code></a>. It could also be a <a href="../../../tf/keras/layers/Layer.md"><code>keras.layers.Layer</code></a> instance
that meets the following criteria:
1. Be a sequence-processing layer (accepts 3D+ inputs).
2. Have a `go_backwards`, `return_sequences` and `return_state`
attribute (with the same semantics as for the `RNN` class).
3. Have an `input_spec` attribute.
4. Implement serialization via `get_config()` and `from_config()`.
Note that the recommended way to create new RNN layers is to write a
custom RNN cell and use it with <a href="../../../tf/keras/layers/RNN.md"><code>keras.layers.RNN</code></a>, instead of
subclassing <a href="../../../tf/keras/layers/Layer.md"><code>keras.layers.Layer</code></a> directly.
</td>
</tr><tr>
<td>
`merge_mode`
</td>
<td>
Mode by which outputs of the forward and backward RNNs will be
combined. One of {'sum', 'mul', 'concat', 'ave', None}. If None, the
outputs will not be combined, they will be returned as a list. Default
value is 'concat'.
</td>
</tr><tr>
<td>
`backward_layer`
</td>
<td>
Optional <a href="../../../tf/keras/layers/RNN.md"><code>keras.layers.RNN</code></a>, or <a href="../../../tf/keras/layers/Layer.md"><code>keras.layers.Layer</code></a>
instance to be used to handle backwards input processing.
If `backward_layer` is not provided, the layer instance passed as the
`layer` argument will be used to generate the backward layer
automatically.
Note that the provided `backward_layer` layer should have properties
matching those of the `layer` argument, in particular it should have the
same values for `stateful`, `return_states`, `return_sequence`, etc.
In addition, `backward_layer` and `layer` should have different
`go_backwards` argument values.
A `ValueError` will be raised if these requirements are not met.
</td>
</tr>
</table>



#### Call arguments:

The call arguments for this layer are the same as those of the wrapped RNN
  layer.
Beware that when passing the `initial_state` argument during the call of
this layer, the first half in the list of elements in the `initial_state`
list will be passed to the forward RNN call and the last half in the list
of elements will be passed to the backward RNN call.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
1. If `layer` or `backward_layer` is not a `Layer` instance.
2. In case of invalid `merge_mode` argument.
3. If `backward_layer` has mismatched properties compared to `layer`.
</td>
</tr>
</table>



#### Examples:



```python
model = Sequential()
model.add(Bidirectional(LSTM(10, return_sequences=True), input_shape=(5, 10)))
model.add(Bidirectional(LSTM(10)))
model.add(Dense(5))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

 # With custom backward layer
 model = Sequential()
 forward_layer = LSTM(10, return_sequences=True)
 backward_layer = LSTM(10, activation='relu', return_sequences=True,
                       go_backwards=True)
 model.add(Bidirectional(forward_layer, backward_layer=backward_layer,
                         input_shape=(5, 10)))
 model.add(Dense(5))
 model.add(Activation('softmax'))
 model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`constraints`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/wrappers.py#L679-L681">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_states()
</code></pre>






