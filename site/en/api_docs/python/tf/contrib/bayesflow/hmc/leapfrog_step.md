

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.hmc.leapfrog_step

``` python
tf.contrib.bayesflow.hmc.leapfrog_step(
    step_size,
    position,
    momentum,
    potential_and_grad,
    grad,
    name=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/hmc_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/bayesflow/python/ops/hmc_impl.py).

Applies one step of the leapfrog integrator.

Assumes a simple quadratic kinetic energy function: 0.5 * ||momentum||^2.

#### Args:

* <b>`step_size`</b>: Scalar step size or array of step sizes for the
    leapfrog integrator. Broadcasts to the shape of
    `position`. Larger step sizes lead to faster progress, but
    too-large step sizes lead to larger discretization error and
    worse energy conservation.
* <b>`position`</b>: Tensor containing the value(s) of the position variable(s)
    to update.
* <b>`momentum`</b>: Tensor containing the value(s) of the momentum variable(s)
    to update.
* <b>`potential_and_grad`</b>: Python callable that takes a position tensor like
    `position` and returns the potential energy and its gradient at that
    position.
* <b>`grad`</b>: Tensor with the value of the gradient of the potential energy
    at `position`.
* <b>`name`</b>: Python `str` name prefixed to Ops created by this function.


#### Returns:

* <b>`updated_position`</b>: Updated value of the position.
* <b>`updated_momentum`</b>: Updated value of the momentum.
* <b>`new_potential`</b>: Potential energy of the new position. Has shape matching
    `potential_and_grad(position)`.
* <b>`new_grad`</b>: Gradient from potential_and_grad() evaluated at the new position.
    Has shape matching `position`.

Example: Simple quadratic potential.

```python
def potential_and_grad(position):
  # Simple quadratic potential
  return tf.reduce_sum(0.5 * tf.square(position)), position
position = tf.placeholder(np.float32)
momentum = tf.placeholder(np.float32)
potential, grad = potential_and_grad(position)
new_position, new_momentum, new_potential, new_grad = hmc.leapfrog_step(
  0.1, position, momentum, potential_and_grad, grad)

sess = tf.Session()
position_val = np.random.randn(10)
momentum_val = np.random.randn(10)
potential_val, grad_val = sess.run([potential, grad],
                                   {position: position_val})
positions = np.zeros([100, 10])
for i in xrange(100):
  position_val, momentum_val, potential_val, grad_val = sess.run(
    [new_position, new_momentum, new_potential, new_grad],
    {position: position_val, momentum: momentum_val})
  positions[i] = position_val
# Should trace out sinusoidal dynamics.
plt.plot(positions[:, 0])
```