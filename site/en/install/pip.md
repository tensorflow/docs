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
    conda install -c conda-forge cudatoolkit=11.8.0
    python3 -m pip install nvidia-cudnn-cu11==8.6.0.163 tensorflow==2.13.*
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    echo 'export LD_LIBRARY_PATH=$CUDNN_PATH/lib:$CONDA_PREFIX/lib/:$LD_LIBRARY_PATH' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    source $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    # Verify install:
    python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
    ```

* {MacOS}

    ```bash
    # There is currently no official GPU support for MacOS.
    python3 -m pip install tensorflow
    # Verify install:
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
    # Verify install:
    python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
    ```

* {Windows WSL2}

    Note: TensorFlow with GPU access is supported for WSL2 on Windows 10 19044 or
    higher. This corresponds to Windows 10 version 21H2, the November 2021
    update. You can get the latest update from here:
    [Download Windows 10](https://www.microsoft.com/software-download/windows10){:.external}.
    For instructions, see
    [Install WSL2](https://docs.microsoft.com/windows/wsl/install){:.external}
    and
    [NVIDIA’s setup docs](https://docs.nvidia.com/cuda/wsl-user-guide/index.html){:.external}
    for CUDA in WSL.

    ```bash
    conda install -c conda-forge cudatoolkit=11.8.0
    python3 -m pip install nvidia-cudnn-cu11==8.6.0.163 tensorflow==2.13.*
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    echo 'export LD_LIBRARY_PATH=$CUDNN_PATH/lib:$CONDA_PREFIX/lib/:$LD_LIBRARY_PATH' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    source $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    # Verify install:
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
*   Windows Native - Windows 7 or higher (64-bit) *(no GPU support after TF 2.10)*
*   Windows WSL2 - Windows 10 19044 or higher (64-bit)

Note: GPU support is available for Ubuntu and Windows with CUDA®-enabled cards.

## Software requirements

*   Python 3.8–3.11
*   pip version 19.0 or higher for Linux (requires `manylinux2014` support) and
    Windows. pip version 20.3 or higher for macOS.
*   Windows Native Requires
    [Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017 and 2019](https://support.microsoft.com/help/2977003/the-latest-supported-visual-c-downloads){:.external}


The following NVIDIA® software are only required for GPU support.

*   [NVIDIA® GPU drivers](https://www.nvidia.com/drivers){:.external}
    version 450.80.02 or higher.
*   [CUDA® Toolkit 11.8](https://developer.nvidia.com/cuda-toolkit-archive){:.external}.
*   [cuDNN SDK 8.6.0](https://developer.nvidia.com/cudnn){:.external}.
*   *(Optional)*
    [TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/archives/index.html#trt_7){:.external}
    to improve latency and throughput for inference.

## Step-by-step instructions

*   {Linux}

    ### 1. System requirements

    *  Ubuntu 16.04 or higher (64-bit)

    TensorFlow only officially support Ubuntu. However, the following
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

    ### 2. Install Miniconda

    [Miniconda](https://docs.conda.io/en/latest/miniconda.html){:.external} is the
    recommended approach for installing TensorFlow with GPU support.
    It creates a separate environment to avoid changing any installed
    software in your system. This is also the easiest way to install the required
    software especially for the GPU setup.

    You can use the following command to install Miniconda. During installation,
    you may need to press enter and type "yes".

    ```bash
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
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

    Make sure it is activated for the rest of the installation.

    ### 4. GPU setup

    You can skip this section if you only run TensorFlow on the CPU.

    First install the
    [NVIDIA GPU driver](https://www.nvidia.com/Download/index.aspx){:.external}
    if you have not. You can use the following command to verify it is
    installed.

    ```bash
    nvidia-smi
    ```

    Then install CUDA and cuDNN with conda and pip.

    ```bash
    conda install -c conda-forge cudatoolkit=11.8.0
    pip install nvidia-cudnn-cu11==8.6.0.163
    ```

    Configure the system paths. You can do it with the following command every time
    you start a new terminal after activating your conda environment.

    ```bash
    CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))
    export LD_LIBRARY_PATH=$CUDNN_PATH/lib:$CONDA_PREFIX/lib/:$LD_LIBRARY_PATH
    ```

    For your convenience it is recommended that you automate it with the following
    commands. The system paths will be automatically configured when you
    activate this conda environment.

    ```bash
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    echo 'export LD_LIBRARY_PATH=$CUDNN_PATH/lib:$CONDA_PREFIX/lib/:$LD_LIBRARY_PATH' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    ```

    ### 5. Install TensorFlow

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
    pip install tensorflow==2.13.*
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

    ### Ubuntu 22.04

    In Ubuntu 22.04, you may encounter the following error:

    ```
    Can't find libdevice directory ${CUDA_DIR}/nvvm/libdevice.
    ...
    Couldn't invoke ptxas --version
    ...
    InternalError: libdevice not found at ./libdevice.10.bc [Op:__some_op]
    ```

    To fix this error, you will need to run the following commands.

    ```bash
    # Install NVCC
    conda install -c nvidia cuda-nvcc=11.3.58
    # Configure the XLA cuda directory
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    printf 'export XLA_FLAGS=--xla_gpu_cuda_data_dir=$CONDA_PREFIX/lib/\n' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    source $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    # Copy libdevice file to the required path
    mkdir -p $CONDA_PREFIX/lib/nvvm/libdevice
    cp $CONDA_PREFIX/lib/libdevice.10.bc $CONDA_PREFIX/lib/nvvm/libdevice/
    ```

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

    Note: Requires Python 3.8–3.11, and pip >= 20.3 for MacOS.

    ```bash
    python3 --version
    python3 -m pip --version
    ```

   ### 3. Install Miniconda

   [Miniconda](https://docs.conda.io/en/latest/miniconda.html){:.external}
   is the recommended approach for installing TensorFlow.
   It creates a separate environment to avoid changing any installed
   software in your system.

   Note: Miniconda is not a requirement for running TensorFlow on CPU. If you'd
   prefer to create a virtual environment using
   [venv](https://docs.python.org/3/library/venv.html) or
   [Virtualenv](https://virtualenv.pypa.io/en/latest/), you can do so. Just
   adjust the installation steps accordingly, and then follow the instructions
   to install TensorFlow using pip.

   Install Miniconda:

    ```bash
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o Miniconda3-latest-MacOSX-x86_64.sh
    bash Miniconda3-latest-MacOSX-x86_64.sh
    ```

    You may need to restart your terminal or `source ~/.bashrc` to enable the
    `conda` command. Use `conda -V` to test if it is installed successfully.

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

    ### 5. Install TensorFlow

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
    pip install tensorflow
    ```

    ### 6. Verify install

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
        [Microsoft Visual C++ downloads](https://support.microsoft.com/help/2977003/the-latest-supported-visual-c-downloads){:.external}.
    2.  Scroll down the page to the *Visual Studio 2015, 2017 and 2019* section.
    3.  Download and install the *Microsoft Visual C++ Redistributable for
        Visual Studio 2015, 2017 and 2019* for your platform.

    Make sure
    [long paths are enabled](https://superuser.com/questions/1119883/windows-10-enable-ntfs-long-paths-policy-option-missing){:.external}
    on Windows.

    ### 3. Install Miniconda

    [Miniconda](https://docs.conda.io/en/latest/miniconda.html){:.external}
    is the recommended approach for installing TensorFlow with GPU support.
    It creates a separate environment to avoid changing any installed
    software in your system. This is also the easiest way to install the
    required software especially for the GPU setup.

    Download the
    [Miniconda Windows Installer](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe){:.external}.
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
    [NVIDIA GPU driver](https://www.nvidia.com/Download/index.aspx){:.external}
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

    ### 7. Verify install

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
   
    * [Download the latest Windows 10 update](https://www.microsoft.com/software-download/windows10){:.external}.
    * [Install WSL2](https://docs.microsoft.com/windows/wsl/install){:.external}
    * [Setup NVIDIA® GPU support in WSL2](https://docs.nvidia.com/cuda/wsl-user-guide/index.html){:.external}

    ### 2. Install Miniconda

    [Miniconda](https://docs.conda.io/en/latest/miniconda.html){:.external} is the
    recommended approach for installing TensorFlow with GPU support.
    It creates a separate environment to avoid changing any installed
    software in your system. This is also the easiest way to install the required
    software especially for the GPU setup.

    You can use the following command to install Miniconda. During installation,
    you may need to press enter and type "yes".

    ```bash
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
    ```

    You may need to restart your terminal or `source ~/.bashrc` to enable the
    `conda` command. Use `conda -V` to test if it is installed successfully.

    ### 3. Create a conda environment

    Create a new conda environment named <a href="https://www.tensorflow.org/api_docs/python/tf"><code>tf</code></a> with the following command.

    ```bash
    conda create --name tf python=3.9
    ```

    You can deactivate and activate it with the following commands.

    ```bash
    conda deactivate
    conda activate tf
    ```

    Make sure it is activated for the rest of the installation.

    ### 4. GPU setup

    You can skip this section if you only run TensorFlow on the CPU.

    First install the
    [NVIDIA GPU driver](https://www.nvidia.com/Download/index.aspx){:.external}
    if you have not. You can use the following command to verify it is
    installed.

    ```bash
    nvidia-smi
    ```

    Then install CUDA and cuDNN with conda and pip.

    ```bash
    conda install -c conda-forge cudatoolkit=11.8.0
    pip install nvidia-cudnn-cu11==8.6.0.163
    ```

    Configure the system paths. You can do it with following command everytime
    your start a new terminal after activating your conda environment.

    ```bash
    CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CUDNN_PATH/lib:$CONDA_PREFIX/lib/
    ```

    For your convenience it is recommended that you automate it with the following
    commands. The system paths will be automatically configured when you
    activate this conda environment.

    ```bash
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CUDNN_PATH/lib:$CONDA_PREFIX/lib/' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    ```

    ### 5. Install TensorFlow

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
    pip install tensorflow==2.13.*
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
    <td>Python 3.8 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-2.13.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.8 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.13.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.9 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-2.13.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.9 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.13.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.10 GPU&nbsp;support</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-2.13.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.10 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.13.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</td>
  </tr>

  <tr class="alt"><td colspan="2">macOS (CPU-only)</td></tr>
  <tr>
    <td>Python 3.8</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-2.13.0-cp38-cp38-macosx_10_15_x86_64.whl</td>
  </tr>
  <tr>
    <td>Python 3.9</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-2.13.0-cp39-cp39-macosx_10_15_x86_64.whl</td>
  </tr>
   <tr>
    <td>Python 3.10</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-2.13.0-cp310-cp310-macosx_10_15_x86_64.whl</td>
  </tr>

  <tr class="alt"><td colspan="2">Windows</td></tr>
  <tr>
    <td>Python 3.8 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow_cpu-2.13.0-cp38-cp38-win_amd64.whl</td>
  </tr>
  <tr>
    <td>Python 3.9 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow_cpu-2.13.0-cp39-cp39-win_amd64.whl</td>
  </tr>
  <tr>
    <td>Python 3.10 CPU-only</td>
    <td class="devsite-click-to-copy">https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow_cpu-2.13.0-cp310-cp310-win_amd64.whl</td>
  </tr>

</table>
