page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.learning_phase


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/learning_phase">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L264-L297">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the learning phase flag.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/learning_phase"><code>tf.compat.v1.keras.backend.learning_phase</code></a>
* <a href="/api_docs/python/tf/keras/backend/learning_phase"><code>tf.compat.v2.keras.backend.learning_phase</code></a>


``` python
tf.keras.backend.learning_phase()
```



<!-- Placeholder for "Used in" -->

The learning phase flag is a bool tensor (0 = test, 1 = train)
to be passed as input to any Keras function
that uses a different behavior at train time and test time.

#### Returns:

Learning phase (scalar integer tensor or Python integer).
