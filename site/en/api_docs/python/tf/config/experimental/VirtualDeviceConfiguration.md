page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.VirtualDeviceConfiguration


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/config/experimental/VirtualDeviceConfiguration">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/eager/context.py#L258-L268">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `VirtualDeviceConfiguration`

Configuration class for virtual devices for a PhysicalDevice.



### Aliases:

* Class <a href="/api_docs/python/tf/config/experimental/VirtualDeviceConfiguration"><code>tf.compat.v1.config.experimental.VirtualDeviceConfiguration</code></a>
* Class <a href="/api_docs/python/tf/config/experimental/VirtualDeviceConfiguration"><code>tf.compat.v2.config.experimental.VirtualDeviceConfiguration</code></a>


<!-- Placeholder for "Used in" -->


#### Fields:


* <b>`memory_limit`</b>: (optional) Maximum memory (in MB) to allocate on the virtual
  device. Currently only supported for GPUs.

<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/eager/context.py#L267-L268">View source</a>

``` python
@staticmethod
__new__(
    cls,
    memory_limit=None
)
```

Create new instance of VirtualDeviceConfiguration(memory_limit,)




## Properties

<h3 id="memory_limit"><code>memory_limit</code></h3>
