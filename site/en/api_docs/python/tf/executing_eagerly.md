page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.executing_eagerly


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/context.py#L1601-L1612">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns True if the current thread has eager execution enabled.

### Aliases:

* `tf.compat.v1.executing_eagerly`
* `tf.compat.v2.executing_eagerly`


``` python
tf.executing_eagerly()
```



### Used in the guide:

* [Eager execution](https://www.tensorflow.org/guide/eager)

### Used in the tutorials:

* [Custom training: walkthrough](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough)
* [Text classification with TensorFlow Hub: Movie reviews](https://www.tensorflow.org/tutorials/keras/text_classification_with_hub)



Eager execution is typically enabled via
<a href="../tf/compat/v1/enable_eager_execution"><code>tf.compat.v1.enable_eager_execution</code></a>, but may also be enabled within the
context of a Python function via tf.contrib.eager.py_func.
