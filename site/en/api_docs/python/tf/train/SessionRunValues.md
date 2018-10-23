

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.train.SessionRunValues

### `class tf.train.SessionRunValues`



Defined in [`tensorflow/python/training/session_run_hook.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/training/session_run_hook.py).

See the guide: [Training > Training Hooks](../../../../api_guides/python/train#Training_Hooks)

Contains the results of `Session.run()`.

In the future we may use this object to add more information about result of
run without changing the Hook API.

#### Args:

* <b>`results`</b>: The return values from `Session.run()` corresponding to the fetches
    attribute returned in the RunArgs. Note that this has the same shape as
    the RunArgs fetches.  For example:
      fetches = global_step_tensor
      => results = nparray(int)
      fetches = [train_op, summary_op, global_step_tensor]
      => results = [None, nparray(string), nparray(int)]
      fetches = {'step': global_step_tensor, 'summ': summary_op}
      => results = {'step': nparray(int), 'summ': nparray(string)}
* <b>`options`</b>: `RunOptions` from the `Session.run()` call.
* <b>`run_metadata`</b>: `RunMetadata` from the `Session.run()` call.

## Properties

<h3 id="options"><code>options</code></h3>

Alias for field number 1

<h3 id="results"><code>results</code></h3>

Alias for field number 0

<h3 id="run_metadata"><code>run_metadata</code></h3>

Alias for field number 2



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
__new__(
    _cls,
    results,
    options,
    run_metadata
)
```

Create new instance of SessionRunValues(results, options, run_metadata)



