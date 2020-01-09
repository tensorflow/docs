page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.latest_checkpoint


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/checkpoint_management.py#L320-L347">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Finds the filename of latest saved checkpoint file.

### Aliases:

* `tf.compat.v1.train.latest_checkpoint`
* `tf.compat.v2.train.latest_checkpoint`


``` python
tf.train.latest_checkpoint(
    checkpoint_dir,
    latest_filename=None
)
```



### Used in the guide:

* [Eager execution](https://www.tensorflow.org/guide/eager)
* [Training checkpoints](https://www.tensorflow.org/guide/checkpoint)

### Used in the tutorials:

* [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)
* [Distributed training with Keras](https://www.tensorflow.org/tutorials/distribute/keras)
* [Neural machine translation with attention](https://www.tensorflow.org/tutorials/text/nmt_with_attention)
* [Pix2Pix](https://www.tensorflow.org/tutorials/generative/pix2pix)
* [Text generation with an RNN](https://www.tensorflow.org/tutorials/text/text_generation)




#### Args:


* <b>`checkpoint_dir`</b>: Directory where the variables were saved.
* <b>`latest_filename`</b>: Optional name for the protocol buffer file that
  contains the list of most recent checkpoint filenames.
  See the corresponding argument to `Saver.save()`.


#### Returns:

The full path to the latest checkpoint or `None` if no checkpoint was found.
