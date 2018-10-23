

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.framework.CriticalSection

## Class `CriticalSection`





Defined in [`tensorflow/contrib/framework/python/ops/critical_section_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/framework/python/ops/critical_section_ops.py).

Critical section.

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
v = tf.get_variable("v", initializer=0.0, use_resource=True)
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

## Properties

<h3 id="name"><code>name</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    name=None,
    shared_name=None,
    critical_section_def=None,
    import_scope=None
)
```

Creates a critical section.

<h3 id="execute"><code>execute</code></h3>

``` python
execute(
    fn,
    *args,
    **kwargs
)
```

Execute function `fn(*args, **kwargs)` inside the CriticalSection.

#### Args:

* <b>`fn`</b>: The function to execute.  Must return at least one tensor.
* <b>`*args`</b>: Additional positional arguments to `fn`.
* <b>`**kwargs`</b>: Additional keyword arguments to `fn`.
    Several keywords are reserved for `execute`.  These are:

    - name; The name to use when creating the execute operation.
    - exclusive_resource_access; Whether the resources required by
      `fn` should be exclusive to this `CriticalSection`.  Default: `True`.
      You may want to set this to `False` if you will be accessing a
      resource in read-only mode in two different CriticalSections.


#### Returns:

The tensors returned from `fn(*args, **kwargs)`.


#### Raises:

* <b>`ValueError`</b>: If `fn` attempts to use this `CriticalSection` in any nested
    way.
* <b>`ValueError`</b>: If `exclusive_resource_access` is not provided (is `True`) and
    another `CriticalSection` has an execution requesting the same
    resources as in `*args`, `**kwargs`, and any additionaly captured
    inputs in `fn`.  Note, even if `exclusive_resource_access` is `True`,
    if another execution in another `CriticalSection` was created without
    `exclusive_resource_access=True`, a `ValueError` will be raised.



