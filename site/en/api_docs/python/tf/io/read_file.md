page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.read_file


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_io_ops.py`



Reads and outputs the entire contents of the input filename.

### Aliases:

* `tf.compat.v1.io.read_file`
* `tf.compat.v1.read_file`
* `tf.compat.v2.io.read_file`


``` python
tf.io.read_file(
    filename,
    name=None
)
```



### Used in the guide:

* [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)

### Used in the tutorials:

* [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)
* [Image captioning with visual attention](https://www.tensorflow.org/tutorials/text/image_captioning)
* [Load images](https://www.tensorflow.org/tutorials/load_data/images)
* [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)
* [Pix2Pix](https://www.tensorflow.org/tutorials/generative/pix2pix)




#### Args:


* <b>`filename`</b>: A `Tensor` of type `string`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
