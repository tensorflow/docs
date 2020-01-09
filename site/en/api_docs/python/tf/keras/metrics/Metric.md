page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.Metric


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/metrics/Metric">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L68-L274">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Metric`

Encapsulates metric logic and state.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/metrics/Metric"><code>tf.compat.v1.keras.metrics.Metric</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/Metric"><code>tf.compat.v2.keras.metrics.Metric</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/Metric"><code>tf.compat.v2.metrics.Metric</code></a>


<!-- Placeholder for "Used in" -->


#### Usage:



```python
m = SomeMetric(...)
for input in ...:
  m.update_state(input)
print('Final result: ', m.result().numpy())
```

Usage with tf.keras API:

```python
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer=tf.compat.v1.train.RMSPropOptimizer(0.01),
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=[tf.keras.metrics.CategoricalAccuracy()])

data = np.random.random((1000, 32))
labels = np.random.random((1000, 10))

dataset = tf.data.Dataset.from_tensor_slices((data, labels))
dataset = dataset.batch(32)
dataset = dataset.repeat()

model.fit(dataset, epochs=10, steps_per_epoch=30)
```

To be implemented by subclasses:
* `__init__()`: All state variables should be created in this method by
  calling `self.add_weight()` like: `self.var = self.add_weight(...)`
* `update_state()`: Has all updates to the state variables like:
  self.var.assign_add(...).
* `result()`: Computes and returns a value for the metric
  from the state variables.

Example subclass implementation:

```
class BinaryTruePositives(tf.keras.metrics.Metric):

  def __init__(self, name='binary_true_positives', **kwargs):
    super(BinaryTruePositives, self).__init__(name=name, **kwargs)
    self.true_positives = self.add_weight(name='tp', initializer='zeros')

  def update_state(self, y_true, y_pred, sample_weight=None):
    y_true = tf.cast(y_true, tf.bool)
    y_pred = tf.cast(y_pred, tf.bool)

    values = tf.logical_and(tf.equal(y_true, True), tf.equal(y_pred, True))
    values = tf.cast(values, self.dtype)
    if sample_weight is not None:
      sample_weight = tf.cast(sample_weight, self.dtype)
      sample_weight = tf.broadcast_weights(sample_weight, values)
      values = tf.multiply(values, sample_weight)
    self.true_positives.assign_add(tf.reduce_sum(values))

  def result(self):
    return self.true_positives
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L136-L143">View source</a>

``` python
__init__(
    name=None,
    dtype=None,
    **kwargs
)
```




<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L145-L161">View source</a>

``` python
@staticmethod
__new__(
    cls,
    *args,
    **kwargs
)
```

Create and return a new object.  See help(type) for accurate signature.




## Methods

<h3 id="add_weight"><code>add_weight</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L245-L274">View source</a>

``` python
add_weight(
    name,
    shape=(),
    aggregation=tf.VariableAggregation.SUM,
    synchronization=tf.VariableSynchronization.ON_READ,
    initializer=None,
    dtype=None
)
```

Adds state variable. Only for use by subclasses.


<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L204-L210">View source</a>

``` python
reset_states()
```

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L235-L242">View source</a>

``` python
result()
```

Computes and returns the metric value tensor.

Result computation is an idempotent operation that simply calculates the
metric value using the state variables.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L212-L233">View source</a>

``` python
update_state(
    *args,
    **kwargs
)
```

Accumulates statistics for the metric.

Note: This function is executed as a graph function in graph mode.
This means:
  a) Operations on the same resource are executed in textual order.
     This should make it easier to do things like add the updated
     value of a variable to another, for example.
  b) You don't need to worry about collecting the update ops to execute.
     All update ops added to the graph by this function will be executed.
  As a result, code should generally work the same way with graph or
  eager execution.

Please use <a href="../../../tf/config/experimental_run_functions_eagerly"><code>tf.config.experimental_run_functions_eagerly(True)</code></a> to execute
this function eagerly for debugging or profiling.

#### Args:


* <b>`*args`</b>: * <b>`**kwargs`</b>: A mini-batch of inputs to the Metric.
