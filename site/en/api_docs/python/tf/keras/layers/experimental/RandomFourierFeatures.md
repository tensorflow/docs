description: Layer that projects its inputs into a random feature space.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.RandomFourierFeatures" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.experimental.RandomFourierFeatures

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/kernelized.py#L40-L247">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Layer that projects its inputs into a random feature space.

Inherits From: [`Layer`](../../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.experimental.RandomFourierFeatures`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.experimental.RandomFourierFeatures(
    output_dim, kernel_initializer='gaussian', scale=None, trainable=(False),
    name=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer implements a mapping from input space to a space with `output_dim`
dimensions, which approximates shift-invariant kernels. A kernel function
`K(x, y)` is shift-invariant if `K(x, y) == k(x - y)` for some function `k`.
Many popular Radial Basis Functions (RBF), including Gaussian and
Laplacian kernels, are shift-invariant.

The implementation of this layer is based on the following paper:
["Random Features for Large-Scale Kernel Machines"](
  https://people.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf)
by Ali Rahimi and Ben Recht.

The distribution from which the parameters of the random features map (layer)
are sampled determines which shift-invariant kernel the layer approximates
(see paper for more details). You can use the distribution of your
choice. The layer supports out-of-the-box
approximation sof the following two RBF kernels:

- Gaussian: `K(x, y) == exp(- square(x - y) / (2 * square(scale)))`
- Laplacian: `K(x, y) = exp(-abs(x - y) / scale))`

**Note:** Unlike what is described in the paper and unlike what is used in
the Scikit-Learn implementation, the output of this layer does not apply
the `sqrt(2 / D)` normalization factor.

**Usage:** Typically, this layer is used to "kernelize" linear models by
applying a non-linear transformation (this layer) to the input features and
then training a linear model on top of the transformed features. Depending on
the loss function of the linear model, the composition of this layer and the
linear model results to models that are equivalent (up to approximation) to
kernel SVMs (for hinge loss), kernel logistic regression (for logistic loss),
kernel linear regression (for squared loss), etc.

#### Examples:



A kernel multinomial logistic regression model with Gaussian kernel for MNIST:

```python
model = keras.Sequential([
  keras.Input(shape=(784,)),
  RandomFourierFeatures(
      output_dim=4096,
      scale=10.,
      kernel_initializer='gaussian'),
  layers.Dense(units=10, activation='softmax'),
])
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['categorical_accuracy']
)
```

A quasi-SVM classifier for MNIST:

```python
model = keras.Sequential([
  keras.Input(shape=(784,)),
  RandomFourierFeatures(
      output_dim=4096,
      scale=10.,
      kernel_initializer='gaussian'),
  layers.Dense(units=10),
])
model.compile(
    optimizer='adam',
    loss='hinge',
    metrics=['categorical_accuracy']
)
```

To use another kernel, just replace the layer creation line with:

```python
random_features_layer = RandomFourierFeatures(
    output_dim=500,
    kernel_initializer=<my_initializer>,
    scale=...,
    ...)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`output_dim`
</td>
<td>
Positive integer, the dimension of the layer's output, i.e., the
number of random features used to approximate the kernel.
</td>
</tr><tr>
<td>
`kernel_initializer`
</td>
<td>
Determines the distribution of the parameters of the
random features map (and therefore the kernel approximated by the layer).
It can be either a string identifier or a Keras `Initializer` instance.
Currently only 'gaussian' and 'laplacian' are supported string
identifiers (case insensitive). Note that the kernel matrix is not
trainable.
</td>
</tr><tr>
<td>
`scale`
</td>
<td>
For Gaussian and Laplacian kernels, this corresponds to a scaling
factor of the corresponding kernel approximated by the layer (see concrete
definitions above). When provided, it should be a positive float. If None,
a default value is used: if the kernel initializer is set to "gaussian",
`scale` defaults to `sqrt(input_dim / 2)`, otherwise, it defaults to 1.0.
Both the approximation error of the kernel and the classification quality
are sensitive to this parameter. If `trainable` is set to `True`, this
parameter is learned end-to-end during training and the provided value
serves as the initial value.
**Note:** When features from this layer are fed to a linear model,
by making `scale` trainable, the resulting optimization problem is
no longer convex (even if the loss function used by the linear model
is convex).
</td>
</tr><tr>
<td>
`trainable`
</td>
<td>
Whether the scaling parameter of the layer should be trainable.
Defaults to `False`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
String, name to use for this layer.
</td>
</tr>
</table>



