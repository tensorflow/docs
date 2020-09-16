description: Wraps arbitrary expressions as a Layer object.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Lambda" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Lambda

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/core.py#L732-L1048">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Wraps arbitrary expressions as a `Layer` object.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Lambda`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Lambda(
    function, output_shape=None, mask=None, arguments=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `Lambda` layer exists so that arbitrary TensorFlow functions
can be used when constructing `Sequential` and Functional API
models. `Lambda` layers are best suited for simple operations or
quick experimentation. For more advanced usecases, follow 
[this guide](https://www.tensorflow.org/guide/keras/custom_layers_and_models)
for subclassing <a href="../../../tf/keras/layers/Layer.md"><code>tf.keras.layers.Layer</code></a>. 

The main reason to subclass <a href="../../../tf/keras/layers/Layer.md"><code>tf.keras.layers.Layer</code></a> instead of using a 
`Lambda` layer is saving and inspecting a Model. `Lambda` layers 
are saved by serializing the Python bytecode, whereas subclassed 
Layers can be saved via overriding their `get_config` method. Overriding 
`get_config` improves the portability of Models. Models that rely on 
subclassed Layers are also often easier to visualize and reason about.

#### Examples:



```python
# add a x -> x^2 layer
model.add(Lambda(lambda x: x ** 2))
```
```python
# add a layer that returns the concatenation
# of the positive part of the input and
# the opposite of the negative part

def antirectifier(x):
    x -= K.mean(x, axis=1, keepdims=True)
    x = K.l2_normalize(x, axis=1)
    pos = K.relu(x)
    neg = K.relu(-x)
    return K.concatenate([pos, neg], axis=1)

model.add(Lambda(antirectifier))
```

#### Variables:

While it is possible to use Variables with Lambda layers, this practice is
discouraged as it can easily lead to bugs. For instance, consider the
following layer:

```python
  scale = tf.Variable(1.)
  scale_layer = tf.keras.layers.Lambda(lambda x: x * scale)
```

Because scale_layer does not directly track the `scale` variable, it will
not appear in `scale_layer.trainable_weights` and will therefore not be
trained if `scale_layer` is used in a Model.

A better pattern is to write a subclassed Layer:

```python
  class ScaleLayer(tf.keras.layers.Layer):
    def __init__(self):
      super(ScaleLayer, self).__init__()
      self.scale = tf.Variable(1.)

    def call(self, inputs):
      return inputs * self.scale
```

In general, Lambda layers can be convenient for simple stateless
computation, but anything more complex should use a subclass Layer instead.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`function`
</td>
<td>
The function to be evaluated. Takes input tensor as first
argument.
</td>
</tr><tr>
<td>
`output_shape`
</td>
<td>
Expected output shape from function. This argument can be
inferred if not explicitly provided. Can be a tuple or function. If a
tuple, it only specifies the first dimension onward;
sample dimension is assumed either the same as the input: `output_shape =
(input_shape[0], ) + output_shape` or, the input is `None` and
the sample dimension is also `None`: `output_shape = (None, ) +
output_shape` If a function, it specifies the entire shape as a function
of the
input shape: `output_shape = f(input_shape)`
</td>
</tr><tr>
<td>
`mask`
</td>
<td>
Either None (indicating no masking) or a callable with the same
signature as the `compute_mask` layer method, or a tensor that will be
returned as output mask regardless what the input is.
</td>
</tr><tr>
<td>
`arguments`
</td>
<td>
Optional dictionary of keyword arguments to be passed to the
function.
</td>
</tr>
</table>


Input shape: Arbitrary. Use the keyword argument input_shape (tuple of
  integers, does not include the samples axis) when using this layer as the
  first layer in a model.
Output shape: Specified by `output_shape` argument

