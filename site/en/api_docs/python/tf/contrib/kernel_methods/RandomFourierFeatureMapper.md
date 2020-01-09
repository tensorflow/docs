page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kernel_methods.RandomFourierFeatureMapper


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/kernel_methods/python/mappers/random_fourier_features.py#L33-L160">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `RandomFourierFeatureMapper`

Class that implements Random Fourier Feature Mapping (RFFM) in TensorFlow.



<!-- Placeholder for "Used in" -->

The RFFM mapping is used to approximate the Gaussian (RBF) kernel:
<div> $$(exp(-||x-y||_2^2 / (2 * \sigma^2))$$ </div>

The implementation of RFFM is based on the following paper:
"Random Features for Large-Scale Kernel Machines" by Ali Rahimi and Ben Recht.
(link: https://people.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf)

The mapping uses a matrix \\(\Omega \in R^{d x D}\\) and a bias vector
\\(b \in R^D\\) where \\(d\\) is the input dimension (number of dense input
features) and \\(D\\) is the output dimension (i.e., dimension of the feature
space the input is mapped to). Each entry of \\(\Omega\\) is sampled i.i.d.
from a (scaled) Gaussian distribution and each entry of \\(b\\) is sampled
independently and uniformly from [0, \\(2 * \pi\\)].

For a single input feature vector \\(x \in R^d\\), its RFFM is defined as:
<div> $$\sqrt(2/D) * cos(x * \Omega + b)$$ </div>

where \\(cos\\) is the element-wise cosine function and \\(x, b\\) are
represented as row vectors. The aforementioned paper shows that the linear
kernel of RFFM-mapped vectors approximates the Gaussian kernel of the initial
vectors.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/kernel_methods/python/mappers/random_fourier_features.py#L60-L85">View source</a>

``` python
__init__(
    input_dim,
    output_dim,
    stddev=1.0,
    seed=1,
    name=None
)
```

Constructs a RandomFourierFeatureMapper instance.


#### Args:


* <b>`input_dim`</b>: The dimension (number of features) of the tensors to be mapped.
* <b>`output_dim`</b>: The output dimension of the mapping.
* <b>`stddev`</b>: The standard deviation of the Gaussian kernel to be approximated.
  The error of the classifier trained using this approximation is very
  sensitive to this parameter.
* <b>`seed`</b>: An integer used to initialize the parameters (\\(\Omega\\) and
  \\(b\\)) of the mapper. For repeatable sequences across different
  invocations of the mapper object (for instance, to ensure consistent
  mapping both at training and eval/inference if these happen in
  different invocations), set this to the same integer.
* <b>`name`</b>: name for the mapper object.



## Properties

<h3 id="input_dim"><code>input_dim</code></h3>




<h3 id="name"><code>name</code></h3>

Returns a name for the `RandomFourierFeatureMapper` instance.

If the name provided in the constructor is `None`, then the object's unique
id is returned.

#### Returns:

A name for the `RandomFourierFeatureMapper` instance.


<h3 id="output_dim"><code>output_dim</code></h3>

Returns the output dimension of the mapping.




## Methods

<h3 id="map"><code>map</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/kernel_methods/python/mappers/random_fourier_features.py#L107-L160">View source</a>

``` python
map(input_tensor)
```

Maps each row of input_tensor using random Fourier features.


#### Args:


* <b>`input_tensor`</b>: a `Tensor` containing input features. It's shape is
[batch_size, self._input_dim].


#### Returns:

A `Tensor` of shape [batch_size, self._output_dim] containing RFFM-mapped
features.



#### Raises:


* <b>`InvalidShapeError`</b>: if the shape of the `input_tensor` is inconsistent with
  expected input dimension.
