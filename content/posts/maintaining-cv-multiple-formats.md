+++
title = "Maintaining a CV in Multiple Formats"
date = 2015-12-14
tags = ["cv", "pandoc", "geekery"]
draft = false
aliases = "/2015/maintaining-a-cv-in-multiple-formats"
type = "post"
toc = false
+++

Suppose you want to keep a CV accessible in PDF, html, and perhaps other
formats (e.g. docx). It&rsquo;s a pain to do them all individually and keep them in
sync. Here&rsquo;s one way to avoid that issue, though it has a bit of initial work
involved in setting everything up. What you want to do is keep your CV (or
really anything of that ilk that you want to have available in multiple
formats) in a [YAML](https://en.wikipedia.org/wiki/YAML) file and then use
[pandoc](http://pandoc.org) to convert the YAML file into whatever documents
you need. I got the idea from looking at
[this template](https://github.com/mrzool/cv-boilerplate) on Github.

What you want to do is keep the CV info in a YAML file like so:

```text
name: Immanuel Kant
address: Königsberg, Prussia
email: manny@copernicanrevolution.edu

AOS:
- Aesthetics, Epistemology, Ethics, Metaphysics, Philosophy of Mind, Political Philosophy

AOC:
- German Idealism, Philosophy of Religion

experience:
- years: 1770-1804
  employer: University of Königsberg
  job: Chair of Logic and Metaphysics
  city: Königsberg, DE
```

Using pandoc, you can then convert this into a variety of formats,
including HTML and PDF. The key is to create a template for every output
format that you need. For example, you might template your employment
history like so:

```text
$for(experience)$
  $experience.years$\\
  \textsc{$experience.employer$}\\
  \emph{$experience.job$}\\
  $experience.city$\\[.2cm]
$endfor$
```

Pandoc then feeds the YAML info to LaTeX for PDF typesetting. You can
see a sample [here](materials/images/preview.jpg).

With this method, you can keep your entire CV in a single YAML file and
easily generate a PDF, HTML, or some other format. For the full set of
templates for LaTeX and HTML, along with a `makefile` for easy
conversion, you can look at
[my repo](https://github.com/mclearc/cv-boilerplate.git) on Github.
