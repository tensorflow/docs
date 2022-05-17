# Install TensorFlow with pip

This guide is for the latest stable version of TensorFlow. For the
preview build *(nightly)*, please use the pip package named
`tf-nightly`. Refer to [these tables](./source#tested_build_configurations) for
older TensorFlow version requirements. For TensorFlow 1.x users, please refer to
the [migration guide](../guide/migrate) to upgrade to TensorFlow 2.

Here is a lookup table for the install commands. Scroll down for the
step-by-step instructions.

* {Linux}

   ```bash
   conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/
   python3 -m pip install tensorflow
   # Verify install:
   python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
   ```

* {MacOS}

   ```bash
   # Currently, we do not have official GPU support for MacOS.
   python3 -m pip install tensorflow
   # Verify install:
   python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
   ```

* {Windows}

   ```bash
   conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
   python3 -m pip install tensorflow
   # Verify install:
   python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
   ```

* {CPU}

   ```bash
   python3 -m pip install tensorflow
   # Verify install:
   python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
   ```

* {Nightly}

   ```bash
   python3 -m pip install tf-nightly
   # Verify install:
   python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
   ```

## Hardware requirements

Note: TensorFlow binaries use
[AVX instructions](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#CPUs_with_AVX){:.external}
which may not run on older CPUs.

The following GPU-enabled devices are supported:

*   NVIDIA® GPU card with CUDA® architectures 3.5, 5.0, 6.0, 7.0, 7.5, 8.0 and
    higher. See the list of
    [CUDA®-enabled GPU cards](https://developer.nvidia.com/cuda-gpus){:.external}.
*   For GPUs with unsupported CUDA® architectures, or to avoid JIT compilation
    from PTX, or to use different versions of the NVIDIA® libraries, see the
    [Linux build from source](./source.md) guide.
*   Packages do not contain PTX code except for the latest supported CUDA®
    architecture; therefore, TensorFlow fails to load on older GPUs when
    `CUDA_FORCE_PTX_JIT=1` is set. (See
    [Application Compatibility](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#application-compatibility)
    for details.) {:.external}

Note: The error message "Status: device kernel image is invalid" indicates that
the TensorFlow package does not contain PTX for your architecture. You can
enable compute capabilities by [building TensorFlow from source](./source.md).

## System requirements

*   Ubuntu 16.04 or higher (64-bit)
*   macOS 10.12.6 (Sierra) or higher (64-bit) *(no GPU support)*
*   Windows 7 or higher (64-bit)

Note: GPU support is available for Ubuntu and Windows with CUDA®-enabled cards.

## Software requirements

*   Python 3.7–3.10
*   pip version 19.0 or higher for Linux (requires `manylinux2010` support) and
    Windows, version 20.3 or higher for macOS
*   Windows Requires
    [Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017 and 2019](https://support.microsoft.com/help/2977003/the-latest-supported-visual-c-downloads){:.external}

The following NVIDIA® software are only required for GPU support.

*   [NVIDIA® GPU drivers](https://www.nvidia.com/drivers){:.external}
    version 450.80.02 or higher.
*   [CUDA® Toolkit 11.2](https://developer.nvidia.com/cuda-toolkit-archive){:.external}.
*   [cuDNN SDK 8.1.0](https://developer.nvidia.com/cudnn){:.external}.
*   *(Optional)*
    [TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/archives/index.html#trt_7){:.external}
    to improve latency and throughput for inference.

## Step-by-step instructions


*   {Linux}

    We only officially support Ubuntu. However, the following instructions may
    also work for other Linux distros.

    We recommend using
    [Miniconda](https://docs.conda.io/en/latest/miniconda.html){:.external} to
    create a separate environment to avoid changing any installed software in
    your system. This is also the easiest way to install the required software,
    especially for the GPU setup.

    ### 1. Install Miniconda

    You can use the following command to install Miniconda. During installation,
    you may need to press enter and type "yes".

    ```bash
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
    ```

    You may need to restart your terminal or `source ~/.bashrc` to enable the
    `conda` command. Use `conda -V` to test if it is installed successfully.

    ### 2. Create a conda environment

    Create a new conda environment named `tf` with the following command.

    ```bash
    conda create --name tf python=3.9
    ```

    You can deactivate and activate it with the following commands.

    ```bash
    conda deactivate
    conda activate tf
    ```

    Please make sure it is activated for the rest of the installation.

    ### 3. GPU setup

    You can skip this section if you only run TensorFlow on CPU.

    First, we need to install
    [NVIDIA GPU driver](https://www.nvidia.com/Download/index.aspx){:.external}
    if you have not. You can use the following command to verify it is
    installed.

    ```bash
    nvidia-smi
    ```

    Then, we install the CUDA, cuDNN with conda.

    ```bash
    conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
    ```

    Configure the system paths. You can do it with following command everytime
    your start a new terminal after activating your conda environment.

    ```bash
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/
    ```

    However, for your convenience, we recommend automating it with the following
    commands. The system paths will be automatically configured when you
    activate this conda environment.

    ```bash
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    ```

    ### 4. Install TensorFlow

    TensorFlow requires a recent version of pip, so upgrade your pip
    installation to be sure you're running the latest version.

    ```bash
    pip install --upgrade pip
    ```

    Then, install TensorFlow with pip.

    Note: Do not install with conda. It may not have the latest stable
    version. We recommend using pip since TensorFlow is only
    officially released to PyPI.

    ```bash
    pip install tensorflow
    ```

    ### 5. Verify install

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

    Note: For users of Apple M1 computers, to get native performance, you'll
    want to follow the instructions found
    [here](https://developer.apple.com/metal/tensorflow-plugin/){:.external}.
    Conda has shown to have the smoothest install. Some TensorFlow binaries
    (specifically, ones with custom C++ extensions like TensorFlow Decision
    Forests, object detection, and TFX) are not compiled against M1 targets. If
    you need those libraries, you will have to use TensorFlow with x86 emulation
    and Rosetta.

    Currently, we do not have official GPU support for running TensorFlow on
    MacOS. The following is instructions are for running on CPU.

    ### 1. Check Python version

    Check if your Python environment is already configured:

    Note: Requires Python 3.7–3.10, and pip >= 20.3 for MacOS.

    ```bash
    python3 --version
    python3 -m pip --version
    ```

    If you have the correct version of Python and pip, you may skip the next two
    steps and go to "4. Install TensorFlow". However, we still recommend not
    skipping the steps. Use
    [Miniconda](https://docs.conda.io/en/latest/miniconda.html){:.external} to
    install Python and pip. It create a separate environment to avoid
    changing any installed software in your system.

    ### 2. Install Miniconda

    You can use the following command to install Miniconda. During installation,
    you may need to press enter and type "yes".

    ```bash
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o Miniconda3-latest-MacOSX-x86_64.sh
    bash Miniconda3-latest-MacOSX-x86_64.sh
    ```

    You may need to restart your terminal or `source ~/.bashrc` to enable the
    `conda` command. Use `conda -V` to test if it is installed successfully.

    ### 3. Create a conda environment

    Create a new conda environment named `tf` with the following command.

    ```bash
    conda create --name tf python=3.9
    ```

    You can deactivate and activate it with the following commands.

    ```bash
    conda deactivate
    conda activate tf
    ```

    Please make sure it is activated for the rest of the installation.

    ### 4. Install TensorFlow

    TensorFlow requires a recent version of pip, so upgrade your pip
    installation to be sure you're running the latest version.

    ```bash
    pip install --upgrade pip
    ```

    Then, install TensorFlow with pip.

    Note: Do not install with conda. It may not have the latest stable
    version. We recommend using pip since TensorFlow is only
    officially released to PyPI.

    ```bash
    pip install tensorflow
    ```

    ### 5. Verify install

    ```bash
    python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    ```

    If a tensor is returned, you've installed TensorFlow successfully.

*   {Windows}

    Note: Experimental support for WSL2 on Windows 10 19044 or higher with GPU
    access is now available. This corresponds to Windows 10 version
    21H2, the November 2021 update. You can get the latest update from here:
    [Download Windows 10](https://www.microsoft.com/en-us/software-download/windows10){:.external}.
    For instructions, please see
    [NVIDIA’s setup docs](https://docs.nvidia.com/cuda/wsl-user-guide/index.html){:.external}
    for CUDA in WSL.

    ### 1. Install Microsoft Visual C++ Redistributable

    Install the *Microsoft Visual C++ Redistributable for Visual Studio 2015,
    2017, and 2019*. Starting with the TensorFlow 2.1.0 version, the
    `msvcp140_1.dll` file is required from this package (which may not be
    provided from older redistributable packages). The redistributable comes
    with *Visual Studio 2019* but can be installed separately:

    1.  Go to the
        [Microsoft Visual C++ downloads](https://support.microsoft.com/help/2977003/the-latest-supported-visual-c-downloads){:.external}.
    2.  Scroll down the page to the *Visual Studio 2015, 2017 and 2019* section.
    3.  Download and install the *Microsoft Visual C++ Redistributable for
        Visual Studio 2015, 2017 and 2019* for your platform.

    Make sure
    [long paths are enabled](https://superuser.com/questions/1119883/windows-10-enable-ntfs-long-paths-policy-option-missing){:.external}
    on Windows.

    ### 2. Install Miniconda

    We recommend using
    [Miniconda](https://docs.conda.io/en/latest/miniconda.html){:.external} to
    create a separate environment to avoid changing any installed software in
    your system. This is also the easiest way to install the required software,
    especially for the GPU setup.

    Download the
    [Miniconda Windows Installer](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe){:.external}.
    Double-click the downloaded file and follow the instructions on the screen.

    ### 3. Create a conda environment

    Create a new conda environment named `tf` with the following command.

    ```bash
    conda create --name tf python=3.9
    ```

    You can deactivate and activate it with the following commands.

    ```bash
    conda deactivate
    conda activate tf
    ```

    Please make sure it is activated for the rest of the installation.

    ### 4. GPU setup

    You can skip this section if you only run TensorFlow on CPU.

    First, we need to install
    [NVIDIA GPU driver](https://www.nvidia.com/Download/index.aspx){:.external}
    if you have not.

    Then, we install the CUDA, cuDNN with conda.

    ```bash
    conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
    ```

    ### 5. Install TensorFlow

    TensorFlow requires a recent version of pip, so upgrade your pip
    installation to be sure you're running the latest version.

    ```bash
    pip install --upgrade pip
    ```

    Then, install TensorFlow with pip.

    Note: Do not install with conda. It may not have the latest stable
    version. We recommend using pip since TensorFlow is only
    officially released to PyPI.

    ```bash
    pip install tensorflow
    ```

    ### 6. Verify install

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
  <tr class="alt"><td colspan="2">Linux</td></tr>
  <tr>
    <td>Python 3.7 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-2.9.0-cp37-cp37m-manylinux2014.whl</td>
  </tr>
  <tr>
    <td>Python 3.7 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.9.0-cp37-cp37m-manylinux2014.whl</td>
  </tr>
  <tr>
    <td>Python 3.8 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-2.9.0-cp38-cp38-manylinux2014.whl</td>
  </tr>
  <tr>
    <td>Python 3.8 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.9.0-cp38-cp38-manylinux2014.whl</td>
  </tr>
  <tr>
    <td>Python 3.9 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-2.9.0-cp39-cp39-manylinux2014.whl</td>
  </tr>
  <tr>
    <td>Python 3.9 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.9.0-cp39-cp39-manylinux2014.whl</td>
  </tr>
  <tr>
    <td>Python 3.10 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-2.9.0-cp310-cp310-manylinux2014.whl</td>
  </tr>
  <tr>
    <td>Python 3.10 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.9.0-cp310-cp310-manylinux2014.whl</td>
  </tr>

  <tr class="alt"><td colspan="2">macOS (CPU-only)</td></tr>
  <tr>
    <td>Python 3.7</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-2.9.0-cp37-cp37m-macosx_10_14_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.8</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-2.9.0-cp38-cp38-macosx_10_14_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.9</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-2.9.0-cp39-cp39-macosx_10_14_x86_64.whl</td>
  </tr>
   <tr>
    <td>Python 3.10</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-2.9.0-cp310-cp310-macosx_10_14_x86_64.whl</td>
  </tr>

  <tr class="alt"><td colspan="2">Windows</td></tr>
  <tr>
    <td>Python 3.7 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-2.9.0-cp37-cp37m-win_amd64.whl</td>
  </tr>
  <tr>
    <td>Python 3.7 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow_cpu-2.9.0-cp37-cp37m-win_amd64.whl</td>
  </tr>
  <tr>
    <td>Python 3.8 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-2.9.0-cp38-cp38-win_amd64.whl</td>
  </tr>
  <tr>
    <td>Python 3.8 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow_cpu-2.9.0-cp38-cp38-win_amd64.whl</td>
  </tr>
  <tr>
    <td>Python 3.9 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-2.9.0-cp39-cp39-win_amd64.whl</td>
  </tr>
  <tr>
    <td>Python 3.9 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow_cpu-2.9.0-cp39-cp39-win_amd64.whl</td>
  </tr>
    <tr>
    <td>Python 3.10 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-2.9.0-cp310-cp310-win_amd64.whl</td>
  </tr>
  <tr>
    <td>Python 3.10 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow_cpu-2.9.0-cp310-cp310-win_amd64.whl</td>
  </tr>

</table>
