page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initializers.tables_initializer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/lookup_ops.py#L66-L84">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns an Op that initializes all tables of the default graph.

### Aliases:

* <a href="/api_docs/python/tf/initializers/tables_initializer"><code>tf.compat.v1.initializers.tables_initializer</code></a>
* <a href="/api_docs/python/tf/initializers/tables_initializer"><code>tf.compat.v1.tables_initializer</code></a>
* <a href="/api_docs/python/tf/initializers/tables_initializer"><code>tf.tables_initializer</code></a>


``` python
tf.initializers.tables_initializer(name='init_all_tables')
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
