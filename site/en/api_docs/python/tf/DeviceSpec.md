

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.DeviceSpec

## Class `DeviceSpec`





Defined in [`tensorflow/python/framework/device.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/framework/device.py).

Represents a (possibly partial) specification for a TensorFlow device.

`DeviceSpec`s are used throughout TensorFlow to describe where state is stored
and computations occur. Using `DeviceSpec` allows you to parse device spec
strings to verify their validity, merge them or compose them programmatically.

Example:

```python
# Place the operations on device "GPU:0" in the "ps" job.
device_spec = DeviceSpec(job="ps", device_type="GPU", device_index=0)
with tf.device(device_spec):
  # Both my_var and squared_var will be placed on /job:ps/device:GPU:0.
  my_var = tf.Variable(..., name="my_variable")
  squared_var = tf.square(my_var)
```

If a `DeviceSpec` is partially specified, it will be merged with other
`DeviceSpec`s according to the scope in which it is defined. `DeviceSpec`
components defined in inner scopes take precedence over those defined in
outer scopes.

```python
with tf.device(DeviceSpec(job="train", )):
  with tf.device(DeviceSpec(job="ps", device_type="GPU", device_index=0):
    # Nodes created here will be assigned to /job:ps/device:GPU:0.
  with tf.device(DeviceSpec(device_type="GPU", device_index=1):
    # Nodes created here will be assigned to /job:train/device:GPU:1.
```

A `DeviceSpec` consists of 5 components -- each of
which is optionally specified:

* Job: The job name.
* Replica: The replica index.
* Task: The task index.
* Device type: The device type string (e.g. "CPU" or "GPU").
* Device index: The device index.

## Properties

<h3 id="job"><code>job</code></h3>



<h3 id="replica"><code>replica</code></h3>



<h3 id="task"><code>task</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    job=None,
    replica=None,
    task=None,
    device_type=None,
    device_index=None
)
```

Create a new `DeviceSpec` object.

#### Args:

* <b>`job`</b>: string.  Optional job name.
* <b>`replica`</b>: int.  Optional replica index.
* <b>`task`</b>: int.  Optional task index.
* <b>`device_type`</b>: Optional device type string (e.g. "CPU" or "GPU")
* <b>`device_index`</b>: int.  Optional device index.  If left
    unspecified, device represents 'any' device_index.

<h3 id="from_string"><code>from_string</code></h3>

``` python
@staticmethod
from_string(spec)
```

Construct a `DeviceSpec` from a string.

#### Args:

* <b>`spec`</b>: a string of the form
   /job:<name>/replica:<id>/task:<id>/device:CPU:<id>
  or
   /job:<name>/replica:<id>/task:<id>/device:GPU:<id>
  as cpu and gpu are mutually exclusive.
  All entries are optional.


#### Returns:

A DeviceSpec.

<h3 id="merge_from"><code>merge_from</code></h3>

``` python
merge_from(dev)
```

Merge the properties of "dev" into this `DeviceSpec`.

#### Args:

* <b>`dev`</b>: a `DeviceSpec`.

<h3 id="parse_from_string"><code>parse_from_string</code></h3>

``` python
parse_from_string(spec)
```

Parse a `DeviceSpec` name into its components.

#### Args:

* <b>`spec`</b>: a string of the form
   /job:<name>/replica:<id>/task:<id>/device:CPU:<id>
  or
   /job:<name>/replica:<id>/task:<id>/device:GPU:<id>
  as cpu and gpu are mutually exclusive.
  All entries are optional.


#### Returns:

The `DeviceSpec`.


#### Raises:

* <b>`ValueError`</b>: if the spec was not valid.

<h3 id="to_string"><code>to_string</code></h3>

``` python
to_string()
```

Return a string representation of this `DeviceSpec`.

#### Returns:

a string of the form
/job:<name>/replica:<id>/task:<id>/device:<device_type>:<id>.



