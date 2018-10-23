

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.train.WorkerSessionCreator

### `class tf.train.WorkerSessionCreator`



Defined in [`tensorflow/python/training/monitored_session.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/training/monitored_session.py).

See the guide: [Training > Distributed execution](../../../../api_guides/python/train#Distributed_execution)

Creates a tf.Session for a worker.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    scaffold=None,
    master='',
    config=None
)
```

Initializes a worker session creator.

#### Args:

* <b>`scaffold`</b>: A `Scaffold` used for gathering or building supportive ops. If
    not specified a default one is created. It's used to finalize the graph.
* <b>`master`</b>: `String` representation of the TensorFlow master to use.
* <b>`config`</b>: `ConfigProto` proto used to configure the session.

<h3 id="create_session"><code>create_session</code></h3>

``` python
create_session()
```





