page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.model_variables


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variables.py#L3134-L3148">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns all variables in the MODEL_VARIABLES collection.

### Aliases:

* <a href="/api_docs/python/tf/model_variables"><code>tf.compat.v1.model_variables</code></a>


``` python
tf.model_variables(scope=None)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`scope`</b>: (Optional.) A string. If supplied, the resulting list is filtered to
  include only items whose `name` attribute matches `scope` using
  `re.match`. Items without a `name` attribute are never returned if a scope
  is supplied. The choice of `re.match` means that a `scope` without special
  tokens filters by prefix.


#### Returns:

A list of local Variable objects.
