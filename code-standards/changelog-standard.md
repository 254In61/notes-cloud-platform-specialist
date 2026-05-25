# CHANGELOG.md

## overview

This file includes notes relating to the changes to the code repository over time.

The CHANGELOG.md file must be updated prior to every release being merged to the master branch.

Each change in the log is headed by the semantic version (major.minor.patch) of the change as well as a link to the diff between the changed code and its predecessor.

Every change can be broken down into one or more Features or Fixes

Changes that "break" the way the code works or can be interacted with must have the relevant feature(s) or fix(es) flagged as BREAKING changes.

All entries must be listed with a link to the Bitbucket compare view between the current and previous version tags.

All entries must be dated in ISO 8601 format (YYYY-MM-DD).

## CHANGELOG.md example

Create an initial entry for the first release of the module, with a link to the diff between the first commit and the 1.0.0 tag that is applied to the first release.

### [1.0.0](https://bitbucket.int.corp.sun/projects/<PROJECT_NAME>/repos/<REPO_NAME>/compare/diff?sourceBranch=refs/tags/1.0.0&targetBranch=<first_commit_on_master_branch>) YYYY-MM-DD

Feature:

* Initial release of [Module Name] module

Consecutive entries should be added for each release, with links to the diffs between the current and previous version tags.

### [3.1.4](https://bitbucket.int.corp.sun/projects/<PROJECT_NAME>/repos/<REPO_NAME>/compare/diff?sourceBranch=refs/tags/3.1.4&targetBranch=refs/tags/3.1.3) 2025-04-31

Features:

* Something new that has been included. Every release including one ore more features requires the _minor_ version to be incremented at a minimum.
* **BREAKING** Changes must be flagged as per this example, and against every item in every related / affected Feature or Fix. Breaking changes always require the _major_ version to be incremented.

Fixes:

* Something that has changed to address a bug or improve the quality of the code, without changing the way the code is consumed by the end user. Fixes generally translate into a _patch_ version increment.
* **BREAKING** A fix that improves the way the code works but requires the end user to change they way they consume the code. Again, breaking changes mean a _major_ version increment must occur.
Tags, Releases
When code is merged into the _master_ (trunk) branch, a corresponding tag of the semantic version for the release should be applied to the commit. The following hypothetical example shows a series of git commands to apply tags for release 4.7.3
