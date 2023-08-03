
# Model hosting protocol

This document describes the URL conventions used when hosting all model types on
[tfhub.dev](https://tfhub.dev) - TFJS, TF Lite and TensorFlow models. It also
describes the HTTP(S)-based protocol implemented by the `tensorflow_hub` library
in order to load TensorFlow models from [tfhub.dev](https://tfhub.dev) and
compatible services into TensorFlow programs.

Its key feature is to use the same URL in code to load a model and in a browser
to view the model documentation.

## General URL conventions

[tfhub.dev](https://tfhub.dev) supports the following URL formats:

*   TF Hub publishers follow `https://tfhub.dev/<publisher>`
*   TF Hub collections follow
    `https://tfhub.dev/<publisher>/collection/<collection_name>`
*   TF Hub models have versioned url
    `https://tfhub.dev/<publisher>/<model_name>/<version>` and unversioned url
    `https://tfhub.dev/<publisher>/<model_name>` that resolves to the latest
    version of the model.

TF Hub models can be downloaded as compressed assets by appending URL parameters
to the [tfhub.dev](https://tfhub.dev) model URL. However, the URL parameters
required to achieve that depend on the model type:

*   TensorFlow models (both SavedModel and TF1 Hub formats): append
    `?tf-hub-format=compressed` to the TensorFlow model url.
*   TFJS models: append `?tfjs-format=compressed` to the TFJS model url to
    download the compressed or `/model.json?tfjs-format=file` to read if from
    remote storage.
*   TF lite models: append `?lite-format=tflite` to the TF Lite model url.

For example:

<table style="width: 100%;">
  <tr style="text-align: center">
    <col style="width: 10%" />
    <col style="width: 20%" />
    <col style="width: 15%" />
    <col style="width: 30%" />
    <col style="width: 25%" />
    <td style="text-align: center; background-color: #D0D0D0">Type</td>
    <td style="text-align: center; background-color: #D0D0D0">Model URL</td>
    <td style="text-align: center; background-color: #D0D0D0">Download type</td>
    <td style="text-align: center; background-color: #D0D0D0">URL param</td>
    <td style="text-align: center; background-color: #D0D0D0">Download URL</td>
  </tr>
  <tr>
    <td>TensorFlow (SavedModel, TF1 Hub format)</td>
    <td>https://tfhub.dev/google/spice/2</td>
    <td>.tar.gz</td>
    <td>?tf-hub-format=compressed </td>
    <td>https://tfhub.dev/google/spice/2?tf-hub-format=compressed</td>
  </tr>
  <tr>
    <td>TF Lite</td>
    <td>https://tfhub.dev/google/lite-model/spice/1</td>
    <td>.tflite</td>
    <td>?lite-format=tflite</td>
    <td>https://tfhub.dev/google/lite-model/spice/1?lite-format=tflite</td>
  </tr>
  <tr>
    <td>TF.js</td>
    <td>https://tfhub.dev/google/tfjs-model/spice/2/default/1</td>
    <td>.tar.gz</td>
    <td>?tfjs-format=compressed</td>
    <td>https://tfhub.dev/google/tfjs-model/spice/2/default/1?tfjs-format=compressed</td>
  </tr>
</table>

Additionally, some models also are hosted in a format that can be read directly
from remote storage without being downloaded. This is especially useful if there
is no local storage available, such as running a TF.js model in the browser or
loading a SavedModel on [Colab](https://colab.research.google.com/). Be
conscious that reading models that are hosted remotely without being downloaded
locally may increase latency.

<table style="width: 100%;">
  <tr style="text-align: center">
    <col style="width: 10%" />
    <col style="width: 20%" />
    <col style="width: 15%" />
    <col style="width: 30%" />
    <col style="width: 25%" />
    <td style="text-align: center; background-color: #D0D0D0">Type</td>
    <td style="text-align: center; background-color: #D0D0D0">Model URL</td>
    <td style="text-align: center; background-color: #D0D0D0">Response type</td>
    <td style="text-align: center; background-color: #D0D0D0">URL param</td>
    <td style="text-align: center; background-color: #D0D0D0">Request URL</td>
  </tr>
  <tr>
    <td>TensorFlow (SavedModel, TF1 Hub format)</td>
    <td>https://tfhub.dev/google/spice/2</td>
    <td>String (Path to GCS folder where the uncompressed model is stored)</td>
    <td>?tf-hub-format=uncompressed</td>
    <td>https://tfhub.dev/google/spice/2?tf-hub-format=uncompressed</td>
  </tr>
  <tr>
    <td>TF.js</td>
    <td>https://tfhub.dev/google/tfjs-model/spice/2/default/1</td>
    <td>.json</td>
    <td>?tfjs-format=file</td>
    <td>https://tfhub.dev/google/tfjs-model/spice/2/default/1/model.json?tfjs-format=file</td>
  </tr>
</table>

## tensorflow_hub library protocol

This section describes how we host models on [tfhub.dev](https://tfhub.dev) for
use with the tensorflow_hub library. If you want to host your own model
repository to work with the tensorflow_hub library, your HTTP(s) distribution
service should provide an implementation of this protocol.

Note that this section does not address hosting TF Lite and TFJS models since
they are not downloaded via the `tensorflow_hub` library. For more information
on hosting these model types, please check [above](#general-url-conventions).

### Compressed Hosting

Models are stored on [tfhub.dev](https://tfhub.dev) as compressed tar.gz files.
By default, the tensorflow_hub library automatically downloads the compressed
model. They can also be manually downloaded by appending the
`?tf-hub-format=compressed` to the model url, for example:

```shell
wget https://tfhub.dev/tensorflow/albert_en_xxlarge/1?tf-hub-format=compressed
```

The root of the archive is the root of the model directory and should contain a
SavedModel, as in this example:

```shell
# Create a compressed model from a SavedModel directory.
$ tar -cz -f model.tar.gz --owner=0 --group=0 -C /tmp/export-model/ .

# Inspect files inside a compressed model
$ tar -tf model.tar.gz
./
./variables/
./variables/variables.data-00000-of-00001
./variables/variables.index
./assets/
./saved_model.pb
```

Tarballs for use with the legacy
[TF1 Hub format](https://www.tensorflow.org/hub/tf1_hub_module) will also
contain a `./tfhub_module.pb` file.

When one of `tensorflow_hub` library model loading APIs is invoked
([hub.KerasLayer](https://www.tensorflow.org/hub/api_docs/python/hub/KerasLayer),
[hub.load](https://www.tensorflow.org/hub/api_docs/python/hub/load), etc) the
library downloads the model, uncompresses the model and caches it locally. The
`tensorflow_hub` library expects that model URLs are versioned and that the
model content of a given version is immutable, so that it can be cached
indefinitely. Learn more about [caching models](caching.md).

![](https://raw.githubusercontent.com/tensorflow/hub/master/docs/images/library_download_cache.png)

### Uncompressed Hosting

When the environment variable `TFHUB_MODEL_LOAD_FORMAT` or the command-line flag
`--tfhub_model_load_format` is set to `UNCOMPRESSED`, the model is read directly
from remote storage (GCS) instead of being downloaded and uncompressed locally.
When this behavior is enabled the library appends `?tf-hub-format=uncompressed`
to the model URL. That request returns the path to the folder on GCS that
contains the uncompressed model files. As an example, \
`https://tfhub.dev/google/spice/2?tf-hub-format=uncompressed` \
returns \
`gs://tfhub-modules/google/spice/2/uncompressed` in the body of the 303
response. The library then reads the model from that GCS destination.
