description: Registers a function for converting objects of base_type to Tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.register_tensor_conversion_function" />
<meta itemprop="path" content="Stable" />
</div>

# tf.register_tensor_conversion_function

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/tensor_conversion_registry.py#L56-L111">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Registers a function for converting objects of `base_type` to `Tensor`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.register_tensor_conversion_function`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.register_tensor_conversion_function(
    base_type, conversion_func, priority=100
)
</code></pre>



<!-- Placeholder for "Used in" -->

The conversion function must have the following signature:

```python
    def conversion_func(value, dtype=None, name=None, as_ref=False):
      # ...
```

It must return a `Tensor` with the given `dtype` if specified. If the
conversion function creates a new `Tensor`, it should use the given
`name` if specified. All exceptions will be propagated to the caller.

The conversion function may return `NotImplemented` for some
inputs. In this case, the conversion process will continue to try
subsequent conversion functions.

If `as_ref` is true, the function must return a `Tensor` reference,
such as a `Variable`.

NOTE: The conversion functions will execute in order of priority,
followed by order of registration. To ensure that a conversion function
`F` runs before another conversion function `G`, ensure that `F` is
registered with a smaller priority than `G`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`base_type`
</td>
<td>
The base type or tuple of base types for all objects that
`conversion_func` accepts.
</td>
</tr><tr>
<td>
`conversion_func`
</td>
<td>
A function that converts instances of `base_type` to
`Tensor`.
</td>
</tr><tr>
<td>
`priority`
</td>
<td>
Optional integer that indicates the priority for applying this
conversion function. Conversion functions with smaller priority values run
earlier than conversion functions with larger priority values. Defaults to
100.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If the arguments do not have the appropriate type.
</td>
</tr>
</table>

