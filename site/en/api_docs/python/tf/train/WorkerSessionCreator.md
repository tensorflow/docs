page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.WorkerSessionCreator


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/monitored_session.py#L651-L688">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `WorkerSessionCreator`

Creates a tf.compat.v1.Session for a worker.

Inherits From: [`SessionCreator`](../../tf/train/SessionCreator)

### Aliases:

* Class <a href="/api_docs/python/tf/train/WorkerSessionCreator"><code>tf.compat.v1.train.WorkerSessionCreator</code></a>


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/monitored_session.py#L654-L672">View source</a>

``` python
__init__(
    scaffold=None,
    master='',
    config=None,
    max_wait_secs=(30 * 60)
)
```

Initializes a worker session creator.


#### Args:


* <b>`scaffold`</b>: A `Scaffold` used for gathering or building supportive ops. If
  not specified a default one is created. It's used to finalize the graph.
* <b>`master`</b>: `String` representation of the TensorFlow master to use.
* <b>`config`</b>: `ConfigProto` proto used to configure the session.
* <b>`max_wait_secs`</b>: Maximum time to wait for the session to become available.



## Methods

<h3 id="create_session"><code>create_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/monitored_session.py#L685-L688">View source</a>

``` python
create_session()
```
