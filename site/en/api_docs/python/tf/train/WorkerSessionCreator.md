page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.WorkerSessionCreator

## Class `WorkerSessionCreator`

Creates a tf.compat.v1.Session for a worker.

Inherits From: [`SessionCreator`](../../tf/train/SessionCreator)

### Aliases:

* Class `tf.compat.v1.train.WorkerSessionCreator`
* Class `tf.train.WorkerSessionCreator`



Defined in [`python/training/monitored_session.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/monitored_session.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

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

``` python
create_session()
```






