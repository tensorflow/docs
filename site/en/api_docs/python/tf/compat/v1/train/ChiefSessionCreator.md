page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.train.ChiefSessionCreator


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/monitored_session.py#L599-L647">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ChiefSessionCreator`

Creates a tf.compat.v1.Session for a chief.

Inherits From: [`SessionCreator`](../../../../tf/compat/v1/train/SessionCreator)

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/monitored_session.py#L602-L624">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/monitored_session.py#L637-L647">View source</a>

``` python
create_session()
```
