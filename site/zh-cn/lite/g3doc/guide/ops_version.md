# Tensorflow Lite 管理员版本
本文档描述了 TensorFlow Lite 的管理员版本架构。管理员版本允许开发人员能够将新功能和参数添加到现有版本中。此外，它保证以下内容：
> 后向兼容性：新版本的 TensorFlow Lite 可以处理旧版本的模型文件。
> 前向兼容性：只要没有使用新功能，旧版本的 TensorFlow Lite 可以处理由新版 TOCO 生成的新版本的模型文件。
> 正向兼容性检测：如果旧的 TensorFlow Lite 读取包含不支持的新版本的模型，则应报告错误。
