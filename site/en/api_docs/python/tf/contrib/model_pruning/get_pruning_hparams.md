page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.model_pruning.get_pruning_hparams

``` python
tf.contrib.model_pruning.get_pruning_hparams()
```



Defined in [`tensorflow/contrib/model_pruning/python/pruning.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/model_pruning/python/pruning.py).

Get a tf.HParams object with the default values for the hyperparameters.

  name: string
    name of the pruning specification. Used for adding summaries and ops under
    a common tensorflow name_scope
  begin_pruning_step: integer
    the global step at which to begin pruning
  end_pruning_step: integer
    the global step at which to terminate pruning. Defaults to -1 implying
    that pruning continues till the training stops
  weight_sparsity_map: list of strings
     comma separed list of weight variable name:target sparsity pairs.
     For layers/weights not in this list, sparsity as specified by the
     target_sparsity hyperparameter is used.
     Eg. [conv1:0.9,conv2/kernel:0.8]
  threshold_decay: float
    the decay factor to use for exponential decay of the thresholds
  pruning_frequency: integer
    How often should the masks be updated? (in # of global_steps)
  nbins: integer
    number of bins to use for histogram computation
  block_height: integer
    number of rows in a block (defaults to 1)
  block_width: integer
    number of cols in a block (defaults to 1)
  block_pooling_function: string
    Whether to perform average (AVG) or max (MAX) pooling in the block
    (default: AVG)
  initial_sparsity: float
    initial sparsity value
  target_sparsity: float
    target sparsity value
  sparsity_function_begin_step: integer
    the global step at this which the gradual sparsity function begins to
    take effect
  sparsity_function_end_step: integer
    the global step used as the end point for the gradual sparsity function
  sparsity_function_exponent: float
    exponent = 1 is linearly varying sparsity between initial and final.
    exponent > 1 varies more slowly towards the end than the beginning
  use_tpu: False
    Indicates whether to use TPU

  We use the following sparsity function:

  num_steps = (sparsity_function_end_step -
               sparsity_function_begin_step)/pruning_frequency
  sparsity(step) = (initial_sparsity - target_sparsity)*
                   [1-step/(num_steps -1)]**exponent + target_sparsity

#### Args:

None


#### Returns:

tf.HParams object initialized to default values