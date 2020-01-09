page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_all_finite


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/debugging/assert_all_finite">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/numerics.py#L31-L49">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Assert that the tensor does not contain any NaN's or Inf's.

### Aliases:

* <a href="/api_docs/python/tf/debugging/assert_all_finite"><code>tf.compat.v1.debugging.assert_all_finite</code></a>
* <a href="/api_docs/python/tf/debugging/assert_all_finite"><code>tf.compat.v1.verify_tensor_all_finite</code></a>
* <a href="/api_docs/python/tf/debugging/assert_all_finite"><code>tf.verify_tensor_all_finite</code></a>


``` python
tf.debugging.assert_all_finite(
    t=None,
    msg=None,
    name=None,
    x=None,
    message=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`t`</b>: Tensor to check.
* <b>`msg`</b>: Message to log on failure.
* <b>`name`</b>: A name for this operation (optional).
* <b>`x`</b>: Alias for t.
* <b>`message`</b>: Alias for msg.


#### Returns:

Same tensor as `t`.
