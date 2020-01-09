page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.print_tensor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L3366-L3394">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Prints `message` and the tensor value when evaluated.

### Aliases:

* `tf.compat.v1.keras.backend.print_tensor`
* `tf.compat.v2.keras.backend.print_tensor`


``` python
tf.keras.backend.print_tensor(
    x,
    message=''
)
```



<!-- Placeholder for "Used in" -->

Note that `print_tensor` returns a new tensor identical to `x`
which should be used in the following code. Otherwise the
print operation is not taken into account during evaluation.

#### Example:

   <pre class="devsite-click-to-copy prettyprint lang-py">
   <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}x = K.print_tensor(x, message="x is: "){% endhtmlescape %}</code>
   </pre>

#### Arguments:


* <b>`x`</b>: Tensor to print.
* <b>`message`</b>: Message to print jointly with the tensor.


#### Returns:

The same tensor `x`, unchanged.
