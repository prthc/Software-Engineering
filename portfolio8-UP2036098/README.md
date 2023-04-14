# **Software Engineering Theory and Practice**

|  School of Computing | ![ University of Portsmouth Logo](images/UoPLogo.jpg) |
| --------------- | --------------- |
| Title | Software Engineering Theory and Practice |
| Module Coordinator| Steven Ossont|
| Email | steven.ossont@port.ac.uk|
| Code | M30819|
| Moodle | [https://moodle.port.ac.uk/course/view.php?id=11429](https://moodle.port.ac.uk/course/view.php?id=11429) |

## Schedule and Deliverables

| Item | Value | Format | Outcomes | Deadline |
| --- | --- | --- | --- | --- |
| Portfolio8 | 1% | GitHub Repo | Pass/Fail |  23 April 2021, 23:00 |

## Notes and Advice

<!-- markdown-link-check-disable -->
* The [Extenuating Circumstances procedure](https://myport.port.ac.uk/my-course/extenuating-circumstances ) is
  there to support you if you have had any circumstances (problems) that have
  been serious or significant enough to prevent you from attending, completing
  or submitting an assessment on time.
* The UNION Extenuating Circumstances [Extenuating Circumstances procedure](https://upsu.net/advice/academic-advice/extenuating-circumstances)
* [ASDAC](https://myport.port.ac.uk/guidance-and-support/additional-support-and-disability-advice )
  are available to any students who disclose a disability or require additional
  support for their academic studies with a good set of resources on the [ASDAC
  Moodle site](https://moodle.port.ac.uk/course/view.php?id=3012)
* The University takes plagiarism seriously. Please ensure you adhere to the
  plagiarism guidelines.
Examination Regulations ([http://regulations.docstore.port.ac.uk/ExamRegs12AssessmentOffences.pdf](http://regulations.docstore.port.ac.uk/ExamRegs12AssessmentOffences.pdf)).
* Any material included in your coursework should be
  fully cited and referenced in APA format (seventh edition). Detailed advice on
  referencing is available from [http://referencing.port.ac.uk/](http://referencing.port.ac.uk/)
* Any material submitted that does not meet format or submission guidelines, or
  falls outside of the submission deadline could be subject to a cap on your
  overall result or disqualification entirely.
* If you need additional assistance, you can ask your personal tutor, learning
  support ana.baker@port.ac.uk and xia.han@port.ac.uk or your lecturers.
<!-- markdown-link-check-enable-->

## Git commands

So far you have learnt the following git commands, if you are unclear what these are you MUST practice. You are expected to know them and how to use them without explanation.

```shell
git clone
git add
git pull
git commit
git push
git branch
git merge
git checkout
```

And your trusted command, to help figure what is going on....

```shell
git status
```

> Your repository will be copied for marking automatically at the deadline.
> EDITS after the deadline are automatically ignored.

When you update the `CheckList.md` file. This will trigger an action to inspect the work for this part of the Portfolio.(You can also manually run the `PortfolioChecker` if you need to see if changes solve any errors)

Files, external to this repo and any images imported via URL will be ignored (Even if they are stored in GitHub).

Large blocks of text that use the 'CODE' formatting will be ignored. This includes using triple \`\`\` (Unless it is code or something sensible).
If it looks like you are using \`\`\` to contain Markdown to avoid the lint checker, it will be ignored.
Code blocks should be labeled with the code language so that the syntax highlighter is enabled.

Here is a helpful Markdown link: [https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)

At no point in this Assessment should you use the `Add file` button on the GitHub webpage -- Pretend it does not exist

Marking is performed on a Ubuntu machine. This means that everything is case sensitive, where it may not be on Windows.

> Clone, Edit, Commit, Push  (Preferably on the command line)

![AddFile.png](./images/AddFile.png)

## Objectives

* Learn how to use LFS (Large file support)  in GitHub

## Portfolio 8 Part 1

Create a file with the filename `Student.id`, add your Student ID to the content of this file. Note:

* Invalid ID = No marks
* The file extension is `.id` other file extensions e.g. `.txt` are not permitted
* The content of the file should be your ID ONLY, e.g. `UP1234567`
* You may have a return character at the end of the line `\n` (Note this is not two ASCII text characters)
* You need the `UP`
* Filename is case sensitive
* File contents are case sensitive
* File should contain one line of text only
* Markdown formatting is NOT permitted e.g. `*` or `-`

> Instructions are slightly different this time, please follow the instructions.

<!-- Save, Commit -->

When you have completed this part of the portfolio :

* Put an `X` in the `CheckList.md` to indicate this part of the Portfolio is complete
* Commit and **push** your changes to GitHub
* Manually run the `PortfolioChecker` action, and ensure it passes. (Must PASS)
* Navigate to the `PortfolioChecker` action on GitHub.com and read the feedback / errors / comments
* Manually run the `Pandoc` action, and check the resulting PDF is as expected. (Must PASS)
* Manually run the `MarkdownChecker` action, this will be superseded by the super-linter. (Must PASS)
* Manually run the `SuperLinter` action, please do your best to ensure there are no errors on *your* files. (Feedback on this action is appreciated)
* Add any files that are needed for this part (if any), to your GitHub repo E.g. new files that you created
* Check you have an `X` in the `CheckList.md` to indicate this part of the Portfolio is complete
* Commit and **push** your changes to GitHub
* Be sure to address any errors from the GitHub actions
* You do not need to wait for the `PortfolioChecker` to complete, if it is running slow. Proceed and come back and look at the checker errors/warnings when it completes.

<!-- Save, Commit -->
## Portfolio 8 Part 2

For this portfolio it is important that you learn how to use git LFS to store large files.

For `Portfolio8` it is important that you use **small files** in place of large files. If you use large files , then it wastes bandwidth, storage and more importantly will become slow.

`Portfolio8` will ensure you have the skills to submit your `CW4` video as this will need LFS support. (You only get one chance to upload your video, so practice in this `Portfolio8` repo first)

Read the following so that you understand what git LFS is and why you would use it.

* [https://docs.github.com/en/github/managing-large-files/about-git-large-file-storage](https://docs.github.com/en/github/managing-large-files/about-git-large-file-storage)

* [https://docs.github.com/en/github/managing-large-files/collaboration-with-git-large-file-storage](https://docs.github.com/en/github/managing-large-files/collaboration-with-git-large-file-storage)

## Portfolio 8 Part 3

In order to use `git lfs`, you'll need to download and install a new program that is separate from Git.
Install `git lfs` support for your operating system, see these instructions:

[https://docs.github.com/en/github/managing-large-files/installing-git-large-file-storage](https://docs.github.com/en/github/managing-large-files/installing-git-large-file-storage)

Here are some examples:

### Ubuntu

```bash
$ sudo apt install git-lfs
$
```

### Windows

[https://github.com/git-lfs/git-lfs/releases/download/v2.13.2/git-lfs-windows-v2.13.2.exe](https://github.com/git-lfs/git-lfs/releases/download/v2.13.2/git-lfs-windows-v2.13.2.exe)

> Check you have lfs installed

```bash
$ git lfs version
git-lfs/2.13.2 (GitHub; linux amd64; go 1.15.5)
```

1. Add a new markdown file to your `.pandoc.yml`
2. Add your `git lfs version` output text to the markdown file, add it to the .pandoc.yml. Use fenced code.

```text

a bit like this

```

<!-- Save, Commit -->

When you have completed this part of the portfolio :

* Manually run the `PortfolioChecker` action, and ensure it passes. (Must PASS)
* Navigate to the `PortfolioChecker` action on GitHub.com and read the feedback / errors / comments
* Manually run the `Pandoc` action, and check the resulting PDF is as expected. (Must PASS)
* Manually run the `MarkdownChecker` action, this will be superseded by the super-linter. (Must PASS)
* Manually run the `SuperLinter` action, please do your best to ensure there are no errors on *your* files. (Feedback on this action is appreciated)
* Add any files that are needed for this part (if any), to your GitHub repo E.g. new files that you created
* Put an `X` in the `CheckList.md` to indicate this part of the Portfolio is complete
* Commit and **push** your changes to GitHub
* Be sure to address any errors from the GitHub actions
* You do not need to wait for the `PortfolioChecker` to complete, if it is running slow. Proceed and come back and look at the checker errors/warnings when it completes.

<!-- Save, Commit -->

## Portfolio 8 Part 4

[https://git-lfs.github.com/](https://git-lfs.github.com/)

* Once downloaded and installed, set up Git LFS for your user account by running:

```bash
git lfs install
```

> You only need to run this **once per user account**.

In each Git repository where you want to use Git LFS (e.g. `Portfolio8` and `CW4`) associate a file type in your repository with Git LFS. Enter `git lfs track` followed by the name of the file extension you want to automatically upload to Git LFS.

> You can configure additional file extensions at anytime.

* For Portfolio8 , associate any file with the `.largefile` extension with Git LFS. (If you run Windows, ensure you can see file extensions). Here is the command:

`git lfs track "*.largefile"`

> This will generate a `.gitattributes` file, which you can edit manually if you want.

Make sure the file `.gitattributes` will be versioned with git. E.g. add the file to your git repo:

`git add .gitattributes`

Note that defining the file types Git LFS should track will not, by itself, convert any pre-existing files to Git LFS, such as files on other branches or in your prior commit history. To do that, use the git lfs migrate command, which has a range of options designed to suit various potential use cases.

* Add the contents of your `.gitattributes` to your `Portfolio8` PDF, consider fenced code and a heading.

From now on any file with the extension `.largefile` will be managed by LFS. For your `CW4` you will need to do this for your Video submission.

> If you run `git lfs track` without any options it will show you what files are being tracked by LFS.

<!-- Save, Commit -->

When you have completed this part of the portfolio :

* Manually run the `PortfolioChecker` action, and ensure it passes. (Must PASS)
* Navigate to the `PortfolioChecker` action on GitHub.com and read the feedback / errors / comments
* Manually run the `Pandoc` action, and check the resulting PDF is as expected. (Must PASS)
* Manually run the `MarkdownChecker` action, this will be superseded by the super-linter. (Must PASS)
* Manually run the `SuperLinter` action, please do your best to ensure there are no errors on *your* files. (Feedback on this action is appreciated)
* Add any files that are needed for this part (if any), to your GitHub repo E.g. new files that you created
* Put an `X` in the `CheckList.md` to indicate this part of the Portfolio is complete
* Commit and **push** your changes to GitHub
* Be sure to address any errors from the GitHub actions
* You do not need to wait for the `PortfolioChecker` to complete, if it is running slow. Proceed and come back and look at the checker errors/warnings when it completes.

<!-- Save, Commit -->

## Portfolio 8 Part 5

Generate a file (Do not make it bigger that 1KiB) name the file: `Test1.largefile`. For those on windows be careful with extensions here.

Add this file to git; commit and push
Here is an example:

```bash
$ echo "Hello large file" > Testing.largefile
$ git add Testing.largefile
$ git commit -m "Adding a LFS file"
$ git push
$
```

Copy the text output of your command line to your `Portfolio8` PDF. It must contain a line showing that an LFS object is being uploaded. Consider a heading; fenced code.

Here is an example output from a git push using LFS:

```bash
$ git push
Uploading LFS objects: 100% (1/1), 5 B | 0 B/s, done.
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 357 bytes | 357.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
...
```

<!-- Save, Commit -->

When you have completed this part of the portfolio :

* Manually run the `PortfolioChecker` action, and ensure it passes. (Must PASS)
* Navigate to the `PortfolioChecker` action on GitHub.com and read the feedback / errors / comments
* Manually run the `Pandoc` action, and check the resulting PDF is as expected. (Must PASS)
* Manually run the `MarkdownChecker` action, this will be superseded by the super-linter. (Must PASS)
* Manually run the `SuperLinter` action, please do your best to ensure there are no errors on *your* files. (Feedback on this action is appreciated)
* Add any files that are needed for this part (if any), to your GitHub repo E.g. new files that you created
* Put an `X` in the `CheckList.md` to indicate this part of the Portfolio is complete
* Commit and **push** your changes to GitHub
* Be sure to address any errors from the GitHub actions
* You do not need to wait for the `PortfolioChecker` to complete, if it is running slow. Proceed and come back and look at the checker errors/warnings when it completes.

<!-- Save, Commit -->

## Portfolio 8 Part 6

> Storing large files in git is often a bad idea, but everyone gets tempted and hence it is worth knowing how to do it properly.

Read the notes on bandwidth and storage

[https://docs.github.com/en/github/managing-large-files/about-storage-and-bandwidth-usage](https://docs.github.com/en/github/managing-large-files/about-storage-and-bandwidth-usage)

Beware that your `CW4` limits will enable you to upload your video **once**. Use this repo to ensure you have a good understanding of LFS. Feel free to practice (using small files).

Take note of this :

*If you push a 500 MB file to Git LFS, you'll use 500 MB of your allotted storage and none of your bandwidth. If you make a 1 byte change and push the file again, you'll use another 500 MB of storage and no bandwidth, bringing your total usage for these two pushes to 1 GB of storage and zero bandwidth.*

* Add a list of the files tracked by LFS (probably one) to your `Portfolio8` PDF. Here is an example:

```bash
$ git lfs ls-files
f2ca1bb6c7 * test.mp4
$
```

<!-- Save, Commit -->

When you have completed this part of the portfolio :

* Manually run the `PortfolioChecker` action, and ensure it passes. (Must PASS)
* Navigate to the `PortfolioChecker` action on GitHub.com and read the feedback / errors / comments
* Manually run the `Pandoc` action, and check the resulting PDF is as expected. (Must PASS)
* Manually run the `MarkdownChecker` action, this will be superseded by the super-linter. (Must PASS)
* Manually run the `SuperLinter` action, please do your best to ensure there are no errors on *your* files. (Feedback on this action is appreciated)
* Add any files that are needed for this part (if any), to your GitHub repo E.g. new files that you created
* Put an `X` in the `CheckList.md` to indicate this part of the Portfolio is complete
* Commit and **push** your changes to GitHub
* Be sure to address any errors from the GitHub actions
* You do not need to wait for the `PortfolioChecker` to complete, if it is running slow. Proceed and come back and look at the checker errors/warnings when it completes.

<!-- Save, Commit -->

## Portfolio 8 Part 7 (Optional)

Optional have a read of this:
[https://shuhrat.github.io/programming/git-lfs-tips-and-tricks.html](https://shuhrat.github.io/programming/git-lfs-tips-and-tricks.html)

Optional: LFS with Kit Kracken (Warning be careful)
[https://support.gitkraken.com/git-workflows-and-extensions/intro-and-requirements/](https://support.gitkraken.com/git-workflows-and-extensions/intro-and-requirements/)

* Consider looking at the following commands and using some...

```text
       git-lfs-env(1)
              Display the Git LFS environment.

       git-lfs-checkout(1)
              Populate working copy with real content from Git LFS files.

       git-lfs-dedup(1)
              De-duplicate Git LFS files.

       git-lfs-ext(1)
              Display Git LFS extension details.

       git-lfs-fetch(1)
              Download Git LFS files from a remote.

       git-lfs-fsck(1)
              Check Git LFS files for consistency.

       git-lfs-install(1)
              Install Git LFS configuration.

       git-lfs-lock(1)
              Set a file as "locked" on the Git LFS server.

       git-lfs-locks(1)
              List currently "locked" files from the Git LFS server.

       git-lfs-logs(1)
              Show errors from the Git LFS command.

       git-lfs-ls-files(1)
              Show information about Git LFS files in the index and working tree.

       git-lfs-migrate(1)
              Migrate history to or from Git LFS

       git-lfs-prune(1)
              Delete old Git LFS files from local storage

       git-lfs-pull(1)
              Fetch Git LFS changes from the remote & checkout any required working tree files.

       git-lfs-push(1)
              Push queued large files to the Git LFS endpoint.

       git-lfs-status(1)
              Show the status of Git LFS files in the working tree.

       git-lfs-track(1)
              View or add Git LFS paths to Git attributes.

       git-lfs-uninstall(1)
              Uninstall Git LFS by removing hooks and smudge/clean filter configuration.

       git-lfs-unlock(1)
              Remove "locked" setting for a file on the Git LFS server.

       git-lfs-untrack(1)
              Remove Git LFS paths from Git Attributes.

       git-lfs-update(1)
              Update Git hooks for the current Git repository.

       git-lfs-version(1)
              Report the version number.

      Low level commands (plumbing)
       git-lfs-clean(1)
              Git clean filter that converts large files to pointers.

       git-lfs-filter-process(1)
              Git process filter that converts between large files and pointers.

       git-lfs-pointer(1)
              Build and compare pointers.

       git-lfs-post-checkout(1)
              Git post-checkout hook implementation.

       git-lfs-post-commit(1)
              Git post-commit hook implementation.

       git-lfs-post-merge(1)
              Git post-merge hook implementation.

       git-lfs-pre-push(1)
              Git pre-push hook implementation.

       git-lfs-smudge(1)
              Git smudge filter that converts pointer in blobs to the actual content.

       git-lfs-standalone-file(1)
              Git LFS standalone transfer adapter for file URLs (local paths).
```

<!-- Save, Commit -->

When you have completed this part of the portfolio :

* Manually run the `PortfolioChecker` action, and ensure it passes. (Must PASS)
* Navigate to the `PortfolioChecker` action on GitHub.com and read the feedback / errors / comments
* Manually run the `Pandoc` action, and check the resulting PDF is as expected. (Must PASS)
* Manually run the `MarkdownChecker` action, this will be superseded by the super-linter. (Must PASS)
* Manually run the `SuperLinter` action, please do your best to ensure there are no errors on *your* files. (Feedback on this action is appreciated)
* Add any files that are needed for this part (if any), to your GitHub repo E.g. new files that you created
* Put an `X` in the `CheckList.md` to indicate this part of the Portfolio is complete
* Commit and **push** your changes to GitHub
* Be sure to address any errors from the GitHub actions
* You do not need to wait for the `PortfolioChecker` to complete, if it is running slow. Proceed and come back and look at the checker errors/warnings when it completes.

<!-- Save, Commit -->

## Portfolio 8 Part 8

1. Remove the `README.md` file from the PDF (see `.pandoc.yml`)
2. In this Portfolio you have added content to the PDF. Please ensure it is readable and formatted well.
3. Check the PDF is built correctly. (PDF is marked)

<!-- Save, Commit -->

When you have completed this part of the portfolio :

* Manually run the `PortfolioChecker` action, and ensure it passes. (Must PASS)
* Navigate to the `PortfolioChecker` action on GitHub.com and read the feedback / errors / comments
* Manually run the `Pandoc` action, and check the resulting PDF is as expected. (Must PASS)
* Manually run the `MarkdownChecker` action, this will be superseded by the super-linter. (Must PASS)
* Manually run the `SuperLinter` action, please do your best to ensure there are no errors on *your* files. (Feedback on this action is appreciated)
* Add any files that are needed for this part (if any), to your GitHub repo E.g. new files that you created
* Put an `X` in the `CheckList.md` to indicate this part of the Portfolio is complete
* Commit and **push** your changes to GitHub
* Be sure to address any errors from the GitHub actions
* You do not need to wait for the `PortfolioChecker` to complete, if it is running slow. Proceed and come back and look at the checker errors/warnings when it completes.

<!-- Save, Commit -->

## Portfolio 8 Completed

> Tip GitHub now has a night/dark mode [https://github.com/settings/appearance](https://github.com/settings/appearance) why not give it a go if you are working at night?

You must run these actions [**Run these actions manually now**]:

* ![MarkdownChecker](../../workflows/MarkdownChecker/badge.svg) [Must pass]
* ![Pandoc](../../workflows/Pandoc/badge.svg) [Must pass]
* ![PortfolioChecker](../../workflows/PortfolioChecker/badge.svg) [Must pass]

[Banners above are **EXPERIMENTAL**; do not rely on them]

* Commit and push your changes to GitHub

Complete the checklist and submit by putting an `X` in the portfolio checklist to indicate the Portfolio is complete and ready to mark.

> If you want to re-submit your work, any time before the deadline. You can un-tick the Portfolio Completed checkbox; **commit & push;** then re-tick Portfolio Completed checkbox; **commit & push.**

Once you have done this step, the commit hash of your latest commit should be in `.Ossonts/latestSHA.log`

* Double check that this commit hash (URL is included in `.Ossonts/latestSHA.log`) is the version you want to submit.
* If this commit hash is **incorrect**; Re-submit your portfolio. (See above).
* If you commit hash was **NOT** correct please raise an issue as well as resubmitting to correct the SHA.

<!-- Save, Commit -->

When you have completed this part of the portfolio :

* Manually run the `PortfolioChecker` action, and ensure it passes. (Must PASS)
* Navigate to the `PortfolioChecker` action on GitHub.com and read the feedback / errors / comments
* Manually run the `Pandoc` action, and check the resulting PDF is as expected. (Must PASS)
* Manually run the `MarkdownChecker` action, this will be superseded by the super-linter. (Must PASS)
* Add any files that are needed for this part (if any), to your GitHub repo E.g. new files that you created
* Put an `X` in the `CheckList.md` to indicate this part of the Portfolio is complete
* Commit and **push** your changes to GitHub
* Be sure to address any errors from the GitHub actions
* You do not need to wait for the `PortfolioChecker` to complete, if it is running slow. Proceed and come back and look at the checker errors/warnings when it completes.

<!-- Save, Commit -->

## **Your repository will be copied for marking automatically at the coursework deadline OR when the Completed checklist item is ticked; whichever is earliest**
