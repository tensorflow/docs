page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.logging.log_first_n


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/platform/tf_logging.py#L235-L248">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Log 'msg % args' at level 'level' only first 'n' times.

### Aliases:

* <a href="/api_docs/python/tf/logging/log_first_n"><code>tf.compat.v1.logging.log_first_n</code></a>


``` python
tf.logging.log_first_n(
    level,
    msg,
    n,
    *args
)
```



<!-- Placeholder for "Used in" -->

Not threadsafe.

#### Args:


* <b>`level`</b>: The level at which to log.
* <b>`msg`</b>: The message to be logged.
* <b>`n`</b>: The number of times this should be called before it is logged.
* <b>`*args`</b>: The args to be substituted into the msg.
