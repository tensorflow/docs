page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.VariableSynchronization

## Class `VariableSynchronization`





Defined in [`tensorflow/python/ops/variables.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/variables.py).

Indicates when a distributed variable will be synced.

* `AUTO`: Indicates that the synchronization will be determined by the current
  `DistributionStrategy` (eg. With `MirroredStrategy` this would be
  `ON_WRITE`).
* `NONE`: Indicates that there will only be one copy of the variable, so
  there is no need to sync.
* `ON_WRITE`: Indicates that the variable will be updated across devices
  every time it is written.
* `ON_READ`: Indicates that the variable will be aggregated across devices
  when it is read (eg. when checkpointing or when evaluating an op that uses
  the variable).

## Class Members

<h3 id="AUTO"><code>AUTO</code></h3>

<h3 id="NONE"><code>NONE</code></h3>

<h3 id="ON_READ"><code>ON_READ</code></h3>

<h3 id="ON_WRITE"><code>ON_WRITE</code></h3>

<h3 id="__members__"><code>__members__</code></h3>

