description: Converts a Keras model to dot format and save to a file.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.utils.plot_model" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.utils.plot_model

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/utils/vis_utils.py#L280-L350">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts a Keras model to dot format and save to a file.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.utils.plot_model`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.utils.plot_model(
    model, to_file='model.png', show_shapes=(False), show_dtype=(False),
    show_layer_names=(True), rankdir='TB', expand_nested=(False), dpi=96
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example:



```python
input = tf.keras.Input(shape=(100,), dtype='int32', name='input')
x = tf.keras.layers.Embedding(
    output_dim=512, input_dim=10000, input_length=100)(input)
x = tf.keras.layers.LSTM(32)(x)
x = tf.keras.layers.Dense(64, activation='relu')(x)
x = tf.keras.layers.Dense(64, activation='relu')(x)
x = tf.keras.layers.Dense(64, activation='relu')(x)
output = tf.keras.layers.Dense(1, activation='sigmoid', name='output')(x)
model = tf.keras.Model(inputs=[input], outputs=[output])
dot_img_file = '/tmp/model_1.png'
tf.keras.utils.plot_model(model, to_file=dot_img_file, show_shapes=True)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`model`
</td>
<td>
A Keras model instance
</td>
</tr><tr>
<td>
`to_file`
</td>
<td>
File name of the plot image.
</td>
</tr><tr>
<td>
`show_shapes`
</td>
<td>
whether to display shape information.
</td>
</tr><tr>
<td>
`show_dtype`
</td>
<td>
whether to display layer dtypes.
</td>
</tr><tr>
<td>
`show_layer_names`
</td>
<td>
whether to display layer names.
</td>
</tr><tr>
<td>
`rankdir`
</td>
<td>
`rankdir` argument passed to PyDot,
a string specifying the format of the plot:
'TB' creates a vertical plot;
'LR' creates a horizontal plot.
</td>
</tr><tr>
<td>
`expand_nested`
</td>
<td>
Whether to expand nested models into clusters.
</td>
</tr><tr>
<td>
`dpi`
</td>
<td>
Dots per inch.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Jupyter notebook Image object if Jupyter is installed.
This enables in-line display of the model plots in notebooks.
</td>
</tr>

</table>

