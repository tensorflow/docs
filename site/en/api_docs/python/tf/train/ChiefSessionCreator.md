page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.ChiefSessionCreator

## Class `ChiefSessionCreator`

Creates a tf.compat.v1.Session for a chief.

Inherits From: [`SessionCreator`](../../tf/train/SessionCreator)

### Aliases:

* Class `tf.compat.v1.train.ChiefSessionCreator`
* Class `tf.train.ChiefSessionCreator`



Defined in [`python/training/monitored_session.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/monitored_session.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    scaffold=None,
    master='',
    config=None,
    checkpoint_dir=None,
    checkpoint_filename_with_path=None
)
```

Initializes a chief session creator.


#### Args:


* <b>`scaffold`</b>: A `Scaffold` used for gathering or building supportive ops. If
  not specified a default one is created. It's used to finalize the graph.
* <b>`master`</b>: `String` representation of the TensorFlow master to use.
* <b>`config`</b>: `ConfigProto` proto used to configure the session.
* <b>`checkpoint_dir`</b>: A string.  Optional path to a directory where to restore
  variables.
* <b>`checkpoint_filename_with_path`</b>: Full file name path to the checkpoint file.



## Methods

<h3 id="create_session"><code>create_session</code></h3>

``` python
create_session()
```






