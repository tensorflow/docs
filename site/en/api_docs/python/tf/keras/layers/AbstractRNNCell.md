page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.AbstractRNNCell

## Class `AbstractRNNCell`

Abstract object representing an RNN cell.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.AbstractRNNCell`
* Class `tf.compat.v2.keras.layers.AbstractRNNCell`
* Class `tf.keras.layers.AbstractRNNCell`



Defined in [`python/keras/layers/recurrent.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/recurrent.py).

<!-- Placeholder for "Used in" -->

This is the base class for implementing RNN cells with custom behavior.

Every `RNNCell` must have the properties below and implement `call` with
the signature `(output, next_state) = call(input, state)`.

#### Examples:



```python
  class MinimalRNNCell(AbstractRNNCell):

    def __init__(self, units, **kwargs):
      self.units = units
      super(MinimalRNNCell, self).__init__(**kwargs)

    @property
    def state_size(self):
      return self.units

    def build(self, input_shape):
      self.kernel = self.add_weight(shape=(input_shape[-1], self.units),
                                    initializer='uniform',
                                    name='kernel')
      self.recurrent_kernel = self.add_weight(
          shape=(self.units, self.units),
          initializer='uniform',
          name='recurrent_kernel')
      self.built = True

    def call(self, inputs, states):
      prev_output = states[0]
      h = K.dot(inputs, self.kernel)
      output = h + K.dot(prev_output, self.recurrent_kernel)
      return output, output
```

This definition of cell differs from the definition used in the literature.
In the literature, 'cell' refers to an object with a single scalar output.
This definition refers to a horizontal array of such units.

An RNN cell, in the most abstract setting, is anything that has
a state and performs some operation that takes a matrix of inputs.
This operation results in an output matrix with `self.output_size` columns.
If `self.state_size` is an integer, this operation also results in a new
state matrix with `self.state_size` columns.  If `self.state_size` is a
(possibly nested tuple of) TensorShape object(s), then it should return a
matching structure of Tensors having shape `[batch_size].concatenate(s)`
for each `s` in `self.batch_size`.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    trainable=True,
    name=None,
    dtype=None,
    dynamic=False,
    **kwargs
)
```






## Properties

<h3 id="output_size"><code>output_size</code></h3>

Integer or TensorShape: size of outputs produced by this cell.


<h3 id="state_size"><code>state_size</code></h3>

size(s) of state(s) used by this cell.

It can be represented by an Integer, a TensorShape or a tuple of Integers
or TensorShapes.



## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

``` python
get_initial_state(
    inputs=None,
    batch_size=None,
    dtype=None
)
```






