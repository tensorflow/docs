page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.SessionRunValues

## Class `SessionRunValues`

Contains the results of <a href="../../tf/InteractiveSession#run"><code>Session.run()</code></a>.



### Aliases:

* Class `tf.compat.v1.estimator.SessionRunValues`
* Class `tf.compat.v1.train.SessionRunValues`
* Class `tf.compat.v2.estimator.SessionRunValues`
* Class `tf.estimator.SessionRunValues`
* Class `tf.train.SessionRunValues`



Defined in [`python/training/session_run_hook.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/session_run_hook.py).

<!-- Placeholder for "Used in" -->

In the future we may use this object to add more information about result of
run without changing the Hook API.

#### Args:


* <b>`results`</b>: The return values from <a href="../../tf/InteractiveSession#run"><code>Session.run()</code></a> corresponding to the fetches
  attribute returned in the RunArgs. Note that this has the same shape as
  the RunArgs fetches.  For example:
    fetches = global_step_tensor
    => results = nparray(int)
    fetches = [train_op, summary_op, global_step_tensor]
    => results = [None, nparray(string), nparray(int)]
    fetches = {'step': global_step_tensor, 'summ': summary_op}
    => results = {'step': nparray(int), 'summ': nparray(string)}
* <b>`options`</b>: `RunOptions` from the <a href="../../tf/InteractiveSession#run"><code>Session.run()</code></a> call.
* <b>`run_metadata`</b>: `RunMetadata` from the <a href="../../tf/InteractiveSession#run"><code>Session.run()</code></a> call.

## Properties

<h3 id="results"><code>results</code></h3>




<h3 id="options"><code>options</code></h3>




<h3 id="run_metadata"><code>run_metadata</code></h3>






