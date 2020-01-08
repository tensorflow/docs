page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.global_step

``` python
tf.train.global_step(
    sess,
    global_step_tensor
)
```



Defined in [`tensorflow/python/training/training_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/training/training_util.py).

See the guide: [Training > Training Utilities](../../../../api_guides/python/train#Training_Utilities)

Small helper to get the global step.

```python
# Create a variable to hold the global_step.
global_step_tensor = tf.Variable(10, trainable=False, name='global_step')
# Create a session.
sess = tf.Session()
# Initialize the variable
sess.run(global_step_tensor.initializer)
# Get the variable value.
print('global_step: %s' % tf.train.global_step(sess, global_step_tensor))

global_step: 10
```

#### Args:

* <b>`sess`</b>: A TensorFlow `Session` object.
* <b>`global_step_tensor`</b>:  `Tensor` or the `name` of the operation that contains
    the global step.


#### Returns:

The global step value.