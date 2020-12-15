description: Basic loop to train a model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.basic_train_loop" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.basic_train_loop

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/basic_loops.py#L24-L65">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Basic loop to train a model.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.basic_train_loop(
    supervisor, train_step_fn, args=None, kwargs=None, master=''
)
</code></pre>



<!-- Placeholder for "Used in" -->

Calls `train_step_fn` in a loop to train a model.  The function is called as:

```python
train_step_fn(session, *args, **kwargs)
```

It is passed a <a href="../../../../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a> in addition to `args` and `kwargs`.  The
function
typically runs one training step in the session.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`supervisor`
</td>
<td>
<a href="../../../../tf/compat/v1/train/Supervisor.md"><code>tf.compat.v1.train.Supervisor</code></a> to run the training services.
</td>
</tr><tr>
<td>
`train_step_fn`
</td>
<td>
Callable to execute one training step.  Called repeatedly as
`train_step_fn(session, *args **kwargs)`.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
Optional positional arguments passed to `train_step_fn`.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Optional keyword arguments passed to `train_step_fn`.
</td>
</tr><tr>
<td>
`master`
</td>
<td>
Master to use to create the training session.  Defaults to `""`
which causes the session to be created in the local process.
</td>
</tr>
</table>

