page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.get_optimizer_variables


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/saver.py#L175-L187">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a list of variables for the given <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>.

``` python
tf.contrib.eager.get_optimizer_variables(optimizer)
```



<!-- Placeholder for "Used in" -->

Equivalent to `optimizer.variables()`.

#### Args:


* <b>`optimizer`</b>: An instance of <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a> which has created
  variables (typically after a call to <a href="/api_docs/python/tf/keras/optimizers/Optimizer#minimize"><code>Optimizer.minimize</code></a>).


#### Returns:

A list of variables which have been created by the `Optimizer`.
