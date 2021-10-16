+++
title = "Teaching Notes, Slides, & Handouts"
date = 2021-10-15T22:50:00-04:00
tags = ["emacs", "geekery", "teaching", "workflows"]
draft = false
toc = false
type = "post"
+++

I&rsquo;ve recently created some functions in emacs to make exporting notes, slides, and
handouts somewhat easier. I do all this using [org-mode](https://orgmode.org). I figure there are at least a
few other people who might find this workflow of interest so I though I would
document it here (it will also serve as a document of how all this works in case I
forget in the future).

I want to be able to turn something like the following:

{{< figure src="/ox-hugo/Screen Shot 2021-10-16 at 12.34.44 AM.png" >}}

Into a nice looking set of PDF notes like this:

{{< figure src="/ox-hugo/Screen Shot 2021-10-16 at 12.37.50 AM.png" >}}

Or a set of slides like this:

{{< figure src="/ox-hugo/Screen Shot 2021-10-16 at 12.40.53 AM.png" >}}


## Notes {#notes}

Basically, I want to be able to export from a file or an org-mode tree in a few
different ways. First, I might want to export from my org files a set of notes that
I&rsquo;ll use during lecture and share with students. I use [org-roam](https://github.com/org-roam/org-roam) to keep all my notes
and I have some custom functions (adapted from [here](https://github.com/minad/consult/wiki/hrm-notes)) to search them. I&rsquo;ll put all
these together in an org file using the `#+INCLUDE:` directive (see [here](https://orgmode.org/manual/Include-Files.html)). This lets me
collect notes from a bunch of different places into one set. I can select specific
files, specific headings, even specific lines. I&rsquo;ll then export using one of the
following functions (depending on context):

```emacs-lisp
(defun cpm/org-export-pdf-notes ()
"Export subtree of notes to PDF file. Note uses a distinctive quote style."
(interactive)
(let ((org-latex-default-quote-environment "quote-b"))
  (org-narrow-to-subtree)
  (save-excursion
    (goto-char (point-min))
    (org-latex-export-to-pdf t t nil nil '(:latex-class "org-notes")))
  (widen)))

(defun cpm/org-export--file-pdf-notes ()
  "Export file notes to PDF file. Note uses a distinctive quote style."
  (interactive)
  (let ((org-latex-default-quote-environment "quote-b"))
    (save-excursion
      (goto-char (point-min))
      (org-latex-export-to-pdf t nil nil nil '(:latex-class "org-notes")))))
```

These functions require that you create the following custom [org-latex class](http://doc.endlessparentheses.com/Var/org-latex-classes.html):

```emacs-lisp
;; Export org to a nice looking PDF file
(with-eval-after-load 'ox-latex
  (add-to-list 'org-latex-classes
               '("org-notes"
                 "\\documentclass[12pt]{article}
                  [NO-DEFAULT-PACKAGES]
                  [EXTRA]
                  \\input{/Users/roambot/.emacs.d/.local/custom-org-latex-classes/notes-setup-file.tex}"
                 ("\\section{%s}" . "\\section*{%s}")
                 ("\\subsection{%s}" . "\\subsection*{%s}")
                 ("\\subsubsection{%s}" . "\\subsubsection*{%s}")
                 ("\\paragraph{%s}" . "\\paragraph*{%s}")
                 ("\\subparagraph{%s}" . "\\subparagraph*{%s}"))))
```

This runs an asynchronous process to produce a nice looking PDF of the relevant
notes. This does also require a specific set of latex packages that I set in another
file I call &ldquo;notes-setup-file.tex&rdquo;. I&rsquo;ll put that at the end of the post.


## Slides & Handouts {#slides-and-handouts}

The other thing I often need to do is create slides for a lecture or talk, as well as
a handout. I like beamer with a custom version of the [Metropolis](https://github.com/matze/mtheme) theme. I don&rsquo;t want
to have to create separate files for the slides and for the handout. I also don&rsquo;t
want to just give a handout that is a set of pictures of the slides. Terrible! So
here&rsquo;s what I do instead.

First, I have a set of custom classes:

```emacs-lisp
;; Presentation slides (with notes)
(with-eval-after-load 'ox-latex
(add-to-list 'org-latex-classes
             '("beamer-presentation"
               "\\documentclass[presentation]{beamer}
                [NO-DEFAULT-PACKAGES]
                [PACKAGES]
                \\usepackage{pgfpages}
                [EXTRA]
                \\setbeameroption{show notes on second screen=right}
                \\setbeamertemplate{note page}{\\pagecolor{yellow!5}\\insertnote}
                \\input{/Users/roambot/.emacs.d/.local/custom-org-latex-classes/unl-beamer-preamble.tex}"
               ("\\section{%s}" . "\\section*{%s}")
               ("\\subsection{%s}" . "\\subsection*{%s}")
               ("\\subsubsection{%s}" . "\\subsubsection*{%s}"))))


;; Making handouts for slides that don't just look like slides
(with-eval-after-load 'ox-latex
(add-to-list 'org-latex-classes
             '("beamer-handout"
               "\\documentclass[12pt]{article}
                [NO-DEFAULT-PACKAGES]
                [EXTRA]
                \\input{/Users/roambot/.emacs.d/.local/custom-org-latex-classes/handout-setup-file.tex}"
               ("\\section{%s}" . "\\section*{%s}")
               ("\\subsection{%s}" . "\\subsection*{%s}")
               ("\\subsubsection{%s}" . "\\subsubsection*{%s}")
               ("\\paragraph{%s}" . "\\paragraph*{%s}")
               ("\\subparagraph{%s}" . "\\subparagraph*{%s}"))))
```

Note that these classes uses a set of custom setup files for the latex packages,
including a custom quote environment (&ldquo;quote-b&rdquo;) to show quoted passages with a
left-side bar and with a slightly shaded background. I&rsquo;ll put a link to the tex files
where all of this is specified at the end of this post.

I also like to have the slides be primarily texts or main ideas, while my notes are
in a separate area, which will show up on the handout but not the slides. I use a src
enviroment called &ldquo;notes&rdquo; for this and the following code for filtering everything
correctly on export.

```emacs-lisp
;; Originally used for exporting notes in reveal.js
;; See
;; https://joonro.github.io/Org-Coursepack/Lectures/04%20Creating%20Content%20for%20Slides%20and%20Handouts.html#speaker-notes

(defun string/starts-with (string prefix)
  "Return t if STRING starts with prefix."
  (and (string-match (rx-to-string `(: bos ,prefix) t) string) t))

(defun my/process-NOTES-blocks (text backend info)
  "Filter NOTES special blocks in export."
  (cond
   ((eq backend 'rst)
    (if (string/starts-with text ".. NOTES::") ""))
   ((eq backend 'html)
    (if (string/starts-with text "<div class=\"NOTES\">") ""))
   ((eq backend 'beamer)
    (let ((text (replace-regexp-in-string "\\\\begin{NOTES}" "\\\\note{" text)))
      (replace-regexp-in-string "\\\\end{NOTES}" "}" text)))
   ))

(eval-after-load 'ox '(add-to-list
                       'org-export-filter-special-block-functions
                       'my/process-NOTES-blocks))
```

Then I have a set of functions for exporting the relevant files asynchronously.

```emacs-lisp
;; Org export to slides w/notes
(defun cpm/org-export-beamer-presentation ()
  (interactive)
  (let ((org-export-exclude-tags '("handout")))
    (save-excursion
      (goto-char (point-min))
      (org-beamer-export-to-pdf nil t nil nil '(:latex-class "beamer-presentation")))))

;; I got the tag based selective export idea from J Kitchin
;; https://kitchingroup.cheme.cmu.edu/blog/2013/12/08/Selectively-exporting-headlines-in-org-mode/
(defun cpm/org-export--file-beamer-presentation ()
  (interactive)
  (let ((org-export-exclude-tags '("handout")))
    (save-excursion
      (goto-char (point-min))
      (org-beamer-export-to-pdf t nil nil nil '(:latex-class "beamer-presentation")))))


;; Org export file to handout
(defun cpm/org-export-beamer-handout ()
"Export subtree content to PDF handout. Handout uses a distinctive quote style."
(interactive)
(let ((org-latex-default-quote-environment "quote-b")
      (org-export-exclude-tags '("slides")))
  (org-narrow-to-subtree)
  (save-excursion
    (goto-char (point-min))
    (org-latex-export-to-pdf t t nil nil '(:latex-class "beamer-handout")))
  (widen)))

(defun cpm/org-export--file-beamer-handout ()
  "Export file content to PDF handout. Handout uses a distinctive quote style."
  (interactive)
  (let ((org-latex-default-quote-environment "quote-b")
        (org-export-exclude-tags '("slides")))
    (save-excursion
      (goto-char (point-min))
      (org-latex-export-to-pdf t nil nil nil '(:latex-class "beamer-handout")))))
```

The nice thing about this is I can use a single file and export a nice looking set of
slides and a good handout, where the handout can also include extra notes or passages
via the tag filter on export.

For a look at the org-latex-classes you can check out the [github repository](https://github.com/mclearc/org-latex-classes). You can
also look at the above functions as they appear in my [dotfiles](https://github.com/mclear-tools/dotemacs/blob/master/setup-config/setup-teaching.el).
