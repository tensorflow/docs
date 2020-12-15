description: Updates the shape of a tensor and checks at runtime that the shape holds.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.ensure_shape" />
<meta itemprop="path" content="Stable" />
</div>

# tf.ensure_shape

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/check_ops.py#L2219-L2338">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Updates the shape of a tensor and checks at runtime that the shape holds.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.ensure_shape`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.ensure_shape(
    x, shape, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### For example:



```
>>> @tf.function(input_signature=[tf.TensorSpec(shape=None, dtype=tf.float32)])
... def f(tensor):
...   return tf.ensure_shape(tensor, [3, 3])
>>>
>>> f(tf.zeros([3, 3])) # Passes
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]], dtype=float32)>
>>> f([1, 2, 3]) # fails
Traceback (most recent call last):
...
InvalidArgumentError:  Shape of tensor x [3] is not compatible with expected shape [3,3].
```

The above example raises <a href="../tf/errors/InvalidArgumentError.md"><code>tf.errors.InvalidArgumentError</code></a>,
because the shape (3,) is not compatible with the shape (None, 3, 3)

With eager execution this is a shape assertion, that returns the input:

```
>>> x = tf.constant([1,2,3])
>>> print(x.shape)
(3,)
>>> x = tf.ensure_shape(x, [3])
>>> x = tf.ensure_shape(x, [5])
Traceback (most recent call last):
...
tf.errors.InvalidArgumentError: Shape of tensor dummy_input [3] is not
  compatible with expected shape [5]. [Op:EnsureShape]
```

Inside a <a href="../tf/function.md"><code>tf.function</code></a> or <a href="../tf/Graph.md"><code>v1.Graph</code></a> context it checks both the buildtime and
runtime shapes. This is stricter than <a href="../tf/Tensor.md#set_shape"><code>tf.Tensor.set_shape</code></a> which only
checks the buildtime shape.

Note: This differs from <a href="../tf/Tensor.md#set_shape"><code>tf.Tensor.set_shape</code></a> in that it sets the static shape
of the resulting tensor and enforces it at runtime, raising an error if the
tensor's runtime shape is incompatible with the specified shape.
<a href="../tf/Tensor.md#set_shape"><code>tf.Tensor.set_shape</code></a> sets the static shape of the tensor without enforcing it
at runtime, which may result in inconsistencies between the statically-known
shape of tensors and the runtime value of tensors.

For example, of loading images of a known size:

```
>>> @tf.function
... def decode_image(png):
...   image = tf.image.decode_png(png, channels=3)
...   # the `print` executes during tracing.
...   print("Initial shape: ", image.shape)
...   image = tf.ensure_shape(image,[28, 28, 3])
...   print("Final shape: ", image.shape)
...   return image
```

When tracing a function, no ops are being executed, shapes may be unknown.
See the [Concrete Functions Guide](https://www.tensorflow.org/guide/concrete_function)
for details.

```
>>> concrete_decode = decode_image.get_concrete_function(
...     tf.TensorSpec([], dtype=tf.string))
Initial shape:  (None, None, 3)
Final shape:  (28, 28, 3)
```

```
>>> image = tf.random.uniform(maxval=255, shape=[28, 28, 3], dtype=tf.int32)
>>> image = tf.cast(image,tf.uint8)
>>> png = tf.image.encode_png(image)
>>> image2 = concrete_decode(png)
>>> print(image2.shape)
(28, 28, 3)
```

```
>>> image = tf.concat([image,image], axis=0)
>>> print(image.shape)
(56, 28, 3)
>>> png = tf.image.encode_png(image)
>>> image2 = concrete_decode(png)
Traceback (most recent call last):
...
tf.errors.InvalidArgumentError:  Shape of tensor DecodePng [56,28,3] is not
  compatible with expected shape [28,28,3].
```

Caution: if you don't use the result of <a href="../tf/ensure_shape.md"><code>tf.ensure_shape</code></a> the check may not
run.

```
>>> @tf.function
... def bad_decode_image(png):
...   image = tf.image.decode_png(png, channels=3)
...   # the `print` executes during tracing.
...   print("Initial shape: ", image.shape)
...   # BAD: forgot to use the returned tensor.
...   tf.ensure_shape(image,[28, 28, 3])
...   print("Final shape: ", image.shape)
...   return image
```

```
>>> image = bad_decode_image(png)
Initial shape:  (None, None, 3)
Final shape:  (None, None, 3)
>>> print(image.shape)
(56, 28, 3)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A `TensorShape` representing the shape of this tensor, a
`TensorShapeProto`, a list, a tuple, or None.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional). Defaults to "EnsureShape".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type and contents as `x`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`tf.errors.InvalidArgumentError`
</td>
<td>
If `shape` is incompatible with the shape
of `x`.
</td>
</tr>
</table>

