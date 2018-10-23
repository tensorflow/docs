

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.logging.log_every_n

``` python
log_every_n(
    level,
    msg,
    n,
    *args
)
```



Defined in [`tensorflow/python/platform/tf_logging.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/platform/tf_logging.py).

Log 'msg % args' at level 'level' once per 'n' times.

Logs the 1st call, (N+1)st call, (2N+1)st call,  etc.
Not threadsafe.

#### Args:

* <b>`level`</b>: The level at which to log.
* <b>`msg`</b>: The message to be logged.
* <b>`n`</b>: The number of times this should be called before it is logged.
  *args: The args to be substituted into the msg.