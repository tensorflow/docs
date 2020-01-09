page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.print


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/logging_ops.py#L138-L383">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Print the specified inputs.

### Aliases:

* `tf.compat.v1.print`
* `tf.compat.v2.print`


``` python
tf.print(
    *inputs,
    **kwargs
)
```



### Used in the guide:

* [Better performance with tf.function and AutoGraph](https://www.tensorflow.org/guide/function)
* [Using the SavedModel format](https://www.tensorflow.org/guide/saved_model)

### Used in the tutorials:

* [Better performance with tf.function](https://www.tensorflow.org/tutorials/customization/performance)



A TensorFlow operator that prints the specified inputs to a desired
output stream or logging level. The inputs may be dense or sparse Tensors,
primitive python objects, data structures that contain tensors, and printable
Python objects. Printed tensors will recursively show the first and last
elements of each dimension to summarize.



#### Example:

Single-input usage:

```python
tensor = tf.range(10)
tf.print(tensor, output_stream=sys.stderr)
```

(This prints "[0 1 2 ... 7 8 9]" to sys.stderr)

Multi-input usage:

```python
tensor = tf.range(10)
tf.print("tensors:", tensor, {2: tensor * 2}, output_stream=sys.stdout)
```

(This prints "tensors: [0 1 2 ... 7 8 9] {2: [0 2 4 ... 14 16 18]}" to
sys.stdout)

Changing the input separator:

```python
tensor_a = tf.range(2)
tensor_b = tensor_a * 2
tf.print(tensor_a, tensor_b, output_stream=sys.stderr, sep=',')
```

(This prints "[0 1],[0 2]" to sys.stderr)

Usage in a <a href="../tf/function"><code>tf.function</code></a>:

```python
@tf.function
def f():
    tensor = tf.range(10)
    tf.print(tensor, output_stream=sys.stderr)
    return tensor

range_tensor = f()
```

(This prints "[0 1 2 ... 7 8 9]" to sys.stderr)


@compatibility(TF 1.x Graphs and Sessions)
In graphs manually created outside of <a href="../tf/function"><code>tf.function</code></a>, this method returns
the created TF operator that prints the data. To make sure the
operator runs, users need to pass the produced op to
<a href="../tf/compat/v1/Session"><code>tf.compat.v1.Session</code></a>'s run method, or to use the op as a control
dependency for executed ops by specifying
`with tf.compat.v1.control_dependencies([print_op])`.
@end_compatibility

  Compatibility usage in TF 1.x graphs:

>     sess = tf.compat.v1.Session()
>     with sess.as_default():
>         tensor = tf.range(10)
>         print_op = tf.print("tensors:", tensor, {2: tensor * 2},
>                             output_stream=sys.stdout)
>         with tf.control_dependencies([print_op]):
>           tripled_tensor = tensor * 3
>         sess.run(tripled_tensor)

  (This prints "tensors: [0 1 2 ... 7 8 9] {2: [0 2 4 ... 14 16 18]}" to
  sys.stdout)

Note: In Jupyter notebooks and colabs, <a href="../tf/print"><code>tf.print</code></a> prints to the notebook
  cell outputs. It will not write to the notebook kernel's console logs.

#### Args:


* <b>`*inputs`</b>: Positional arguments that are the inputs to print. Inputs in the
  printed output will be separated by spaces. Inputs may be python
  primitives, tensors, data structures such as dicts and lists that may
  contain tensors (with the data structures possibly nested in arbitrary
  ways), and printable python objects.
* <b>`output_stream`</b>: The output stream, logging level, or file to print to.
  Defaults to sys.stderr, but sys.stdout, tf.compat.v1.logging.info,
  tf.compat.v1.logging.warning, tf.compat.v1.logging.error,
  absl.logging.info, absl.logging.warning and absl.loogging,error are also
  supported. To print to a file, pass a string started with "file://"
  followed by the file path, e.g., "file:///tmp/foo.out".
* <b>`summarize`</b>: The first and last `summarize` elements within each dimension are
  recursively printed per Tensor. If None, then the first 3 and last 3
  elements of each dimension are printed for each tensor. If set to -1, it
  will print all elements of every tensor.
* <b>`sep`</b>: The string to use to separate the inputs. Defaults to " ".
* <b>`end`</b>: End character that is appended at the end the printed string.
  Defaults to the newline character.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

None when executing eagerly. During graph tracing this returns
a TF operator that prints the specified inputs in the specified output
stream or logging level. This operator will be automatically executed
except inside of <a href="../tf/compat/v1"><code>tf.compat.v1</code></a> graphs and sessions.



#### Raises:


* <b>`ValueError`</b>: If an unsupported output stream is specified.

#### Python2 Compatibility
In python 2.7, make sure to import the following:
`from __future__ import print_function`
