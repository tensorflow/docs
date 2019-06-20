page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cluster_resolver.ClusterResolver

## Class `ClusterResolver`





Defined in [`tensorflow/contrib/cluster_resolver/python/training/cluster_resolver.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/cluster_resolver/python/training/cluster_resolver.py).

Abstract class for all implementations of ClusterResolvers.

This defines the skeleton for all implementations of ClusterResolvers.
ClusterResolvers are a way for TensorFlow to communicate with various cluster
management systems (e.g. GCE, AWS, etc...).

By letting TensorFlow communicate with these systems, we will be able to
automatically discover and resolve IP addresses for various TensorFlow
workers. This will eventually allow us to automatically recover from
underlying machine failures and scale TensorFlow worker clusters up and down.

## Methods

<h3 id="cluster_spec"><code>cluster_spec</code></h3>

``` python
cluster_spec()
```

Retrieve the current state of the cluster and returns a ClusterSpec.

#### Returns:

  A ClusterSpec representing the state of the cluster at the moment this
  function is called.

Implementors of this function must take care in ensuring that the
ClusterSpec returned is up-to-date at the time of calling this function.
This usually means retrieving the information from the underlying cluster
management system every time this function is invoked and reconstructing
a cluster_spec, rather than attempting to cache anything.

<h3 id="master"><code>master</code></h3>

``` python
master()
```

...



