

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.model_pruning.Pruning

## Class `Pruning`





Defined in [`tensorflow/contrib/model_pruning/python/pruning.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/model_pruning/python/pruning.py).



## Methods

<h3 id="__init__"><code>__init__</code></h3>

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

<h3 id="add_pruning_summaries"><code>add_pruning_summaries</code></h3>

``` python
add_pruning_summaries()
```

Adds summaries for this pruning spec.

Args: none

Returns: none

<h3 id="conditional_mask_update_op"><code>conditional_mask_update_op</code></h3>

``` python
conditional_mask_update_op()
```



<h3 id="mask_update_op"><code>mask_update_op</code></h3>

``` python
mask_update_op()
```



<h3 id="print_hparams"><code>print_hparams</code></h3>

``` python
print_hparams()
```





