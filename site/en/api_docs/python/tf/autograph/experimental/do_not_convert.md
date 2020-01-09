page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.autograph.experimental.do_not_convert


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/autograph/experimental/do_not_convert">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/impl/api.py#L273-L298">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Decorator that suppresses the conversion of a function.

### Aliases:

* <a href="/api_docs/python/tf/autograph/experimental/do_not_convert"><code>tf.compat.v1.autograph.experimental.do_not_convert</code></a>
* <a href="/api_docs/python/tf/autograph/experimental/do_not_convert"><code>tf.compat.v2.autograph.experimental.do_not_convert</code></a>
* <a href="/api_docs/python/tf/autograph/experimental/do_not_convert"><code>tf.contrib.autograph.do_not_convert</code></a>


``` python
tf.autograph.experimental.do_not_convert(func=None)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`func`</b>: function to decorate.


#### Returns:

If `func` is not None, returns a `Callable` which is equivalent to
`func`, but is not converted by AutoGraph.
If `func` is None, returns a decorator that, when invoked with a
single `func` argument, returns a `Callable` equivalent to the
above case.
