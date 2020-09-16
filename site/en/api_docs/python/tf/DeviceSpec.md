description: Represents a (possibly partial) specification for a TensorFlow device.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.DeviceSpec" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_string"/>
<meta itemprop="property" content="make_merged_spec"/>
<meta itemprop="property" content="parse_from_string"/>
<meta itemprop="property" content="replace"/>
<meta itemprop="property" content="to_string"/>
</div>

# tf.DeviceSpec

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/device_spec.py#L51-L393">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents a (possibly partial) specification for a TensorFlow device.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.DeviceSpec(
    job=None, replica=None, task=None, device_type=None, device_index=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`DeviceSpec`s are used throughout TensorFlow to describe where state is stored
and computations occur. Using `DeviceSpec` allows you to parse device spec
strings to verify their validity, merge them or compose them programmatically.

#### Example:



```python
# Place the operations on device "GPU:0" in the "ps" job.
device_spec = DeviceSpec(job="ps", device_type="GPU", device_index=0)
with tf.device(device_spec.to_string()):
  # Both my_var and squared_var will be placed on /job:ps/device:GPU:0.
  my_var = tf.Variable(..., name="my_variable")
  squared_var = tf.square(my_var)
```

With eager execution disabled (by default in TensorFlow 1.x and by calling
disable_eager_execution() in TensorFlow 2.x), the following syntax
can be used:

```python
tf.compat.v1.disable_eager_execution()

# Same as previous
device_spec = DeviceSpec(job="ps", device_type="GPU", device_index=0)
# No need of .to_string() method.
with tf.device(device_spec):
  my_var = tf.Variable(..., name="my_variable")
  squared_var = tf.square(my_var)
 ```

If a `DeviceSpec` is partially specified, it will be merged with other
`DeviceSpec`s according to the scope in which it is defined. `DeviceSpec`
components defined in inner scopes take precedence over those defined in
outer scopes.

```python
gpu0_spec = DeviceSpec(job="ps", device_type="GPU", device_index=0)
with tf.device(DeviceSpec(job="train").to_string()):
  with tf.device(gpu0_spec.to_string()):
    # Nodes created here will be assigned to /job:ps/device:GPU:0.
  with tf.device(DeviceSpec(device_type="GPU", device_index=1).to_string()):
    # Nodes created here will be assigned to /job:train/device:GPU:1.
```

A `DeviceSpec` consists of 5 components -- each of
which is optionally specified:

* Job: The job name.
* Replica: The replica index.
* Task: The task index.
* Device type: The device type string (e.g. "CPU" or "GPU").
* Device index: The device index.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`job`
</td>
<td>
string.  Optional job name.
</td>
</tr><tr>
<td>
`replica`
</td>
<td>
int.  Optional replica index.
</td>
</tr><tr>
<td>
`task`
</td>
<td>
int.  Optional task index.
</td>
</tr><tr>
<td>
`device_type`
</td>
<td>
Optional device type string (e.g. "CPU" or "GPU")
</td>
</tr><tr>
<td>
`device_index`
</td>
<td>
int.  Optional device index.  If left
unspecified, device represents 'any' device_index.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`device_index`
</td>
<td>

</td>
</tr><tr>
<td>
`device_type`
</td>
<td>

</td>
</tr><tr>
<td>
`job`
</td>
<td>

</td>
</tr><tr>
<td>
`replica`
</td>
<td>

</td>
</tr><tr>
<td>
`task`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="from_string"><code>from_string</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/device_spec.py#L142-L157">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_string(
    spec
)
</code></pre>

Construct a `DeviceSpec` from a string.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`spec`
</td>
<td>
a string of the form
/job:<name>/replica:<id>/task:<id>/device:CPU:<id>
or
/job:<name>/replica:<id>/task:<id>/device:GPU:<id>
as cpu and gpu are mutually exclusive.
All entries are optional.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A DeviceSpec.
</td>
</tr>

</table>



<h3 id="make_merged_spec"><code>make_merged_spec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/device_spec.py#L212-L234">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>make_merged_spec(
    dev
)
</code></pre>

Returns a new DeviceSpec which incorporates `dev`.

When combining specs, `dev` will take precedence over the current spec.
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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`dev`
</td>
<td>
a `DeviceSpec`
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A new `DeviceSpec` which combines `self` and `dev`
</td>
</tr>

</table>



<h3 id="parse_from_string"><code>parse_from_string</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/device_spec.py#L159-L210">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>parse_from_string(
    spec
)
</code></pre>

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

  In general, <a href="../tf/DeviceSpec.md#from_string"><code>DeviceSpec.from_string</code></a> should completely replace
  <a href="../tf/DeviceSpec.md#parse_from_string"><code>DeviceSpec.parse_from_string</code></a>, and <a href="../tf/DeviceSpec.md#replace"><code>DeviceSpec.replace</code></a> should
  completely replace setting attributes directly.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`spec`
</td>
<td>
an optional string of the form
/job:<name>/replica:<id>/task:<id>/device:CPU:<id>
or
/job:<name>/replica:<id>/task:<id>/device:GPU:<id>
as cpu and gpu are mutually exclusive.
All entries are optional.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The `DeviceSpec`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if the spec was not valid.
</td>
</tr>
</table>



<h3 id="replace"><code>replace</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/device_spec.py#L236-L258">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>replace(
    **kwargs
)
</code></pre>

Convenience method for making a new DeviceSpec by overriding fields.


#### For instance:


```
my_spec = DeviceSpec=(job="my_job", device="CPU")
my_updated_spec = my_spec.replace(device="GPU")
my_other_spec = my_spec.replace(device=None)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`**kwargs`
</td>
<td>
This method takes the same args as the DeviceSpec constructor
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A DeviceSpec with the fields specified in kwargs overridden.
</td>
</tr>

</table>



<h3 id="to_string"><code>to_string</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/device_spec.py#L133-L140">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_string()
</code></pre>

Return a string representation of this `DeviceSpec`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
a string of the form
/job:<name>/replica:<id>/task:<id>/device:<device_type>:<id>.
</td>
</tr>

</table>



<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/device_spec.py#L376-L390">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Checks if the `other` DeviceSpec is same as the current instance, eg have

   same value for all the internal fields.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`other`
</td>
<td>
Another DeviceSpec
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Return `True` if `other` is also a DeviceSpec instance and has same value
as the current instance.
Return `False` otherwise.
</td>
</tr>

</table>





