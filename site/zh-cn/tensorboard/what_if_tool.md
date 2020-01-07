# 基于 What-If 工具仪表盘的模型理解

![What-If Tool](./images/what_if_tool.png)

What-If 工具（WIT）提供了易于使用的界面，用于扩展对黑盒分类和回归机器学习模型的理解。使用该插件，您可以对大量样本进行推断，并以各种方式立即可视化结果。此外，可以手动或以编程方式编辑样本，然后在模型中重新运行示例以查看更改结果。它包含用于研究基于数据子集的模型性能和公平性的工具。

该工具的目的是为人们提供一种简单，直观且功能强大的方法，通过可视化界面，无需任何代码，即可探索和研究经过训练的机器学习模型。

可以通过 TensorBoard 或直接在 Jupyter 或 Colab 笔记本中访问该工具。 有关在 notebook 模式下使用 WIT 的更多深入细节，演示，教程和信息，请访问 [What-If 工具](https://pair-code.github.io/what-if-tool) 网站。

## 使用要求

要在 TensorBoard 中使用 WIT，需要做两件事：

* 您希望探索的模型必须使用 [TensorFlow Serving](https://github.com/tensorflow/serving) 进行服务，该服务使用分类，回归或预测API。
* 要由模型推断的数据集必须位于 TensorBoard web 服务器可访问的 TFRecord 文件中。

## 用法

在 TensorBoard 中打开 What-If 工具仪表板时，您将看到一个设置界面，在其中提供模型服务器的主机和端口，所服务模型的名称，模型类型以及需要加载的 TFRecords 文件的路径。填写完此信息并单击「Accept」后，WIT 将加载数据集并对模型进行推断，同时显示结果。

有关 WIT 不同功能的详细信息以及它们如何帮助模型理解和公平性研究，请参阅 [What-If 工具网站](https://pair-code.github.io/what-if-tool)上的教程。

## 演示模型和数据集

如果您想使用预先训练的模型在 TensorBoard 中测试 WIT，可以从 https://storage.googleapis.com/what-if-tool-resources/uci-census-demo/uci-census-demo.zip 下载并解压缩预先训练的模型和数据集。该模型是一个二分类模型，使用 [UCI 人口普查](https://archive.ics.uci.edu/ml/datasets/census+income)数据集来预测一个人的年收入是否超过 5 万美元。该数据集和预测任务通常用于机器学习建模和公平性研究中。

将环境变量 MODEL_PATH 设置为机器上生成模型结果的位置。

按照[官方文档](https://tensorflow.google.cn/tfx/serving/docker)安装 docker 和 TensorFlow Serving 。

通过 `docker run -p 8500:8500 --mount type=bind,source=${MODEL_PATH},target=/models/uci_income -e MODEL_NAME=uci_income -t tensorflow/serving` 使用 docker 进行服务模型。请注意，根据您的 Docker 设置，您可能需要使用 `sudo` 运行命令。

现在启动 tensorboard 并使用仪表板下拉菜单导航至 What-If 工具。

在设置界面上，将推断地址设置为「localhost:8500」，将模型名称设置为「uci_income」，并将样本文件的路径设置为已下载的 `adult.tfrecord` 文件的完整路径，然后点击「Accept」。

![Setup screen for demo](./images/what_if_tool_demo_setup.png)

在此演示中使用 What-If  工具可以尝试以下操作：

- 编辑单个数据点并查看推断的结果变化。
- 通过部分依赖图探索数据集中各个特征与模型推断结果之间的关系。
- 将数据集切片为子集，然后比较不同切片之间的性能。

要深入了解该工具的功能，请查看 [What-If 工具实际演示教程](https://pair-code.github.io/what-if-tool/walkthrough.html)。

请注意，此模型试图预测的数据集中的真实特征称为 「目标（Target）」，因此，在使用「性能和公平性（Performance & Fairness）」标签页时，需要在真实特征下拉列表中指定「目标（Target）」。