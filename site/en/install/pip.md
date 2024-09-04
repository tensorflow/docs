
# Install TensorFlow with pip
<!-- mdformat global-off -->

This guide is for the latest stable version of TensorFlow. For the
preview build *(nightly)*, use the pip package named
`tf-nightly`. Refer to [these tables](./source#tested_build_configurations) for
older TensorFlow version requirements. For the CPU-only build, use the pip
package named `tensorflow-cpu`.

Here are the quick versions of the install commands. Scroll down for the
step-by-step instructions.

* {Linux}

    Note: Starting with TensorFlow `2.10`, Linux CPU-builds for Aarch64/ARM64
    processors are built, maintained, tested and released by a third party:
    [AWS](https://aws.amazon.com/).
    Installing the [`tensorflow`](https://pypi.org/project/tensorflow/)
    package on an ARM machine installs AWS's
    [`tensorflow-cpu-aws`](https://pypi.org/project/tensorflow-cpu-aws/) package.
    They are provided as-is. Tensorflow will use reasonable efforts to maintain
    the availability and integrity of this pip package. There may be delays if
    the third party fails to release the pip package. See
    [this blog post](https://blog.tensorflow.org/2022/09/announcing-tensorflow-official-build-collaborators.html)
    for more information about this collaboration.

    ```bash
    python3 -m pip install tensorflow[and-cuda]
    # Verify the installation:
    python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
    ```

* {MacOS}

    ```bash
    # There is currently no official GPU support for MacOS.
    python3 -m pip install tensorflow
    # Verify the installation:
    python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    ```

* {Windows Native}

    Caution: TensorFlow `2.10` was the **last** TensorFlow release that
    supported GPU on native-Windows.
    Starting with TensorFlow `2.11`, you will need to install
    [TensorFlow in WSL2](https://tensorflow.org/install/pip#windows-wsl2),
    or install `tensorflow` or `tensorflow-cpu` and, optionally, try the
    [TensorFlow-DirectML-Plugin](https://github.com/microsoft/tensorflow-directml-plugin#tensorflow-directml-plugin-)

    ```bash
    conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
    # Anything above 2.10 is not supported on the GPU on Windows Native
    python -m pip install "tensorflow<2.11"
    # Verify the installation:
    python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
    ```

* {Windows WSL2}

    Note: TensorFlow with GPU access is supported for WSL2 on Windows 10 19044 or
    higher. This corresponds to Windows 10 version 21H2, the November 2021
    update. You can get the latest update from here:
    [Download Windows 10](https://www.microsoft.com/software-download/windows10).
    For instructions, see
    [Install WSL2](https://docs.microsoft.com/windows/wsl/install)
    and
    [NVIDIA’s setup docs](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)
    for CUDA in WSL.

    ```bash
    python3 -m pip install tensorflow[and-cuda]
    # Verify the installation:
    python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
    ```

* {CPU}

    Note: Starting with TensorFlow `2.10`, Windows CPU-builds for x86/x64
    processors are built, maintained, tested and released by a third party:
    [Intel](https://www.intel.com/).
    Installing the Windows-native [`tensorflow`](https://pypi.org/project/tensorflow/)
    or [`tensorflow-cpu`](https://pypi.org/project/tensorflow-cpu/)
    package installs Intel's
    [`tensorflow-intel`](https://pypi.org/project/tensorflow-intel/)
    package. These packages are provided as-is. Tensorflow will use reasonable
    efforts to maintain the availability and integrity of this pip package.
    There may be delays if the third party fails to release the pip package. See
    [this blog post](https://blog.tensorflow.org/2022/09/announcing-tensorflow-official-build-collaborators.html)
    for more information about this
    collaboration.

    ```bash
    python3 -m pip install tensorflow
    # Verify the installation:
    python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    ```

* {Nightly}

    ```bash
    python3 -m pip install tf-nightly
    # Verify the installation:
    python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    ```

## Hardware requirements

Note: TensorFlow binaries use
[AVX instructions](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#CPUs_with_AVX)
which may not run on older CPUs.

The following GPU-enabled devices are supported:

*   NVIDIA® GPU card with CUDA® architectures 3.5, 5.0, 6.0, 7.0, 7.5, 8.0 and
    higher. See the list of
    [CUDA®-enabled GPU cards](https://developer.nvidia.com/cuda-gpus).
*   For GPUs with unsupported CUDA® architectures, or to avoid JIT compilation
    from PTX, or to use different versions of the NVIDIA® libraries, see the
    [Linux build from source](./source.md) guide.
*   Packages do not contain PTX code except for the latest supported CUDA®
    architecture; therefore, TensorFlow fails to load on older GPUs when
    `CUDA_FORCE_PTX_JIT=1` is set. (See
    [Application Compatibility](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#application-compatibility)
    for details.) 

Note: The error message "Status: device kernel image is invalid" indicates that
the TensorFlow package does not contain PTX for your architecture. You can
enable compute capabilities by [building TensorFlow from source](./source.md).

## System requirements

*   Ubuntu 16.04 or higher (64-bit)
*   macOS 10.12.6 (Sierra) or higher (64-bit) *(no GPU support)*
*   Windows Native - Windows 7 or higher (64-bit) *(no GPU support after TF 2.10)*
*   Windows WSL2 - Windows 10 19044 or higher (64-bit)

Note: GPU support is available for Ubuntu and Windows with CUDA®-enabled cards.

## Software requirements

*   Python 3.9–3.12
*   pip version 19.0 or higher for Linux (requires `manylinux2014` support) and
    Windows. pip version 20.3 or higher for macOS.
*   Windows Native Requires
    [Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017 and 2019](https://support.microsoft.com/help/2977003/the-latest-supported-visual-c-downloads)


The following NVIDIA® software are only required for GPU support.

*   [NVIDIA® GPU drivers](https://www.nvidia.com/drivers)
    * >= 525.60.13 for Linux
    * >= 528.33 for WSL on Windows
*   [CUDA® Toolkit 12.3](https://developer.nvidia.com/cuda-toolkit-archive).
*   [cuDNN SDK 8.9.7](https://developer.nvidia.com/cudnn).
*   *(Optional)*
    [TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/archives/index.html#trt_7)
    to improve latency and throughput for inference.

## Step-by-step instructions

*   {Linux}

    ### 1. System requirements

    *  Ubuntu 16.04 or higher (64-bit)

    TensorFlow only officially supports Ubuntu. However, the following
    instructions may also work for other Linux distros.

    Note: Starting with TensorFlow `2.10`, Linux CPU-builds for Aarch64/ARM64
    processors are built, maintained, tested and released by a third party:
    [AWS](https://aws.amazon.com/).
    Installing the [`tensorflow`](https://pypi.org/project/tensorflow/)
    package on an ARM machine installs AWS's
    [`tensorflow-cpu-aws`](https://pypi.org/project/tensorflow-cpu-aws/) package.
    They are provided as-is. Tensorflow will use reasonable efforts to maintain
    the availability and integrity of this pip package. There may be delays if
    the third party fails to release the pip package. See
    [this blog post](https://blog.tensorflow.org/2022/09/announcing-tensorflow-official-build-collaborators.html)
    for more information about this collaboration.

    ### 2. GPU setup

    You can skip this section if you only run TensorFlow on the CPU.

    Install the
    [NVIDIA GPU driver](https://www.nvidia.com/Download/index.aspx)
    if you have not. You can use the following command to verify it is
    installed.

    ```bash
    nvidia-smi
    ```

    ### 3. Install TensorFlow

    TensorFlow requires a recent version of pip, so upgrade your pip
    installation to be sure you're running the latest version.

    ```bash
    pip install --upgrade pip
    ```

    Then, install TensorFlow with pip.

    ```bash
    # For GPU users
    pip install tensorflow[and-cuda]
    # For CPU users
    pip install tensorflow
    ```

    ### 4. Verify the installation

    Verify the CPU setup:

    ```bash
    python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    ```

    If a tensor is returned, you've installed TensorFlow successfully.

    Verify the GPU setup:

    ```bash
    python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
    ```

    If a list of GPU devices is returned, you've installed TensorFlow
    successfully.

*   {MacOS}

   ### 1. System requirements

    *   macOS 10.12.6 (Sierra) or higher (64-bit)

    Note: While TensorFlow supports Apple Silicon (M1), packages that include
    custom C++ extensions for TensorFlow also need to be compiled for Apple M1.
    Some packages, like
    [tensorflow_decision_forests](https://www.tensorflow.org/decision_forests)
    publish M1-compatible versions, but many packages don't. To use those
    libraries, you will have to use TensorFlow with x86 emulation and Rosetta.

    Currently there is no official GPU support for running TensorFlow on
    MacOS. The following instructions are for running on CPU.

    ### 2. Check Python version

    Check if your Python environment is already configured:

    Note: Requires Python 3.9–3.11, and pip >= 20.3 for MacOS.

    ```bash
    python3 --version
    python3 -m pip --version
    ```

    ### 3. Install TensorFlow

    TensorFlow requires a recent version of pip, so upgrade your pip
    installation to be sure you're running the latest version.

    ```bash
    pip install --upgrade pip
    ```

    Then, install TensorFlow with pip.

    ```bash
    pip install tensorflow
    ```

    ### 4. Verify the installation

    ```bash
    python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    ```

    If a tensor is returned, you've installed TensorFlow successfully.

*   {Windows Native}

   Caution: TensorFlow `2.10` was the **last** TensorFlow release that
   supported GPU on native-Windows.
   Starting with TensorFlow `2.11`, you will need to install
   [TensorFlow in WSL2](https://tensorflow.org/install/pip#windows-[wsl2]),
   or install `tensorflow-cpu` and, optionally, try the
   [TensorFlow-DirectML-Plugin](https://github.com/microsoft/tensorflow-directml-plugin#tensorflow-directml-plugin-)

   ## 1. System requirements

   *   Windows 7 or higher (64-bit)

    Note: Starting with TensorFlow `2.10`, Windows CPU-builds for x86/x64
    processors are built, maintained, tested and released by a third party:
    [Intel](https://www.intel.com/).
    Installing the windows-native [`tensorflow`](https://pypi.org/project/tensorflow/)
    or [`tensorflow-cpu`](https://pypi.org/project/tensorflow-cpu/)
    package installs Intel's
    [`tensorflow-intel`](https://pypi.org/project/tensorflow-intel/)
    package. These packages are provided as-is. Tensorflow will use reasonable
    efforts to maintain the availability and integrity of this pip package.
    There may be delays if the third party fails to release the pip package. See
    [this blog post](https://blog.tensorflow.org/2022/09/announcing-tensorflow-official-build-collaborators.html)
    for more information about this
    collaboration.

    ### 2. Install Microsoft Visual C++ Redistributable

    Install the *Microsoft Visual C++ Redistributable for Visual Studio 2015,
    2017, and 2019*. Starting with the TensorFlow 2.1.0 version, the
    `msvcp140_1.dll` file is required from this package (which may not be
    provided from older redistributable packages). The redistributable comes
    with *Visual Studio 2019* but can be installed separately:

    1.  Go to the
        [Microsoft Visual C++ downloads](https://support.microsoft.com/help/2977003/the-latest-supported-visual-c-downloads).
    2.  Scroll down the page to the *Visual Studio 2015, 2017 and 2019* section.
    3.  Download and install the *Microsoft Visual C++ Redistributable for
        Visual Studio 2015, 2017 and 2019* for your platform.

    Make sure
    [long paths are enabled](https://superuser.com/questions/1119883/windows-10-enable-ntfs-long-paths-policy-option-missing)
    on Windows.

    ### 3. Install Miniconda

    [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
    is the recommended approach for installing TensorFlow with GPU support.
    It creates a separate environment to avoid changing any installed
    software in your system. This is also the easiest way to install the
    required software especially for the GPU setup.

    Download the
    [Miniconda Windows Installer](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe).
    Double-click the downloaded file and follow the instructions on the screen.

    ### 4. Create a conda environment

    Create a new conda environment named `tf` with the following command.

    ```bash
    conda create --name tf python=3.9
    ```

    You can deactivate and activate it with the following commands.

    ```bash
    conda deactivate
    conda activate tf
    ```

    Make sure it is activated for the rest of the installation.

    ### 5. GPU setup

    You can skip this section if you only run TensorFlow on CPU.

    First install
    [NVIDIA GPU driver](https://www.nvidia.com/Download/index.aspx)
    if you have not.

    Then install the CUDA, cuDNN with conda.

    ```bash
    conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
    ```

    ### 6. Install TensorFlow

    TensorFlow requires a recent version of pip, so upgrade your pip
    installation to be sure you're running the latest version.

    ```bash
    pip install --upgrade pip
    ```

    Then, install TensorFlow with pip.

    Note: Do not install TensorFlow with conda. It may not have the latest stable
    version. pip is recommended since TensorFlow is only officially released to
    PyPI.

    ```bash
    # Anything above 2.10 is not supported on the GPU on Windows Native
    pip install "tensorflow<2.11" 
    ```

    ### 7. Verify the installation

    Verify the CPU setup:

    ```bash
    python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    ```

    If a tensor is returned, you've installed TensorFlow successfully.

    Verify the GPU setup:

    ```bash
    python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
    ```

    If a list of GPU devices is returned, you've installed TensorFlow
    successfully.

*   {Windows WSL2}

    ### 1. System requirements

    *   Windows 10 19044 or higher (64-bit). This corresponds to Windows 10
        version 21H2, the November 2021 update.
   
    See the following documents to:
   
    * [Download the latest Windows 10 update](https://www.microsoft.com/software-download/windows10).
    * [Install WSL2](https://docs.microsoft.com/windows/wsl/install)
    * [Setup NVIDIA® GPU support in WSL2](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)

    ### 2. GPU setup

    You can skip this section if you only run TensorFlow on the CPU.

    Install the
    [NVIDIA GPU driver](https://www.nvidia.com/Download/index.aspx)
    if you have not. You can use the following command to verify it is
    installed.

    ```bash
    nvidia-smi
    ```

    ### 3. Install TensorFlow

    TensorFlow requires a recent version of pip, so upgrade your pip
    installation to be sure you're running the latest version.

    ```bash
    pip install --upgrade pip
    ```

    Then, install TensorFlow with pip.

    ```bash
    # For GPU users
    pip install tensorflow[and-cuda]
    # For CPU users
    pip install tensorflow
    ```

    ### 4. Verify the installation

    Verify the CPU setup:

    ```bash
    python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    ```

    If a tensor is returned, you've installed TensorFlow successfully.

    Verify the GPU setup:

    ```bash
    python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
    ```

    If a list of GPU devices is returned, you've installed TensorFlow
    successfully.


## Package location

A few installation mechanisms require the URL of the TensorFlow Python package.
The value you specify depends on your Python version.

<table>
  <tr><th>Version</th><th>URL</th></tr>
  <tr class="alt"><td colspan="2">Linux x86</td></tr>
  <tr>
    <td>Python 3.9 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.9 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow_cpu-2.17.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.10 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.10 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow_cpu-2.17.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.11 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.11 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow_cpu-2.17.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.12 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.12 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow_cpu-2.17.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</td>
  </tr>

  <tr class="alt"><td colspan="2">Linux Arm64 (CPU-only)</td></tr>
  <tr>
    <td>Python 3.9</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl</td>
  </tr>
  <tr>
    <td>Python 3.10</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl</td>
  </tr>
  <tr>
    <td>Python 3.11</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl</td>
  </tr>
  <tr>
    <td>Python 3.12</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl</td>
  </tr>

  <tr class="alt"><td colspan="2">macOS x86 (CPU-only)</td></tr>
  <tr class="alt"><td colspan="2"><b>Caution</b>: TensorFlow 2.16 was the <b>last</b> TensorFlow release that supported macOS x86</td></tr>
  <tr>
    <td>Python 3.9</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.16.2/tensorflow-2.16.2-cp39-cp39-macosx_10_15_x86_64.whl</td>
  </tr>
   <tr>
    <td>Python 3.10</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.16.2/tensorflow-2.16.2-cp310-cp310-macosx_10_15_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.11</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.16.2/tensorflow-2.16.2-cp311-cp311-macosx_10_15_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.12</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.16.2/tensorflow-2.16.2-cp312-cp312-macosx_10_15_x86_64.whl</td>
  </tr>

  <tr class="alt"><td colspan="2">macOS Arm64 (CPU-only)</td></tr>
  <tr>
    <td>Python 3.9</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp39-cp39-macosx_12_0_arm64.whl</td>
  </tr>
  <tr>
    <td>Python 3.10</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp310-cp310-macosx_12_0_arm64.whl</td>
  </tr>
  <tr>
    <td>Python 3.11</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp311-cp311-macosx_12_0_arm64.whl</td>
  </tr>
  <tr>
    <td>Python 3.12</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp312-cp312-macosx_12_0_arm64.whl</td>
  </tr>

  <tr class="alt"><td colspan="2">Windows (CPU-only)</td></tr>
  <tr>
    <td>Python 3.9</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp39-cp39-win_amd64.whl</td>
  </tr>
  <tr>
    <td>Python 3.10</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp310-cp310-win_amd64.whl</td>
  </tr>
  <tr>
    <td>Python 3.11</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp311-cp311-win_amd64.whl</td>
  </tr>
  <tr>
    <td>Python 3.12</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/versions/2.17.0/tensorflow-2.17.0-cp312-cp312-win_amd64.whl</td>
  </tr>

</table>
