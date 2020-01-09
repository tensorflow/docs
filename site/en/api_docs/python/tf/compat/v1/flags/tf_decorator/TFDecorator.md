page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.tf_decorator.TFDecorator


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/util/tf_decorator.py#L229-L280">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TFDecorator`

Base class for all TensorFlow decorators.



### Aliases:

* Class `tf.compat.v1.app.flags.tf_decorator.TFDecorator`


<!-- Placeholder for "Used in" -->

TFDecorator captures and exposes the wrapped target, and provides details
about the current decorator.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/util/tf_decorator.py#L236-L254">View source</a>

``` python
__init__(
    decorator_name,
    target,
    decorator_doc='',
    decorator_argspec=None
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Properties

<h3 id="decorated_target"><code>decorated_target</code></h3>




<h3 id="decorator_argspec"><code>decorator_argspec</code></h3>




<h3 id="decorator_doc"><code>decorator_doc</code></h3>




<h3 id="decorator_name"><code>decorator_name</code></h3>






## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/util/tf_decorator.py#L259-L260">View source</a>

``` python
__call__(
    *args,
    **kwargs
)
```

Call self as a function.
