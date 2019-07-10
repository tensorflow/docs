page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.experimental.terminate_keras_multiprocessing_pools

Destroy Keras' multiprocessing pools to prevent deadlocks.

### Aliases:

* `tf.compat.v1.keras.experimental.terminate_keras_multiprocessing_pools`
* `tf.compat.v2.keras.experimental.terminate_keras_multiprocessing_pools`
* `tf.keras.experimental.terminate_keras_multiprocessing_pools`

``` python
tf.keras.experimental.terminate_keras_multiprocessing_pools(
    grace_period=0.1,
    use_sigkill=False
)
```



Defined in [`python/keras/utils/data_utils.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/utils/data_utils.py).

<!-- Placeholder for "Used in" -->

In general multiprocessing.Pool can interact quite badly with other, seemingly
unrelated, parts of a codebase due to Pool's reliance on fork. This method
cleans up all pools which are known to belong to Keras (and thus can be safely
terminated).

#### Args:


* <b>`grace_period`</b>: Time (in seconds) to wait for process cleanup to propagate.
* <b>`use_sigkill`</b>: Boolean of whether or not to perform a cleanup pass using
  SIGKILL.


#### Returns:

A list of human readable strings describing all issues encountered. It is up
to the caller to decide whether to treat this as an error condition.
