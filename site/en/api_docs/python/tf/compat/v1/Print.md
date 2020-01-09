page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.Print


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/logging_ops.py#L66-L112">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Prints a list of tensors. (deprecated)

``` python
tf.compat.v1.Print(
    input_,
    data,
    message=None,
    first_n=None,
    summarize=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2018-08-20.
Instructions for updating:
Use tf.print instead of tf.Print. Note that tf.print returns a no-output operator that directly prints the output. Outside of defuns or eager mode, this operator will not be executed unless it is directly specified in session.run or used as a control dependency for other operators. This is only a concern in graph mode. Below is an example of how to ensure tf.print executes in graph mode:


This is an identity op (behaves like <a href="../../../tf/identity"><code>tf.identity</code></a>) with the side effect
of printing `data` when evaluating.

Note: This op prints to the standard error. It is not currently compatible
  with jupyter notebook (printing to the notebook *server's* output, not into
  the notebook).

#### Args:


* <b>`input_`</b>: A tensor passed through this op.
* <b>`data`</b>: A list of tensors to print out when op is evaluated.
* <b>`message`</b>: A string, prefix of the error message.
* <b>`first_n`</b>: Only log `first_n` number of times. Negative numbers log always;
  this is the default.
* <b>`summarize`</b>: Only print this many entries of each tensor. If None, then a
  maximum of 3 elements are printed per input tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type and contents as `input_`.

>     sess = tf.compat.v1.Session()
>     with sess.as_default():
>         tensor = tf.range(10)
>         print_op = tf.print(tensor)
>         with tf.control_dependencies([print_op]):
>           out = tf.add(tensor, tensor)
>         sess.run(out)
    Additionally, to use tf.print in python 2.7, users must make sure to import
    the following:


`from __future__ import print_function`
