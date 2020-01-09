page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.list_physical_devices


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/config.py#L296-L318">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Return a list of physical devices visible to the runtime.

### Aliases:

* `tf.compat.v1.config.experimental.list_physical_devices`
* `tf.compat.v2.config.experimental.list_physical_devices`


``` python
tf.config.experimental.list_physical_devices(device_type=None)
```



### Used in the guide:

* [Eager execution](https://www.tensorflow.org/guide/eager)
* [Use a GPU](https://www.tensorflow.org/guide/gpu)

### Used in the tutorials:

* [Customization basics: tensors and operations](https://www.tensorflow.org/tutorials/customization/basics)
* [Text classification with TensorFlow Hub: Movie reviews](https://www.tensorflow.org/tutorials/keras/text_classification_with_hub)



Physical devices are hardware devices locally present on the current machine.
By default all discovered CPU and GPU devices are considered visible. The
`list_physical_devices` allows querying the hardware prior to runtime
initialization.

The following example ensures the machine can see at least 1 GPU.

```python
physical_devices = tf.config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "No GPUs found."
```

#### Args:


* <b>`device_type`</b>: (optional) Device type to filter by such as "CPU" or "GPU"


#### Returns:

List of PhysicalDevice objects
