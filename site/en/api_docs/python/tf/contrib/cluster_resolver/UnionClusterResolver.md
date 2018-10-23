

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cluster_resolver.UnionClusterResolver

## Class `UnionClusterResolver`

Inherits From: [`ClusterResolver`](../../../tf/contrib/cluster_resolver/ClusterResolver)



Defined in [`tensorflow/contrib/cluster_resolver/python/training/cluster_resolver.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/cluster_resolver/python/training/cluster_resolver.py).

Performs a union on underlying ClusterResolvers.

This class performs a union given two or more existing ClusterResolvers. It
merges the underlying ClusterResolvers, and returns one unified ClusterSpec
when cluster_spec is called. The details of the merge function is
documented in the cluster_spec function.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(*args)
```

Initializes a UnionClusterResolver with other ClusterResolvers.

#### Args:

* <b>`*args`</b>: `ClusterResolver` objects to be unionized.


#### Raises:

* <b>`TypeError`</b>: If any argument is not a subclass of `ClusterResolvers`.
* <b>`ValueError`</b>: If there are no arguments passed.

<h3 id="cluster_spec"><code>cluster_spec</code></h3>

``` python
cluster_spec()
```

Returns a union of all the ClusterSpecs from the ClusterResolvers.

#### Returns:

A ClusterSpec containing host information merged from all the underlying
ClusterResolvers.


#### Raises:

* <b>`KeyError`</b>: If there are conflicting keys detected when merging two or
  more dictionaries, this exception is raised.

Note: If there are multiple ClusterResolvers exposing ClusterSpecs with the
same job name, we will merge the list/dict of workers.

If *all* underlying ClusterSpecs expose the set of workers as lists, we will
concatenate the lists of workers, starting with the list of workers from
the first ClusterResolver passed into the constructor.

If *any* of the ClusterSpecs expose the set of workers as a dict, we will
treat all the sets of workers as dicts (even if they are returned as lists)
and will only merge them into a dict if there is no conflicting keys. If
there is a conflicting key, we will raise a `KeyError`.

<h3 id="master"><code>master</code></h3>

``` python
master()
```

master returns the master address from the first cluster resolver.



