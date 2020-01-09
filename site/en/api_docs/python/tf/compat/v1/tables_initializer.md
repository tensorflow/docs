page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.tables_initializer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/lookup_ops.py#L66-L84">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns an Op that initializes all tables of the default graph.

### Aliases:

* `tf.compat.v1.initializers.tables_initializer`


``` python
tf.compat.v1.tables_initializer(name='init_all_tables')
```



<!-- Placeholder for "Used in" -->

See the [Low Level
Intro](https://www.tensorflow.org/guide/low_level_intro#feature_columns)
guide, for an example of usage.

#### Args:


* <b>`name`</b>: Optional name for the initialization op.


#### Returns:

An Op that initializes all tables.  Note that if there are
not tables the returned Op is a NoOp.
