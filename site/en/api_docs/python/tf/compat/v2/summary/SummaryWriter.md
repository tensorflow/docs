page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.summary.SummaryWriter

## Class `SummaryWriter`

Interface representing a stateful summary writer object.



### Aliases:

* Class `tf.compat.v2.summary.SummaryWriter`
* Class `tf.contrib.summary.SummaryWriter`



Defined in [`python/ops/summary_ops_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/summary_ops_v2.py).

<!-- Placeholder for "Used in" -->


## Methods

<h3 id="as_default"><code>as_default</code></h3>

``` python
as_default()
```

Returns a context manager that enables summary writing.


<h3 id="close"><code>close</code></h3>

``` python
close()
```

Flushes and closes the summary writer.


<h3 id="flush"><code>flush</code></h3>

``` python
flush()
```

Flushes any buffered data.


<h3 id="init"><code>init</code></h3>

``` python
init()
```

Initializes the summary writer.


<h3 id="set_as_default"><code>set_as_default</code></h3>

``` python
set_as_default()
```

Enables this summary writer for the current thread.




