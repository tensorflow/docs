# 参与TensorFlow文档编写

TensorFlow欢迎文档贡献 - 如果您改进了文档，等同于改进TensorFlow库本身。 tensorflow.org上的文档分为以下几类：

* *API 文档* —[API 文档](https://www.tensorflow.org/api_docs/)
  经由
  [TensorFlow 源代码](https://github.com/tensorflow/tensorflow)中的文档字符串(docstring)生成.
* *叙述文档* —这部分内容为[教程](https://www.tensorflow.org/tutorials)、
  [指南](https://www.tensorflow.org/guide)以及其他不属于TensorFlow代码的内容. 这部分代码位于GitHub的
  [tensorflow/docs](https://github.com/tensorflow/docs) 仓库(repository)中.
* *社区翻译* —这些是经由社区翻译的指南和教程。他们都被存放在
  [tensorflow/docs](https://github.com/tensorflow/docs/tree/master/site) 仓库(repository)中.

一些 [TensorFlow 项目](https://github.com/tensorflow) 将文档源文件保存在单独的存储库中，通常位于`docs/`目录中。 请参阅项目的`CONTRIBUTING.md`文件或联系维护者以参与。

参与到TensorFlow文档社区的方式有:

* 关注GitHub中的 [tensorflow/docs](https://github.com/tensorflow/docs) 仓库(repository).
* 订阅 [docs@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs).
* 加入 [Gitter 聊天室](https://gitter.im/tensorflow/docs).

## API 文档

如果想更新API文档，找到其对应的
[源文件](https://www.tensorflow.org/code/tensorflow/python/)
并编辑相应的
<a href="https://www.python.org/dev/peps/pep-0257/" class="external">文档字符串(docstring)</a>.
tensorflow.org上的许多API 引用的页面都包含了指向源文件定义位置的链接。 文档字符串支持
<a href="https://help.github.com/en/articles/about-writing-and-formatting-on-github" class="external">Markdown格式</a>
并且（绝大多数时候）都能使用
<a href="http://tmpvar.com/markdown.html" class="external">Markdown 预览器</a>
进行浏览.

有关参考文档质量以及如何参与文档冲刺和社区，请参阅
[TensorFlow 2.0 API文档建议](https://docs.google.com/document/d/1e20k9CuaZ_-hp25-sSd8E8qldxKPKQR-SkwojYr_r-U/preview)。

### 版本(Versions) 和 分支(Branches)

本网站的 [API 文档](https://www.tensorflow.org/api_docs/python/tf)
版本默认为最新的稳定二进制文件—即与通过`pip install tensorflow`安装的版本所匹配.

默认的TensorFlow 包是根据<a href="https://github.com/tensorflow/tensorflow" class="external">tensorflow/tensorflow</a>仓库(repository)中的稳定分支`rX.x`所构建的。文档则是由
<a href="https://www.tensorflow.org/code/tensorflow/python/" class="external">Python</a>、
<a href="https://www.tensorflow.org/code/tensorflow/cc/" class="external">C++</a>与
<a href="https://www.tensorflow.org/code/tensorflow/java/" class="external">Java</a>代码中的注释与文档字符串所生成。

以前版本的TensorFlow文档在TensorFlow Docs 仓库(repository)中以[rX.x 分支](https://github.com/tensorflow/docs/branches) 的形式提供。在发布新版本时会添加这些分支。

### 构建API文档

注意：编辑或预览API文档字符串不需要此步骤，只需生成tensorflow.org上使用的HTML。

#### Python 文档

`tensorflow_docs`包中包含[Python API 文档](https://www.tensorflow.org/api_docs/python/tf)的生成器。
安装方式：

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install git+https://github.com/tensorflow/docs</code>
</pre>

要生成TensorFlow 2.0文档，使用
`tensorflow/tools/docs/generate2.py` 脚本:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git clone https://github.com/tensorflow/tensorflow tensorflow</code>
<code class="devsite-terminal">cd tensorflow/tensorflow/tools/docs</code>
<code class="devsite-terminal">pip install tensorflow</code>
<code class="devsite-terminal">python generate2.py --output_dir=/tmp/out</code>
</pre>

注意：此脚本使用*已安装*的TensorFlow包生成文档并且仅适用于TensorFlow 2.x.

## 叙述文档

TensorFlow [指南](https://www.tensorflow.org/guide) 和
[教程](https://www.tensorflow.org/tutorials) 是通过
<a href="https://guides.github.com/features/mastering-markdown/" class="external">Markdown</a>
文件和交互式的
<a href="https://jupyter.org/" class="external">Jupyter</a> 笔记本所编写。 可以使用
<a href="https://colab.research.google.com/notebooks/welcome.ipynb"
   class="external">Google Colaboratory</a>
在您的浏览器中运行笔记本。
[tensorflow.org](https://www.tensorflow.org)中的叙述文档是根据
<a href="https://github.com/tensorflow/docs" class="external">tensorflow/docs</a>的
`master` 分支构建. 旧版本存储在在GitHub 仓库(repository)下的`rX.x`发行版分支中。

### 简单更改

进行简单文档更新和修复的最简单方法是使用GitHub的
<a href="https://help.github.com/en/articles/editing-files-in-your-repository" class="external">Web文件编辑器</a>。
浏览[tensorflow/docs](https://github.com/tensorflow/docs/tree/master/site/en)
仓库(repository) 以寻找与
<a href="https://www.tensorflow.org">tensorflow.org</a>
中的URL 结构相对应的Markdown或notebook文件。 在文件视图的右上角，单击铅笔图标
<svg version="1.1" width="14" height="16" viewBox="0 0 14 16" class="octicon octicon-pencil" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"></path></svg>
来打开文件编辑器。 编辑文件，然后提交新的拉取请求(pull request)。

### 设置本地Git仓库(repository)

对于多文件编辑或更复杂的更新，最好使用本地Git工作流来创建拉取请求(pull request)。

注意：<a href="https://git-scm.com/" class="external">Git</a> 是用于跟踪源代码更改的开源版本控制系统（VCS）。
<a href="https://github.com" class="external">GitHub</a>是一种在线服务，
提供与Git配合使用的协作工具。请参阅<a href="https://help.github.com" class="external">GitHub Help</a>以设置您的GitHub帐户并开始使用。

只有在第一次设置本地项目时才需要以下Git步骤。

#### 复制(fork) tensorflow/docs 仓库(repository)

在
<a href="https://github.com/tensorflow/docs" class="external">tensorflow/docs</a>
的Github页码中，点击*Fork*按钮
<svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
在您的GitHub帐户下创建您自己的仓库副本。复制(fork) 完成，您需要保持您的仓库副本副本与上游TensorFlow仓库的同步。

#### 克隆您的仓库(repository)

下载一份您 <var>username</var>/docs 仓库的副本到本地计算机。这是您之后进行操作的工作目录：

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git clone git@github.com:<var>username</var>/docs</code>
<code class="devsite-terminal">cd ./docs</code>
</pre>

#### 添加上游仓库(upstream repo)以保持最新（可选）

要使本地存储库与`tensorflow/docs`保持同步，需要添加一个*上游(upstream)*
仓库来下载最新的更改。

注意：确保在开始撰稿*之前*更新您的本地仓库。定期向上游同步会降低您在提交拉取请求(pull request)时产生<a href="https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line" class="external">合并冲突(merge conflict)</a>的可能性。

添加远程仓库:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git remote add <var>upstream</var> git@github.com:tensorflow/docs.git</code>

# 浏览远程仓库
<code class="devsite-terminal">git remote -v</code>
origin    git@github.com:<var>username</var>/docs.git (fetch)
origin    git@github.com:<var>username</var>/docs.git (push)
<var>upstream</var>  git@github.com:tensorflow/docs.git (fetch)
<var>upstream</var>  git@github.com:tensorflow/docs.git (push)
</pre>

更新:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git checkout master</code>
<code class="devsite-terminal">git pull <var>upstream</var> master</code>

<code class="devsite-terminal">git push</code>  # Push changes to your GitHub account (defaults to origin)
</pre>

### GitHub 工作流

#### 1. 创建一个新分支

从`tensorflow / docs`更新您的仓库后，从本地*master*分支中创建一个新的分支:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git checkout -b <var>feature-name</var></code>

<code class="devsite-terminal">git branch</code>  # 列出本地分支
  master
* <var>feature-name</var>
</pre>

#### 2. 做更改

在您喜欢的编辑器中编辑文件，并请遵守
[TensorFlow文档样式指南](./docs_style.md)。

提交文件更改：

<pre class="prettyprint lang-bsh">
# 查看更改
<code class="devsite-terminal">git status</code>  # 查看哪些文件被修改
<code class="devsite-terminal">git diff</code>    # 查看文件中的更改内容

<code class="devsite-terminal">git add <var>path/to/file.md</var></code>
<code class="devsite-terminal">git commit -m "Your meaningful commit message for the change."</code>
</pre>

根据需要添加更多提交。

#### 3. 创建一个拉取请求(pull request)

将您的本地分支上传到您的远程GitHub仓库
(github.com/<var>username</var>/docs):

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git push</code>
</pre>

推送完成后，消息可能会显示一个URL，以自动向上游存储库提交拉取请求。如果没有，请转到
<a href="https://github.com/tensorflow/docs" class="external">tensorflow/docs</a>
仓库—或者您自己的仓库—GitHub将提示您创建拉取请求(pull request)。

#### 4. 审校

维护者和其他贡献者将审核您的拉取请求(pull request)。请参与讨论并根据要求进行修改。当您的请求获得批准后，它将合并到上游TensorFlow文档仓库中。

成功后：您的更改会被TensorFlow文档接受。

从GitHub仓库更新
[tensorflow.org](https://www.tensorflow.org)是一个单独的步骤。通常情况下，多个更改将被一并处理，并定期上传至网站中。

## 交互式笔记本（notebook）

虽然可以使用GitHub的<a href="https://help.github.com/en/articles/editing-files-in-your-repository" class="external">web文本编辑器</a>来编辑笔记本JSON文件，但不推荐使用它，因为格式错误的JSON可能会损坏文件。 确保在提交拉取请求(pull request)之前测试笔记本。

<a href="https://colab.research.google.com/notebooks/welcome.ipynb" class="external">Google Colaboratory</a>
是一个托管笔记本环境，可以轻松编辑和运行笔记本文档。 GitHub中的笔记本通过将路径传递给Colab URL（例如，位于GitHub中的笔记本）在Google Colab中加载：
<a href="https&#58;//github.com/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_classification.ipynb">https&#58;//github.com/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_classification.ipynb</a><br/>
可以通过以下URL链接在Google Colab中加载:
<a href="https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_classification.ipynb">https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_classification.ipynb</a>

有一个
<a href="https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo" class="external">Open in Colab</a>
扩展程序，可以在GitHub上浏览笔记本时执行此URL替换。 这在您复制的仓库中中打开笔记本时非常有用，因为顶部按钮始终链接到TensorFlow Docs的`master`分支。

### 在Colab编辑

在Google Colab环境中，双击单元格以编辑文本和代码块。文本单元格使用Markdown格式，请遵循
[TensorFlow文档样式指南](./docs_style.md).

通过点击 *File > Download .pynb* 可以从Colab中下载笔记本文件。 将此文件提交到您的[本地Git仓库](###设置本地Git仓库(repository))后再提交拉取请求。

如需要创建新笔记本，请复制和编辑
<a href="https://github.com/tensorflow/docs/blob/master/tools/templates/notebook.ipynb" external="class">TensorFlow 笔记本模板</a>.

### Colab-GitHub工作流

您可以直接从Google Colab编辑和更新复制的GitHub仓库，而不是下载笔记本文件并使用本地Git工作流：

1. 在您复制(fork)的 <var>username</var>/docs 仓库中，使用GitHub Web界面
   <a href="https://help.github.com/articles/creating-and-deleting-branches-within-your-repository" class="external">创建新分支</a>。
2. 导航到要编辑的笔记本文件。
3. 在Google Colab中打开笔记本：使用URL替换或*Open in Colab* Chrome扩展程序。
4. 在Colab中编辑笔记本。
5. 通过点击
   *File > Save a copy in GitHub...*从Colab中向GitHub提交更改。保存对话框中选择到相应的仓库与分支。并添加一条有意义的提交消息。
6. 保存之后，浏览您的仓库或者
   <a href="https://github.com/tensorflow/docs" class="external">tensorflow/docs</a>
   仓库，GitHub会提示您创建一个pull请求。
7. 仓库维护者会审核您的拉取请求(pull request)。

成功后：您的更改会被TensorFlow文档接受。

## 社区翻译

社区翻译是让TensorFlow在全世界都可以访问的好方法。如需更新或添加翻译，在[语言目录](https://github.com/tensorflow/docs/tree/master/site)中按照`en/`相同的目录结构找到或添加一个新文件。英语文档是*最基础*的来源，翻译应尽可能地遵循这些指南。也就是说，翻译应尽量保持原汁原味。如果英语术语，短语，风格或语气不能翻译成其他语言，请采用适合读者的翻译。

注意：*请勿翻译* tensorflow.org中的API引用.

有特定于语言的文档组，使翻译贡献者可以更轻松地进行组织。 如果您是作者，评论者或只是想为社区构建TensorFlow.org内容，请加入：

* 简体中文: [docs-zh-cn@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-zh-cn)
* 日语: [docs-ja@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)
* 韩语: [docs-ko@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ko)
* 俄文: [docs-ru@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ru)
* 土耳其语: [docs-tr@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-tr)

### 审校须知

所有文档更新都需要审核。 为了更有效地与TensorFlow翻译社区进行协作，以下是一些保持语言特定活动的方法：

* 加入上面列出的语言组，以接收任何涉及该语言<code><a
  href="https://github.com/tensorflow/docs/tree/master/site">site/<var>lang</var></a></code>目录的*已创建的* 拉取请求。
* 将您的GitHub用户名添加至`site/<lang>/REVIEWERS`文件在拉取请求中能被自动注释标记。在被标记后，GitHub会向您发送该拉取请求中所有更改和讨论的通知。

### 在翻译中让代码保持最新

对于像TensorFlow这样的开源项目，保持文档最新是一项挑战。在与社区交谈之后，翻译内容的读者能容忍有点过时的文本，但过时的代码会让人抓狂。为了更容易保持代码同步，请为翻译的笔记本使用
[nb-code-sync](https://github.com/tensorflow/docs/blob/master/tools/nb_code_sync.py)工具：

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">./tools/nb_code_sync.py [--lang=en] site/<var>lang</var>/notebook.ipynb</code>
</pre>

此脚本读取语言笔记本的代码单元格，并根据英语版本进行检查。 剥离注释后，它会比较代码块并更新语言笔记本（如果它们不同）。 此工具对于交互式git工作流特别有用，可以选择性地将文件添加至更改中: `git add --patch site/lang/notebook.ipynb`

## Docs sprint

参加您附近的
[TensorFlow 2.0 Global Docs Sprint](https://www.google.com/maps/d/viewer?mid=1FmxIWZBXi4cvSy6gJUW9WRPfvVRbievf)
活动，或远程加入。 请关注此
[博客文章](https://medium.com/tensorflow/https-medium-com-margaretmz-tf-docs-sprint-cheatsheet-7cb1dfd3e8b5?linkId=68384164)。这些事件是开始为TensorFlow文档做出贡献的好方法。
