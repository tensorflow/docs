description: Turns positive integers (indexes) into dense vectors of fixed size.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Embedding" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Embedding

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/embeddings.py#L36-L208">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Turns positive integers (indexes) into dense vectors of fixed size.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Embedding`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Embedding(
    input_dim, output_dim, embeddings_initializer='uniform',
    embeddings_regularizer=None, activity_regularizer=None,
    embeddings_constraint=None, mask_zero=(False), input_length=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

e.g. `[[4], [20]] -> [[0.25, 0.1], [0.6, -0.2]]`

This layer can only be used as the first layer in a model.

#### Example:



```
>>> model = tf.keras.Sequential()
>>> model.add(tf.keras.layers.Embedding(1000, 64, input_length=10))
>>> # The model will take as input an integer matrix of size (batch,
>>> # input_length), and the largest integer (i.e. word index) in the input
>>> # should be no larger than 999 (vocabulary size).
>>> # Now model.output_shape is (None, 10, 64), where `None` is the batch
>>> # dimension.
>>> input_array = np.random.randint(1000, size=(32, 10))
>>> model.compile('rmsprop', 'mse')
>>> output_array = model.predict(input_array)
>>> print(output_array.shape)
(32, 10, 64)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`input_dim`
</td>
<td>
Integer. Size of the vocabulary,
i.e. maximum integer index + 1.
</td>
</tr><tr>
<td>
`output_dim`
</td>
<td>
Integer. Dimension of the dense embedding.
</td>
</tr><tr>
<td>
`embeddings_initializer`
</td>
<td>
Initializer for the `embeddings`
matrix (see <a href="../../../tf/keras/initializers.md"><code>keras.initializers</code></a>).
</td>
</tr><tr>
<td>
`embeddings_regularizer`
</td>
<td>
Regularizer function applied to
the `embeddings` matrix (see <a href="../../../tf/keras/regularizers.md"><code>keras.regularizers</code></a>).
</td>
</tr><tr>
<td>
`embeddings_constraint`
</td>
<td>
Constraint function applied to
the `embeddings` matrix (see <a href="../../../tf/keras/constraints.md"><code>keras.constraints</code></a>).
</td>
</tr><tr>
<td>
`mask_zero`
</td>
<td>
Boolean, whether or not the input value 0 is a special "padding"
value that should be masked out.
This is useful when using recurrent layers
which may take variable length input.
If this is `True`, then all subsequent layers
in the model need to support masking or an exception will be raised.
If mask_zero is set to True, as a consequence, index 0 cannot be
used in the vocabulary (input_dim should equal size of
vocabulary + 1).
</td>
</tr><tr>
<td>
`input_length`
</td>
<td>
Length of input sequences, when it is constant.
This argument is required if you are going to connect
`Flatten` then `Dense` layers upstream
(without it, the shape of the dense outputs cannot be computed).
</td>
</tr>
</table>



#### Input shape:

2D tensor with shape: `(batch_size, input_length)`.



#### Output shape:

3D tensor with shape: `(batch_size, input_length, output_dim)`.


