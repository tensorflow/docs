# Usage

```
$ cd text-lint
$ make build-image   #create Docker image to run text lint
$ make run-check       # run text lint on the Docker container
Please choose language.
ja
$ make clear-output   # remove temporary files
```

# Why use RedPen?

We are working on translation with more than one person. So It is expected that a lot of orthographical variants will occur.
[Redpen](http://redpen.cc/) is a proofreading tool to help writing documents that need to adhere to a writing standard. 
We can guarantee the quality of documents without lose writing speed while distributing translation tasks among multiple people.
RedPen officially support English and Japanese, but we can use some of the functions with another language.


checking process consists of the following two parts.
1. run `jupyter nbconvert` to convert jupyter notebook to markdown
2. run `redpen`  to read proofs
