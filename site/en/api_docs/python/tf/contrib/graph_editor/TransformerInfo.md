page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.TransformerInfo


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/transform.py#L194-L316">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TransformerInfo`

"Contains information about the result of a transform operation.



<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/transform.py#L197-L209">View source</a>

``` python
__init__(info)
```

Constructor.


#### Args:


* <b>`info`</b>: an instance of Transformer._TmpInfo containing various internal
  information about the transform operation.



## Methods

<h3 id="original"><code>original</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/transform.py#L281-L297">View source</a>

``` python
original(
    transformed,
    missing_fn=None
)
```

Return the original op/tensor corresponding to the transformed one.

Note that the output of this function mimics the hierarchy
of its input argument `transformed`.
Given an iterable, it returns a list. Given an operation or a tensor,
it will return an operation or a tensor.

#### Args:


* <b>`transformed`</b>: the transformed tensor/operation.
* <b>`missing_fn`</b>: function handling the case where the counterpart
  cannot be found. By default, None is returned.

#### Returns:

the original tensor/operation (or None if no match is found).


<h3 id="transformed"><code>transformed</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/transform.py#L263-L279">View source</a>

``` python
transformed(
    original,
    missing_fn=None
)
```

Return the transformed op/tensor corresponding to the original one.

Note that the output of this function mimics the hierarchy
of its input argument `original`.
Given an iterable, it returns a list. Given an operation or a tensor,
it will return an operation or a tensor.

#### Args:


* <b>`original`</b>: the original tensor/operation.
* <b>`missing_fn`</b>: function handling the case where the counterpart
  cannot be found. By default, None is returned.

#### Returns:

the transformed tensor/operation (or None if no match is found).
