

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.SessionRunArgs

## Class `SessionRunArgs`





Defined in [`tensorflow/python/training/session_run_hook.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/training/session_run_hook.py).

See the guide: [Training > Training Hooks](../../../../api_guides/python/train#Training_Hooks)

Represents arguments to be added to a `Session.run()` call.

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
* <b>`options`</b>: Exactly like the `options` argument to `Session.run()`, i.e., a
    config_pb2.RunOptions proto.

## Properties

<h3 id="feed_dict"><code>feed_dict</code></h3>

Alias for field number 1

<h3 id="fetches"><code>fetches</code></h3>

Alias for field number 0

<h3 id="options"><code>options</code></h3>

Alias for field number 2



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
@staticmethod
__new__(
    cls,
    fetches,
    feed_dict=None,
    options=None
)
```





