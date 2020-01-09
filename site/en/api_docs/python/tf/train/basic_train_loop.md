page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.basic_train_loop


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/basic_loops.py#L24-L65">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Basic loop to train a model.

### Aliases:

* <a href="/api_docs/python/tf/train/basic_train_loop"><code>tf.compat.v1.train.basic_train_loop</code></a>


``` python
tf.train.basic_train_loop(
    supervisor,
    train_step_fn,
    args=None,
    kwargs=None,
    master=''
)
```



<!-- Placeholder for "Used in" -->

Calls `train_step_fn` in a loop to train a model.  The function is called as:

```python
train_step_fn(session, *args, **kwargs)
```

It is passed a <a href="../../tf/Session"><code>tf.compat.v1.Session</code></a> in addition to `args` and `kwargs`.  The
function
typically runs one training step in the session.

#### Args:


* <b>`supervisor`</b>: <a href="../../tf/train/Supervisor"><code>tf.compat.v1.train.Supervisor</code></a> to run the training services.
* <b>`train_step_fn`</b>: Callable to execute one training step.  Called repeatedly as
  `train_step_fn(session, *args **kwargs)`.
* <b>`args`</b>: Optional positional arguments passed to `train_step_fn`.
* <b>`kwargs`</b>: Optional keyword arguments passed to `train_step_fn`.
* <b>`master`</b>: Master to use to create the training session.  Defaults to `""`
  which causes the session to be created in the local process.
