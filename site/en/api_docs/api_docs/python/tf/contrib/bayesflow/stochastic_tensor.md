

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.bayesflow.stochastic_tensor



Defined in [`tensorflow/contrib/bayesflow/python/ops/stochastic_tensor.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/bayesflow/python/ops/stochastic_tensor.py).

Support for creating Stochastic Tensors.

See the [BayesFlow Stochastic Tensors (contrib)](../../../../../api_guides/python/contrib.bayesflow.stochastic_tensor) guide.


## Classes

[`class BaseStochasticTensor`](../../../tf/contrib/bayesflow/stochastic_tensor/BaseStochasticTensor): Base Class for Tensor-like objects that emit stochastic values.

[`class MeanValue`](../../../tf/contrib/bayesflow/stochastic_tensor/MeanValue)

[`class ObservedStochasticTensor`](../../../tf/contrib/bayesflow/stochastic_tensor/ObservedStochasticTensor): A StochasticTensor with an observed value.

[`class SampleValue`](../../../tf/contrib/bayesflow/stochastic_tensor/SampleValue): Draw samples, possibly adding new outer dimensions along the way.

[`class StochasticTensor`](../../../tf/contrib/bayesflow/stochastic_tensor/StochasticTensor): StochasticTensor is a BaseStochasticTensor backed by a distribution.

## Functions

[`get_current_value_type(...)`](../../../tf/contrib/bayesflow/stochastic_tensor/get_current_value_type)

[`value_type(...)`](../../../tf/contrib/bayesflow/stochastic_tensor/value_type): Creates a value type context for any StochasticTensor created within.

