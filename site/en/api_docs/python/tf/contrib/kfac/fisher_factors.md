

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.kfac.fisher_factors



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_factors_lib.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/kfac/python/ops/fisher_factors_lib.py).

FisherFactor definitions.

## Classes

[`class ConvDiagonalFactor`](../../../tf/contrib/kfac/fisher_factors/ConvDiagonalFactor): FisherFactor for a diagonal approx of a convolutional layer's Fisher.

[`class ConvInputKroneckerFactor`](../../../tf/contrib/kfac/fisher_factors/ConvInputKroneckerFactor): Kronecker factor for the input side of a convolutional layer.

[`class ConvOutputKroneckerFactor`](../../../tf/contrib/kfac/fisher_factors/ConvOutputKroneckerFactor): Kronecker factor for the output side of a convolutional layer.

[`class DiagonalFactor`](../../../tf/contrib/kfac/fisher_factors/DiagonalFactor): A base class for FisherFactors that use diagonal approximations.

[`class FisherFactor`](../../../tf/contrib/kfac/fisher_factors/FisherFactor): Base class for objects modeling factors of approximate Fisher blocks.

[`class FullFactor`](../../../tf/contrib/kfac/fisher_factors/FullFactor): FisherFactor for a full matrix representation of the Fisher of a parameter.

[`class FullyConnectedDiagonalFactor`](../../../tf/contrib/kfac/fisher_factors/FullyConnectedDiagonalFactor): FisherFactor for a diagonal approx of a fully-connected layer's Fisher.

[`class FullyConnectedKroneckerFactor`](../../../tf/contrib/kfac/fisher_factors/FullyConnectedKroneckerFactor): Kronecker factor for the input or output side of a fully-connected layer.

[`class InverseProvidingFactor`](../../../tf/contrib/kfac/fisher_factors/InverseProvidingFactor): Base class for FisherFactors that maintain inverses, powers, etc of _cov.

[`class NaiveDiagonalFactor`](../../../tf/contrib/kfac/fisher_factors/NaiveDiagonalFactor): FisherFactor for a diagonal approximation of any type of param's Fisher.

## Functions

[`covariance_initializer(...)`](../../../tf/contrib/kfac/fisher_factors/covariance_initializer)

[`diagonal_covariance_initializer(...)`](../../../tf/contrib/kfac/fisher_factors/diagonal_covariance_initializer)

[`inverse_initializer(...)`](../../../tf/contrib/kfac/fisher_factors/inverse_initializer)

[`scalar_or_tensor_to_string(...)`](../../../tf/contrib/kfac/fisher_factors/scalar_or_tensor_to_string)

[`scope_string_from_name(...)`](../../../tf/contrib/kfac/fisher_factors/scope_string_from_name)

[`scope_string_from_params(...)`](../../../tf/contrib/kfac/fisher_factors/scope_string_from_params): Builds a variable scope string name from the given parameters.

[`set_global_constants(...)`](../../../tf/contrib/kfac/fisher_factors/set_global_constants): Sets various global constants used by the classes in this module.

