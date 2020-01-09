page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.model_pruning.Pruning


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/model_pruning/python/pruning.py#L232-L622">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Pruning`





<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/model_pruning/python/pruning.py#L234-L281">View source</a>

``` python
__init__(
    spec=None,
    global_step=None,
    sparsity=None
)
```

Set up the specification for model pruning.

If a spec is provided, the sparsity is set up based on the sparsity_function
in the spec. The effect of sparsity_function is overridden if the sparsity
variable is passed to the constructor. This enables setting up arbitrary
sparsity profiles externally and passing it to this pruning functions.

#### Args:


* <b>`spec`</b>: Pruning spec as defined in pruning.proto
* <b>`global_step`</b>: A tensorflow variable that is used while setting up the
  sparsity function
* <b>`sparsity`</b>: A tensorflow scalar variable storing the sparsity



## Methods

<h3 id="add_pruning_summaries"><code>add_pruning_summaries</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/model_pruning/python/pruning.py#L610-L619">View source</a>

``` python
add_pruning_summaries()
```

Adds summaries of weight sparsities and thresholds.


<h3 id="conditional_mask_update_op"><code>conditional_mask_update_op</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/model_pruning/python/pruning.py#L583-L608">View source</a>

``` python
conditional_mask_update_op()
```




<h3 id="mask_update_op"><code>mask_update_op</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/model_pruning/python/pruning.py#L569-L581">View source</a>

``` python
mask_update_op()
```




<h3 id="print_hparams"><code>print_hparams</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/model_pruning/python/pruning.py#L621-L622">View source</a>

``` python
print_hparams()
```
