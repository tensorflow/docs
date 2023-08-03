
# Write documentation

For contributing to tfhub.dev, documentation in Markdown format must be
provided. For a full overview of the process of contributing models to
tfhub.dev, see the [contribute a model](contribute_a_model.md) guide.

**Note:** the term "publisher" is used throughout this documentation -- this
refers to the owner-of-record for a model hosted on tfhub.dev.

## Types of Markdown documentation

There are 3 types of Markdown documentation used in tfhub.dev:

*   Publisher Markdown - information about a publisher
    ([see markdown syntax](#publisher))
*   Model Markdown - information about a specific model and how to use it
    ([see markdown syntax](#model))
*   Collection Markdown - contains information about a publisher-defined
    collection of models ([see markdown syntax](#collection))

## Content organization

The following content organization is required when contributing to the
[TensorFlow Hub GitHub](https://github.com/tensorflow/tfhub.dev) repository:

*   each publisher directory is in the `assets/docs` directory
*   each publisher directory contains optional `models` and `collections`
    directories
*   each model should have its own directory under
    `assets/docs/<publisher_name>/models`
*   each collection should have its own directory under
    `assets/docs/<publisher_name>/collections`

Publisher markdowns are unversioned, while models can have different versions.
Each model version requires a separate Markdown file named after the version it
describes (i.e. 1.md, 2.md). Collections are versioned but only a single version
(1.md) is supported.

All model versions for a given model should be located in the model directory.

Below is an illustration on how the Markdown content is organized:

```
assets/docs
├── <publisher_name_a>
│   ├── <publisher_name_a>.md  -> Documentation of the publisher.
│   └── models
│       └── <model_name>       -> Model name with slashes encoded as sub-path.
│           ├── 1.md           -> Documentation of the model version 1.
│           └── 2.md           -> Documentation of the model version 2.
├── <publisher_name_b>
│   ├── <publisher_name_b>.md  -> Documentation of the publisher.
│   ├── models
│   │   └── ...
│   └── collections
│       └── <collection_name>
│           └── 1.md           -> Documentation for the collection.
├── <publisher_name_c>
│   └── ...
└── ...
```

## Publisher markdown format {:#publisher}

Publisher documentation is declared in the same kind of markdown files as
models, with slight syntactic differences.

The correct location for the publisher file on the TensorFlow Hub repo is:
[tfhub.dev/assets/docs](https://github.com/tensorflow/tfhub.dev/tree/master/assets/docs)/\<publisher_id>/\<publisher_id.md>

See the minimal publisher documentation example for the "vtab" publisher:

```markdown
# Publisher vtab
Visual Task Adaptation Benchmark

[![Icon URL]](https://storage.googleapis.com/vtab/vtab_logo_120.png)

## VTAB
The Visual Task Adaptation Benchmark (VTAB) is a diverse, realistic and
challenging benchmark to evaluate image representations.
```

The example above specifies the publisher id, the publisher name, the path to
the icon to use, and a longer free-form markdown documentation. Note that the
publisher id should only contain lowercase letters, digits, and hyphens.

### Publisher name guideline

Your publisher name can be your GitHub username or the name of the GitHub
organization you manage.

## Model page markdown format {:#model}

The model documentation is a Markdown file with some add-on syntax. See the
example below for a minimal example or
[a more realistic example Markdown file](https://github.com/tensorflow/tfhub.dev/blob/master/examples/docs/tf2_model_example.md).

### Example documentation

A high-quality model documentation contains code snippets, information how the
model was trained and intended usage. You should also make use of model-specific
metadata properties [explained below](#metadata) so users can find your models
on tfhub.dev faster.

~~~markdown
# Module google/text-embedding-model/1

Simple one sentence description.

<!-- asset-path: https://path/to/text-embedding-model/model.tar.gz -->
<!-- task: text-embedding -->
<!-- fine-tunable: true -->
<!-- format: saved_model_2 -->

## Overview

Here we give more information about the model including how it was trained,
expected use cases, and code snippets demonstrating how to use the model:

```
Code snippet demonstrating use (e.g. for a TF model using the tensorflow_hub library)

import tensorflow_hub as hub

model = hub.KerasLayer(<model name>)
inputs = ...
output = model(inputs)
```
~~~

### Model deployments and grouping deployments together

tfhub.dev allows publishing TF.js, TFLite and Coral deployments of a TensorFlow
SavedModel.

The first line of the Markdown file should specify the type of the format:

*   `# Module publisher/model/version` for SavedModels
*   `# Tfjs publisher/model/version` for TF.js deployments
*   `# Lite publisher/model/version` for Lite deployments
*   `# Coral publisher/model/version` for Coral deployments

It is a good idea for these different formats of the same conceptual model to
show up on the same model page on tfhub.dev. To associate a given TF.js, TFLite
or Coral deployment to a TensorFlow SavedModel model, specify the parent-model
tag:

```markdown
<!-- parent-model: publisher/model/version -->
```

Sometimes you might want to publish one or more deployments without a TensorFlow
SavedModel. In that case, you'll need to create a Placeholder model and specify
its handle in the `parent-model` tag. The placeholder Markdown is identical to
TensorFlow model Markdown, except that the first line is: `# Placeholder
publisher/model/version` and it doesn't require the `asset-path` property.

### Model Markdown specific metadata properties {:#metadata}

The Markdown files can contain metadata properties. These are used to provide
filters and tags to help users find your model. The metadata attributes are
included as Markdown comments after the short description of the Markdown file,
e.g.

```markdown
# Module google/universal-sentence-encoder/1
Encoder of greater-than-word length text trained on a variety of data.

<!-- task: text-embedding -->
...
```

The following metadata properties are supported:

*   `format`: For TensorFlow models: the TensorFlow Hub format of the model.
    Valid values are `hub` when the model was exported via the legacy
    [TF1 hub format](exporting_hub_format.md) or `saved_model_2` when the model
    was exported via a [TF2 Saved Model](exporting_tf2_saved_model.md).
*   `asset-path`: the world-readable remote path to the actual model assets to
    upload, such as to a Google Cloud Storage bucket. The URL should be allowed
    to be fetched from by the robots.txt file (for this reason,
    "https://github.com/.*/releases/download/.*" is not supported as it is
    forbidden by https://github.com/robots.txt). See
    [below](#model-specific-asset-content) for more information on the expected
    file type and content.
*   `parent-model`: For TF.js/TFLite/Coral models: handle of the accompanying
    SavedModel/Placeholder
*   `fine-tunable`: Boolean, whether the model can be fine-tuned by the user.
*   `task`: the problem domain, e.g. "text-embedding". All supported values are
    defined in
    [task.yaml](https://github.com/tensorflow/tfhub.dev/blob/master/tags/task.yaml).
*   `dataset`: the dataset the model was trained on, e.g. "wikipedia". All
    supported values are defined in
    [dataset.yaml](https://github.com/tensorflow/tfhub.dev/blob/master/tags/dataset.yaml).
*   `network-architecture`: the network architecture the model is based on, e.g.
    "mobilenet-v3". All supported values are defined in
    [network_architecture.yaml](https://github.com/tensorflow/tfhub.dev/blob/master/tags/network_architecture.yaml).
*   `language`: the language code of the language a text model was trained on,
    e.g. "en". All supported values are defined in
    [language.yaml](https://github.com/tensorflow/tfhub.dev/blob/master/tags/language.yaml).
*   `license`: The license that applies to the model, e.g. "mit". The default
    assumed license for a published model is
    [Apache 2.0 License](https://opensource.org/licenses/Apache-2.0). All
    supported values are defined in
    [license.yaml](https://github.com/tensorflow/tfhub.dev/blob/master/tags/license.yaml).
    Note that the `custom` license will require special consideration case by
    case.
*   `colab`: HTTPS URL to a notebook that demonstrates how the model can be used
    or trained
    ([example](https://colab.sandbox.google.com/github/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/bigbigan_with_tf_hub.ipynb)
    for [bigbigan-resnet50](https://tfhub.dev/deepmind/bigbigan-resnet50/1)).
    Must lead to `colab.research.google.com`. Note that Jupyter notebooks hosted
    on GitHub can be accessed via
    `https://colab.research.google.com/github/ORGANIZATION/PROJECT/
    blob/master/.../my_notebook.ipynb`.
*   `demo`: HTTPS URL to a website that demonstrates how the TF.js model can be
    used ([example](https://teachablemachine.withgoogle.com/train/pose) for
    [posenet](https://tfhub.dev/tensorflow/tfjs-model/posenet/mobilenet/float/075/1/default/1)).
*   `interactive-visualizer`: name of the visualizer that should be embedded on
    the model page, e.g. "vision". Displaying a visualizer allows users to
    explore the model's predictions interactively. All supported values are
    defined in
    [interactive_visualizer.yaml](https://github.com/tensorflow/tfhub.dev/blob/master/tags/interactive_visualizer.yaml).

The Markdown documentation types support different required and optional
metadata properties:

| Type        | Required                 | Optional                            |
| ----------- | ------------------------ | ----------------------------------- |
| Publisher   |                          |                                     |
| Collection  | task                     | dataset, language,                  |
:             :                          : network-architecture                :
| Placeholder | task                     | dataset, fine-tunable,              |
:             :                          : interactive-visualizer, language,   :
:             :                          : license, network-architecture       :
| SavedModel  | asset-path, task,        | colab, dataset,                     |
:             : fine-tunable, format     : interactive-visualizer, language,   :
:             :                          : license, network-architecture       :
| Tfjs        | asset-path, parent-model | colab, demo, interactive-visualizer |
| Lite        | asset-path, parent-model | colab, interactive-visualizer       |
| Coral       | asset-path, parent-model | colab, interactive-visualizer       |

### Model-specific asset content

Depending on the model type, the following file types and contents are expected:

*   SavedModel: a tar.gz archive containing content like so:

```
saved_model.tar.gz
├── assets/            # Optional.
├── assets.extra/      # Optional.
├── variables/
│     ├── variables.data-?????-of-?????
│     └──  variables.index
├── saved_model.pb
├── keras_metadata.pb  # Optional, only required for Keras models.
└── tfhub_module.pb    # Optional, only required for TF1 models.
```

*   TF.js: a tar.gz archive containing content like so:

```
tf_js_model.tar.gz
├── group*
├── *.json
├── *.txt
└── *.pb
```

*   TFLite: a .tflite file
*   Coral: a .tflite file

For tar.gz archives: assuming your model files are in the directory `my_model`
(e.g. `my_model/saved_model.pb` for SavedModels or `my_model/model.json` for
TF.js models), you can create a valid tar.gz archive using the
[tar](https://www.gnu.org/software/tar/manual/tar.html) tool via `cd my_model &&
tar -czvf ../model.tar.gz *`.

Generally, all files and directories (whether compressed or uncompressed) must
start with a word character so e.g. dots are no valid prefix of file
names/directories.

## Collection page markdown format {:#collection}

Collections are a feature of tfhub.dev that enables publishers to bundle related
models together to improve user search experience.

See the [list of all collections](https://tfhub.dev/s?subtype=model-family) on
tfhub.dev.

The correct location for the collection file in the repository
[github.com/tensorflow/tfhub.dev](https://github.com/tensorflow/tfhub.dev) is
[assets/docs](https://github.com/tensorflow/tfhub.dev/tree/master/assets/docs)/<b>publisher_name&gt;</b>/collections/<b>&lt;collection_name&gt;</b>/<b>1</b>.md

Here is a minimal example that would go into
assets/docs/<b>vtab</b>/collections/<b>benchmark</b>/<b>1</b>.md. Note that the
collection's name in the first line does not include the `collections/` part
which is included in the filepath.

```markdown
# Collection vtab/benchmark/1
Collection of visual representations that have been evaluated on the VTAB
benchmark.

<!-- task: image-feature-vector -->

## Overview
This is the list of visual representations in TensorFlow Hub that have been
evaluated on VTAB. Results can be seen in
[google-research.github.io/task_adaptation/](https://google-research.github.io/task_adaptation/)

#### Models
|                   |
|-------------------|
| [vtab/sup-100/1](https://tfhub.dev/vtab/sup-100/1)   |
| [vtab/rotation/1](https://tfhub.dev/vtab/rotation/1) |
|------------------------------------------------------|
```

The example specifies the name of the collection, a short one sentence
description, problem domain metadata and free-form markdown documentation.
