page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.get_file

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



Defined in [`tensorflow/python/keras/utils/data_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/utils/data_utils.py).

Downloads a file from a URL if it not already in the cache.

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
          Directory](/faq/#where-is-the-keras-configuration-filed-stored).


#### Returns:

Path to the downloaded file