page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.DeviceSpec

## Class `DeviceSpec`

Represents a (possibly partial) specification for a TensorFlow device.





Defined in [`python/framework/device_spec.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/device_spec.py).

<!-- Placeholder for "Used in" -->

`DeviceSpec`s are used throughout TensorFlow to describe where state is stored
and computations occur. Using `DeviceSpec` allows you to parse device spec
strings to verify their validity, merge them or compose them programmatically.

#### Example:



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

<h2 id="__init__"><code>__init__</code></h2>

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



## Properties

<h3 id="device_index"><code>device_index</code></h3>




<h3 id="device_type"><code>device_type</code></h3>




<h3 id="job"><code>job</code></h3>




<h3 id="replica"><code>replica</code></h3>




<h3 id="task"><code>task</code></h3>






## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```

Checks if the `other` DeviceSpec is same as the current instance, eg have

   same value for all the internal fields.

#### Args:


* <b>`other`</b>: Another DeviceSpec


#### Returns:

Return `True` if `other` is also a DeviceSpec instance and has same value
as the current instance.
Return `False` otherwise.


<h3 id="from_string"><code>from_string</code></h3>

``` python
@classmethod
from_string(
    cls,
    spec
)
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


<h3 id="make_merged_spec"><code>make_merged_spec</code></h3>

``` python
make_merged_spec(dev)
```

Returns a new DeviceSpec which incorporates `dev`.

When combining specs, `dev` will take precidence over the current spec.
So for instance:

```
first_spec = tf.DeviceSpec(job=0, device_type="CPU")
second_spec = tf.DeviceSpec(device_type="GPU")
combined_spec = first_spec.make_merged_spec(second_spec)
```

is equivalent to:

```
combined_spec = tf.DeviceSpec(job=0, device_type="GPU")
```

#### Args:


* <b>`dev`</b>: a `DeviceSpec`


#### Returns:

A new `DeviceSpec` which combines `self` and `dev`


<h3 id="parse_from_string"><code>parse_from_string</code></h3>

``` python
parse_from_string(spec)
```

Parse a `DeviceSpec` name into its components.

2.x behavior change:
  In TensorFlow 1.x, this function mutates its own state and returns itself.
  In 2.x, DeviceSpecs are immutable, and this function will return a
    DeviceSpec which contains the spec.

  Recommended:

    ```
    # my_spec and my_updated_spec are unrelated.
    my_spec = tf.DeviceSpec.from_string("/CPU:0")
    my_updated_spec = tf.DeviceSpec.from_string("/GPU:0")
    with tf.device(my_updated_spec):
      ...
    ```

  Will work in 1.x and 2.x (though deprecated in 2.x):

    ```
    my_spec = tf.DeviceSpec.from_string("/CPU:0")
    my_updated_spec = my_spec.parse_from_string("/GPU:0")
    with tf.device(my_updated_spec):
      ...
    ```

  Will NOT work in 2.x:

    ```
    my_spec = tf.DeviceSpec.from_string("/CPU:0")
    my_spec.parse_from_string("/GPU:0")  # <== Will not update my_spec
    with tf.device(my_spec):
      ...
    ```

  In general, `DeviceSpec.from_string` should completely replace
  `DeviceSpec.parse_from_string`, and `DeviceSpec.replace` should
  completely replace setting attributes directly.

#### Args:


* <b>`spec`</b>: an optional string of the form
 /job:<name>/replica:<id>/task:<id>/device:CPU:<id>
or
 /job:<name>/replica:<id>/task:<id>/device:GPU:<id>
as cpu and gpu are mutually exclusive.
All entries are optional.


#### Returns:

The `DeviceSpec`.



#### Raises:


* <b>`ValueError`</b>: if the spec was not valid.

<h3 id="replace"><code>replace</code></h3>

``` python
replace(**kwargs)
```

Convenience method for making a new DeviceSpec by overriding fields.


#### For instance:


```
my_spec = DeviceSpec=(job="my_job", device="CPU")
my_updated_spec = my_spec.replace(device="GPU")
my_other_spec = my_spec.replace(device=None)
```

#### Args:


* <b>`**kwargs`</b>: This method takes the same args as the DeviceSpec constructor


#### Returns:

A DeviceSpec with the fields specified in kwargs overridden.


<h3 id="to_string"><code>to_string</code></h3>

``` python
to_string()
```

Return a string representation of this `DeviceSpec`.


#### Returns:

a string of the form
/job:<name>/replica:<id>/task:<id>/device:<device_type>:<id>.




