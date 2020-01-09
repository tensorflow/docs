page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.keras.backend.get_session


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L465-L492">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the TF session to be used by the backend.

``` python
tf.compat.v1.keras.backend.get_session(op_input_list=())
```



<!-- Placeholder for "Used in" -->

If a default TensorFlow session is available, we will return it.

Else, we will return the global Keras session assuming it matches
the current graph.

If no global Keras session exists at this point:
we will create a new global session.

Note that you can manually set the global session
via `K.set_session(sess)`.

#### Arguments:


* <b>`op_input_list`</b>: An option sequence of tensors or ops, which will be used
  to determine the current graph. Otherwise the default graph will be
  used.


#### Returns:

A TensorFlow session.
