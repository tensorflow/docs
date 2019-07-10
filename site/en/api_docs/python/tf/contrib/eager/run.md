page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.run

Runs the program with an optional main function and argv list.

``` python
tf.contrib.eager.run(
    main=None,
    argv=None
)
```



Defined in [`python/framework/ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/ops.py).

<!-- Placeholder for "Used in" -->

The program will run with eager execution enabled.

#### Example:


```python
import tensorflow as tf
# Import subject to future changes:
from tensorflow.contrib.eager.python import tfe

def main(_):
  u = tf.constant(6.0)
  v = tf.constant(7.0)
  print(u * v)

if __name__ == "__main__":
  tfe.run()
```

#### Args:


* <b>`main`</b>: the main function to run.
* <b>`argv`</b>: the arguments to pass to it.