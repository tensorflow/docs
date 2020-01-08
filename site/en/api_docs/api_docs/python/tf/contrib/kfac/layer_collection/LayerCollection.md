

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.layer_collection.LayerCollection

## Class `LayerCollection`





Defined in [`tensorflow/contrib/kfac/python/ops/layer_collection.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/kfac/python/ops/layer_collection.py).

Registry of information about layers and losses.

Note that you need to create a new one of these for each MatrixEstimator or
KfacOptimizer.

#### Attributes:

* <b>`fisher_blocks`</b>: a LayersParamsDict (subclass of OrderedDict) mapping layer
      parameters (Tensors or tuples of Tensors) to FisherBlock instances.
* <b>`fisher_factors`</b>: an OrderedDict mapping tuples to FisherFactor instances.
* <b>`losses`</b>: a list of LossFunction objects. The loss to be optimized is their
      sum.
* <b>`loss_colocation_ops`</b>: ops to colocate loss function evaluations with.  These
      will typically be the inputs to the losses.

## Properties

<h3 id="default_conv2d_approximation"><code>default_conv2d_approximation</code></h3>



<h3 id="default_conv2d_multi_approximation"><code>default_conv2d_multi_approximation</code></h3>



<h3 id="default_embedding_approximation"><code>default_embedding_approximation</code></h3>



<h3 id="default_embedding_multi_approximation"><code>default_embedding_multi_approximation</code></h3>



<h3 id="default_fully_connected_approximation"><code>default_fully_connected_approximation</code></h3>



<h3 id="default_fully_connected_multi_approximation"><code>default_fully_connected_multi_approximation</code></h3>



<h3 id="default_generic_approximation"><code>default_generic_approximation</code></h3>



<h3 id="graph"><code>graph</code></h3>



<h3 id="linked_parameters"><code>linked_parameters</code></h3>

Groups of parameters with an optionally specified approximation.

Linked parameters can be added using `define_linked_parameters`.
If an approximation is specified, then this approximation will be used
when registering a layer with exactly these parameters, unless an
approximation is specified when calling the registration function.

#### Returns:

A `dict` mapping tuples of parameters to an optional string.

<h3 id="losses"><code>losses</code></h3>

Tuple of LossFunction objects registered with this LayerCollection.

<h3 id="registered_variables"><code>registered_variables</code></h3>

A tuple of all of the variables currently registered.

<h3 id="subgraph"><code>subgraph</code></h3>



<h3 id="towers_by_loss"><code>towers_by_loss</code></h3>

Tuple across losses of LossFunction objects registered to each tower.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    graph=None,
    name='LayerCollection'
)
```



<h3 id="as_default"><code>as_default</code></h3>

``` python
as_default(
    *args,
    **kwds
)
```

Sets this LayerCollection as the default.

<h3 id="check_registration"><code>check_registration</code></h3>

``` python
check_registration(variables)
```

Checks that all variable uses have been registered properly.

#### Args:

* <b>`variables`</b>: List of variables.


#### Raises:

* <b>`ValueError`</b>: If any registered variables are not included in the list.
* <b>`ValueError`</b>: If any variable in the list is not registered.
* <b>`ValueError`</b>: If any variable in the list is registered with the wrong
      number of "uses" in the subgraph recorded (vs the number of times that
      variable is actually used in the subgraph).

<h3 id="create_subgraph"><code>create_subgraph</code></h3>

``` python
create_subgraph()
```



<h3 id="define_linked_parameters"><code>define_linked_parameters</code></h3>

``` python
define_linked_parameters(
    params,
    approximation=None
)
```

Identify a set of parameters that should be grouped together.

During automatic graph scanning, any matches containing variables that have
been identified as part of a linked group will be filtered out unless
the match parameters are exactly equal to the ones specified in the linked
group.

#### Args:

* <b>`params`</b>: A variable, or a tuple or list of variables. The variables
    to be linked.
* <b>`approximation`</b>: Optional string specifying the type of approximation to use
    for these variables. If unspecified, this layer collection's default
    approximation for the layer type will be used.


#### Raises:

* <b>`ValueError`</b>: If the parameters were already registered in a layer or
    identified as part of an incompatible group.

<h3 id="eval_losses"><code>eval_losses</code></h3>

``` python
eval_losses()
```

Return evaluated losses (colocated with inputs to losses).

<h3 id="eval_losses_on_samples"><code>eval_losses_on_samples</code></h3>

``` python
eval_losses_on_samples()
```

Return losses evaluated on samples (colocated with inputs to losses).

<h3 id="get_blocks"><code>get_blocks</code></h3>

``` python
get_blocks()
```



<h3 id="get_factors"><code>get_factors</code></h3>

``` python
get_factors()
```



<h3 id="make_or_get_factor"><code>make_or_get_factor</code></h3>

``` python
make_or_get_factor(
    cls,
    args
)
```

Insert `cls(args)` into 'self.fisher_factors` if not already present.

Wraps constructor in `tf.variable_scope()` to ensure variables constructed
in `cls.__init__` are placed under this LayerCollection's scope.

#### Args:

* <b>`cls`</b>: Class that implements FisherFactor.
* <b>`args`</b>: Tuple of arguments to pass into `cls's constructor. Must be
    hashable.


#### Returns:

Instance of `cls` found in self.fisher_factors.

<h3 id="register_block"><code>register_block</code></h3>

``` python
register_block(
    layer_key,
    fisher_block,
    reuse=VARIABLE_SCOPE
)
```

Validates and registers the layer_key associated with the fisher_block.

#### Args:

* <b>`layer_key`</b>: A variable or tuple of variables. The key to check for in
      existing registrations and to register if valid.
* <b>`fisher_block`</b>: The associated `FisherBlock`.
* <b>`reuse`</b>: Method to use for inserting new `FisherBlock's. One of True, False,
    or `VARIABLE_SCOPE`.


#### Raises:

* <b>`ValueError`</b>: If `layer_key` was already registered and reuse is `False`,
    if `layer_key` was registered with a different block type, or if
    `layer_key` shares any variables with but is not equal to a previously
    registered key.
* <b>`KeyError`</b>: If `reuse` is `True` but `layer_key` was not previously
    registered.


#### Returns:

The `FisherBlock` registered under `layer_key`. If `layer_key` was already
registered, this will be the previously registered `FisherBlock`.

<h3 id="register_categorical_predictive_distribution"><code>register_categorical_predictive_distribution</code></h3>

``` python
register_categorical_predictive_distribution(
    logits,
    seed=None,
    targets=None,
    name=None,
    reuse=VARIABLE_SCOPE
)
```

Registers a categorical predictive distribution.

#### Args:

* <b>`logits`</b>: The logits of the distribution (i.e. its parameters).
* <b>`seed`</b>: The seed for the RNG (for debugging) (Default: None)
* <b>`targets`</b>: (OPTIONAL) The targets for the loss function.  Only required if
    one wants to call total_loss() instead of total_sampled_loss().
    total_loss() is required, for example, to estimate the
    "empirical Fisher" (instead of the true Fisher).
    (Default: None)
* <b>`name`</b>: (OPTIONAL) str or None. Unique name for this loss function. If None,
    a new name is generated. (Default: None)
* <b>`reuse`</b>: bool or str.  If True, this adds `logits` as an additional
    mini-batch/tower of inputs to the loss-function/predictive distribution
    (which must have already been registered). If "VARIABLE_SCOPE", use
    tf.get_variable_scope().reuse. (Default: "VARIABLE_SCOPE")

<h3 id="register_conv2d"><code>register_conv2d</code></h3>

``` python
register_conv2d(
    params,
    strides,
    padding,
    inputs,
    outputs,
    data_format=None,
    dilations=None,
    approx=None,
    reuse=VARIABLE_SCOPE
)
```

Registers a call to tf.nn.conv2d().

#### Args:

* <b>`params`</b>: Tensor or 2-tuple of Tensors corresponding to weight and bias of
    this layer. Weight matrix should have shape [kernel_height,
    kernel_width, in_channels, out_channels].  Bias should have shape
    [out_channels].
* <b>`strides`</b>: List of 4 ints. Strides for convolution kernel.
* <b>`padding`</b>: string. see tf.nn.conv2d for valid values.
* <b>`inputs`</b>: Tensor of shape [batch_size, height, width, in_channels]. Inputs
    to layer.
* <b>`outputs`</b>: Tensor of shape [batch_size, height, width, out_channels].
    Output produced by layer.
* <b>`data_format`</b>: str or None. Format of data.
* <b>`dilations`</b>: List of 4 ints. Dilations along each dimension.
* <b>`approx`</b>: str or None. If not None must be one of "kron" or "diagonal".
    The Fisher approximation to use. If None the default value is used.
    (Default: None)
* <b>`reuse`</b>: bool or str.  If True, this adds `inputs` and `outputs` as an
    additional mini-batch/tower of data to use when estimating the Fisher
    block for this layer (which must have already been registered). If
    "VARIABLE_SCOPE", use tf.get_variable_scope().reuse.
    (Default: "VARIABLE_SCOPE")


#### Raises:

* <b>`ValueError`</b>: For improper value to `approx`.
* <b>`KeyError`</b>: If reuse == True but no FisherBlock found for `params`.
* <b>`ValueError`</b>: If reuse == True and FisherBlock found but of the wrong type.

<h3 id="register_conv2d_multi"><code>register_conv2d_multi</code></h3>

``` python
register_conv2d_multi(
    params,
    strides,
    padding,
    inputs,
    outputs,
    num_uses=None,
    data_format=None,
    dilations=None,
    approx=None,
    reuse=VARIABLE_SCOPE
)
```

Registers convolutional layers with shared parameters.

#### Args:

* <b>`params`</b>: Tensor or 2-tuple of Tensors corresponding to weight and bias of
    this layer. Weight matrix should have shape [kernel_height,
    kernel_width, in_channels, out_channels].  Bias should have shape
    [out_channels].
* <b>`strides`</b>: 1-D Tensor of length 4. Strides for convolution kernel.
* <b>`padding`</b>: string. see tf.nn.conv2d for valid values.
* <b>`inputs`</b>: A list of Tensors, each of shape [batch_size, height, width,
    in_channels]. Inputs to layer. The list indexes each use in the graph
    (which might correspond to a "time-step" in an RNN). OR, can be single
    Tensor, of shape [num_uses * batch_size, height, width, in_channels],
    which is a reshaped version of a Tensor of shape [num_uses, batch_size,
    height, width, in_channels].
* <b>`outputs`</b>: A list of Tensors, each of shape [batch_size, height, width,
    out_channels]. Output produced by layer. The list indexes each use
    in the graph (which might correspond to a "time-step" in an RNN).
    Needs to correspond with the order used in `inputs`.  OR, can be a
    single Tensor, of shape [num_uses * batch_size, height, width,
    out_channels], which is a reshaped version of a Tensor of shape
    [num_uses, batch_size, height, width, out_channels].
* <b>`num_uses`</b>: int or None. The number uses/time-steps in the graph where the
    layer appears. Only needed if both inputs and outputs are given in the
    single Tensor format. (Default: None)
* <b>`data_format`</b>: str or None. Format of data.
* <b>`dilations`</b>: List of 4 ints. Dilations along each dimension.
* <b>`approx`</b>: str or None. If not None must by "kron_indep". The Fisher
    approximation to use. If None the default value is used.
    (Default: None)
* <b>`reuse`</b>: bool or str.  If True, this adds `inputs` and `outputs` as an
    additional mini-batch/tower of data to use when estimating the Fisher
    block for this layer (which must have already been registered). If
    "VARIABLE_SCOPE", use tf.get_variable_scope().reuse.  (Note that the
    word `use` here has a completely different meaning to "use in the graph"
    as it perturns to the `inputs`, `outputs`, and `num_uses` arguments.)
    (Default: "VARIABLE_SCOPE")


#### Raises:

* <b>`ValueError`</b>: For improper value to `approx`.
* <b>`KeyError`</b>: If reuse == True but no FisherBlock found for `params`.
* <b>`ValueError`</b>: If reuse == True and FisherBlock found but of the wrong type.

<h3 id="register_convolution"><code>register_convolution</code></h3>

``` python
register_convolution(
    params,
    inputs,
    outputs,
    padding,
    strides=None,
    dilation_rate=None,
    data_format=None,
    approx=None,
    reuse=VARIABLE_SCOPE
)
```

Register a call to tf.nn.convolution().

#### Args:

* <b>`params`</b>: Tensor or 2-tuple of Tensors corresponding to weight and bias of
    this layer. Weight matrix should have shape [..filter_spatial_size..,
    in_channels, out_channels].  Bias should have shape [out_channels].
* <b>`inputs`</b>: Tensor of shape [batch_size, ..input_spatial_size.., in_channels].
    Inputs to layer.
* <b>`outputs`</b>: Tensor of shape [batch_size, ..output_spatial_size..,
    out_channels].  Output produced by layer.
* <b>`padding`</b>: string. see tf.nn.conv2d for valid values.
* <b>`strides`</b>: List of ints of length len(..input_spatial_size..). Strides for
    convolution kernel in spatial dimensions.
* <b>`dilation_rate`</b>: List of ints of length len(..input_spatial_size..).
    Dilations along spatial dimension.
* <b>`data_format`</b>: str or None. Format of data.
* <b>`approx`</b>: str or None. If not None must be one of "kron" or "diagonal".
    The Fisher approximation to use. If None the default value is used.
    (Default: None)
* <b>`reuse`</b>: bool or str.  If True, this adds `inputs` and `outputs` as an
    additional mini-batch/tower of data to use when estimating the Fisher
    block for this layer (which must have already been registered). If
    "VARIABLE_SCOPE", use tf.get_variable_scope().reuse.
    (Default: "VARIABLE_SCOPE")


#### Raises:

* <b>`ValueError`</b>: For improper value to `approx`.
* <b>`KeyError`</b>: If reuse == True but no FisherBlock found for `params`.
* <b>`ValueError`</b>: If reuse == True and FisherBlock found but of the wrong type.

<h3 id="register_depthwise_conv2d"><code>register_depthwise_conv2d</code></h3>

``` python
register_depthwise_conv2d(
    params,
    inputs,
    outputs,
    strides,
    padding,
    rate=None,
    data_format=None,
    approx=None,
    reuse=VARIABLE_SCOPE
)
```

Register a call to tf.nn.depthwise_conv2d().

#### Args:

* <b>`params`</b>: 4-D Tensor of shape [filter_height, filter_width,
    in_channels, channel_multiplier].  Convolutional filter.
* <b>`inputs`</b>: Tensor of shape [batch_size, input_height, input_width,
    in_channels].  Inputs to layer.
* <b>`outputs`</b>: Tensor of shape [batch_size, output_height, output_width,
    in_channels * channel_multiplier].  Output produced by depthwise conv2d.
* <b>`strides`</b>: List of ints of length 4. Strides along all dimensions.
* <b>`padding`</b>: string. see tf.nn.conv2d for valid values.
* <b>`rate`</b>: None or List of ints of length 2. Dilation rates in spatial
    dimensions.
* <b>`data_format`</b>: str or None. Format of data.
* <b>`approx`</b>: str or None. If not None must "diagonal".  The Fisher
    approximation to use. If None the default value is used. (Default: None)
* <b>`reuse`</b>: bool or str.  If True, this adds `inputs` and `outputs` as an
    additional mini-batch/tower of data to use when estimating the Fisher
    block for this layer (which must have already been registered). If
    "VARIABLE_SCOPE", use tf.get_variable_scope().reuse.
    (Default: "VARIABLE_SCOPE")


#### Raises:

* <b>`ValueError`</b>: For improper value to `approx`.
* <b>`KeyError`</b>: If reuse == True but no FisherBlock found for `params`.
* <b>`ValueError`</b>: If reuse == True and FisherBlock found but of the wrong type.

<h3 id="register_embedding"><code>register_embedding</code></h3>

``` python
register_embedding(
    params,
    inputs,
    outputs,
    approx=None,
    reuse=VARIABLE_SCOPE
)
```

Registers an embedding layer.

#### Args:

* <b>`params`</b>: Embedding matrix of shape [vocab_size, embedding_size].
* <b>`inputs`</b>: Tensor of shape [batch_size, input_size] and dtype int32. Indices
    into embedding matrix.
* <b>`outputs`</b>: Tensor of shape [batch_size, embedding_size]. Outputs
    produced by layer.
* <b>`approx`</b>: str or None. If not None must be "kron".  The Fisher
    approximation to use. If None the default value is used. (Default: None)
* <b>`reuse`</b>: bool or str.  If True, this adds `inputs` and `outputs` as an
    additional mini-batch/tower of data to use when estimating the Fisher
    block for this layer (which must have already been registered). If
    "VARIABLE_SCOPE", use tf.get_variable_scope().reuse.
    (Default: "VARIABLE_SCOPE")


#### Raises:

* <b>`ValueError`</b>: For improper value to `approx`.
* <b>`KeyError`</b>: If reuse == True but no FisherBlock found for `params`.
* <b>`ValueError`</b>: If reuse == True and FisherBlock found but of the wrong type.

<h3 id="register_embedding_multi"><code>register_embedding_multi</code></h3>

``` python
register_embedding_multi(
    params,
    inputs,
    outputs,
    num_uses=None,
    approx=None,
    reuse=VARIABLE_SCOPE
)
```

Registers embedding layers with shared parameters.

#### Args:

* <b>`params`</b>: Embedding matrix of shape [vocab_size, embedding_size].
* <b>`inputs`</b>: A list of Tensors, each of shape [batch_size, input_size] and
    dtype int32. Indices into embedding matrix. The list indexes each use
    in the graph (which might correspond to a "time-step" in an RNN).
    OR, can be single Tensor, of shape [num_uses*batch_size, input_size],
    which is a reshaped version of a Tensor of shape [num_uses, batch_size,
    input_size].
* <b>`outputs`</b>: A list of Tensors, each of shape [batch_size, embedding_size].
    Outputs produced by layer. The list indexes each use in the graph
    (which might correspond to a "time-step" in an RNN). Needs to
    correspond with the order used in `inputs`. OR, can be a
    single Tensor, of shape [num_uses * batch_size, embedding_size], which
    is a reshaped version of a Tensor of shape [num_uses, batch_size,
    embedding_size].
* <b>`num_uses`</b>: int or None. The number uses/time-steps in the graph where the
    layer appears. Only needed if both inputs and outputs are given in the
    single Tensor format. (Default: None)
* <b>`approx`</b>: str or None. If not None must by "kron_indep". The Fisher
    approximation to use. If None the default value is used.
    (Default: None)
* <b>`reuse`</b>: bool or str.  If True, this adds `inputs` and `outputs` as an
    additional mini-batch/tower of data to use when estimating the Fisher
    block for this layer (which must have already been registered). If
    "VARIABLE_SCOPE", use tf.get_variable_scope().reuse.  (Note that the
    word `use` here has a completely different meaning to "use in the graph"
    as it perturns to the `inputs`, `outputs`, and `num_uses` arguments.)
    (Default: "VARIABLE_SCOPE")


#### Raises:

* <b>`ValueError`</b>: For improper value to `approx`.
* <b>`KeyError`</b>: If reuse == True but no FisherBlock found for `params`.
* <b>`ValueError`</b>: If reuse == True and FisherBlock found but of the wrong type.

<h3 id="register_fully_connected"><code>register_fully_connected</code></h3>

``` python
register_fully_connected(
    params,
    inputs,
    outputs,
    approx=None,
    reuse=VARIABLE_SCOPE
)
```

Registers a fully connnected layer.

#### Args:

* <b>`params`</b>: Tensor or 2-tuple of Tensors corresponding to weight and bias of
    this layer. Weight matrix should have shape [input_size, output_size].
    Bias should have shape [output_size].
* <b>`inputs`</b>: Tensor of shape [batch_size, input_size]. Inputs to layer.
* <b>`outputs`</b>: Tensor of shape [batch_size, output_size]. Outputs
    produced by layer.
* <b>`approx`</b>: str or None. If not None must be one of "kron" or "diagonal".
    The Fisher approximation to use. If None the default value is used.
    (Default: None)
* <b>`reuse`</b>: bool or str.  If True, this adds `inputs` and `outputs` as an
    additional mini-batch/tower of data to use when estimating the Fisher
    block for this layer (which must have already been registered). If
    "VARIABLE_SCOPE", use tf.get_variable_scope().reuse.
    (Default: "VARIABLE_SCOPE")


#### Raises:

* <b>`ValueError`</b>: For improper value to `approx`.
* <b>`KeyError`</b>: If reuse == True but no FisherBlock found for `params`.
* <b>`ValueError`</b>: If reuse == True and FisherBlock found but of the wrong type.

<h3 id="register_fully_connected_multi"><code>register_fully_connected_multi</code></h3>

``` python
register_fully_connected_multi(
    params,
    inputs,
    outputs,
    num_uses=None,
    approx=None,
    reuse=VARIABLE_SCOPE
)
```

Register fully connected layers with shared parameters.

This can handle general fully-connected layers with shared parameters, but
has specialized approximations to deal with the case where there is a
meaningful linear order to the share instances (such as in an RNN).

#### Args:

* <b>`params`</b>: Tensor or 2-tuple of Tensors corresponding to weight and bias of
    this layer. Weight matrix should have shape [input_size, output_size].
    Bias should have shape [output_size].
* <b>`inputs`</b>: A list of Tensors, each of shape [batch_size, input_size]. Inputs
    to layer. The list indexes each use in the graph (which might
    correspond to a "time-step" in an RNN). OR, can be single Tensor, of
    shape [num_uses * batch_size , input_size], which is a reshaped version
    of a Tensor of shape [num_uses, batch_size, input_size].
* <b>`outputs`</b>: A list of Tensors, the same length as `inputs`, each of shape
    [batch_size, output_size]. Outputs produced by layer. The list indexes
    each use in the graph (which might correspond to a "time-step" in an
    RNN). Needs to correspond with the order used in `inputs`.  OR, can be
    a single Tensor of shape [num_uses * batch_size, output_size], which is
    a reshaped version of a Tensor of shape [num_uses, batch_size,
    output_size].
* <b>`num_uses`</b>: int or None. The number uses/time-steps in the graph where the
    layer appears. Only needed if both inputs and outputs are given in the
    single Tensor format. (Default: None)
* <b>`approx`</b>: str or None. If not None, must be of "kron_indep", "kron_series_1"
    or "kron_series_2". The Fisher approximation to use. If None the default
    value is used. (Default: None)
* <b>`reuse`</b>: bool or str.  If True, this adds `inputs` and `outputs` as an
    additional mini-batch/tower of data to use when estimating the Fisher
    block for this layer (which must have already been registered). If
    "VARIABLE_SCOPE", use tf.get_variable_scope().reuse.  (Note that the
    word `use` here has a completely different meaning to "use in the graph"
    as it perturns to the `inputs`, `outputs`, and `num_uses` arguments.)
    (Default: "VARIABLE_SCOPE")


#### Raises:

* <b>`ValueError`</b>: For improper value to `approx`.

<h3 id="register_generic"><code>register_generic</code></h3>

``` python
register_generic(
    params,
    batch_size,
    approx=None,
    reuse=VARIABLE_SCOPE
)
```

Registers a generic layer.

#### Args:

* <b>`params`</b>: Tensor or tuple of Tensors corresponding to the parameters.
* <b>`batch_size`</b>: 0-D Tensor. Size of the minibatch (for this tower).
* <b>`approx`</b>: str or None. It not None, must be one of "full" or "diagonal".
    The Fisher approximation to use. If None the default value is used.
    (Default: None)
* <b>`reuse`</b>: bool or str. If True, this adds `batch_size` to the total
    mini-batch size use when estimating the Fisher block for this layer
    (which must have already been registered). If "VARIABLE_SCOPE", use
    tf.get_variable_scope().reuse. (Default: "VARIABLE_SCOPE")


#### Raises:

* <b>`ValueError`</b>: For improper value to `approx`.
* <b>`KeyError`</b>: If reuse == True but no FisherBlock found for `params`.
* <b>`ValueError`</b>: If reuse == True and FisherBlock found but of the wrong type.

<h3 id="register_loss_function"><code>register_loss_function</code></h3>

``` python
register_loss_function(
    loss,
    colocation_op,
    base_name,
    name=None,
    reuse=VARIABLE_SCOPE
)
```

Registers a LossFunction object.

#### Args:

* <b>`loss`</b>: The LossFunction object.
* <b>`colocation_op`</b>: The op to colocate the loss function's computations with.
* <b>`base_name`</b>: The name to derive a new unique name from is the name argument
    is None.
* <b>`name`</b>: (OPTIONAL) str or None. Unique name for this loss function. If None,
    a new name is generated. (Default: None)
* <b>`reuse`</b>: (OPTIONAL) bool or str.  If True, adds `loss` as an additional
    tower for the existing loss function.


#### Raises:

* <b>`ValueError`</b>: If reuse == True and name == None.
* <b>`ValueError`</b>: If reuse == True and seed != None.
* <b>`KeyError`</b>: If reuse == True and no existing LossFunction with `name` found.
* <b>`KeyError`</b>: If reuse == False and existing LossFunction with `name` found.

<h3 id="register_multi_bernoulli_predictive_distribution"><code>register_multi_bernoulli_predictive_distribution</code></h3>

``` python
register_multi_bernoulli_predictive_distribution(
    logits,
    seed=None,
    targets=None,
    name=None,
    reuse=VARIABLE_SCOPE
)
```

Registers a multi-Bernoulli predictive distribution.

#### Args:

* <b>`logits`</b>: The logits of the distribution (i.e. its parameters).
* <b>`seed`</b>: The seed for the RNG (for debugging) (Default: None)
* <b>`targets`</b>: (OPTIONAL) The targets for the loss function.  Only required if
    one wants to call total_loss() instead of total_sampled_loss().
    total_loss() is required, for example, to estimate the
    "empirical Fisher" (instead of the true Fisher).
    (Default: None)
* <b>`name`</b>: (OPTIONAL) str or None. Unique name for this loss function. If None,
    a new name is generated. (Default: None)
* <b>`reuse`</b>: bool or str.  If True, this adds `logits` as an additional
    mini-batch/tower of inputs to the loss-function/predictive distribution
    (which must have already been registered). If "VARIABLE_SCOPE", use
    tf.get_variable_scope().reuse. (Default: "VARIABLE_SCOPE")

<h3 id="register_normal_predictive_distribution"><code>register_normal_predictive_distribution</code></h3>

``` python
register_normal_predictive_distribution(
    mean,
    var=0.5,
    seed=None,
    targets=None,
    name=None,
    reuse=VARIABLE_SCOPE
)
```

Registers a normal predictive distribution.

#### Args:

* <b>`mean`</b>: The mean vector defining the distribution.
* <b>`var`</b>: The variance (must be a scalar).  Note that the default value of
    0.5 corresponds to a standard squared error loss (target -
    prediction)**2. If your squared error loss is of the form
    0.5*(target - prediction)**2 you should use var=1.0. (Default: 0.5)
* <b>`seed`</b>: The seed for the RNG (for debugging) (Default: None)
* <b>`targets`</b>: (OPTIONAL) The targets for the loss function.  Only required if
    one wants to call total_loss() instead of total_sampled_loss().
    total_loss() is required, for example, to estimate the
    "empirical Fisher" (instead of the true Fisher).
    (Default: None)
* <b>`name`</b>: (OPTIONAL) str or None. Unique name for this loss function. If None,
    a new name is generated. (Default: None)
* <b>`reuse`</b>: bool or str.  If True, this adds `mean` and `var` as an additional
    mini-batch/tower of inputs to the loss-function/predictive distribution
    (which must have already been registered). If "VARIABLE_SCOPE", use
    tf.get_variable_scope().reuse. (Default: "VARIABLE_SCOPE")

<h3 id="register_separable_conv2d"><code>register_separable_conv2d</code></h3>

``` python
register_separable_conv2d(
    depthwise_params,
    pointwise_params,
    inputs,
    depthwise_outputs,
    pointwise_outputs,
    strides,
    padding,
    rate=None,
    data_format=None,
    approx=None,
    reuse=VARIABLE_SCOPE
)
```

Register a call to tf.nn.separable_conv2d().

Note: This requires access to intermediate outputs between depthwise and
pointwise convolutions.

#### Args:

* <b>`depthwise_params`</b>: 4-D Tensor of shape [filter_height, filter_width,
    in_channels, channel_multiplier].  Filter for depthwise conv2d.
* <b>`pointwise_params`</b>: 4-D Tensor of shape [1, 1, in_channels *
    channel_multiplier, out_channels].  Filter for pointwise conv2d.
* <b>`inputs`</b>: Tensor of shape [batch_size, input_height, input_width,
    in_channels].  Inputs to layer.
* <b>`depthwise_outputs`</b>: Tensor of shape [batch_size, output_height,
    output_width, in_channels * channel_multiplier].  Output produced by
    depthwise conv2d.
* <b>`pointwise_outputs`</b>: Tensor of shape [batch_size, output_height,
    output_width, out_channels].  Output produced by pointwise conv2d.
* <b>`strides`</b>: List of ints of length 4. Strides for depthwise conv2d kernel in
    all dimensions.
* <b>`padding`</b>: string. see tf.nn.conv2d for valid values.
* <b>`rate`</b>: None or List of ints of length 2. Dilation rate of depthwise conv2d
    kernel in spatial dimensions.
* <b>`data_format`</b>: str or None. Format of data.
* <b>`approx`</b>: str or None. If not None must be one of "kron" or "diagonal".
    The Fisher approximation to use. If None the default value is used.
    (Default: None)
* <b>`reuse`</b>: bool or str.  If True, this adds `inputs` and `outputs` as an
    additional mini-batch/tower of data to use when estimating the Fisher
    block for this layer (which must have already been registered). If
    "VARIABLE_SCOPE", use tf.get_variable_scope().reuse.
    (Default: "VARIABLE_SCOPE")


#### Raises:

* <b>`ValueError`</b>: For improper value to `approx`.
* <b>`KeyError`</b>: If reuse == True but no FisherBlock found for `params`.
* <b>`ValueError`</b>: If reuse == True and FisherBlock found but of the wrong type.

<h3 id="set_default_conv2d_approximation"><code>set_default_conv2d_approximation</code></h3>

``` python
set_default_conv2d_approximation(value)
```



<h3 id="set_default_embedding_approximation"><code>set_default_embedding_approximation</code></h3>

``` python
set_default_embedding_approximation(value)
```



<h3 id="set_default_fully_connected_approximation"><code>set_default_fully_connected_approximation</code></h3>

``` python
set_default_fully_connected_approximation(value)
```



<h3 id="set_default_fully_connected_multi_approximation"><code>set_default_fully_connected_multi_approximation</code></h3>

``` python
set_default_fully_connected_multi_approximation(value)
```



<h3 id="set_default_generic_approximation"><code>set_default_generic_approximation</code></h3>

``` python
set_default_generic_approximation(value)
```



<h3 id="total_loss"><code>total_loss</code></h3>

``` python
total_loss()
```



<h3 id="total_sampled_loss"><code>total_sampled_loss</code></h3>

``` python
total_sampled_loss()
```





