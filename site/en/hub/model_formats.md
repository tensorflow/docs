
# Model formats

[tfhub.dev](https://tfhub.dev) hosts the following model
formats: TF2 SavedModel, TF1 Hub format, TF.js and TFLite. This page provides an
overview of each model format.

Content published to tfhub.dev can be automatically mirrored to other model
hubs, provided it follows a specified format and is permitted by our Terms
(https://tfhub.dev/terms). See [our publishing documentation](publish.md) for
more details, and [our contribution documentation](contribute_a_model.md) if
you'd like to opt-out of mirroring.

## TensorFlow formats

[tfhub.dev](https://tfhub.dev) hosts TensorFlow models in the TF2 SavedModel
format and TF1 Hub format. We recommend using models in the standardized TF2
SavedModel format instead of the deprecated TF1 Hub format when possible.

### SavedModel

TF2 SavedModel is the recommended format for sharing TensorFlow models. You can
learn more about the SavedModel format in the
[TensorFlow SavedModel](https://www.tensorflow.org/guide/saved_model) guide.

You can browse SavedModels on tfhub.dev by using the TF2 version filter on the
[tfhub.dev browse page](https://tfhub.dev/s?subtype=module,placeholder) or by
following
[this link](https://tfhub.dev/s?subtype=module,placeholder&tf-version=tf2).

You can use SavedModels from tfhub.dev without depending on the `tensorflow_hub`
library, since this format is a part of core TensorFlow.

Learn more about SavedModels on TF Hub:

*   [Using TF2 SavedModels](tf2_saved_model.md)
*   [Exporting a TF2 SavedModel](exporting_tf2_saved_model.md)
*   [TF1/TF2 compatibility of TF2 SavedModels](model_compatibility.md)

### TF1 Hub format

The TF1 Hub format is a custom serialization format used in by TF Hub library.
The TF1 Hub format is similar to the SavedModel format of TensorFlow 1 on a
syntactic level (same file names and protocol messages) but semantically
different to allow for module reuse, composition and re-training (e.g.,
different storage of resource initializers, different tagging conventions for
metagraphs). The easiest way to tell them apart on disk is the presence or
absence of the `tfhub_module.pb` file.

You can browse models in the TF1 Hub format on tfhub.dev by using the TF1
version filter on the
[tfhub.dev browse page](https://tfhub.dev/s?subtype=module,placeholder) or by
following
[this link](https://tfhub.dev/s?subtype=module,placeholder&tf-version=tf1).

Learn more about models in TF1 Hub format on TF Hub:

*   [Using TF1 Hub format models](tf1_hub_module.md)
*   [Exporting a model in the TF1 Hub format](exporting_hub_format.md)
*   [TF1/TF2 compatibility of TF1 Hub format](model_compatibility.md)

## TFLite format

The TFLite format is used for on-device inference. You can learn more at the
[TFLite documentation](https://www.tensorflow.org/lite).

You can browse TF Lite models on tfhub.dev by using the TF Lite model format
filter on the
[tfhub.dev browse page](https://tfhub.dev/s?subtype=module,placeholder) or by
following [this link](https://tfhub.dev/lite).

## TFJS format

The TF.js format is used for in-browser ML. You can learn more at the
[TF.js documentation](https://www.tensorflow.org/js).

You can browse TF.js models on tfhub.dev by using the TF.js model format filter
on the [tfhub.dev browse page](https://tfhub.dev/s?subtype=module,placeholder)
or by following [this link](https://tfhub.dev/js).
