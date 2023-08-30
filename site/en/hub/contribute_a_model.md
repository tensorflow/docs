
# Submit a pull request

This page is about submitting a pull request containing Markdown documentation
files to the [tensorflow/tfhub.dev](https://github.com/tensorflow/tfhub.dev).
GitHub Repo. For more information on how to write the Markdown files in the
first place, please see the
[writing documentation guide](writing_documentation.md).

**Note:** If you would like your model to be mirrored to other model hubs,
please use an MIT, CC0, or Apache license. If you would not like your model to
be mirrored to other model hubs, please use another appropriate license.

## GitHub Actions checks

The [tensorflow/tfhub.dev](https://github.com/tensorflow/tfhub.dev) repo uses
GitHub Actions to validate the format of the files in a PR. The workflow used to
validate PRs is defined in
[.github/workflows/contributions-validator.yml](https://github.com/tensorflow/tfhub.dev/blob/master/.github/workflows/contributions-validator.yml).
You can run the validator script on your own branch outside of the workflow, but
you will need to ensure you have all the correct pip package dependencies
installed.

First time contributors are only able to run automated checks with the approval
of a repo maintainer, per
[GitHub policy](https://github.blog/changelog/2021-04-22-github-actions-maintainers-must-approve-first-time-contributor-workflow-runs/).
Publishers are encouraged to submit a small PR fixing typos, otherwise improving
model documentation, or submitting a PR containing only their publisher page as
their first PR to be able to run automated checks on subsequent PRs.

Important: Your pull request must pass the automated checks before it will be
reviewed!

## Submitting the PR

The complete Markdown files can be pulled into the master branch of
[tensorflow/tfhub.dev](https://github.com/tensorflow/tfhub.dev/tree/master) by
one of the following methods.

### Git CLI submission

Assuming the identified markdown file path is
`assets/docs/publisher/model/1.md`, you can follow the standard Git[Hub] steps
to create a new Pull Request with a newly added file.

This starts with forking the TensorFlow Hub GitHub repository, then creating a
[Pull Request from this fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork)
into the TensorFlow Hub master branch.

The following are typical CLI git commands needed to adding a new file to a
master branch of the forked repository.

```bash
git clone https://github.com/[github_username]/tfhub.dev.git
cd tfhub.dev
mkdir -p assets/docs/publisher/model
cp my_markdown_file.md ./assets/docs/publisher/model/1.md
git add *
git commit -m "Added model file."
git push origin master
```

### GitHub GUI submission

A somewhat more straightforward way of submitting is via GitHub graphical user
interface. GitHub allows creating PRs for
[new files](https://help.github.com/en/github/managing-files-in-a-repository/creating-new-files)
or
[file edits](https://help.github.com/en/github/managing-files-in-a-repository/editing-files-in-your-repository)
directly through GUI.

1.  On the
    [TensorFlow Hub GitHub page](https://github.com/tensorflow/tfhub.dev), press
    `Create new file` button.
1.  Set the right file path: `assets/docs/publisher/model/1.md`
1.  Copy-paste the existing markdown.
1.  At the bottom, select "Create a new branch for this commit and start a pull
    request."
