page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.global_variable


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/ops/variables.py#L185-L206">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Create a variable with a value and add it to <a href="/api_docs/python/tf/GraphKeys#GLOBAL_VARIABLES"><code>GraphKeys.GLOBAL_VARIABLES</code></a>.

``` python
tf.contrib.framework.global_variable(
    initial_value,
    validate_shape=True,
    name=None,
    use_resource=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`initial_value`</b>: See variables.Variable.__init__.
* <b>`validate_shape`</b>: See variables.Variable.__init__.
* <b>`name`</b>: See variables.Variable.__init__.
* <b>`use_resource`</b>: If `True` use a ResourceVariable instead of a Variable.


#### Returns:

New variable.
