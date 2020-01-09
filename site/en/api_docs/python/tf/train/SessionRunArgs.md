page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.SessionRunArgs


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/session_run_hook.py#L190-L211">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SessionRunArgs`

Represents arguments to be added to a <a href="../../tf/InteractiveSession#run"><code>Session.run()</code></a> call.



### Aliases:

* Class <a href="/api_docs/python/tf/train/SessionRunArgs"><code>tf.compat.v1.estimator.SessionRunArgs</code></a>
* Class <a href="/api_docs/python/tf/train/SessionRunArgs"><code>tf.compat.v1.train.SessionRunArgs</code></a>
* Class <a href="/api_docs/python/tf/train/SessionRunArgs"><code>tf.compat.v2.estimator.SessionRunArgs</code></a>
* Class <a href="/api_docs/python/tf/train/SessionRunArgs"><code>tf.estimator.SessionRunArgs</code></a>


<!-- Placeholder for "Used in" -->


#### Args:


* <b>`fetches`</b>: Exactly like the 'fetches' argument to Session.Run().
  Can be a single tensor or op, a list of 'fetches' or a dictionary
  of fetches.  For example:
    fetches = global_step_tensor
    fetches = [train_op, summary_op, global_step_tensor]
    fetches = {'step': global_step_tensor, 'summ': summary_op}
  Note that this can recurse as expected:
    fetches = {'step': global_step_tensor,
               'ops': [train_op, check_nan_op]}
* <b>`feed_dict`</b>: Exactly like the `feed_dict` argument to `Session.Run()`
* <b>`options`</b>: Exactly like the `options` argument to <a href="../../tf/InteractiveSession#run"><code>Session.run()</code></a>, i.e., a
  config_pb2.RunOptions proto.

<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/session_run_hook.py#L210-L211">View source</a>

``` python
@staticmethod
__new__(
    cls,
    fetches,
    feed_dict=None,
    options=None
)
```

Create new instance of SessionRunArgs(fetches, feed_dict, options)




## Properties

<h3 id="fetches"><code>fetches</code></h3>




<h3 id="feed_dict"><code>feed_dict</code></h3>




<h3 id="options"><code>options</code></h3>
