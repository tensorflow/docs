description: Create a TensorProto.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.make_tensor_proto" />
<meta itemprop="path" content="Stable" />
</div>

# tf.make_tensor_proto

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/tensor_util.py#L361-L566">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Create a TensorProto.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.make_tensor_proto`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.make_tensor_proto(
    values, dtype=None, shape=None, verify_shape=(False), allow_broadcast=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

In TensorFlow 2.0, representing tensors as protos should no longer be a
common workflow. That said, this utility function is still useful for
generating TF Serving request protos:

```python
  request = tensorflow_serving.apis.predict_pb2.PredictRequest()
  request.model_spec.name = "my_model"
  request.model_spec.signature_name = "serving_default"
  request.inputs["images"].CopyFrom(tf.make_tensor_proto(X_new))
```

`make_tensor_proto` accepts "values" of a python scalar, a python list, a
numpy ndarray, or a numpy scalar.

If "values" is a python scalar or a python list, make_tensor_proto
first convert it to numpy ndarray. If dtype is None, the
conversion tries its best to infer the right numpy data
type. Otherwise, the resulting numpy array has a compatible data
type with the given dtype.

In either case above, the numpy ndarray (either the caller provided
or the auto-converted) must have the compatible type with dtype.

`make_tensor_proto` then converts the numpy array to a tensor proto.

If "shape" is None, the resulting tensor proto represents the numpy
array precisely.

Otherwise, "shape" specifies the tensor's shape and the numpy array
can not have more elements than what "shape" specifies.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`values`
</td>
<td>
Values to put in the TensorProto.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Optional tensor_pb2 DataType value.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
List of integers representing the dimensions of tensor.
</td>
</tr><tr>
<td>
`verify_shape`
</td>
<td>
Boolean that enables verification of a shape of values.
</td>
</tr><tr>
<td>
`allow_broadcast`
</td>
<td>
Boolean that enables allowing scalars and 1 length vector
broadcasting. Cannot be true when verify_shape is true.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `TensorProto`. Depending on the type, it may contain data in the
"tensor_content" attribute, which is not directly useful to Python programs.
To access the values you should convert the proto back to a numpy ndarray
with <a href="../tf/make_ndarray.md"><code>tf.make_ndarray(proto)</code></a>.

If `values` is a `TensorProto`, it is immediately returned; `dtype` and
`shape` are ignored.
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
if unsupported types are provided.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if arguments have inappropriate values or if verify_shape is
True and shape of values is not equals to a shape from the argument.
</td>
</tr>
</table>

