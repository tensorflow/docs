page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.initialize_all_tables


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/lookup_ops.py#L51-L63">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns an Op that initializes all tables of the default graph. (deprecated)

``` python
tf.compat.v1.initialize_all_tables(name='init_all_tables')
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `tf.tables_initializer` instead.

#### Args:


* <b>`name`</b>: Optional name for the initialization op.


#### Returns:

An Op that initializes all tables.  Note that if there are
not tables the returned Op is a NoOp.
