page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.xavier_initializer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/initializers.py#L31-L57">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns an initializer performing "Xavier" initialization for weights.

### Aliases:

* <a href="/api_docs/python/tf/contrib/layers/xavier_initializer"><code>tf.contrib.layers.xavier_initializer_conv2d</code></a>


``` python
tf.contrib.layers.xavier_initializer(
    uniform=True,
    seed=None,
    dtype=tf.dtypes.float32
)
```



<!-- Placeholder for "Used in" -->

This function implements the weight initialization from:

Xavier Glorot and Yoshua Bengio (2010):
         [Understanding the difficulty of training deep feedforward neural
         networks. International conference on artificial intelligence and
         statistics.](
         http://www.jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf)

This initializer is designed to keep the scale of the gradients roughly the
same in all layers. In uniform distribution this ends up being the range:
`x = sqrt(6. / (in + out)); [-x, x]` and for normal distribution a standard
deviation of `sqrt(2. / (in + out))` is used.

#### Args:


* <b>`uniform`</b>: Whether to use uniform or normal distributed random initialization.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
      <a href="../../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.
* <b>`dtype`</b>: The data type. Only floating point types are supported.


#### Returns:

An initializer for a weight matrix.
