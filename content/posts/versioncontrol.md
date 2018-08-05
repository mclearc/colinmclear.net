+++
title = "Version Control and Academic Writing"
date = 2015-07-17
tags = ["workflows", "geekery", "writing", "git"]
draft = false
aliases = "/2015/version-control-and-academic-writing"
type = "post"
toc = false
+++

Academic writing typically requires writing something in drafts. Many drafts.
Until recently there have been few ways of elegantly handling this. Often, one
would need to title the current draft with the day&rsquo;s date, then save this
draft in a folder (named, e.g., &ldquo;drafts&rdquo; or &ldquo;versions&rdquo;), and do this every
time one sits down to write. This works, in some ways. The data is there. The
problem is that you quickly end up with a folder (or desktop&rsquo;s) worth of
files. These filenames have typically ridiculous and increasingly obscure
titles (e.g. final-draft-final-revision\final-draft-04-2018.docx). And it
is seldom clear, using this method, exactly what one did when, without
actually opening a particular file and looking, or trying to remember when
(and where) it was that one made the relevant change.

Nowadays, especially if you use some sort of cloud-based word-processor, it&rsquo;s
likely that you have access to various ways of looking at your version
history. For example, Google docs has a [revision history](https://support.google.com/docs/answer/190843?hl=en) option (something
similar exists for [Dropbox](http://www.macinstruct.com/node/516), which lets you easily move back and forth among
different versions. Revision histories of this kind offer a way to
automatically back up one&rsquo;s writing. This is especially helpful if you&rsquo;re not
the type of person to carefully name each day&rsquo;s writing with a new time/date
stamp and save them all in the appropriate folder. There are also service (as
opposed to application) specific ways of tracking changes to a file. At least
[some](http://versionrocket.com) of [them](http://versionrocket.com) allow you to compare differences between versions of files. But
at least two things are missing. First, there is no straightforward way of
seeing what has changed where, and to see this at arbitrary levels of
granularity. Second, in order to see what&rsquo;s changed when, you have to look in
the document itself. There is no general log of the changes you&rsquo;ve made to the
file.

Here&rsquo;s what I have in mind:

{{< figure src="/materials/images/ScreenShot52964.png" caption="Figure 1: Change Log" >}}

You see here a series of entries going back over two years, with a description
of what I took to be the most important changes at the time. I can then open
any one of the those entries and see a more detailed, line by line,
description of changes. This is called a &ldquo;diff&rdquo;. I can also roll back the
version of the file I&rsquo;m working on to any of these changes. Each &ldquo;commit&rdquo; is a
snapshot of the relevant files at the time, which I can retrieve at any point.

I think this is a really nice way to track and visualize one&rsquo;s progress on
some piece of writing. This is hard to do with standard word processors and
their means of versioning, but very straightforward to do with a more
sophisticated kind of [version control system](https://en.wikipedia.org/wiki/Revision%5Fcontrol). A version control system can
manage changes to a file at an extremely fine level of grain--down to a line
or character if necessary. While this system was originally adopted by
programmers, it can also be very useful in academic writing (or really any
writing where multiple drafts are created).

This form of version control pictured above depends on a system called
[Git](https://git-scm.com).[^fn:1] There are lots of [tutorials](http://rogerdudler.github.io/git-guide/) and [other resources](https://www.atlassian.com/git/) for using Git.
Though Git is often used from the command line there are also some [great](http://gitup.co) free
[graphical interfaces](https://www.sourcetreeapp.com) for Git. There are also a lot of helpful [discussions](http://writers.stackexchange.com/questions/10440/what-is-the-purpose-of-version-control/10443#10443)
online concerning writing while using a version control system like Git.

The basic idea is that, using whatever writing application one likes,
one tracks changes to a document, or a whole directory of documents
(e.g. adding image files for presentations, or additional parts of a
document kept in separate files when writing longer works like a thesis
or novel). The changes can be tracked at an arbitrary level of grain--to
the sentence, word, or character--and different versions can be easily
compared. All of this can be done without generating lots of files with
different numbers or date/time stamps. Everything is kept in a database
that one can easily interact with using either the command line or some
form of graphical interface.

So far, this isn&rsquo;t necessarily any different from what one can do using
Word or Google Docs. One additional benefit of using a version control
system is that one can easily label and describe batches of changes
(e.g. revisions to a particular section of a paper or chapter) and keep
a single record of these changes. Then, if one want to look back at
one&rsquo;s progress, or for a specific change that one made, all one need do
is look at the single general document listing the changes. You can even
do this in the text editor of your choice (e.g. vim or sublime text)

For example, here&rsquo;s a sample log of the changes made to a paper I&rsquo;ve been
working on, using a vim plugin called &ldquo;[gitv](https://github.com/gregsexton/gitv)&rdquo;, which depends on Tim Pope&rsquo;s
[fugitive](https://github.com/tpope/vim-fugitive) plugin ([SublimeGit](https://sublimegit.net) is an equally excellent sublime text plugin).

{{< figure src="/materials/images/ScreenShot56089.png" >}}

On the left is the git log of changes. On the right is a more detailed
description of what changed--what was added, deleted, or moved.


## Using Git {#using-git}

The basic workflow for using Git is as follows. In the directory you&rsquo;re
keeping your project in (you do keep this in a directory and not just on
your desktop right?) you need to create a Git repository. This means
typing `git init` on the command line from the directory, or doing so
via whatever GUI app you&rsquo;ve picked. You only have to do this once per
writing project. So that&rsquo;s:

-   `cd \path\to\repository`
-   `git init`
-   `git add filename.file`
-   `git commit`
    -   write commit message
    -   write and quit file

Once you&rsquo;ve got your repository (or &ldquo;repo&rdquo;) you need to add files for
tracking. Just type `git add` and the name of the file you&rsquo;re tracking.
Then type `git commit`. You&rsquo;ll then type a commit message to go along
with the commit--e.g. &ldquo;first commit&rdquo;. Write and quit, or press commit in
whatever application you&rsquo;re using. At this point you&rsquo;ve got a
functioning version control system. So your workflow should be something
like the following:

-   Write
-   Add/stage changes
-   Write commit message and commit

There&rsquo;s a lot to Git that I can&rsquo;t cover here. It can be very helpful when
experimenting with an idea. It&rsquo;s also a nice way to think about and track your
work over time. One downside of using a system like git is that it doesn&rsquo;t
work well with Microsoft Word or other rich text WYSIWIG text editors. But
there are ways [around](http://blog.martinfenner.org/2014/08/25/using-microsoft-word-with-git/) [this](https://www.martineve.com/2013/08/18/using-git-in-my-writing-workflow/).

If you like the idea of git, commit messages, and a readable log of changes
you&rsquo;ve made to a file, but don&rsquo;t want to deal with the more technical aspects
of setting up git and using it, there are also great web apps like [Penflip](https://www.penflip.com),
which streamline much of the process.

[^fn:1]: You might also look at [Mercurial](https://mercurial.selenic.com), which is a popular, and perhaps slightly easier to use, alternative to Git.
