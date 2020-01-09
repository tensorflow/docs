page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.opt


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/opt/__init__.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A module containing optimization routines.

<!-- Placeholder for "Used in" -->


## Classes

[`class AGNCustomGetter`](../../tf/contrib/opt/AGNCustomGetter): Custom_getter class is used to do:

[`class AGNOptimizer`](../../tf/contrib/opt/AGNOptimizer): Wrapper that implements the Accumulated GradientNormalization algorithm.

[`class AdaMaxOptimizer`](../../tf/contrib/opt/AdaMaxOptimizer): Optimizer that implements the AdaMax algorithm.

[`class AdamGSOptimizer`](../../tf/contrib/opt/AdamGSOptimizer): Optimizer that implements the Adam algorithm.

[`class AdamWOptimizer`](../../tf/contrib/opt/AdamWOptimizer): Optimizer that implements the Adam algorithm with weight decay.

[`class AddSignOptimizer`](../../tf/contrib/opt/AddSignOptimizer): Optimizer that implements the AddSign update.

[`class DecoupledWeightDecayExtension`](../../tf/contrib/opt/DecoupledWeightDecayExtension): This class allows to extend optimizers with decoupled weight decay.

[`class DropStaleGradientOptimizer`](../../tf/contrib/opt/DropStaleGradientOptimizer): Wrapper optimizer that checks and drops stale gradient.

[`class ElasticAverageCustomGetter`](../../tf/contrib/opt/ElasticAverageCustomGetter): Custom_getter class is used to do:

[`class ElasticAverageOptimizer`](../../tf/contrib/opt/ElasticAverageOptimizer): Wrapper optimizer that implements the Elastic Average SGD algorithm.

[`class ExternalOptimizerInterface`](../../tf/contrib/opt/ExternalOptimizerInterface): Base class for interfaces with external optimization algorithms.

[`class GGTOptimizer`](../../tf/contrib/opt/GGTOptimizer): Optimizer that implements the GGT algorithm.

[`class LARSOptimizer`](../../tf/contrib/opt/LARSOptimizer): Layer-wise Adaptive Rate Scaling for large batch training.

[`class LazyAdamGSOptimizer`](../../tf/contrib/opt/LazyAdamGSOptimizer): Variant of the Adam optimizer that handles sparse updates more efficiently.

[`class LazyAdamOptimizer`](../../tf/contrib/opt/LazyAdamOptimizer): Variant of the Adam optimizer that handles sparse updates more efficiently.

[`class ModelAverageCustomGetter`](../../tf/contrib/opt/ModelAverageCustomGetter): Custom_getter class is used to do.

[`class ModelAverageOptimizer`](../../tf/contrib/opt/ModelAverageOptimizer): Wrapper optimizer that implements the Model Average algorithm.

[`class MomentumWOptimizer`](../../tf/contrib/opt/MomentumWOptimizer): Optimizer that implements the Momentum algorithm with weight_decay.

[`class MovingAverageOptimizer`](../../tf/contrib/opt/MovingAverageOptimizer): Optimizer that computes a moving average of the variables.

[`class MultitaskOptimizerWrapper`](../../tf/contrib/opt/MultitaskOptimizerWrapper): Optimizer wrapper making all-zero gradients harmless.

[`class NadamOptimizer`](../../tf/contrib/opt/NadamOptimizer): Optimizer that implements the Nadam algorithm.

[`class PowerSignOptimizer`](../../tf/contrib/opt/PowerSignOptimizer): Optimizer that implements the PowerSign update.

[`class RegAdagradOptimizer`](../../tf/contrib/opt/RegAdagradOptimizer): RegAdagrad: Adagrad with updates that optionally skip updating the slots.

[`class ScipyOptimizerInterface`](../../tf/contrib/opt/ScipyOptimizerInterface): Wrapper allowing `scipy.optimize.minimize` to operate a <a href="../../tf/Session"><code>tf.compat.v1.Session</code></a>.

[`class ShampooOptimizer`](../../tf/contrib/opt/ShampooOptimizer): The Shampoo Optimizer

[`class VariableClippingOptimizer`](../../tf/contrib/opt/VariableClippingOptimizer): Wrapper optimizer that clips the norm of specified variables after update.

## Functions

[`clip_gradients_by_global_norm(...)`](../../tf/contrib/opt/clip_gradients_by_global_norm): Clips gradients of a multitask loss by their global norm.

[`extend_with_decoupled_weight_decay(...)`](../../tf/contrib/opt/extend_with_decoupled_weight_decay): Factory function returning an optimizer class with decoupled weight decay.
