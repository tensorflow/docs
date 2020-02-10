# Build and install error messages

TensorFlow uses [GitHub issues](https://github.com/tensorflow/tensorflow/issues){:.external}
and [Stack Overflow](https://stackoverflow.com/questions/tagged/tensorflow){:.external}
to track and document build and installation problems.

The following list links error messages to a solution or discussion. If you find
an installation or build problem that is not listed, please search the GitHub
issues and Stack Overflow. If you still can't find the error message, ask a new
question on Stack Overflow with the `tensorflow` tag.

<table>
<tr><th>GitHub issue or Stack&nbsp;Overflow</th> <th>Error Message</th></tr>
  <tr><td><a href="https://stackoverflow.com/q/38896424">38896424</a>
          <a href=https://github.com/tensorflow/tensorflow/issues/31058>31058</a></td>
    <td>"No matching distribution found for tensorflow": 
      Pip can't find a TensorFlow package compatible with your system. Check the
      <a href="https://tensorflow.org/install">system requirements and
        python version</a>
    </td>
  </tr>
<tr>
  <td><a href="https://github.com/tensorflow/tensorflow/issues/22390">22390</a></td>
  <td><pre>Unzipping simple_console_for_windows.zip to create runfiles tree...
[./bazel-bin/tensorflow/tools/pip_package/simple_console_for_windows.zip]
  End-of-central-directory signature not found.  Either this file is not
  a zipfile, or it constitutes one disk of a multi-part archive.  In the
  latter case the central directory and zipfile comment will be found on
  the last disk(s) of this archive.
unzip: cannot find zipfile directory in one of ./bazel-bin/tensorflow/tools/pip_package/simple_console_for_windows.zip or
        ./bazel-bin/tensorflow/tools/pip_package/simple_console_for_windows.zip.zip, and cannot find ./bazel-bin/tensorflow/tools/pip_package/simple_console_for_windows.zip.ZIP, period.
</pre></td>
</tr>

<tr>
  <td><a href="https://stackoverflow.com/q/36159194">36159194</a></td>
  <td><pre>ImportError: libcudart.so.<i>Version</i>: cannot open shared object file:
  No such file or directory</pre></td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/q/41991101">41991101</a></td>
  <td><pre>ImportError: libcudnn.<i>Version</i>: cannot open shared object file:
  No such file or directory</pre></td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/36371137">36371137</a> and
  <a href="#Protobuf31">here</a></td>
  <td><pre>libprotobuf ERROR google/protobuf/src/google/protobuf/io/coded_stream.cc:207] A
  protocol message was rejected because it was too big (more than 67108864 bytes).
  To increase the limit (or to disable these warnings), see
  CodedInputStream::SetTotalBytesLimit() in google/protobuf/io/coded_stream.h.</pre></td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/q/35252888">35252888</a></td>
  <td><pre>Error importing tensorflow. Unless you are using bazel, you should
  not try to import tensorflow from its source directory; please exit the
  tensorflow source tree, and relaunch your python interpreter from
  there.</pre></td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/q/33623453">33623453</a></td>
  <td><pre>IOError: [Errno 2] No such file or directory:
  '/tmp/pip-o6Tpui-build/setup.py'</tt></pre>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/42006320">42006320</a></td>
  <td><pre>ImportError: Traceback (most recent call last):
  File ".../tensorflow/core/framework/graph_pb2.py", line 6, in <module>
  from google.protobuf import descriptor as _descriptor
  ImportError: cannot import name 'descriptor'</pre>
  </td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/questions/35190574">35190574</a> </td>
  <td><pre>SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify
  failed</pre></td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/42009190">42009190</a></td>
  <td><pre>
  Installing collected packages: setuptools, protobuf, wheel, numpy, tensorflow
  Found existing installation: setuptools 1.1.6
  Uninstalling setuptools-1.1.6:
  Exception:
  ...
  [Errno 1] Operation not permitted:
  '/tmp/pip-a1DXRT-uninstall/.../lib/python/_markerlib' </pre></td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/questions/36933958">36933958</a></td>
  <td><pre>
  ...
  Installing collected packages: setuptools, protobuf, wheel, numpy, tensorflow
  Found existing installation: setuptools 1.1.6
  Uninstalling setuptools-1.1.6:
  Exception:
  ...
  [Errno 1] Operation not permitted:
  '/tmp/pip-a1DXRT-uninstall/System/Library/Frameworks/Python.framework/
   Versions/2.7/Extras/lib/python/_markerlib'</pre>
  </td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/42006320">42006320</a></td>
  <td><pre>ImportError: Traceback (most recent call last):
File ".../tensorflow/core/framework/graph_pb2.py", line 6, in <module>
from google.protobuf import descriptor as _descriptor
ImportError: cannot import name 'descriptor'</pre>
  </td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/q/33623453">33623453</a></td>
  <td><pre>IOError: [Errno 2] No such file or directory:
  '/tmp/pip-o6Tpui-build/setup.py'</tt></pre>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/questions/35190574">35190574</a> </td>
  <td><pre>SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify
  failed</pre></td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/42009190">42009190</a></td>
  <td><pre>
  Installing collected packages: setuptools, protobuf, wheel, numpy, tensorflow
  Found existing installation: setuptools 1.1.6
  Uninstalling setuptools-1.1.6:
  Exception:
  ...
  [Errno 1] Operation not permitted:
  '/tmp/pip-a1DXRT-uninstall/.../lib/python/_markerlib' </pre></td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/q/33622019">33622019</a></td>
  <td><pre>ImportError: No module named copyreg</pre></td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/37810228">37810228</a></td>
  <td>During a <tt>pip install</tt> operation, the system returns:
  <pre>OSError: [Errno 1] Operation not permitted</pre>
  </td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/33622842">33622842</a></td>
  <td>An <tt>import tensorflow</tt> statement triggers an error such as the
  following:<pre>Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/site-packages/tensorflow/__init__.py",
    line 4, in <module>
    from tensorflow.python import *
    ...
  File "/usr/local/lib/python2.7/site-packages/tensorflow/core/framework/tensor_shape_pb2.py",
    line 22, in <module>
    serialized_pb=_b('\n,tensorflow/core/framework/tensor_shape.proto\x12\ntensorflow\"d\n\x10TensorShapeProto\x12-\n\x03\x64im\x18\x02
      \x03(\x0b\x32
      .tensorflow.TensorShapeProto.Dim\x1a!\n\x03\x44im\x12\x0c\n\x04size\x18\x01
      \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\tb\x06proto3')
  TypeError: __init__() got an unexpected keyword argument 'syntax'</pre>
  </td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/42075397">42075397</a></td>
  <td>A <tt>pip install</tt> command triggers the following error:
<pre>...<lots of warnings and errors>
You have not agreed to the Xcode license agreements, please run
'xcodebuild -license' (for user-level acceptance) or
'sudo xcodebuild -license' (for system-wide acceptance) from within a
Terminal window to review and agree to the Xcode license agreements.
...<more stack trace output>
  File "numpy/core/setup.py", line 653, in get_mathlib_info

    raise RuntimeError("Broken toolchain: cannot link a simple C program")

RuntimeError: Broken toolchain: cannot link a simple C program</pre>
  </td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/q/41007279">41007279</a></td>
  <td>
  <pre>[...\stream_executor\dso_loader.cc] Couldn't open CUDA library nvcuda.dll</pre>
  </td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/q/41007279">41007279</a></td>
  <td>
  <pre>[...\stream_executor\cuda\cuda_dnn.cc] Unable to load cuDNN DSO</pre>
  </td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/42006320">42006320</a></td>
  <td><pre>ImportError: Traceback (most recent call last):
File "...\tensorflow\core\framework\graph_pb2.py", line 6, in <module>
from google.protobuf import descriptor as _descriptor
ImportError: cannot import name 'descriptor'</pre>
  </td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/q/42011070">42011070</a></td>
  <td><pre>No module named "pywrap_tensorflow"</pre></td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/q/42217532">42217532</a></td>
  <td>
  <pre>OpKernel ('op: "BestSplits" device_type: "CPU"') for unknown op: BestSplits</pre>
  </td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/q/43134753">43134753</a></td>
  <td>
  <pre>The TensorFlow library wasn't compiled to use SSE instructions</pre>
  </td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/q/38896424">38896424</a></td>
  <td>
  <pre>Could not find a version that satisfies the requirement tensorflow</pre>
  </td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/42006320">42006320</a></td>
  <td><pre>ImportError: Traceback (most recent call last):
File ".../tensorflow/core/framework/graph_pb2.py", line 6, in <module>
from google.protobuf import descriptor as _descriptor
ImportError: cannot import name 'descriptor'</pre>
  </td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/q/33623453">33623453</a></td>
  <td><pre>IOError: [Errno 2] No such file or directory:
  '/tmp/pip-o6Tpui-build/setup.py'</tt></pre>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/questions/35190574">35190574</a> </td>
  <td><pre>SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify
  failed</pre></td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/42009190">42009190</a></td>
  <td><pre>
  Installing collected packages: setuptools, protobuf, wheel, numpy, tensorflow
  Found existing installation: setuptools 1.1.6
  Uninstalling setuptools-1.1.6:
  Exception:
  ...
  [Errno 1] Operation not permitted:
  '/tmp/pip-a1DXRT-uninstall/.../lib/python/_markerlib' </pre></td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/q/33622019">33622019</a></td>
  <td><pre>ImportError: No module named copyreg</pre></td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/37810228">37810228</a></td>
  <td>During a <tt>pip install</tt> operation, the system returns:
  <pre>OSError: [Errno 1] Operation not permitted</pre>
  </td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/33622842">33622842</a></td>
  <td>An <tt>import tensorflow</tt> statement triggers an error such as the
  following:<pre>Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/site-packages/tensorflow/__init__.py",
    line 4, in <module>
    from tensorflow.python import *
    ...
  File "/usr/local/lib/python2.7/site-packages/tensorflow/core/framework/tensor_shape_pb2.py",
    line 22, in <module>
    serialized_pb=_b('\n,tensorflow/core/framework/tensor_shape.proto\x12\ntensorflow\"d\n\x10TensorShapeProto\x12-\n\x03\x64im\x18\x02
      \x03(\x0b\x32
      .tensorflow.TensorShapeProto.Dim\x1a!\n\x03\x44im\x12\x0c\n\x04size\x18\x01
      \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\tb\x06proto3')
  TypeError: __init__() got an unexpected keyword argument 'syntax'</pre>
  </td>
</tr>
<tr>
  <td><a
  href="https://stackoverflow.com/questions/41293077/how-to-compile-tensorflow-with-sse4-2-and-avx-instructions">41293077</a></td>
  <td><pre>W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow
  library wasn't compiled to use SSE4.1 instructions, but these are available on
  your machine and could speed up CPU computations.</pre></td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/42013316">42013316</a></td>
  <td><pre>ImportError: libcudart.so.8.0: cannot open shared object file:
  No such file or directory</pre></td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/42013316">42013316</a></td>
  <td><pre>ImportError: libcudnn.5: cannot open shared object file:
  No such file or directory</pre></td>
</tr>
<tr>
  <td><a href="http://stackoverflow.com/q/35953210">35953210</a></td>
  <td>Invoking `python` or `ipython` generates the following error:
  <pre>ImportError: cannot import name pywrap_tensorflow</pre></td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/questions/45276830">45276830</a></td>
  <td><pre>external/local_config_cc/BUILD:50:5: in apple_cc_toolchain rule
  @local_config_cc//:cc-compiler-darwin_x86_64: Xcode version must be specified
  to use an Apple CROSSTOOL.</pre>
  </td>
</tr>
<tr>
  <td><a href="https://stackoverflow.com/q/47080760">47080760</a></td>
  <td><pre>undefined reference to `cublasGemmEx@libcublas.so.9.0'</pre></td>
</tr>
<tr>
  <td><a href="https://github.com/tensorflow/tensorflow/issues/22512">22512</a></td>
  <td><pre>ModuleNotFoundError: No module named 'tensorflow.python._pywrap_tensorflow_internal'</pre></td>
</tr>
<tr>
  <td><a href="https://github.com/tensorflow/tensorflow/issues/22512">22512</a>, <a href="https://github.com/tensorflow/tensorflow/issues/22794">22794</a></td>
  <td><pre>ImportError: DLL load failed: The specified module could not be found.</pre></td>
</tr>
<tr>
  <td><a href="https://github.com/tensorflow/tensorflow/issues/24835">24835</a></td>
  <td><pre>Could not install packages due to an EnvironmentError: [Errno 2] No such file or directory: [long path name]</pre></td>
</tr>
</table>
