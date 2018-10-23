

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.summary.SummaryWriter

## Class `SummaryWriter`





Defined in [`tensorflow/contrib/summary/summary_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/summary/summary_ops.py).

Encapsulates a stateful summary writer resource.

See also:
- <a href="../../../tf/contrib/summary/create_file_writer"><code>tf.contrib.summary.create_file_writer</code></a>
- <a href="../../../tf/contrib/summary/create_db_writer"><code>tf.contrib.summary.create_db_writer</code></a>

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(resource)
```



<h3 id="as_default"><code>as_default</code></h3>

``` python
as_default()
```

Enables summary writing within a `with` block.

<h3 id="set_as_default"><code>set_as_default</code></h3>

``` python
set_as_default()
```

Enables this summary writer for the current thread.



