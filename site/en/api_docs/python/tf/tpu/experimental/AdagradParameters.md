page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.experimental.AdagradParameters


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/tpu/tpu_embedding.py#L261-L303">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `AdagradParameters`

Optimization parameters for Adagrad with TPU embeddings.



### Aliases:

* Class <a href="/api_docs/python/tf/tpu/experimental/AdagradParameters"><code>tf.compat.v1.tpu.experimental.AdagradParameters</code></a>


<!-- Placeholder for "Used in" -->

Pass this to <a href="../../../tf/estimator/tpu/experimental/EmbeddingConfigSpec"><code>tf.estimator.tpu.experimental.EmbeddingConfigSpec</code></a> via the
`optimization_parameters` argument to set the optimizer and its parameters.
See the documentation for <a href="../../../tf/estimator/tpu/experimental/EmbeddingConfigSpec"><code>tf.estimator.tpu.experimental.EmbeddingConfigSpec</code></a>
for more details.

```
estimator = tf.estimator.tpu.TPUEstimator(
    ...
    embedding_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
        ...
        optimization_parameters=tf.tpu.experimental.AdagradParameters(0.1),
        ...))
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/tpu/tpu_embedding.py#L280-L303">View source</a>

``` python
__init__(
    learning_rate,
    initial_accumulator=0.1,
    use_gradient_accumulation=True,
    clip_weight_min=None,
    clip_weight_max=None
)
```

Optimization parameters for Adagrad.


#### Args:


* <b>`learning_rate`</b>: used for updating embedding table.
* <b>`initial_accumulator`</b>: initial accumulator for Adagrad.
* <b>`use_gradient_accumulation`</b>: setting this to `False` makes embedding
  gradients calculation less accurate but faster. Please see
  `optimization_parameters.proto` for details.
  for details.
* <b>`clip_weight_min`</b>: the minimum value to clip by; None means -infinity.
* <b>`clip_weight_max`</b>: the maximum value to clip by; None means +infinity.
