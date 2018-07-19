+++
title = "Writing a syllabus for multiple formats"
date = 2016-07-17
tags = ["workflows", "teaching"]
draft = false
toc = false
type = "post"
+++

I find it generally preferable to keep information I use for teaching in a
format that allows for different styles of presentation. I&rsquo;ve written [before](http://colinmclear.net/2015/maintaining-a-cv-in-multiple-formats)
about how one might keep a CV in a yaml document that outputs to a variety of
different possible formats using [pandoc](http://pandoc.org/README.html). I also use a similar system for
syllabi.

The basic idea is to keep your syllabus in a yaml file and export it to html,
pdf, or rtf using a makefile. The nice thing about this is that you can, e.g.,
hand out a nicely formatted PDF (or printout) of your syllabus at the
beginning of the semester, and then keep a continually updated version on your
course website as HTML, all without having to have multiple documents that
you&rsquo;re editing. You can find the basic template on [Github](https://github.com/mclear-teaching-projects/syllabus%5Ftemplate) and an example from
my [PHIL 101 class](http://phil101.colinmclear.net), also on [Github](https://github.com/mclear-teaching-projects/phil101/tree/master/Syllabus%5FIntro).

The html and latex templates are pretty basic, but serviceable. You should be
able to easily modify them to fit your particular needs.
