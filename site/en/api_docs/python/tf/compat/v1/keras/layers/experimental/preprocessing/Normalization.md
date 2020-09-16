description: Feature-wise normalization of the data.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.keras.layers.experimental.preprocessing.Normalization" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="adapt"/>
</div>

# tf.compat.v1.keras.layers.experimental.preprocessing.Normalization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/preprocessing/normalization_v1.py#L27-L28">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Feature-wise normalization of the data.

Inherits From: [`Normalization`](../../../../../../../tf/keras/layers/experimental/preprocessing/Normalization.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.keras.layers.experimental.preprocessing.Normalization(
    axis=-1, dtype=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer will coerce its inputs into a distribution centered around
0 with standard deviation 1. It accomplishes this by precomputing the mean and
variance of the data, and calling (input-mean)/sqrt(var) at runtime.

What happens in `adapt`: Compute mean and variance of the data and store them
  as the layer's weights. `adapt` should be called before `fit`, `evaluate`,
  or `predict`.

#### Examples:



Calculate the mean and variance by analyzing the dataset in `adapt`.

```
>>> adapt_data = np.array([[1.], [2.], [3.], [4.], [5.]], dtype=np.float32)
>>> input_data = np.array([[1.], [2.], [3.]], np.float32)
>>> layer = Normalization()
>>> layer.adapt(adapt_data)
>>> layer(input_data)
<tf.Tensor: shape=(3, 1), dtype=float32, numpy=
array([[-1.4142135 ],
       [-0.70710677],
       [ 0.        ]], dtype=float32)>
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`axis`
</td>
<td>
Integer or tuple of integers, the axis or axes that should be
"kept". These axes are not be summed over when calculating the
normalization statistics. By default the last axis, the `features` axis
is kept and any `space` or `time` axes are summed. Each element in the
the axes that are kept is normalized independently. If `axis` is set to
'None', the layer will perform scalar normalization (diving the input
by a single scalar value). The `batch` axis, 0, is always summed over
(`axis=0` is not allowed).
</td>
</tr>
</table>



## Methods

<h3 id="adapt"><code>adapt</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/base_preprocessing_layer.py#L130-L216">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>adapt(
    data, reset_state=(True)
)
</code></pre>

Fits the state of the preprocessing layer to the data being passed.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`data`
</td>
<td>
The data to train on. It can be passed either as a tf.data Dataset,
or as a numpy array.
</td>
</tr><tr>
<td>
`reset_state`
</td>
<td>
Optional argument specifying whether to clear the state of
the layer at the start of the call to `adapt`, or whether to start from
the existing state. Subclasses may choose to throw if reset_state is set
to 'False'.
</td>
</tr>
</table>





