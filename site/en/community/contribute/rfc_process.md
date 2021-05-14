# The TensorFlow RFC process

Every new TensorFlow feature begins life as a Request for Comment (RFC).

An RFC is a document that describes a requirement and the proposed changes that
will solve it. Specifically, the RFC will:

*   Be formatted according to the
    [RFC template](https://github.com/tensorflow/community/blob/master/rfcs/yyyymmdd-rfc-template.md).
*   Be submitted as a pull request to the
    [community/rfcs](https://github.com/tensorflow/community/tree/master/rfcs)
    directory.
*   Be subject to discussion and a review meeting prior to acceptance.

The purpose of a TensorFlow Request for Comments (RFC) is to engage the
TensorFlow community in development, by getting feedback from stakeholders and
experts, and communicating design changes broadly.

## How to submit an RFC

1.  Before submitting an RFC, discuss your aims with project contributors and
    maintainers and get early feedback. Use the developer mailing list for the
    project concerned (developers@tensorflow.org, or the list for the relevant
    SIG).

2.  Draft your RFC.

    *   Read the [design review criteria](https://github.com/tensorflow/community/blob/master/governance/design-reviews.md)
    *   Follow the
        [RFC template](https://github.com/tensorflow/community/blob/master/rfcs/yyyymmdd-rfc-template.md).
    *   Name your RFC file `YYYYMMDD-descriptive-name.md`, where `YYYYMMDD` is
        the date of submission, and `descriptive-name` relates to the title of
        your RFC. (For instance, if your RFC is titled _Parallel Widgets API_,
        you might use the filename `20180531-parallel-widgets.md`.
    *   If you have images or other auxiliary files, create a directory of the
        form `YYYYMMDD-descriptive-name` in which to store those files.

    After writing the RFC draft, get feedback from maintainers and contributors
    before submitting it.

    Writing implementation code is not a requirement, but it may help design
    discussions.

3.  Recruit a sponsor.

    *   A sponsor must be a maintainer of the project.
    *   Identify the sponsor in the RFC, before posting the PR.

    You _may_ post an RFC without a sponsor, but if within a month of posting
    the PR there is still no sponsor, it will be closed.

4.  Submit your RFC as a pull request to
    [tensorflow/community/rfcs](https://github.com/tensorflow/community/tree/master/rfcs).

    Include the header table and the contents of the _Objective_ section in the
    comment of your pull request, using Markdown. For an example, please see
    [this example RFC](https://github.com/tensorflow/community/pull/5). Include
    the GitHub handles of co-authors, reviewers, and sponsors.

    At the top of the PR identify how long the comment period will be. This
    should be a _minimum of two weeks_ from posting the PR.

5.  Email the developer mailing list with a brief description, a link to the PR
    and a request for review. Follow the format of previous mailings, as you can
    see in
    [this example](https://groups.google.com/a/tensorflow.org/forum/#!topic/developers/PIChGLLnpTE).

6.  The sponsor will request a review committee meeting, no sooner than two
    weeks after the RFC PR is posted. If discussion is lively, wait until it has
    settled before going to review. The goal of the review meeting is to resolve
    minor issues; consensus should be reached on major issues beforehand.

7.  The meeting may approve the RFC, reject it, or require changes before it can
    be considered again. Approved RFCs will be merged into
    [community/rfcs](https://github.com/tensorflow/community/tree/master/rfcs),
    and rejected RFCs will have their PRs closed.

## RFC participants

Many people are involved in the RFC process:

*   **RFC author** — one or more community members who write an RFC and are
    committed to championing it through the process

*   **RFC sponsor** — a maintainer who sponsors the RFC and will shepherd it
    through the RFC review process

*   **review committee** — a group of maintainers who have the responsibility of
    recommending the adoption of the RFC

*   Any **community member** may help by providing feedback on whether the RFC
    will meet their needs.

### RFC sponsors

A sponsor is a project maintainer responsible for ensuring the best possible
outcome of the RFC process. This includes:

*   Advocating for the proposed design.
*   Guiding the RFC to adhere to existing design and style conventions.
*   Guiding the review committee to come to a productive consensus.
*   If changes are requested by the review committee, ensure these are made and
    seek subsequent approval from the committee members.
*   If the RFC moves to implementation:
    *   Ensuring proposed implementation adheres to the design.
    *   Coordinate with appropriate parties to successfully land implementation.

### RFC review committees

The review committee decides on a consensus basis whether to approve, reject, or
request changes. They are responsible for:

*   Ensuring that substantive items of public feedback have been accounted for.
*   Adding their meeting notes as comments to the PR.
*   Providing reasons for their decisions.

The constitution of a review committee may change according to the particular
governance style and leadership of each project. For core TensorFlow, the
committee will consist of contributors to the TensorFlow project who have
expertise in the domain area concerned.

### Community members and the RFC process

The purpose of RFCs is to ensure the community is well represented and served by
new changes to TensorFlow. It is the responsibility of community members to
participate in reviewing RFCs where they have an interest in the outcome.

Community members who are interested in an RFC should:

*   **Provide feedback** as soon as possible to allow adequate time for
    consideration.
*   **Read RFCs** thoroughly before providing feedback.
*   Be **civil and constructive**.

## Implementing new features

Once an RFC has been approved, implementation can begin.

If you are working on new code to implement an RFC:

*   Make sure you understand the feature and the design approved in the RFC. Ask
    questions and discuss the approach before beginning work.
*   New features must include new unit tests that verify the feature works as
    expected. It's a good idea to write these tests before writing the code.
*   Follow the [TensorFlow Code Style Guide](#tensorflow-code-style-guide)
*   Add or update relevant API documentation. Reference the RFC in the new
    documentation.
*   Follow any other guidelines laid out in the `CONTRIBUTING.md` file in the
    project repo you're contributing to.
*   Run unit tests before submitting your code.
*   Work with the RFC sponsor to successfully land the new code.

## Keeping the bar high

While we encourage and celebrate every contributor, the bar for RFC acceptance
is kept intentionally high. A new feature may be rejected or need significant
revision at any one of these stages:

*   Initial design conversations on the relevant mailing list.
*   Failure to recruit a sponsor.
*   Critical objections during the feedback phase.
*   Failure to achieve consensus during the design review.
*   Concerns raised during implementation (for example: inability to achieve
    backwards compatibility, concerns about maintenance).

If this process is functioning well, RFCs are expected to fail in the earlier,
rather than later, stages. An approved RFC is no guarantee of a commitment to
implement, and acceptance of a proposed RFC implementation is still subject to
the usual code review process.

If you have any questions about this process, feel free to ask on the developers
mailing list or file an issue in
[tensorflow/community](https://github.com/tensorflow/community/tree/master/rfcs).
