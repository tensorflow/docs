description: Interpreter interface for TensorFlow Lite Models.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.lite.Interpreter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="allocate_tensors"/>
<meta itemprop="property" content="get_input_details"/>
<meta itemprop="property" content="get_output_details"/>
<meta itemprop="property" content="get_tensor"/>
<meta itemprop="property" content="get_tensor_details"/>
<meta itemprop="property" content="invoke"/>
<meta itemprop="property" content="reset_all_variables"/>
<meta itemprop="property" content="resize_tensor_input"/>
<meta itemprop="property" content="set_tensor"/>
<meta itemprop="property" content="tensor"/>
</div>

# tf.lite.Interpreter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/lite/python/interpreter.py#L169-L514">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Interpreter interface for TensorFlow Lite Models.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.lite.Interpreter`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.lite.Interpreter(
    model_path=None, model_content=None, experimental_delegates=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This makes the TensorFlow Lite interpreter accessible in Python.
It is possible to use this interpreter in a multithreaded Python environment,
but you must be sure to call functions of a particular instance from only
one thread at a time. So if you want to have 4 threads running different
inferences simultaneously, create  an interpreter for each one as thread-local
data. Similarly, if you are calling invoke() in one thread on a single
interpreter but you want to use tensor() on another thread once it is done,
you must use a synchronization primitive between the threads to ensure invoke
has returned before calling tensor().

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`model_path`
</td>
<td>
Path to TF-Lite Flatbuffer file.
</td>
</tr><tr>
<td>
`model_content`
</td>
<td>
Content of model.
</td>
</tr><tr>
<td>
`experimental_delegates`
</td>
<td>
Experimental. Subject to change. List of
[TfLiteDelegate](https://www.tensorflow.org/lite/performance/delegates)
objects returned by lite.load_delegate().
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If the interpreter was unable to create.
</td>
</tr>
</table>



## Methods

<h3 id="allocate_tensors"><code>allocate_tensors</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/lite/python/interpreter.py#L240-L242">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>allocate_tensors()
</code></pre>




<h3 id="get_input_details"><code>get_input_details</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/lite/python/interpreter.py#L380-L388">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_input_details()
</code></pre>

Gets model input details.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of input details.
</td>
</tr>

</table>



<h3 id="get_output_details"><code>get_output_details</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/lite/python/interpreter.py#L423-L431">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_output_details()
</code></pre>

Gets model output details.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of output details.
</td>
</tr>

</table>



<h3 id="get_tensor"><code>get_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/lite/python/interpreter.py#L433-L446">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_tensor(
    tensor_index
)
</code></pre>

Gets the value of the input tensor (get a copy).

If you wish to avoid the copy, use `tensor()`. This function cannot be used
to read intermediate results.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`tensor_index`
</td>
<td>
Tensor index of tensor to get. This value can be gotten from
the 'index' field in get_output_details.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
a numpy array.
</td>
</tr>

</table>



<h3 id="get_tensor_details"><code>get_tensor_details</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/lite/python/interpreter.py#L363-L378">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_tensor_details()
</code></pre>

Gets tensor details for every tensor with valid tensor details.

Tensors where required information about the tensor is not found are not
added to the list. This includes temporary tensors without a name.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of dictionaries containing tensor information.
</td>
</tr>

</table>



<h3 id="invoke"><code>invoke</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/lite/python/interpreter.py#L498-L511">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>invoke()
</code></pre>

Invoke the interpreter.

Be sure to set the input sizes, allocate tensors and fill values before
calling this. Also, note that this function releases the GIL so heavy
computation can be done in the background while the Python interpreter
continues. No other function on this object should be called while the
invoke() call has not finished.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
When the underlying interpreter fails raise ValueError.
</td>
</tr>
</table>



<h3 id="reset_all_variables"><code>reset_all_variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/lite/python/interpreter.py#L513-L514">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_all_variables()
</code></pre>




<h3 id="resize_tensor_input"><code>resize_tensor_input</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/lite/python/interpreter.py#L406-L421">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>resize_tensor_input(
    input_index, tensor_size
)
</code></pre>

Resizes an input tensor.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`input_index`
</td>
<td>
Tensor index of input to set. This value can be gotten from
the 'index' field in get_input_details.
</td>
</tr><tr>
<td>
`tensor_size`
</td>
<td>
The tensor_shape to resize the input to.
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
If the interpreter could not resize the input tensor.
</td>
</tr>
</table>



<h3 id="set_tensor"><code>set_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/lite/python/interpreter.py#L390-L404">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_tensor(
    tensor_index, value
)
</code></pre>

Sets the value of the input tensor. Note this copies data in `value`.

If you want to avoid copying, you can use the `tensor()` function to get a
numpy buffer pointing to the input buffer in the tflite interpreter.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`tensor_index`
</td>
<td>
Tensor index of tensor to set. This value can be gotten from
the 'index' field in get_input_details.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
Value of tensor to set.
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
If the interpreter could not set the tensor.
</td>
</tr>
</table>



<h3 id="tensor"><code>tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/lite/python/interpreter.py#L448-L496">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tensor(
    tensor_index
)
</code></pre>

Returns function that gives a numpy view of the current tensor buffer.

This allows reading and writing to this tensors w/o copies. This more
closely mirrors the C++ Interpreter class interface's tensor() member, hence
the name. Be careful to not hold these output references through calls
to `allocate_tensors()` and `invoke()`. This function cannot be used to read
intermediate results.

#### Usage:



```
interpreter.allocate_tensors()
input = interpreter.tensor(interpreter.get_input_details()[0]["index"])
output = interpreter.tensor(interpreter.get_output_details()[0]["index"])
for i in range(10):
  input().fill(3.)
  interpreter.invoke()
  print("inference %s" % output())
```

Notice how this function avoids making a numpy array directly. This is
because it is important to not hold actual numpy views to the data longer
than necessary. If you do, then the interpreter can no longer be invoked,
because it is possible the interpreter would resize and invalidate the
referenced tensors. The NumPy API doesn't allow any mutability of the
the underlying buffers.

#### WRONG:



```
input = interpreter.tensor(interpreter.get_input_details()[0]["index"])()
output = interpreter.tensor(interpreter.get_output_details()[0]["index"])()
interpreter.allocate_tensors()  # This will throw RuntimeError
for i in range(10):
  input.fill(3.)
  interpreter.invoke()  # this will throw RuntimeError since input,output
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`tensor_index`
</td>
<td>
Tensor index of tensor to get. This value can be gotten from
the 'index' field in get_output_details.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A function that can return a new numpy array pointing to the internal
TFLite tensor state at any point. It is safe to hold the function forever,
but it is not safe to hold the numpy array forever.
</td>
</tr>

</table>





