
# Caching model downloads from TF Hub

## Overview

The `tensorflow_hub` library currently supports two modes for downloading
models. By default, a model is downloaded as a compressed archive and cached on
disk. Secondly, models can directly be read from remote storage into TensorFlow.
Either way, the calls to `tensorflow_hub` functions in the actual Python code
can and should continue to use the canonical tfhub.dev URLs of models, which are
portable across systems and navigable for documentation. In the rare case that
user code needs the actual filesystem location (after downloading  and
decompressing, or after resolving a model handle into a filesystem path),
it can be obtained by the function `hub.resolve(handle)`.

### Caching of compressed downloads

The `tensorflow_hub` library by default caches models on the filesystem when
they have been downloaded from tfhub.dev (or other [hosting sites](hosting.md))
and decompressed. This mode is recommended for most environments, except if disk
space is scarce but network bandwidth and latency are superb.

The download location defaults to a local temporary directory but can be
customized by setting the environment variable `TFHUB_CACHE_DIR` (recommended)
or by passing the command-line flag `--tfhub_cache_dir`. The default cache
location `/tmp/tfhub_modules` (or whatever `os.path.join(tempfile.gettempdir(),
"tfhub_modules")` is evaluated to) should work in most cases.

Users who prefer persistent caching across system reboots can instead set
`TFHUB_CACHE_DIR` to a location in their home directory. For example, a user of
the bash shell on a Linux system can add a line like the following to
`~/.bashrc`

```bash
export TFHUB_CACHE_DIR=$HOME/.cache/tfhub_modules
```

...restart the shell, and then this location will be used. When using a
persistent location, be aware that there is no automatic cleanup.

### Reading from remote storage

Users can instruct the `tensorflow_hub` library to directly read models from
remote storage (GCS) instead of downloading the models locally with

```shell
os.environ["TFHUB_MODEL_LOAD_FORMAT"] = "UNCOMPRESSED"
```

or by setting the command-line flag `--tfhub_model_load_format` to
`UNCOMPRESSED`. This way, no caching directory is needed, which is especially
helpful in environments that provide little disk space but a fast internet
connection.

### Running on TPU in Colab notebooks

On [colab.research.google.com](https://colab.research.google.com), downloading
compressed models will conflict with the TPU runtime since the computation
workload is delegated to another machine that does not have access to the cache
location by default. There are two workarounds for this situation:

#### 1) Use a GCS bucket that the TPU worker can access

The easiest solution is to instruct the `tensorflow_hub` library to read the
models from TF Hub's GCS bucket as explained above. Users with their own GCS
bucket can instead specify a directory in their bucket as the cache location
with code like

```python
import os
os.environ["TFHUB_CACHE_DIR"] = "gs://my-bucket/tfhub-modules-cache"
```

...before calling the `tensorflow_hub` library.

#### 2) Redirect all reads through the Colab host

Another workaround is to redirect all reads (even of large variables) through
the Colab host:

```python
load_options =
tf.saved_model.LoadOptions(experimental_io_device='/job:localhost')
reloaded_model = hub.load("https://tfhub.dev/...", options=load_options)
```
**Note:** See more information regarding valid handles [here](tf2_saved_model.md#model_handles).