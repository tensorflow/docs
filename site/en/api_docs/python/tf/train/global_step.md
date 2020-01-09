page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.global_step


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/training_util.py#L40-L68">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Small helper to get the global step.

### Aliases:

* <a href="/api_docs/python/tf/train/global_step"><code>tf.compat.v1.train.global_step</code></a>


``` python
tf.train.global_step(
    sess,
    global_step_tensor
)
```



<!-- Placeholder for "Used in" -->

```python
# Create a variable to hold the global_step.
global_step_tensor = tf.Variable(10, trainable=False, name='global_step')
# Create a session.
sess = tf.compat.v1.Session()
# Initialize the variable
sess.run(global_step_tensor.initializer)
# Get the variable value.
print('global_step: %s' % tf.compat.v1.train.global_step(sess,
global_step_tensor))

global_step: 10
```

#### Args:


* <b>`sess`</b>: A TensorFlow `Session` object.
* <b>`global_step_tensor`</b>:  `Tensor` or the `name` of the operation that contains
  the global step.


#### Returns:

The global step value.
