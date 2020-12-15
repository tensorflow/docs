description: Context manager that generates a trace event in the profiler.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.profiler.experimental.Trace" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__enter__"/>
<meta itemprop="property" content="__exit__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="set_metadata"/>
</div>

# tf.profiler.experimental.Trace

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/profiler/trace.py#L32-L127">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Context manager that generates a trace event in the profiler.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.profiler.experimental.Trace(
    name, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

A trace event will start when entering the context, and stop and save the
result to the profiler when exiting the context. Open TensorBoard Profile tab
and choose trace viewer to view the trace event in the timeline.

Trace events are created only when the profiler is enabled. More information
on how to use the profiler can be found at
https://tensorflow.org/guide/profiler

#### Example usage:


```python
tf.profiler.experimental.start('logdir')
for step in range(num_steps):
  # Creates a trace event for each training step with the step number.
  with tf.profiler.experimental.Trace("Train", step_num=step):
    train_fn()
tf.profiler.experimental.stop()
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
The name of the trace event.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Keyword arguments added to the trace event.
Both the key and value are of types that
can be converted to strings, which will be
interpreted by the profiler according to the
traceme name.

Example usage:

```python

tf.profiler.experimental.start('logdir')
for step in range(num_steps):
# Creates a trace event for each training step with the
# step number.
with tf.profiler.experimental.Trace("Train", step_num=step):
train_fn()
tf.profiler.experimental.stop()

```
The example above uses the keyword argument "step_num" to specify the
training step being traced.
</td>
</tr>
</table>



## Methods

<h3 id="set_metadata"><code>set_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/profiler/trace.py#L91-L123">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_metadata(
    **kwargs
)
</code></pre>

Sets metadata in this trace event.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`**kwargs`
</td>
<td>
metadata in key-value pairs.
</td>
</tr>
</table>


This method enables setting metadata in a trace event after it is
created.

#### Example usage:



```python

  def call(function):
    with tf.profiler.experimental.Trace("call",
         function_name=function.name) as tm:
      binary, in_cache = jit_compile(function)
      tm.set_metadata(in_cache=in_cache)
      execute(binary)

```
In this example, we want to trace how much time spent on
calling a function, which includes compilation and execution.
The compilation can be either getting a cached copy of the
binary or actually generating the binary, which is indicated
by the boolean "in_cache" returned by jit_compile(). We need
to use set_metadata() to pass in_cache because we did not know
the in_cache value when the trace was created (and we cannot
create the trace after jit_compile(), because we want
to measure the entire duration of call()).

<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/profiler/trace.py#L87-L89">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__enter__()
</code></pre>




<h3 id="__exit__"><code>__exit__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/profiler/trace.py#L125-L127">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__exit__(
    exc_type, exc_val, exc_tb
)
</code></pre>






