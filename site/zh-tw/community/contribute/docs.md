# 參與TensorFlow文檔編寫

TensorFlow歡迎文檔貢獻 - 如果您改進了文檔，等同於改進TensorFlow庫本身。 tensorflow.org上的文檔分為以下幾類：

* *API 文檔* —[API 文檔](https://www.tensorflow.org/api_docs/)
  經由
  [TensorFlow 源代碼](https://github.com/tensorflow/tensorflow)中的文檔字符串(docstring)生成.
* *敘述文檔* —這部分內容為[教程](https://www.tensorflow.org/tutorials)、
  [指南](https://www.tensorflow.org/guide)以及其他不屬於TensorFlow代碼的內容. 這部分代碼位於GitHub的
  [tensorflow/docs](https://github.com/tensorflow/docs) 倉庫(repository)中.
* *社區翻譯* —這些是經由社區翻譯的指南和教程。他們都被存放在
  [tensorflow/docs](https://github.com/tensorflow/docs/tree/master/site) 倉庫(repository)中.

一些 [TensorFlow 項目](https://github.com/tensorflow) 將文檔源文件保存在單獨的存儲庫中，通常位於`docs/`目錄中。請參閱項目的`CONTRIBUTING.md`文件或聯繫維護者以參與。

參與到TensorFlow文檔社區的方式有:

* 關注GitHub中的 [tensorflow/docs](https://github.com/tensorflow/docs) 倉庫(repository).
* 訂閱 [docs@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs).
* 加入 [Gitter 聊天室](https://gitter.im/tensorflow/docs).

## API 文檔

如果想更新API文檔，找到其對應的
[源文件](https://www.tensorflow.org/code/tensorflow/python/)
並編輯相應的
<a href="https://www.python.org/dev/peps/pep-0257/" class="external">文檔字符串(docstring)</a>.
tensorflow.org上的許多API 引用的頁面都包含了指向源文件定義位置的鏈接。文檔字符串支持
<a href="https://help.github.com/en/articles/about-writing-and-formatting-on-github" class="external">Markdown格式</a>
並且（絕大多數時候）都能使用
<a href="http://tmpvar.com/markdown.html" class="external">Markdown 預覽器</a>
進行瀏覽.

有關參考文檔質量以及如何參與文檔衝刺和社區，請參閱
[TensorFlow 2.0 API文檔建議](https://docs.google.com/document/d/1e20k9CuaZ_-hp25-sSd8E8qldxKPKQR-SkwojYr_r-U/preview)。

### 版本(Versions) 和 分支(Branches)

本網站的 [API 文檔](https://www.tensorflow.org/api_docs/python/tf)
版本默認為最新的穩定二進製文件—即與通過`pip install tensorflow`安裝的版本所匹配.

默認的TensorFlow 包是根據<a href="https://github.com/tensorflow/tensorflow" class="external">tensorflow/tensorflow</a>倉庫(repository)中的穩定分支`rX.x`所構建的。文檔則是由
<a href="https://www.tensorflow.org/code/tensorflow/python/" class="external">Python</a>、
<a href="https://www.tensorflow.org/code/tensorflow/cc/" class="external">C++</a>與
<a href="https://www.tensorflow.org/code/tensorflow/java/" class="external">Java</a>代碼中的註釋與文檔字符串所生成。

以前版本的TensorFlow文檔在TensorFlow Docs 倉庫(repository)中以[rX.x 分支](https://github.com/tensorflow/docs/branches) 的形式提供。在發布新版本時會添加這些分支。

### 構建API文檔

注意：編輯或預覽API文檔字符串不需要此步驟，只需生成tensorflow.org上使用的HTML。

#### Python 文檔

`tensorflow_docs`包中包含[Python API 文檔](https://www.tensorflow.org/api_docs/python/tf)的生成器。
安裝方式：

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install git https://github.com/tensorflow/docs</code>
</pre>

要生成TensorFlow 2.0文檔，使用
`tensorflow/tools/docs/generate2.py` 腳本:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git clone https://github.com/tensorflow/tensorflow tensorflow</code>
<code class="devsite-terminal">cd tensorflow/tensorflow/tools/docs</code>
<code class="devsite-terminal">pip install tensorflow</code>
<code class="devsite-terminal">python generate2.py --output_dir=/tmp/out</code>
</pre>

注意：此腳本使用*已安裝*的TensorFlow包生成文檔並且僅適用於TensorFlow 2.x.

## 敘述文檔

TensorFlow [指南](https://www.tensorflow.org/guide) 和
[教程](https://www.tensorflow.org/tutorials) 是通過
<a href="https://guides.github.com/features/mastering-markdown/" class="external">Markdown</a>
文件和交互式的
<a href="https://jupyter.org/" class="external">Jupyter</a> 筆記本所編寫。可以使用
<a href="https://colab.research.google.com/notebooks/welcome.ipynb"
   class="external">Google Colaboratory</a>
在您的瀏覽器中運行筆記本。
[tensorflow.org](https://www.tensorflow.org)中的敘述文檔是根據
<a href="https://github.com/tensorflow/docs" class="external">tensorflow/docs</a>的
`master` 分支構建. 舊版本存儲在在GitHub 倉庫(repository)下的`rX.x`發行版分支中。

### 簡單更改

進行簡單文檔更新和修復的最簡單方法是使用GitHub的
<a href="https://help.github.com/en/articles/editing-files-in-your-repository" class="external">Web文件編輯器</a>。
瀏覽[tensorflow/docs](https://github.com/tensorflow/docs/tree/master/site/en)
倉庫(repository) 以尋找與
<a href="https://www.tensorflow.org">tensorflow.org</a>
中的URL 結構相對應的Markdown或notebook文件。在文件視圖的右上角，單擊鉛筆圖標
<svg version="1.1" width="14" height="16" viewBox="0 0 14 16" class="octicon octicon-pencil" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z" ></path></svg>
來打開文件編輯器。編輯文件，然後提交新的拉取請求(pull request)。

### 設置本地Git倉庫(repository)

對於多文件編輯或更複雜的更新，最好使用本地Git工作流來創建拉取請求(pull request)。

注意：<a href="https://git-scm.com/" class="external">Git</a> 是用於跟踪源代碼更改的開源版本控制系統（VCS）。
<a href="https://github.com" class="external">GitHub</a>是一種在線服務，
提供與Git配合使用的協作工具。請參閱<a href="https://help.github.com" class="external">GitHub Help</a>以設置您的GitHub帳戶並開始使用。

只有在第一次設置本地項目時才需要以下Git步驟。

#### 複製(fork) tensorflow/docs 倉庫(repository)

在
<a href="https://github.com/tensorflow/docs" class="external">tensorflow/docs</a>
的Github頁碼中，點擊*Fork*按鈕
<svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule=" evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2 .55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65- .55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z "></path></svg>
在您的GitHub帳戶下創建您自己的倉庫副本。複製(fork) 完成，您需要保持您的倉庫副本副本與上游TensorFlow倉庫的同步。

#### 克隆您的倉庫(repository)

下載一份您 <var>username</var>/docs 倉庫的副本到本地計算機。這是您之後進行操作的工作目錄：

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git clone git@github.com:<var>username</var>/docs</code>
<code class="devsite-terminal">cd ./docs</code>
</pre>

#### 添加上游倉庫(upstream repo)以保持最新（可選）

要使本地存儲庫與`tensorflow/docs`保持同步，需要添加一個*上游(upstream)*
倉庫來下載最新的更改。

注意：確保在開始撰稿*之前*更新您的本地倉庫。定期向上游同步會降低您在提交拉取請求(pull request)時產生<a href="https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line " class="external">合併衝突(merge conflict)</a>的可能性。

添加遠程倉庫:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git remote add <var>upstream</var> git@github.com:tensorflow/docs.git</code>

# 瀏覽遠程倉庫
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

<code class="devsite-terminal">git push</code> # Push changes to your GitHub account (defaults to origin)
</pre>

### GitHub 工作流

#### 1. 創建一個新分支

從`tensorflow / docs`更新您的倉庫後，從本地*master*分支中創建一個新的分支:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git checkout -b <var>feature-name</var></code>

<code class="devsite-terminal">git branch</code>  # 列出本地分支
  master
* <var>feature-name</var>
</pre>

#### 2. 做更改

在您喜歡的編輯器中編輯文件，並請遵守
[TensorFlow文檔樣式指南](./docs_style.md)。

提交文件更改：

<pre class="prettyprint lang-bsh">
# 查看更改
<code class="devsite-terminal">git status</code>  # 查看哪些文件被修改
<code class="devsite-terminal">git diff</code>    # 查看文件中的更改內容

<code class="devsite-terminal">git add <var>path/to/file.md</var></code>
<code class="devsite-terminal">git commit -m "Your meaningful commit message for the change."</code>
</pre>

根據需要添加更多提交。

#### 3. 創建一個拉取請求(pull request)

將您的本地分支上傳到您的遠程GitHub倉庫
(github.com/<var>username</var>/docs):

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git push</code>
</pre>

推送完成後，消息可能會顯示一個URL，以自動向上游存儲庫提交拉取請求。如果沒有，請轉到
<a href="https://github.com/tensorflow/docs" class="external">tensorflow/docs</a>
倉庫—或者您自己的倉庫—GitHub將提示您創建拉取請求(pull request)。

#### 4. 審校

維護者和其他貢獻者將審核您的拉取請求(pull request)。請參與討論並根據要求進行修改。當您的請求獲得批准後，它將合併到上游TensorFlow文檔倉庫中。

成功後：您的更改會被TensorFlow文檔接受。

從GitHub倉庫更新
[tensorflow.org](https://www.tensorflow.org)是一個單獨的步驟。通常情況下，多個更改將被一併處理，並定期上傳至網站中。

## 交互式筆記本（notebook）

雖然可以使用GitHub的<a href="https://help.github.com/en/articles/editing-files-in-your-repository" class="external">web文本編輯器</a>來編輯筆記本JSON文件，但不推薦使用它，因為格式錯誤的JSON可能會損壞文件。確保在提交拉取請求(pull request)之前測試筆記本。

<a href="https://colab.research.google.com/notebooks/welcome.ipynb" class="external">Google Colaboratory</a>
是一個託管筆記本環境，可以輕鬆編輯和運行筆記本文檔。 GitHub中的筆記本通過將路徑傳遞給Colab URL（例如，位於GitHub中的筆記本）在Google Colab中加載：
<a href="https&#58;//github.com/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_classification.ipynb">https&#58;//github.com/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_classification.ipynb</a><br/>
可以通過以下URL鏈接在Google Colab中加載:
<a href="https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_classification.ipynb">https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_classification.ipynb</a>

有一個
<a href="https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo" class="external">Open in Colab</a>
擴展程序，可以在GitHub上瀏覽筆記本時執行此URL替換。這在您複製的倉庫中中打開筆記本時非常有用，因為頂部按鈕始終鏈接到TensorFlow Docs的`master`分支。

### 在Colab編輯

在Google Colab環境中，雙擊單元格以編輯文本和代碼塊。文本單元格使用Markdown格式，請遵循
[TensorFlow文檔樣式指南](./docs_style.md).

通過點擊 *File > Download .pynb* 可以從Colab中下載筆記本文件。將此文件提交到您的[本地Git倉庫](###設置本地Git倉庫(repository))後再提交拉取請求。

如需要創建新筆記本，請複制和編輯
<a href="https://github.com/tensorflow/docs/blob/master/tools/templates/notebook.ipynb" external="class">TensorFlow 筆記本模板</a>.

### Colab-GitHub工作流

您可以直接從Google Colab編輯和更新復制的GitHub倉庫，而不是下載筆記本文件並使用本地Git工作流：

1. 在您複製(fork)的 <var>username</var>/docs 倉庫中，使用GitHub Web界面<a href="https://help.github.com/articles/creating-and-deleting-branches-within-your-repository" class="external">創建新分支</a>。
2. 導航到要編輯的筆記本文件。
3. 在Google Colab中打開筆記本：使用URL替換或*Open in Colab* Chrome擴展程序。
4. 在Colab中編輯筆記本。
5. 通過點擊
   *File > Save a copy in GitHub...*從Colab中向GitHub提交更改。保存對話框中選擇到相應的倉庫與分支。並添加一條有意義的提交消息。
6. 保存之後，瀏覽您的倉庫或者<a href="https://github.com/tensorflow/docs" class="external">tensorflow/docs</a>倉庫，GitHub會提示您創建一個pull請求。
7. 倉庫維護者會審核您的拉取請求(pull request)。

成功後：您的更改會被TensorFlow文檔接受。

## 社區翻譯

社區翻譯是讓TensorFlow在全世界都可以訪問的好方法。如需更新或添加翻譯，在[語言目錄](https://github.com/tensorflow/docs/tree/master/site)中按照`en/`相同的目錄結構找到或添加一個新文件。英語文檔是*最基礎*的來源，翻譯應盡可能地遵循這些指南。也就是說，翻譯應盡量保持原汁原味。如果英語術語，短語，風格或語氣不能翻譯成其他語言，請採用適合讀者的翻譯。

注意：*請勿翻譯* tensorflow.org中的API引用.

有特定於語言的文檔組，使翻譯貢獻者可以更輕鬆地進行組織。如果您是作者，評論者或只是想為社區構建TensorFlow.org內容，請加入：

* 簡體中文: [docs-zh-cn@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-zh-cn)
* 日語: [docs-ja@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)
* 韓語: [docs-ko@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ko)
* 俄文: [docs-ru@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ru)
* 土耳其語: [docs-tr@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-tr)

### 審校須知

所有文檔更新都需要審核。為了更有效地與TensorFlow翻譯社區進行協作，以下是一些保持語言特定活動的方法：

* 加入上面列出的語言組，以接收任何涉及該語言<code><a href="https://github.com/tensorflow/docs/tree/master/site">site/<var>lang</var></a></code>目錄的*已創建的* 拉取請求。
* 將您的GitHub用戶名添加至`site/<lang>/REVIEWERS`文件在拉取請求中能被自動註釋標記。在被標記後，GitHub會向您發送該拉取請求中所有更改和討論的通知。

### 在翻譯中讓代碼保持最新

對於像TensorFlow這樣的開源項目，保持文檔最新是一項挑戰。在與社區交談之後，翻譯內容的讀者能容忍有點過時的文本，但過時的代碼會讓人抓狂。為了更容易保持代碼同步，請為翻譯的筆記本使用
[nb-code-sync](https://github.com/tensorflow/docs/blob/master/tools/nb_code_sync.py)工具：

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">./tools/nb_code_sync.py [--lang=en] site/<var>lang</var>/notebook.ipynb</code>
</pre>

此腳本讀取語言筆記本的代碼單元格，並根據英語版本進行檢查。剝離註釋後，它會比較代碼塊並更新語言筆記本（如果它們不同）。此工具對於交互式git工作流特別有用，可以選擇性地將文件添加至更改中: `git add --patch site/lang/notebook.ipynb`

## Docs sprint

參加您附近的
[TensorFlow 2.0 Global Docs Sprint](https://www.google.com/maps/d/viewer?mid=1FmxIWZBXi4cvSy6gJUW9WRPfvVRbievf)
活動，或遠程加入。請關注此
[博客文章](https://medium.com/tensorflow/https-medium-com-margaretmz-tf-docs-sprint-cheatsheet-7cb1dfd3e8b5?linkId=68384164)。這些事件是開始為TensorFlow文檔做出貢獻的好方法。
