# Install TensorFlow for C

TensorFlow provides a C API that can be used to build
[bindings for other languages](../extend/language_bindings.md). The API is defined in
<a href="https://github.com/tensorflow/tensorflow/blob/master/tensorflow/c/c_api.h" class="external"><code>c_api.h</code></a>
and designed for simplicity and uniformity rather than convenience.

Note: There is no `libtensorflow` support for TensorFlow 2 yet. It is expected
in a future release.

## Supported Platforms

TensorFlow for C is supported on the following systems:

* Linux, 64-bit, x86
* macOS X, Version 10.12.6 (Sierra) or higher
* Windows, 64-bit x86

## Setup

### Download

<table>
  <tr><th>TensorFlow C library</th><th>URL</th></tr>
  <tr class="alt"><td colspan="2">Linux</td></tr>
  <tr>
    <td>Linux CPU only</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-linux-x86_64-1.15.0.tar.gz">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-linux-x86_64-1.15.0.tar.gz</a></td>
  </tr>
  <tr>
    <td>Linux GPU support</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-linux-x86_64-1.15.0.tar.gz">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-linux-x86_64-1.15.0.tar.gz</a></td>
  </tr>
  <tr class="alt"><td colspan="2">macOS</td></tr>
  <tr>
    <td>macOS CPU only</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-darwin-x86_64-1.15.0.tar.gz">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-darwin-x86_64-1.15.0.tar.gz</a></td>
  </tr>
  <tr class="alt"><td colspan="2">Windows</td></tr>
  <tr>
    <td>Windows CPU only</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-windows-x86_64-1.15.0.zip">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-windows-x86_64-1.15.0.zip</a></td>
  </tr>
  <tr>
    <td>Windows GPU only</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-windows-x86_64-1.15.0.zip">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-windows-x86_64-1.15.0.zip</a></td>
  </tr>
</table>

### Extract

Extract the downloaded archive, which contains the header files to include in
your C program and the shared libraries to link against.

On Linux and macOS, you may want to extract to `/usr/local/lib`:

<pre class="devsite-terminal devsite-click-to-copy">
sudo tar -C /usr/local -xzf <var>(downloaded file)</var>
</pre>

### Linker

On Linux/macOS, if you extract the TensorFlow C library to a system directory,
such as `/usr/local`, configure the linker with `ldconfig`:

<pre class="devsite-terminal devsite-click-to-copy">
sudo ldconfig
</pre>

If you extract the TensorFlow C library to a non-system directory, such as
`~/mydir`, then configure the linker environmental variables:

<div class="ds-selector-tabs">
<section>
<h3>Linux</h3>
<pre class="prettyprint lang-bsh">
export LIBRARY_PATH=$LIBRARY_PATH:~/mydir/lib
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/mydir/lib
</pre>
</section>
<section>
<h3>mac OS</h3>
<pre class="prettyprint lang-bsh">
export LIBRARY_PATH=$LIBRARY_PATH:~/mydir/lib
export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:~/mydir/lib
</pre>
</section>
</div><!--/ds-selector-tabs-->


## Build

### Example program

With the TensorFlow C library installed, create an example program with the
following source code (`hello_tf.c`):

```c
#include <stdio.h>
#include <tensorflow/c/c_api.h>

int main() {
  printf("Hello from TensorFlow C library version %s\n", TF_Version());
  return 0;
}
```

### Compile

Compile the example program to create an executable, then run:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">gcc hello_tf.c -ltensorflow -o hello_tf</code>

<code class="devsite-terminal">./hello_tf</code>
</pre>

The command outputs: <code>Hello from TensorFlow C library version <em>number</em></code>

Success: The TensorFlow C library is configured.

If the program doesn't build, make sure that `gcc` can access the TensorFlow C
library. If extracted to `/usr/local`, explicitly pass the library location to
the compiler:

<pre class="devsite-terminal devsite-click-to-copy">
gcc -I/usr/local/include -L/usr/local/lib hello_tf.c -ltensorflow -o hello_tf
</pre>


## Build from source

TensorFlow is open source. Read
[the instructions](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/lib_package/README.md){:.external}
to build TensorFlow's C library from source code.
