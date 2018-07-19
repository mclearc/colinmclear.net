+++
title = "Moving to Hugo"
date = 2018-07-19T10:49:00-04:00
tags = ["hugo", "pelican", "website"]
draft = false
toc = false
type = "post"
+++

Another summer, another excuse to tinker with my wesbite. I&rsquo;ve used [pelican](https://blog.getpelican.com), a
python [static site generator](https://en.wikipedia.org/wiki/Web%5Ftemplate%5Fsystem#Static%5Fsite%5Fgenerators), to run this website for nearly six years. It&rsquo;s a
great tool. But I dislike python [dependency hell](https://en.wikipedia.org/wiki/Dependency%5Fhell), and pelican is a bit slow.
So I&rsquo;ve looked elsewhere. [Hugo](https://gohugo.io) is blazing fast, has a thriving community,
decent templates, and a downloadable binary that you can get via [homebrew](https://brew.sh). No
more dependency management! Also important for me (as an [emacs](https://www.gnu.org/software/emacs/) user), there is
a great [org-mode](https://orgmode.org) exporter---[ox-hugo](https://ox-hugo.netlify.com)---that lets me easily generate the web
content from an org-file. On the whole I&rsquo;ve been very happy with the move.

I&rsquo;ve also changed hosting from github to [Netlify](https://netlify.com), which provides dead-simple
hosting. All you do is point it at a git repository (which remains on [Github](https://github.com/mclearc))
and tell it what commands to run and it provides continuous deployment. So
whenever I make a change to the site and push that change to [my repository](https://github.com/mclearc/colinmclear.net) on
Github Netlify automatically regenerates the site. Very cool.
