page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.CosineSimilarity

## Class `CosineSimilarity`

Computes the cosine similarity between the labels and predictions.



### Aliases:

* Class `tf.compat.v1.keras.metrics.CosineSimilarity`
* Class `tf.compat.v2.keras.metrics.CosineSimilarity`
* Class `tf.compat.v2.metrics.CosineSimilarity`
* Class `tf.keras.metrics.CosineSimilarity`



Defined in [`python/keras/metrics.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/metrics.py).

<!-- Placeholder for "Used in" -->

cosine similarity = (a . b) / ||a|| ||b||
[Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)

For example, if `y_true` is [0, 1, 1], and `y_pred` is [1, 0, 1], the cosine
similarity is 0.5.

This metric keeps the average cosine similarity between `predictions` and
`labels` over a stream of data.

#### Usage:


```python
m = tf.keras.metrics.CosineSimilarity(axis=1)
m.update_state([[0., 1.], [1., 1.]], [[1., 0.], [1., 1.]])
# l2_norm(y_true) = [[0., 1.], [1./1.414], 1./1.414]]]
# l2_norm(y_pred) = [[1., 0.], [1./1.414], 1./1.414]]]
# l2_norm(y_true) . l2_norm(y_pred) = [[0., 0.], [0.5, 0.5]]
# result = mean(sum(l2_norm(y_true) . l2_norm(y_pred), axis=1))
       = ((0. + 0.) +  (0.5 + 0.5)) / 2

print('Final result: ', m.result().numpy())  # Final result: 0.5
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile(
    'sgd',
    loss='mse',
    metrics=[tf.keras.metrics.CosineSimilarity(axis=1)])
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    name='cosine_similarity',
    dtype=None,
    axis=-1
)
```

Creates a `CosineSimilarity` instance.


#### Args:


* <b>`name`</b>: (Optional) string name of the metric instance.
* <b>`dtype`</b>: (Optional) data type of the metric result.
* <b>`axis`</b>: (Optional) Defaults to -1. The dimension along which the cosine
  similarity is computed.



## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

``` python
reset_states()
```

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

``` python
result()
```




<h3 id="update_state"><code>update_state</code></h3>

``` python
update_state(
    y_true,
    y_pred,
    sample_weight=None
)
```

Accumulates metric statistics.

`y_true` and `y_pred` should have the same shape.

#### Args:


* <b>`y_true`</b>: The ground truth values.
* <b>`y_pred`</b>: The predicted values.
* <b>`sample_weight`</b>: Optional weighting of each example. Defaults to 1. Can be
  a `Tensor` whose rank is either 0, or the same rank as `y_true`,
  and must be broadcastable to `y_true`.


#### Returns:

Update op.




