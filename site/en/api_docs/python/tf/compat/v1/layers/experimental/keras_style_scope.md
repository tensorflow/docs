page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.layers.experimental.keras_style_scope


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/layers/base.py#L45-L111">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Use Keras-style variable management.

``` python
tf.compat.v1.layers.experimental.keras_style_scope()
```



<!-- Placeholder for "Used in" -->

All tf.layers and tf RNN cells created in this scope use Keras-style
variable management.  Creating such layers with a scope= argument is
disallowed, and reuse=True is disallowed.

The purpose of this scope is to allow users of existing layers to
slowly transition to a Keras layers API without breaking existing
functionality.

One example of this is when using TensorFlow's RNN classes with Keras
Models or Networks.  Because Keras models do not properly set variable
scopes, users of RNNs may either accidentally share scopes between two
different models, or get errors about variables that already exist.

#### Example:



```python
class RNNModel(tf.keras.Model):

  def __init__(self, name):
    super(RNNModel, self).__init__(name=name)
    self.rnn = tf.compat.v1.nn.rnn_cell.MultiRNNCell(
      [tf.compat.v1.nn.rnn_cell.LSTMCell(64) for _ in range(2)])

  def call(self, input, state):
    return self.rnn(input, state)

model_1 = RNNModel("model_1")
model_2 = RNNModel("model_2")

# OK
output_1, next_state_1 = model_1(input, state)
# Raises an error about trying to create an already existing variable.
output_2, next_state_2 = model_2(input, state)
```

The solution is to wrap the model construction and execution in a keras-style
scope:

```python
with keras_style_scope():
  model_1 = RNNModel("model_1")
  model_2 = RNNModel("model_2")

  # model_1 and model_2 are guaranteed to create their own variables.
  output_1, next_state_1 = model_1(input, state)
  output_2, next_state_2 = model_2(input, state)

  assert len(model_1.weights) > 0
  assert len(model_2.weights) > 0
  assert(model_1.weights != model_2.weights)
```

#### Yields:

A keras layer style scope.
