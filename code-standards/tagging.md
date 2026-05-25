# Tagging releases

## Only tag in Master

NB: On the CHANGELOG.md , if it is the 1st push to master branch, you will have a [1.0.0] entry. This entry will be a "fake" link that will become active ONLY after merging.

## [1.0.0](https://bitbucket.int.corp.sun/projects/<PROJECT_NAME>/repos/<REPO_NAME>/compare/diff?sourceBranch=refs/tags/1.0.0&targetBranch=<first_commit_on_master_branch>) YYYY-MM-DD

* The value /refs/tags/1.0.0 doesn't exist until AFTER code is merged to Master and then the tag 1.0.0 is applied next.
* Code MUST be in Master branch before you apply the tag 1.0.0. See below.
* The targetBranch is the FIRST COMMIT onto the Master Branch

## Apply Tag

### First push to master

```bash
git tag -a 1.0.0 -m "Release version 1.0.0"
git push --tags
```

### Updating of master

WARN: Only ever apply semantic version tags (e.g. 3.4.17, 2.LATEST) to commits that are present in the master branch. If you do need to apply a tag to a commit in a non-master branch, use any other tag format.

Semantic version tags are reserved exclusively for approved releases that have passed peer review.

git checkout master
git pull
git tag 4.7.3
git push --tags

Taking this concept a step further, we can place mutable "LATEST" tags against a repository's commits to identify the current/latest major or minor release of a codebase:

## Using LATEST tags

git checkout master
git pull
git tag 4.7.3         # add a new tag to the latest commit in our local copy of the master branch
git tag -f 4.LATEST   # assuming we already have a 4.LATEST tag applied to the 4.7.2 release, we will need to forcibly update the tag with the -f flag
git tag -f 4.7.LATEST
git push -f --tags    # push the locally applied tags to the remote repository, forcibly, to allow overwriting existing tags on the protected master branch

Finally, end users can lock to a release of a module with one of the following statements:

Referencing semantic versions of Terraform modules
module "some_module_specific" {
  source = "git::ssh://bitbucket.int.corp.sun:2222/cs/some-terraform-module.git?ref=4.7.3" # lock to specific semantic version
  ...
}

module "some_module_major" {
  source = "git::ssh://bitbucket.int.corp.sun:2222/cs/some-terraform-module.git?ref=4.LATEST" # lock to LATEST major release
  ...
}

module "some_module_minor" {
  source = "git::ssh://bitbucket.int.corp.sun:2222/cs/some-terraform-module.git?ref=4.7.LATEST" # lock to LATEST minor release
  ...
}

"LATEST" tag do not serve any purpose in root/configuration repositories, because they are not referenced as a module by any other Terraform code. 
Therefore in root/configuration repositories only, they should be ommitted leaving only the specific version tags, e.g. 1.0.0, 1.1.0 etc.
