

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.utils.get_file

### `tf.contrib.keras.utils.get_file`

``` python
get_file(
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



Defined in [`tensorflow/contrib/keras/python/keras/utils/data_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/utils/data_utils.py).

Downloads a file from a URL if it not already in the cache.

By default the file at the url `origin` is downloaded to the
cache_dir `~/.keras`, placed in the cache_subdir `datasets`,
and given the filename `fname`. The final location of a file
`example.txt` would therefore be `~/.keras/datasets/example.txt`.

Files in tar, tar.gz, tar.bz, and zip formats can also be extracted.
Passing a hash will verify the file after download. The command line
programs `shasum` and `sha256sum` can compute the hash.

#### Arguments:

    fname: Name of the file. If an absolute path `/path/to/file.txt` is
        specified the file will be saved at that location.
    origin: Original URL of the file.
    untar: Deprecated in favor of 'extract'.
        boolean, whether the file should be decompressed
    md5_hash: Deprecated in favor of 'file_hash'.
        md5 hash of the file for verification
    file_hash: The expected hash string of the file after download.
        The sha256 and md5 hash algorithms are both supported.
    cache_subdir: Subdirectory under the Keras cache dir where the file is
        saved. If an absolute path `/path/to/folder` is
        specified the file will be saved at that location.
    hash_algorithm: Select the hash algorithm to verify the file.
        options are 'md5', 'sha256', and 'auto'.
        The default 'auto' detects the hash algorithm in use.
    extract: True tries extracting the file as an Archive, like tar or zip.
    archive_format: Archive format to try for extracting the file.
        Options are 'auto', 'tar', 'zip', and None.
        'tar' includes tar, tar.gz, and tar.bz files.
        The default 'auto' is ['tar', 'zip'].
        None or an empty list will return no matches found.
    cache_dir: Location to store cached files, when None it
        defaults to the [Keras
          Directory](/faq/#where-is-the-keras-configuration-filed-stored).


#### Returns:

    Path to the downloaded file