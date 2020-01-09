page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.summary.SummaryWriter


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/summary_ops_v2.py#L178-L202">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SummaryWriter`

Interface representing a stateful summary writer object.



### Aliases:

* Class <a href="/api_docs/python/tf/compat/v2/summary/SummaryWriter"><code>tf.contrib.summary.SummaryWriter</code></a>


<!-- Placeholder for "Used in" -->


## Methods

<h3 id="as_default"><code>as_default</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/summary_ops_v2.py#L186-L190">View source</a>

``` python
as_default()
```

Returns a context manager that enables summary writing.


<h3 id="close"><code>close</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/summary_ops_v2.py#L200-L202">View source</a>

``` python
close()
```

Flushes and closes the summary writer.


<h3 id="flush"><code>flush</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/summary_ops_v2.py#L196-L198">View source</a>

``` python
flush()
```

Flushes any buffered data.


<h3 id="init"><code>init</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/summary_ops_v2.py#L192-L194">View source</a>

``` python
init()
```

Initializes the summary writer.


<h3 id="set_as_default"><code>set_as_default</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/summary_ops_v2.py#L181-L184">View source</a>

``` python
set_as_default()
```

Enables this summary writer for the current thread.
