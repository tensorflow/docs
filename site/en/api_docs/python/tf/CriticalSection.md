page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.CriticalSection


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/critical_section_ops.py#L75-L376">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `CriticalSection`

Critical section.



### Aliases:

* Class `tf.compat.v1.CriticalSection`
* Class `tf.compat.v2.CriticalSection`


<!-- Placeholder for "Used in" -->

A `CriticalSection` object is a resource in the graph which executes subgraphs
in **serial** order.  A common example of a subgraph one may wish to run
exclusively is the one given by the following function:

```python
v = resource_variable_ops.ResourceVariable(0.0, name="v")

def count():
  value = v.read_value()
  with tf.control_dependencies([value]):
    with tf.control_dependencies([v.assign_add(1)]):
      return tf.identity(value)
```

Here, a snapshot of `v` is captured in `value`; and then `v` is updated.
The snapshot value is returned.

If multiple workers or threads all execute `count` in parallel, there is no
guarantee that access to the variable `v` is atomic at any point within
any thread's calculation of `count`.  In fact, even implementing an atomic
counter that guarantees that the user will see each value `0, 1, ...,` is
currently impossible.

The solution is to ensure any access to the underlying resource `v` is
only processed through a critical section:

```python
cs = CriticalSection()
f1 = cs.execute(count)
f2 = cs.execute(count)
output = f1 + f2
session.run(output)
```
The functions `f1` and `f2` will be executed serially, and updates to `v`
will be atomic.

**NOTES**

All resource objects, including the critical section and any captured
variables of functions executed on that critical section, will be
colocated to the same device (host and cpu/gpu).

When using multiple critical sections on the same resources, there is no
guarantee of exclusive access to those resources.  This behavior is disallowed
by default (but see the kwarg `exclusive_resource_access`).

For example, running the same function in two separate critical sections
will not ensure serial execution:

```python
v = tf.compat.v1.get_variable("v", initializer=0.0, use_resource=True)
def accumulate(up):
  x = v.read_value()
  with tf.control_dependencies([x]):
    with tf.control_dependencies([v.assign_add(up)]):
      return tf.identity(x)
ex1 = CriticalSection().execute(
  accumulate, 1.0, exclusive_resource_access=False)
ex2 = CriticalSection().execute(
  accumulate, 1.0, exclusive_resource_access=False)
bad_sum = ex1 + ex2
sess.run(v.initializer)
sess.run(bad_sum)  # May return 0.0
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/critical_section_ops.py#L144-L154">View source</a>

``` python
__init__(
    name=None,
    shared_name=None,
    critical_section_def=None,
    import_scope=None
)
```

Creates a critical section.




## Properties

<h3 id="name"><code>name</code></h3>






## Methods

<h3 id="execute"><code>execute</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/critical_section_ops.py#L189-L292">View source</a>

``` python
execute(
    fn,
    exclusive_resource_access=True,
    name=None
)
```

Execute function `fn()` inside the critical section.

`fn` should not accept any arguments.  To add extra arguments to when
calling `fn` in the critical section, create a lambda:

```python
critical_section.execute(lambda: fn(*my_args, **my_kwargs))
```

#### Args:


* <b>`fn`</b>: The function to execute.  Must return at least one tensor.
* <b>`exclusive_resource_access`</b>: Whether the resources required by
  `fn` should be exclusive to this `CriticalSection`.  Default: `True`.
  You may want to set this to `False` if you will be accessing a
  resource in read-only mode in two different CriticalSections.
* <b>`name`</b>: The name to use when creating the execute operation.


#### Returns:

The tensors returned from `fn()`.



#### Raises:


* <b>`ValueError`</b>: If `fn` attempts to lock this `CriticalSection` in any nested
  or lazy way that may cause a deadlock.
* <b>`ValueError`</b>: If `exclusive_resource_access == True` and
  another `CriticalSection` has an execution requesting the same
  resources as `fn``.  Note, even if `exclusive_resource_access` is
  `True`, if another execution in another `CriticalSection` was created
  without `exclusive_resource_access=True`, a `ValueError` will be raised.
