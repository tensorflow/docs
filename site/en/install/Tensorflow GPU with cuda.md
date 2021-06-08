CUDA11.0 installation
First create a virtual environment and name it yourself. I am using python3.7.

>>conda create -n tensorflow2.4 python=3.7

Check the downloadable CUDA version

>>conda search cuda

Here, for cuda toolkit=11.0

>>conda install cudatoolkit=11.0

cudnn8.05 installation
If you directly use conda to view the downloadable version, the highest version is only 7.6.5. There is no way but to download from the official website. The download URL is https://developer.nvidia.com/rdp/cudnn-download , select the package underlined in the figure below to download directly, but the download speed is real ink, if you download Is too slow, you can look here.
Extract the code ekil , but everyone knows the speed of a certain disk, try it anyway, whoever will use which one.

Unzip the command, in the directory where the installation package is located, run

Next is the name of the download package. After decompression, enter the cuda/lib64 path and copy all the files inside into the lib of the corresponding virtual environment (tensorflow2.4) (there are a lot of files, don't panic, just do it).

tensorflow2.4 installation
The use of conda command to install directly to reinstall cuda and cudnn, but this version is not appropriate (such as it is estimated that next year, the official updates), we passed pip install, put forward a domestic source, or run time out will make you self-closing.

>>pip install tensorflow-gpu==2.4

Tensorflow2.4 should be installed without accident (I am not surprised anyway, I don't know you anymore). Check to see if it is successful. Open Python in tensorflow2.4 environment.

>>> import tensorflow as tf
>>> print(tf.__version__)
>>> print('GPU', tf.test.is_gpu_available())