page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.get_default_session


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L5352-L5367">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the default session for the current thread.

### Aliases:

* <a href="/api_docs/python/tf/get_default_session"><code>tf.compat.v1.get_default_session</code></a>


``` python
tf.get_default_session()
```



<!-- Placeholder for "Used in" -->

The returned `Session` will be the innermost session on which a
`Session` or <a href="../tf/InteractiveSession#as_default"><code>Session.as_default()</code></a> context has been entered.

NOTE: The default session is a property of the current thread. If you
create a new thread, and wish to use the default session in that
thread, you must explicitly add a `with sess.as_default():` in that
thread's function.

#### Returns:

The default `Session` being used in the current thread.
