page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.experimental.StochasticGradientDescentParameters


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/tpu/tpu_embedding.py#L377-L406">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `StochasticGradientDescentParameters`

Optimization parameters for stochastic gradient descent for TPU embeddings.



### Aliases:

* Class <a href="/api_docs/python/tf/tpu/experimental/StochasticGradientDescentParameters"><code>tf.compat.v1.tpu.experimental.StochasticGradientDescentParameters</code></a>


<!-- Placeholder for "Used in" -->

Pass this to <a href="../../../tf/estimator/tpu/experimental/EmbeddingConfigSpec"><code>tf.estimator.tpu.experimental.EmbeddingConfigSpec</code></a> via the
`optimization_parameters` argument to set the optimizer and its parameters.
See the documentation for <a href="../../../tf/estimator/tpu/experimental/EmbeddingConfigSpec"><code>tf.estimator.tpu.experimental.EmbeddingConfigSpec</code></a>
for more details.

```
estimator = tf.estimator.tpu.TPUEstimator(
    ...
    embedding_config_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
        ...
        optimization_parameters=(
            tf.tpu.experimental.StochasticGradientDescentParameters(0.1))))
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/tpu/tpu_embedding.py#L396-L406">View source</a>

``` python
__init__(
    learning_rate,
    clip_weight_min=None,
    clip_weight_max=None
)
```

Optimization parameters for stochastic gradient descent.


#### Args:


* <b>`learning_rate`</b>: a floating point value. The learning rate.
* <b>`clip_weight_min`</b>: the minimum value to clip by; None means -infinity.
* <b>`clip_weight_max`</b>: the maximum value to clip by; None means +infinity.
