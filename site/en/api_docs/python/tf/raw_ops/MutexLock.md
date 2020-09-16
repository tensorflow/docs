description: Locks a mutex resource.  The output is the lock.  So long as the lock tensor

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.MutexLock" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.MutexLock

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Locks a mutex resource.  The output is the lock.  So long as the lock tensor

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.MutexLock`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.MutexLock(
    mutex, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

is alive, any other request to use `MutexLock` with this mutex will wait.

This is particularly useful for creating a critical section when used in
conjunction with `MutexLockIdentity`:

```python

mutex = mutex_v2(
  shared_name=handle_name, container=container, name=name)

def execute_in_critical_section(fn, *args, **kwargs):
  lock = gen_resource_variable_ops.mutex_lock(mutex)

  with ops.control_dependencies([lock]):
    r = fn(*args, **kwargs)

  with ops.control_dependencies(nest.flatten(r)):
    with ops.colocate_with(mutex):
      ensure_lock_exists = mutex_lock_identity(lock)

    # Make sure that if any element of r is accessed, all of
    # them are executed together.
    r = nest.map_structure(tf.identity, r)

  with ops.control_dependencies([ensure_lock_exists]):
    return nest.map_structure(tf.identity, r)
```

While `fn` is running in the critical section, no other functions which wish to
use this critical section may run.

Often the use case is that two executions of the same graph, in parallel,
wish to run `fn`; and we wish to ensure that only one of them executes
at a time.  This is especially important if `fn` modifies one or more
variables at a time.

It is also useful if two separate functions must share a resource, but we
wish to ensure the usage is exclusive.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`mutex`
</td>
<td>
A `Tensor` of type `resource`. The mutex resource to lock.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `variant`.
</td>
</tr>

</table>

