description: Indicates when a distributed variable will be synced.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.VariableSynchronization" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="AUTO"/>
<meta itemprop="property" content="NONE"/>
<meta itemprop="property" content="ON_READ"/>
<meta itemprop="property" content="ON_WRITE"/>
</div>

# tf.VariableSynchronization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/variables.py#L73-L90">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Indicates when a distributed variable will be synced.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.VariableSynchronization`</p>
</p>
</section>

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

## Class Variables

* `AUTO` <a id="AUTO"></a>
* `NONE` <a id="NONE"></a>
* `ON_READ` <a id="ON_READ"></a>
* `ON_WRITE` <a id="ON_WRITE"></a>
