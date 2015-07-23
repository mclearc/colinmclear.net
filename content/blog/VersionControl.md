---
title: Version Control and Academic Writing
author: Colin McLear
date: 2015-07-17
tags: geekery, writing, workflows
modified: 
status: draft
---

Academic writing requires writing something in drafts. Many drafts. Until
recently there have been few ways of elegantly handling this. Often, one would
need to title the current draft with the day's date, then save this draft in a
folder (named, e.g., "drafts" or "versions"), and do this every time one sits
down to write. This works, in some ways. The data is there. The problem is that
you quickly end up with a folder (or desktop's) worth of files. These filenames
have typically ridiculous and increasingly obscure titles (e.g.
4_26_13_Really_Final_FinalPaper.docx). And it is seldom clear, using this
method, exactly what one did when, without actually opening a particular file
and looking, or trying to remember when (and where) it was that one made the
relevant change. Nowadays, especially if you use some sort of cloud-based
word-processor, it's likely that you have access to various ways of looking at
your version history. For example, Google docs has a [revision
history](https://support.google.com/docs/answer/190843?hl=en) option (something
similar exists for [Dropbox](http://www.macinstruct.com/node/516), which lets
you easily move back and forth among different versions. Revision histories of
this kind offer a way to automatically back up one's writing. This is especially
helpful if you're not the type of person to carefully name each day's writing
with a new time/date stamp and save them all in the appropriate folder. But at
least two things are missing. First, there is no straightforward way of seeing
what has changed where, and to see this at arbitrary levels of granularity.
Second, in order to see what's changed when, you have to look in the document
itself. There is no general log of the changes you've made to the file.  




. . . 

While everyone's writing process is different, one thing in academic writing is
for certain: anything you write is going to see many revisions. A common way to
handle such revisions is to title the current draft with the day's date. Save
this draft in a folder (named, e.g., "drafts" or "versions"), and do this every
time one sits down to write. The problem is that you quickly end up with a
folder (or desktop's) worth of files. And it is seldom clear, using this method,
exactly what one did when, without actually opening a particular file and
looking, or trying to remember when it was that one made the relevant change.
This is where a more sophisticated kind of [version
control](https://en.wikipedia.org/wiki/Revision_control) becomes useful. A
version control system can manage changes to a file at an extremely fine level
of grain--down to a line or character if necessary. While this is obviously
helpful in programming, it can also be very useful in academic writing (or
really any writing where multiple drafts are created). Below I discuss some of
the different ways that one might incorporate different aspects of a version
control system into one's writing.

## Track Changes

Anyone using *Microsoft Word*, *Open Office*, or Apple's *Pages* should be familiar with
the option to track changes to one's work over time. [This article] provides a
nice overview of the different ways one can track changes in a Word document.
Tracking changes is great for collaboration, but it doesn't really solve the
problem that one needs to solve in writing daily--viz. easily tracking
milestones in one's writing, or important changes of direction, etc. All changes
are treated equally even when they aren't. There also is no simple way to view
changes without simply looking in the document itself.

  [This article]: http://www.techrepublic.com/article/microsoft-office-word-101-use-track-changes-more-efficiently/

## Document Revision History

If you use a cloud service like Dropbox or Google docs you also have a [revision
history](https://support.google.com/docs/answer/190843?hl=en) option, which lets
you easily move back and forth among different versions. Revision histories of
this kind offer a way to automatically back-up one's writing. This is especially
helpful if one isn't the type of person to carefully name each day's writing
with a new time/date stamp and save them all in the appropriate folder. But the
method, while a helpful back-up, doesn't resolve the issue of granularity or
ease of getting information about what was changed when. 

## Version Control

What we've looked at so far are application or service specific ways of tracking
changes to a file. At least some of them allow you to compare differences
between versions of files, or you can use a variety of
[different](http://versionrocket.com) [services](http://versionrocket.com) 
to do the job as well. 

Another option is to use a system familiar to programmers, and adopt some form
of version control. The basic idea is that, using whatever writing application
one likes, one tracks changes to a document, or a whole directory of documents
(e.g. adding image files for presentations, or additional parts of a document
kept in separate files when writing longer works like a thesis or novel). The
changes can be tracked at an arbitrary level of grain--to the sentence, word,
or character--and different versions can be easily compared. All of this can be
done without generating lots of files with different numbers or date/time
stamps. Everything is kept in a database that one can easily interact with using
either the command line or some form of graphical interface. 

So far, this isn't necessarily any different from what one can do using Word or
Google Docs. One additional benefit of using a version control system is that
one can easily label and describe batches of changes (e.g. revisions to a
particular section of a paper or chapter) and keep a single record of these
changes. Then, if one want to look back at one's progress, or for a specific
change that one made, all one need do is look at the single general document
listing the changes. For example, here's a sample log of the changes made to a
paper I've been working on. 

![]({filename}/images/GitLog.png)

You see on the left a series of entries going back six weeks, with a description
of what I took to be the most important changes at the time. I can then open any
one of the those entries and see a more detailed, line by line, description of
changes. This is called a "diff". I can also roll back the version of the file
I'm working on to any of these changes. 

This form of version control depends on a system called *[Git]*.[^mercurial] There are lots of
[tutorials] and [other resources] for using Git. Though Git is often used from
the command line there are also some [great] free [graphical interfaces] for Git. There
are also a lot of helpful [discussions] online concerning writing while using a
version control system like Git.

[^mercurial]: You might also look at [mercurial](https://mercurial.selenic.com),
which is a popular, and perhaps slightly easier to use, alternative to git.

  [Git]: https://git-scm.com
  [tutorials]: http://rogerdudler.github.io/git-guide/
  [other resources]: https://www.atlassian.com/git/
  [great]: http://gitup.co
  [graphical interfaces]: https://www.sourcetreeapp.com
  [discussions]: http://writers.stackexchange.com/questions/10440/what-is-the-purpose-of-version-control/10443#10443

## Using Git

The basic workflow for using Git is as follows. In the directory you're keeping
your project in (you do keep this in a directory and not just on your desktop
right?) you need to create a Git repository. This means typing `git init` on the
command line from the directory, or doing so via whatever GUI app you've picked.
You only have to do this once per writing project. So that's:

- `cd \path\to\repository`
- `git init`
- `git add filename.file`
- `git commit`
  - write commit message
  - write and quit file

Once you've got your repository (or "repo") you need to add files for tracking. 
Just type `git add` and the name of the file you're tracking. Then type `git
commit`. You'll then type a commit message to go along with the commit--e.g.
"first commit". Write and quit, or press commit in whatever application you're
using. At this point you've got a functioning version control system. So your
workflow should be something like the following:

- Write
- Add/stage changes
- Write commit message and commit

There's a lot to Git that I can't cover here. It can be very helpful when
experimenting with an idea. It's also a nice way to think about and track your
work over time. One downside of using a system like git is that it doesn't work
well with Microsoft Word or other rich text WYSIWIG text editors. But there are
ways
[around](http://blog.martinfenner.org/2014/08/25/using-microsoft-word-with-git/)
[this](https://www.martineve.com/2013/08/18/using-git-in-my-writing-workflow/).

If you like the idea of git, commit messages, and a readable log of changes
you've made to a file, but don't want to deal with the more technical aspects of
setting up git and using it, there are also great web apps like
[Penflip](https://www.penflip.com), which streamline much of the process. 


