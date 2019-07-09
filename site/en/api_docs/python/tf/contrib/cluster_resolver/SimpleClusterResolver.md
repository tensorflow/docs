page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cluster_resolver.SimpleClusterResolver

## Class `SimpleClusterResolver`

Inherits From: [`ClusterResolver`](../../../tf/contrib/cluster_resolver/ClusterResolver)



Defined in [`tensorflow/contrib/cluster_resolver/python/training/cluster_resolver.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/cluster_resolver/python/training/cluster_resolver.py).

Simple implementation of ClusterResolver that accepts a ClusterSpec.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    cluster_spec,
    master=''
)
```

Creates a SimpleClusterResolver from a ClusterSpec.



## Methods

<h3 id="cluster_spec"><code>cluster_spec</code></h3>

``` python
cluster_spec()
```

Returns the ClusterSpec passed into the constructor.

<h3 id="master"><code>master</code></h3>

``` python
master()
```

Returns the master address to use when creating a session.



