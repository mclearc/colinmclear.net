+++
title = "Text Editors and Academic Writing"
date = 2016-09-05
tags = ["writing"]
draft = false
aliases = "/2016/text-editors-and-academic-writing"
type = "post"
toc = false
+++

Tools for writing using a computer fall into two broad camps. On the one side
we have [WYSIWIG](https://en.wikipedia.org/wiki/WYSIWYG) word processing applications like Microsoft Word, Apple Pages,
and Google Docs. They allow not only the typing of text but also real-time
formatting and display. These applications are familiar to most, and are the
dominant ones used in higher-ed today. They also tend to be expensive (or
available only to those with institutional affiliation), suffer from issues of
feature-bloat and unnecessary make-overs, and use proprietary
non-human-readable file formats.

In contrast to the WYSIWIG editors stands the [text editor](https://en.wikipedia.org/wiki/Text%5Feditor). It operates on
plain text, human readable, files. And its main purpose is to parse text in
the most efficient way possible. It does not (typically) display a page as it
will look when printed. There are many, many text editors one can choose from
them, and the two most well-known---[emacs](https://www.gnu.org/software/emacs/) and [vim](http://www.vim.org)---are free.

As far as I can tell there are basically three main reasons to prefer a
text editor over a word processing application.

-   Text editors are more efficient at editing text
-   Text editors connect better with other research and writing tools
-   Text editors are easier to enjoy working in/with

I&rsquo;m not sure that I find any of these or the [many other various arguments](https://www.google.com/search?q=writing+in+plain+text) for
writing in plain text with a text editor totally convincing, at least in
isolation. Certainly there is no one-size-fits-all answer. If you like writing
in MS Word or Apple Pages, if such programs help you get on with writing, then
great.

That said, there are some really useful things that you can do when writing in
plain text and using a powerful (and often free) text editor, or command line
tools made for manipulating text (like [cat](https://en.wikipedia.org/wiki/Cat%5F(Unix)), [grep](https://en.wikipedia.org/wiki/Grep) or [sed](https://en.wikipedia.org/wiki/Sed)). Here are a few
reasons that I find compelling. I&rsquo;m sure there are others.

1.  Search

    Whether searching in a single file or across files, when writing in plain
    text it is really quite simple to perform searches looking for a particular
    word or combination of words. If you know the syntax for writing [regular
    expressions](https://en.wikipedia.org/wiki/Regular%5Fexpression) the process is even easier. For example, from a directory of
    notes I can search for the occurrence of particular words or phrases and
    then move to each occurrence (even if they are in separate files)
    seamlessly, all using just a text editor ([emacs](https://www.gnu.org/software/emacs/)) and a simple search
    command (in this case using emacs to [interface](https://github.com/Wilfred/ag.el) with a search program called
    the [silver searcher](https://github.com/ggreer/the%5Fsilver%5Fsearcher) or &ldquo;ag&rdquo;).

2.  Version control

    I&rsquo;ve [written before](%7Bfilename%7D/blog/VersionControl.md)
    about how useful it is to have your writing under some sort of
    version control. Most modern text editors allow you to directly and
    easily interface with the vc of your choice in the course of an
    editing session. In the case of emacs there is the incomparable
    [Magit](https://github.com/magit/magit).

3.  Outlining & Notetaking

    Since their main use is manipulating text, text editors are unsurprisingly
    great for outlining and notetakeing. For example, Vim has a great outlining
    tool called [Voom](http://www.vim.org/scripts/script.php?script%5Fid=2657) and emacs has the incomparable [org-mode](http://orgmode.org). You can even use
    org-mode for keeping a [research wiki](http://stackoverflow.com/questions/26669280/setup-a-personal-wiki-in-emacs-org-mode) if that&rsquo;s you&rsquo;re thing. You can see a
    historian making use of vim&rsquo;s notetaking powers [here](http://wcm1.web.rice.edu/plain-text-citations.html).

4.  Flexibility

    Do you spend a lot of time on your computer at night and wish MS Word
    wasn&rsquo;t such a blaringly bright white application to work with? Do you wish
    you could automate or create keyboard shortcuts for repetitive tasks during
    editing? At least with the three major open source editors---[emacs](https://www.gnu.org/software/emacs/), [vim](http://www.vim.org),
    and [atom](https://atom.io)---this is relatively easy to do (or to learn to do). You can
    change how your editor looks, what kind of keyboard combinations do what,
    and automate simple (or even [complex](http://cestlaz.github.io/posts/using-emacs-15-macros/#.V8sXlTuMCYU)) tasks.

5.  Interface with other programs

    Though this connects with the second bullet point above, it is useful to
    emphasize. For example, I use [pandoc](http://pandoc.org/MANUAL.html) for converting all my academic writing
    and teaching materials. I also keep all my bibliographic material in a
    [bibtex](http://www.bibtex.org) document. My text editor has plug-ins which allow me to seamlessly
    interact with these programs and others, without having to leave the
    editor. I&rsquo;m also able to do all the upkeep for my various websites within
    the editor. I&rsquo;ve found this kind of uniform interface for everything to be
    extremely useful.

So try a text editor (or two or three) and see what you think (but really, use
[emacs](https://www.gnu.org/software/emacs/)). Write your next paper in it (or at least the notes for it) and see if
you find it helpful. There is always a [learning curve](http://www.terminally-incoherent.com/blog/wp-content/uploads/2006/08/curves.jpg) to take into account.
But after you get the hang of a particular editor you can decide whether it is
really a help or if you&rsquo;d rather just chuck it and go back to MS Word, Pages,
or [whatever worked for you](https://www.literatureandlatte.com/scrivener.php) before.
