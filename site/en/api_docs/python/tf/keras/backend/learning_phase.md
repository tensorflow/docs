page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.learning_phase


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L269-L302">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the learning phase flag.

### Aliases:

* `tf.compat.v1.keras.backend.learning_phase`
* `tf.compat.v2.keras.backend.learning_phase`


``` python
tf.keras.backend.learning_phase()
```



<!-- Placeholder for "Used in" -->

The learning phase flag is a bool tensor (0 = test, 1 = train)
to be passed as input to any Keras function
that uses a different behavior at train time and test time.

#### Returns:

Learning phase (scalar integer tensor or Python integer).
