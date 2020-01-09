page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_name_scope


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/ops/ops.py#L58-L73">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the current name scope of the default graph.

``` python
tf.contrib.framework.get_name_scope()
```



<!-- Placeholder for "Used in" -->


#### For example:


```python
with tf.name_scope('scope1'):
  with tf.name_scope('scope2'):
    print(tf.contrib.framework.get_name_scope())
```
would print the string `scope1/scope2`.



#### Returns:

A string representing the current name scope.
