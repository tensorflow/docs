page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Bidirectional


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/wrappers.py#L339-L742">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Bidirectional`

Bidirectional wrapper for RNNs.

Inherits From: [`Wrapper`](../../../tf/keras/layers/Wrapper)

### Aliases:

* Class `tf.compat.v1.keras.layers.Bidirectional`
* Class `tf.compat.v2.keras.layers.Bidirectional`


### Used in the guide:

* [Recurrent Neural Networks (RNN) with Keras](https://www.tensorflow.org/guide/keras/rnn)

### Used in the tutorials:

* [Load text](https://www.tensorflow.org/tutorials/load_data/text)
* [Text classification with an RNN](https://www.tensorflow.org/tutorials/text/text_classification_rnn)




#### Arguments:


* <b>`layer`</b>: `Recurrent` instance.
* <b>`merge_mode`</b>: Mode by which outputs of the
  forward and backward RNNs will be combined.
  One of {'sum', 'mul', 'concat', 'ave', None}.
  If None, the outputs will not be combined,
  they will be returned as a list.
* <b>`backward_layer`</b>: Optional `Recurrent` instance to be used to handle
  backwards input processing. If `backward_layer` is not provided,
  the layer instance passed as the `layer` argument will be used to
  generate the backward layer automatically.
  Note that the provided `backward_layer` layer should have properties
  matching those of the `layer` argument, in particular it should have the
  same values for `stateful`, `return_states`, `return_sequence`, etc.
  In addition, `backward_layer` and `layer` should have
  different `go_backwards` argument values.
  A `ValueError` will be raised if these requirements are not met.


#### Call arguments:

The call arguments for this layer are the same as those of the wrapped RNN
  layer.



#### Raises:


* <b>`ValueError`</b>:   1. If `layer` or `backward_layer` is not a `Layer` instance.
  2. In case of invalid `merge_mode` argument.
  3. If `backward_layer` has mismatched properties compared to `layer`.


#### Examples:



```python
model = Sequential()
model.add(Bidirectional(LSTM(10, return_sequences=True), input_shape=(5, 10)))
model.add(Bidirectional(LSTM(10)))
model.add(Dense(5))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

 # With custom backward layer
 model = Sequential()
 forward_layer = LSTM(10, return_sequences=True)
 backard_layer = LSTM(10, activation='relu', return_sequences=True,
                      go_backwards=True)
 model.add(Bidirectional(forward_layer, backward_layer=backward_layer,
                         input_shape=(5, 10)))
 model.add(Dense(5))
 model.add(Activation('softmax'))
 model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/wrappers.py#L393-L453">View source</a>

``` python
__init__(
    layer,
    merge_mode='concat',
    weights=None,
    backward_layer=None,
    **kwargs
)
```






## Properties

<h3 id="constraints"><code>constraints</code></h3>






## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/wrappers.py#L676-L678">View source</a>

``` python
reset_states()
```
