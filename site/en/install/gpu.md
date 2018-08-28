# GPU support

Note: Due to the number of libraries required, using [Docker](./docker.md)
is recommended over installing directly on the host system.

The following NVIDIA® *hardware* must be installed on your system:

* GPU card with CUDA Compute Capability 3.5 or higher. See
  [NVIDIA documentation](https://developer.nvidia.com/cuda-gpus) for a list of
  supported GPU cards.

The following NVIDIA® <i>software</i> must be installed on your system:

* [GPU drivers](http://nvidia.com/driver). CUDA 9.0 requires 384.x or higher.
* [CUDA Toolkit 9.0](http://nvidia.com/cuda).
* [cuDNN SDK](http://developer.nvidia.com/cudnn) (>= 7.0). Version 7.1 is
  recommended.
* [CUPTI](http://docs.nvidia.com/cuda/cupti/) ships with the CUDA Toolkit, but
  you also need to append its path to the `LD_LIBRARY_PATH` environment
  variable: `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64`
* *OPTIONAL*: [NCCL 2.2](https://developer.nvidia.com/nccl) to use TensorFlow
  with multiple GPUs.
* *OPTIONAL*: [TensorRT](http://docs.nvidia.com/deeplearning/sdk/tensorrt-install-guide/index.html)
  which can improve latency and throughput for inference for some models.

To use a GPU with CUDA Compute Capability 3.0, or different versions of the
preceding NVIDIA libraries see the
<a href="./source.md">TensorFlow build from source guide</a>. If using
Ubuntu&nbsp;16.04 and possibly other Debian based linux distros, `apt-get` can be
used with the NVIDIA repository to simplify installation.

```bash
# Adds NVIDIA package repository.
sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.1.85-1_amd64.deb
wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1604_9.1.85-1_amd64.deb
sudo dpkg -i nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb
sudo apt-get update
# Includes optional NCCL 2.x.
sudo apt-get install cuda9.0 cuda-cublas-9-0 cuda-cufft-9-0 cuda-curand-9-0 \
  cuda-cusolver-9-0 cuda-cusparse-9-0 libcudnn7=7.1.4.18-1+cuda9.0 \
   libnccl2=2.2.13-1+cuda9.0 cuda-command-line-tools-9-0
# Optionally install TensorRT runtime, must be done after above cuda install.
sudo apt-get update
sudo apt-get install libnvinfer4=4.1.2-1+cuda9.0
```


## Windows

If you are installing TensorFlow with GPU support using one of the mechanisms
described in this guide, then the following NVIDIA software must be
installed on your system:

* CUDA® Toolkit 9.0. For details, see
  [NVIDIA's documentation](http://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/)
  Ensure that you append the relevant CUDA pathnames to the `%PATH%`
  environment variable as described in the NVIDIA documentation.
* The NVIDIA drivers associated with CUDA Toolkit 9.0.
* cuDNN v7.0. For details, see
  [NVIDIA's documentation](https://developer.nvidia.com/cudnn).
  Note that cuDNN is typically installed in a different location from the
  other CUDA DLLs. Ensure that you add the directory where you installed
  the cuDNN DLL to your `%PATH%` environment variable.
* GPU card with CUDA Compute Capability 3.0 or higher for building
  from source and 3.5 or higher for our binaries. See
  [NVIDIA documentation](https://developer.nvidia.com/cuda-gpus) for a
  list of supported GPU cards.

If you have a different version of one of the preceding packages, please
change to the specified versions.  In particular, the cuDNN version
must match exactly: TensorFlow will not load if it cannot find `cuDNN64_7.dll`.
To use a different version of cuDNN, you must build from source.


<!-- from source_windows -->
The following NVIDIA® _hardware_ must be installed on your system:

* GPU card with CUDA Compute Capability 3.5 or higher. See
  [NVIDIA documentation](https://developer.nvidia.com/cuda-gpus) for a list of
  supported GPU cards.

The following NVIDIA® _software_ must be installed on your system:

* [GPU drivers](http://nvidia.com/driver). CUDA 9.0 requires 384.x or higher.
* [CUDA Toolkit](http://nvidia.com/cuda) (>= 8.0). We recommend version 9.0.
* [cuDNN SDK](http://developer.nvidia.com/cudnn) (>= 6.0). We recommend
  version 7.1.x.
