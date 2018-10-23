

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.WorkerSessionCreator

## Class `WorkerSessionCreator`

Inherits From: [`SessionCreator`](../../tf/train/SessionCreator)



Defined in [`tensorflow/python/training/monitored_session.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/training/monitored_session.py).

See the guide: [Training > Distributed execution](../../../../api_guides/python/train#Distributed_execution)

Creates a tf.Session for a worker.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    scaffold=None,
    master='',
    config=None,
    max_wait_secs=30 * 60
)
```

Initializes a worker session creator.

#### Args:

* <b>`scaffold`</b>: A `Scaffold` used for gathering or building supportive ops. If
    not specified a default one is created. It's used to finalize the graph.
* <b>`master`</b>: `String` representation of the TensorFlow master to use.
* <b>`config`</b>: `ConfigProto` proto used to configure the session.
* <b>`max_wait_secs`</b>: Maximum time to wait for the session to become available.

<h3 id="create_session"><code>create_session</code></h3>

``` python
create_session()
```





