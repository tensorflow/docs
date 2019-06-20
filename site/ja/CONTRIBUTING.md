# Contribution Guideline

## Communities

* Slack
  * Slack の #doc_translation チャンネルで議論をしています
  * [TensorFlow User Group の公式ページ](https://tfug.jp/)から参加可能です
* Google Groups
  * [docs@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs)
  * [docs-ja@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)

## Directory Structure

ドキュメントのディレクトリ構成は次のようになっています:

```
site
├── en
│   ├── ...
│   ├── ...     
│   └── ...
├── ja
│   ├── ...
│   ├── ...     
│   └── ...
├── ...
└── ...
```

`site/en` 以下にあるけれど `site/ja` 以下に無いものは、まだ翻訳が済んでいないドキュメントです。
それらを翻訳して `site/en` 以下と同じ構成で `site/ja` 以下に配置して pull request を送ってください。

## Pull Request Title

Pull request のタイトルは "JA: ..." とすることを推奨しています。
レビュアーが "JA" で検索することもあるので、見落としを防ぐためご協力お願いします。

## Proofreading Tool

一部レビューの自動化や多人数の翻訳による表記ゆれ対策として[校正ツール](https://github.com/tfug/proofreading)を使用しています。
レビュー時にレビュアー側でも確認を行うので必須ではありませんが、予めチェックを行っておくと pull request の修正が少なく済みます。

また、校正ツールへの pull request も歓迎します。

## Frequently Asked Questions

### ソースコードのコメントは翻訳した方が良いですか?

基本的に翻訳する方針です。

### どのドキュメントを翻訳すれば良いですか?

[TF 1.0 の翻訳はアップデートの終了が宣言された](https://groups.google.com/a/tensorflow.org/forum/#!msg/docs/vO0gQnEXcSM/YK_ybv7tBQAJ)ので TF 2.0 のドキュメントを翻訳してください。
それ以外は特に制限はありません。

### 誰がどのドキュメントを翻訳中か確認できますか?

正確に把握することは難しいので、必要に応じて次のように確認してください:

* "JA" で検索して現在作成されている pull request を調べる
* 心配であれば Slack 上などで呼びかける

### どうすればレビュアーになれますか?

現在議論中ですが、次の条件を目安としています:

* 既に 1 つドキュメントを翻訳して pull request が取り込まれている

上記の条件を充たしており、レビュアーになりたい場合は [`REVIEWERS`](https://github.com/tensorflow/docs/blob/master/site/ja/REVIEWERS) に自分の GitHub ID を書き加えて pull request を送ってください。

### 英語ドキュメント側が外部リポジトリへのリンクになっている場合はどうすれば良いですか?

リンク先のリポジトリと同じ構成で `site/ja` 以下に配置してください。
