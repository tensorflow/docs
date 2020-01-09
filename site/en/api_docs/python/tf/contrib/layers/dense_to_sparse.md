page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.dense_to_sparse


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/layers.py#L1547-L1569">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts a dense tensor into a sparse tensor.

``` python
tf.contrib.layers.dense_to_sparse(
    tensor,
    eos_token=0,
    outputs_collections=None,
    scope=None
)
```



<!-- Placeholder for "Used in" -->

An example use would be to convert dense labels to sparse ones
so that they can be fed to the ctc_loss.

#### Args:


* <b>`tensor`</b>: An `int` `Tensor` to be converted to a `Sparse`.
* <b>`eos_token`</b>: An integer. It is part of the target label that signifies the
  end of a sentence.
* <b>`outputs_collections`</b>: Collection to add the outputs.
* <b>`scope`</b>: Optional scope for name_scope.
