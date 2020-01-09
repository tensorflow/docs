page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.set_memory_growth


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/config.py#L434-L454">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Set if memory growth should be enabled for a PhysicalDevice.

### Aliases:

* `tf.compat.v1.config.experimental.set_memory_growth`
* `tf.compat.v2.config.experimental.set_memory_growth`


``` python
tf.config.experimental.set_memory_growth(
    device,
    enable
)
```



### Used in the guide:

* [Use a GPU](https://www.tensorflow.org/guide/gpu)



A PhysicalDevice with memory growth set will not allocate all memory on the
device upfront. Memory growth cannot be configured on a PhysicalDevice with
virtual devices configured.

#### For example:



```python
physical_devices = tf.config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
tf.config.experimental.set_memory_growth(physical_devices[0], True)
```

#### Args:


* <b>`device`</b>: PhysicalDevice to configure
* <b>`enable`</b>: Whether to enable or disable memory growth
