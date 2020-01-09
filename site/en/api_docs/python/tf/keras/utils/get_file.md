page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.get_file


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/data_utils.py#L150-L270">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Downloads a file from a URL if it not already in the cache.

### Aliases:

* `tf.compat.v1.keras.utils.get_file`
* `tf.compat.v2.keras.utils.get_file`


``` python
tf.keras.utils.get_file(
    fname,
    origin,
    untar=False,
    md5_hash=None,
    file_hash=None,
    cache_subdir='datasets',
    hash_algorithm='auto',
    extract=False,
    archive_format='auto',
    cache_dir=None
)
```



### Used in the guide:

* [Using the SavedModel format](https://www.tensorflow.org/guide/saved_model)
* [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)

### Used in the tutorials:

* [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)
* [Basic classification: Predict an image of clothing](https://www.tensorflow.org/tutorials/keras/classification)
* [Basic regression: Predict fuel efficiency](https://www.tensorflow.org/tutorials/keras/regression)
* [Custom training: walkthrough](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough)
* [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)
* [Image captioning with visual attention](https://www.tensorflow.org/tutorials/text/image_captioning)
* [Image classification](https://www.tensorflow.org/tutorials/images/classification)
* [Load CSV data](https://www.tensorflow.org/tutorials/load_data/csv)
* [Load NumPy data](https://www.tensorflow.org/tutorials/load_data/numpy)
* [Load a pandas.DataFrame](https://www.tensorflow.org/tutorials/load_data/pandas_dataframe)
* [Load images](https://www.tensorflow.org/tutorials/load_data/images)
* [Load text](https://www.tensorflow.org/tutorials/load_data/text)
* [Neural machine translation with attention](https://www.tensorflow.org/tutorials/text/nmt_with_attention)
* [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)
* [Pix2Pix](https://www.tensorflow.org/tutorials/generative/pix2pix)
* [Premade Estimators](https://www.tensorflow.org/tutorials/estimator/premade)
* [TFRecord and tf.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord)
* [Text generation with an RNN](https://www.tensorflow.org/tutorials/text/text_generation)
* [Time series forecasting](https://www.tensorflow.org/tutorials/structured_data/time_series)
* [Transfer learning with TensorFlow Hub](https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub)



By default the file at the url `origin` is downloaded to the
cache_dir `~/.keras`, placed in the cache_subdir `datasets`,
and given the filename `fname`. The final location of a file
`example.txt` would therefore be `~/.keras/datasets/example.txt`.

Files in tar, tar.gz, tar.bz, and zip formats can also be extracted.
Passing a hash will verify the file after download. The command line
programs `shasum` and `sha256sum` can compute the hash.

#### Arguments:


* <b>`fname`</b>: Name of the file. If an absolute path `/path/to/file.txt` is
    specified the file will be saved at that location.
* <b>`origin`</b>: Original URL of the file.
* <b>`untar`</b>: Deprecated in favor of 'extract'.
    boolean, whether the file should be decompressed
* <b>`md5_hash`</b>: Deprecated in favor of 'file_hash'.
    md5 hash of the file for verification
* <b>`file_hash`</b>: The expected hash string of the file after download.
    The sha256 and md5 hash algorithms are both supported.
* <b>`cache_subdir`</b>: Subdirectory under the Keras cache dir where the file is
    saved. If an absolute path `/path/to/folder` is
    specified the file will be saved at that location.
* <b>`hash_algorithm`</b>: Select the hash algorithm to verify the file.
    options are 'md5', 'sha256', and 'auto'.
    The default 'auto' detects the hash algorithm in use.
* <b>`extract`</b>: True tries extracting the file as an Archive, like tar or zip.
* <b>`archive_format`</b>: Archive format to try for extracting the file.
    Options are 'auto', 'tar', 'zip', and None.
    'tar' includes tar, tar.gz, and tar.bz files.
    The default 'auto' is ['tar', 'zip'].
    None or an empty list will return no matches found.
* <b>`cache_dir`</b>: Location to store cached files, when None it
    defaults to the [Keras
      Directory](/faq/#where_is_the_keras_configuration_filed_stored).


#### Returns:

Path to the downloaded file
