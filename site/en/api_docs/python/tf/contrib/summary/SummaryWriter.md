page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.summary.SummaryWriter

## Class `SummaryWriter`





Defined in [`tensorflow/python/ops/summary_ops_v2.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/summary_ops_v2.py).

Encapsulates a stateful summary writer resource.

See also:
- <a href="../../../tf/contrib/summary/create_file_writer"><code>tf.contrib.summary.create_file_writer</code></a>
- <a href="../../../tf/contrib/summary/create_db_writer"><code>tf.contrib.summary.create_db_writer</code></a>

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    resource,
    init_op_fn
)
```



<h3 id="as_default"><code>as_default</code></h3>

``` python
as_default()
```

Enables summary writing within a `with` block.

<h3 id="close"><code>close</code></h3>

``` python
close()
```

Operation to flush and close the summary writer resource.

<h3 id="flush"><code>flush</code></h3>

``` python
flush()
```

Operation to force the summary writer to flush any buffered data.

<h3 id="init"><code>init</code></h3>

``` python
init()
```

Operation to initialize the summary writer resource.

<h3 id="set_as_default"><code>set_as_default</code></h3>

``` python
set_as_default()
```

Enables this summary writer for the current thread.



