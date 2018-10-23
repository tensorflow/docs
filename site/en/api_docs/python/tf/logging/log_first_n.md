

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.logging.log_first_n

``` python
tf.logging.log_first_n(
    level,
    msg,
    n,
    *args
)
```



Defined in [`tensorflow/python/platform/tf_logging.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/platform/tf_logging.py).

Log 'msg % args' at level 'level' only first 'n' times.

Not threadsafe.

#### Args:

* <b>`level`</b>: The level at which to log.
* <b>`msg`</b>: The message to be logged.
* <b>`n`</b>: The number of times this should be called before it is logged.
* <b>`*args`</b>: The args to be substituted into the msg.