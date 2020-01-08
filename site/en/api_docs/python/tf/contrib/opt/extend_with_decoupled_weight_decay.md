page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.extend_with_decoupled_weight_decay

``` python
tf.contrib.opt.extend_with_decoupled_weight_decay(base_optimizer)
```



Defined in [`tensorflow/contrib/opt/python/training/weight_decay_optimizers.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/opt/python/training/weight_decay_optimizers.py).

Factory function returning an optimizer class with decoupled weight decay.

Returns an optimizer class. An instance of the returned class computes the
update step of `base_optimizer` and additionally decays the weights.
E.g., the class returned by
`extend_with_decoupled_weight_decay(tf.train.AdamOptimizer)` is equivalent to
<a href="../../../tf/contrib/opt/AdamWOptimizer"><code>tf.contrib.opt.AdamWOptimizer</code></a>.

The API of the new optimizer class slightly differs from the API of the
base optimizer:
- The first argument to the constructor is the weight decay rate.
- `minimize` and `apply_gradients` accept the optional keyword argument
  `decay_var_list`, which specifies the variables that should be decayed.
  If `None`, all variables that are optimized are decayed.

Usage example:

```python
# MyAdamW is a new class
MyAdamW = extend_with_decoupled_weight_decay(tf.train.AdamOptimizer)
# Create a MyAdamW object
optimizer = MyAdamW(weight_decay=0.001, learning_rate=0.001)
sess.run(optimizer.minimize(loss, decay_variables=[var1, var2]))

Note that this extension decays weights BEFORE applying the update based
on the gradient, i.e. this extension only has the desired behaviour for
optimizers which do not depend on the value of'var' in the update step!
```

#### Args:

* <b>`base_optimizer`</b>: An optimizer class that inherits from tf.train.Optimizer.


#### Returns:

A new optimizer class that inherits from DecoupledWeightDecayExtension
and base_optimizer.