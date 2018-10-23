

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.staging.StagingArea

### `class tf.contrib.staging.StagingArea`



Defined in [`tensorflow/python/ops/data_flow_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/data_flow_ops.py).

See the guide: [Staging (contrib)](../../../../../api_guides/python/contrib.staging)

Class for staging inputs. No ordering guarantees.

A `StagingArea` is a TensorFlow data structure that stores tensors across
multiple steps, and exposes operations that can put and get tensors.

Each `StagingArea` element is a tuple of one or more tensors, where each
tuple component has a static dtype, and may have a static shape.

The capacity of a `StagingArea` is unbounded and supports multiple
concurrent producers and consumers; and provides exactly-once delivery.

Each element of a `StagingArea` is a fixed-length tuple of tensors whose
dtypes are described by `dtypes`, and whose shapes are optionally described
by the `shapes` argument.

If the `shapes` argument is specified, each component of a staging area
element must have the respective fixed shape. If it is
unspecified, different elements may have different shapes,

## Properties

<h3 id="dtypes"><code>dtypes</code></h3>

The list of dtypes for each component of a staging area element.

<h3 id="name"><code>name</code></h3>

The name of the staging area.

<h3 id="names"><code>names</code></h3>

The list of names for each component of a staging area element.

<h3 id="shapes"><code>shapes</code></h3>

The list of shapes for each component of a staging area element.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    dtypes,
    shapes=None,
    names=None,
    shared_name=None
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


#### Raises:

* <b>`ValueError`</b>: If one of the arguments is invalid.

<h3 id="get"><code>get</code></h3>

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

<h3 id="put"><code>put</code></h3>

``` python
put(
    values,
    name=None
)
```

Create an op that places a value into the staging area.

#### Args:

* <b>`values`</b>: Tensor (or a tuple of Tensors) to place into the staging area.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

    The created op.


#### Raises:

* <b>`ValueError`</b>: If the number or type of inputs don't match the staging area.



