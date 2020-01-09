page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.input_pipeline.obtain_next


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/input_pipeline/python/ops/input_pipeline_ops.py#L35-L46">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Basic wrapper for the ObtainNextOp.

``` python
tf.contrib.input_pipeline.obtain_next(
    string_list_tensor,
    counter
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`string_list_tensor`</b>: A tensor that is a list of strings
* <b>`counter`</b>: an int64 ref tensor to keep track of which element is returned.


#### Returns:

An op that produces the element at counter + 1 in the list, round
robin style.
