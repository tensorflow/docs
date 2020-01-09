page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.staging.StagingArea


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/data_flow_ops.py#L1770-L1993">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `StagingArea`

Class for staging inputs. No ordering guarantees.



<!-- Placeholder for "Used in" -->

A `StagingArea` is a TensorFlow data structure that stores tensors across
multiple steps, and exposes operations that can put and get tensors.

Each `StagingArea` element is a tuple of one or more tensors, where each
tuple component has a static dtype, and may have a static shape.

The capacity of a `StagingArea` may be bounded or unbounded.
It supports multiple concurrent producers and consumers; and
provides exactly-once delivery.

Each element of a `StagingArea` is a fixed-length tuple of tensors whose
dtypes are described by `dtypes`, and whose shapes are optionally described
by the `shapes` argument.

If the `shapes` argument is specified, each component of a staging area
element must have the respective fixed shape. If it is
unspecified, different elements may have different shapes,

It can be configured with a capacity in which case
put(values) will block until space becomes available.

Similarly, it can be configured with a memory limit which
will block put(values) until space is available.
This is mostly useful for limiting the number of tensors on
devices such as GPUs.

All get() and peek() commands block if the requested data
is not present in the Staging Area.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/data_flow_ops.py#L1804-L1846">View source</a>

``` python
__init__(
    dtypes,
    shapes=None,
    names=None,
    shared_name=None,
    capacity=0,
    memory_limit=0
)
```

Constructs a staging area object.

The two optional lists, `shapes` and `names`, must be of the same length
as `dtypes` if provided.  The values at a given index `i` indicate the
shape and name to use for the corresponding queue component in `dtypes`.

The device scope at the time of object creation determines where the
storage for the `StagingArea` will reside.  Calls to `put` will incur a copy
to this memory space, if necessary.  Tensors returned by `get` will be
placed according to the device scope when `get` is called.

#### Args:


* <b>`dtypes`</b>:  A list of types.  The length of dtypes must equal the number
  of tensors in each element.
* <b>`shapes`</b>: (Optional.) Constraints on the shapes of tensors in an element.
  A list of shape tuples or None. This list is the same length
  as dtypes.  If the shape of any tensors in the element are constrained,
  all must be; shapes can be None if the shapes should not be constrained.
* <b>`names`</b>: (Optional.) If provided, the `get()` and
  `put()` methods will use dictionaries with these names as keys.
  Must be None or a list or tuple of the same length as `dtypes`.
* <b>`shared_name`</b>: (Optional.) A name to be used for the shared object. By
  passing the same name to two different python objects they will share
  the underlying staging area. Must be a string.
* <b>`capacity`</b>: (Optional.) Maximum number of elements.
  An integer. If zero, the Staging Area is unbounded
* <b>`memory_limit`</b>: (Optional.) Maximum number of bytes of all tensors
  in the Staging Area.
  An integer. If zero, the Staging Area is unbounded


#### Raises:


* <b>`ValueError`</b>: If one of the arguments is invalid.



## Properties

<h3 id="capacity"><code>capacity</code></h3>

The maximum number of elements of this staging area.


<h3 id="dtypes"><code>dtypes</code></h3>

The list of dtypes for each component of a staging area element.


<h3 id="memory_limit"><code>memory_limit</code></h3>

The maximum number of bytes of this staging area.


<h3 id="name"><code>name</code></h3>

The name of the staging area.


<h3 id="names"><code>names</code></h3>

The list of names for each component of a staging area element.


<h3 id="shapes"><code>shapes</code></h3>

The list of shapes for each component of a staging area element.




## Methods

<h3 id="clear"><code>clear</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/data_flow_ops.py#L1976-L1993">View source</a>

``` python
clear(name=None)
```

Clears the staging area.


#### Args:


* <b>`name`</b>: A name for the operation (optional)


#### Returns:

The created op


<h3 id="get"><code>get</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/data_flow_ops.py#L1893-L1925">View source</a>

``` python
get(name=None)
```

Gets one element from this staging area.

If the staging area is empty when this operation executes, it will block
until there is an element to dequeue.

Note that unlike others ops that can block, like the queue Dequeue
operations, this can stop other work from happening.  To avoid this, the
intended use is for this to be called only when there will be an element
already available.  One method for doing this in a training loop would be to
run a `put()` call during a warmup session.run call, and then call both
`get()` and `put()` in each subsequent step.

The placement of the returned tensor will be determined by the current
device scope when this function is called.

#### Args:


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The tuple of tensors that was gotten.


<h3 id="peek"><code>peek</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/data_flow_ops.py#L1927-L1955">View source</a>

``` python
peek(
    index,
    name=None
)
```

Peeks at an element in the staging area.

If the staging area is too small to contain the element at
the specified index, it will block until enough elements
are inserted to complete the operation.

The placement of the returned tensor will be determined by
the current device scope when this function is called.

#### Args:


* <b>`index`</b>: The index of the tensor within the staging area
        to look up.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The tuple of tensors that was gotten.


<h3 id="put"><code>put</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/data_flow_ops.py#L1848-L1884">View source</a>

``` python
put(
    values,
    name=None
)
```

Create an op that places a value into the staging area.

This operation will block if the `StagingArea` has reached
its capacity.

#### Args:


* <b>`values`</b>: A single tensor, a list or tuple of tensors, or a dictionary with
  tensor values. The number of elements must match the length of the
  list provided to the dtypes argument when creating the StagingArea.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created op.



#### Raises:


* <b>`ValueError`</b>: If the number or type of inputs don't match the staging area.

<h3 id="size"><code>size</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/data_flow_ops.py#L1957-L1974">View source</a>

``` python
size(name=None)
```

Returns the number of elements in the staging area.


#### Args:


* <b>`name`</b>: A name for the operation (optional)


#### Returns:

The created op
