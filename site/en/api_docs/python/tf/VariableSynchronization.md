page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.VariableSynchronization

## Class `VariableSynchronization`

Indicates when a distributed variable will be synced.



### Aliases:

* Class `tf.VariableSynchronization`
* Class `tf.compat.v1.VariableSynchronization`
* Class `tf.compat.v2.VariableSynchronization`



Defined in [`python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/variables.py).

<!-- Placeholder for "Used in" -->

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

* `AUTO` <a id="AUTO"></a>
* `NONE` <a id="NONE"></a>
* `ON_READ` <a id="ON_READ"></a>
* `ON_WRITE` <a id="ON_WRITE"></a>
