# SIG playbook

## Scope of a SIG

TensorFlow hosts *Special Interest Groups* (SIGs) to focus collaboration on particular areas. SIGs do their work in public. To join and contribute, review the work of the group, and get in touch with the SIG leader. Membership policies vary on a per-SIG basis.

The ideal scope for a SIG meets a well-defined domain, where the majority of
participation is from the community. Additionally, there should be
sufficient evidence that there are community members willing to engage and
contribute should the interest group be established.

Not all SIGs will have the same level of energy, breadth of scope, or governance
models, so expect some variability.

See the complete list of [TensorFlow SIGs](https://github.com/tensorflow/community/tree/master/sigs).

### Non-goals: What a SIG is *not*

SIGs are intended is to facilitate collaboration on shared work. A SIG is
therefore:

*   *Not a support forum*: a mailing list and a SIG is not the same thing.
*   *Not immediately required*: early on in a project's life, you may not know
    if you have shared work or collaborators.
*   *Not free labor*: energy is required to grow and coordinate the work
    collaboratively.
    
Our approach to SIG creation will be conservative—thanks to the ease of starting projects on GitHub, there are many avenues where collaboration can happen without the need for a SIG.


## SIG lifecycle

### Research and consultation

Proposers of groups should gather evidence for approval, as specified below.
Some possible avenues to consider are:

*   A well-defined problem or set of problems the group would solve.
*   Consultation with community members who would benefit, assessing both the
    benefit and their willingness to commit.
*   For existing projects, evidence from issues and PRs that contributors care
    about the topic.
*   Potential goals for the group to achieve.
*   Resource requirements of running the group.

Even if the need for a SIG seems self-evident, the research and consultation is
still important to the success of the group.

### Creating the new group

The new group should follow the below process for chartering. In particular, it
must demonstrate:

*   A clear purpose and benefit to TensorFlow (either around a sub-project or
    application area)
*   Two or more contributors willing to act as group leads, existence of other
    contributors, and evidence of demand for the group
*   Resources it will initially require (usually, mailing list and regular VC
    call.) 

Approval for the group will be given by a decision of the TF Community Team,
defined as being the maintainers of the tensorflow/community project. The team
will consult other stakeholders as necessary.

Before entering the formal parts of the process, it is advisable to consult with
the TensorFlow community team, community-team@tensorflow.org. It is highly
likely that conversation and iteration will be required before the SIG request
is ready.

The formal request for the new group is done by submitting a charter as a PR to
tensorflow/community, and including the request in the comments on the PR (see
template below). On approval, the PR for the group will be merged and the
required resources created.

### Template Request for New SIG

This template will be available in the community repo:
[SIG-request-template.md](https://github.com/tensorflow/community/blob/master/governance/SIG-request-template.md).

### Chartering

Each group will be established with a charter, and be governed by the TensorFlow
code of conduct. Archives of the group will be public. Membership may either be
open to all without approval, or available on request, pending approval of the
group administrator.

The charter must nominate an administrator. As well as an administrator, the
group must include at least one person as lead (these may be the same person),
who will serve as point of contact for coordination as required with the TensorFlow
community team.

This charter will be posted initially to the group mailing list. The community
repository in the TensorFlow GitHub organization will archive such documents and
policies ([example from Kubernetes](https://github.com/kubernetes/community)).
As any group evolves its practices and conventions, we expect it to document
these within the relevant part of the community repository.

### Collaboration and inclusion

While it is not mandated, the group should choose to make use of collaboration
via scheduled conference call or chat channels to conduct meetings. Any such
meetings should be advertised on the mailing list, and notes posted to the
mailing list afterwards. Regular meeting helps drive accountability and progress
in a SIG.

TensorFlow community team members will proactively monitor and encourage the
group to discussion and action as appropriate.

### Launching

Required activities:

*   Notifying TensorFlow general discussion groups
    ([discuss@](https://groups.google.com/a/tensorflow.org/forum/#!forum/discuss),
    [developers@](https://groups.google.com/a/tensorflow.org/forum/#!forum/developers)).
*   Adding SIG to the community pages on TensorFlow web site. 

Optional activities:

*   Creating a blog post for the TensorFlow blog community.

### Health and termination of SIGs

The TensorFlow community team will make a best effort to ensure the health of
SIGs. From time to time it will request the SIG lead to provide a report of the
SIG's work, which will be used to inform the broader TensorFlow community of the
activity of the group.

If a SIG no longer has a useful purpose or interested community, it may be
archived and cease operation. The TF community team reserves the right to
archive such inactive SIGs, in order to maintain the health of the project at
large, though it is a less preferable outcome. A SIG may also opt to disband if
it recognizes it has reached the end of its useful life.
