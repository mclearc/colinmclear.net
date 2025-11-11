+++
title = "Emacs Configurations"
date = 2019-10-22T20:26:00-04:00
tags = ["emacs", "geekery"]
draft = false
toc = false
type = "post"
+++

I spend a lot of time writing and editing. I use a [text editor](https://en.wikipedia.org/wiki/Text_editor) for this. I&rsquo;ve [written
before](https://www.colinmclear.net/posts/texteditor/) on why I think text editors are the best means for writing and editing one can
have. But part of why a text editor can be so important is that they tend to be
extensible or configurable (or both)---you can fit the editor to your needs. I use
[emacs](https://www.gnu.org/s/emacs/), which is perhaps the most configurable and extensible text editor there is.

But the configurability and extensibility can also cause frustration. Many people
don&rsquo;t want to think about configuring emacs. For such folks I strongly recommend the
configurations of [purcell](https://github.com/purcell/emacs.d) and [batsov (prelude)](https://github.com/bbatsov/prelude) and [many others](https://github.com/caisah/emacs.dz). I come originally
from using [vim](https://www.vim.org). If you prefer vim&rsquo;s [modal editing](https://en.wikipedia.org/wiki/Vi#Interface) style you should try [spacemacs](http://spacemacs.org) or
[doom-emacs](https://github.com/hlissner/doom-emacs) as a way of managing your configuration. Whatever you choose you should
look at some [sensible defaults](https://github.com/hrs/sensible-defaults.el) for configuring emacs.

I started using emacs via spacemacs about three years ago and fairly quickly migrated
to developing [my own config](https://github.com/mclear-tools/dotemacs). There tend to be [three styles of config](https://emacs.stackexchange.com/questions/2520/organize-the-content-of-emacs-d-init-el-and-emacs-d): a [single
`init.el`](http://milkbox.net/note/single-file-master-emacs-configuration/) file with all the elisp necessary to run emacs as you like it; a [&ldquo;literate&rdquo;
config](https://harryrschwartz.com/2016/02/15/switching-to-a-literate-emacs-configuration) using [org-mode](http://orgmode.org) to organize and then &ldquo;tangle&rdquo; the file using [org-babel](http://orgmode.org/worg/org-contrib/babel/) (you can
find another helpful discussion of this method [here](http://stackoverflow.com/questions/17416738/emacs-initialization-as-org-file-how-can-i-get-the-right-version-of-org-mode)); or a [&ldquo;modular&rdquo; file](http://ergoemacs.org/emacs/organize_your_dot_emacs.html) in which
the `init.el` file loads separate &ldquo;libraries&rdquo; of code.

For configurations of any reasonable level of complexity I think the single file
approach is ill-conceived.

The literate config using org is great for two reasons. First, it is extremely simple
to organize one&rsquo;s config and comment significantly on every part. This is especially
helpful when one is just starting out with elisp so that one can verbosely comment on
how the various elisp code one uses works to achieve the desired results. Second,
literate configs can be great learning sources for others. If you use a code
repository like Github then you can display the org file natively. This makes
browsing someone&rsquo;s emacs config very easy (especially when they include a [table of
contents](https://github.com/mclear-tools/dotemacs/blob/master/config.org#table-of-contents)).

But a literate config can have its [down sides](https://valignatev.com/posts/emacs-org-config/). In addition to the issues discussed in
that link, some of which may be resolvable, I found a few key problems. First, if you
like to run the latest org-mode then you have to work around emacs&rsquo; built-in org
version, which can be a [pain in the neck](https://www.reddit.com/r/emacs/comments/5sx7j0/how_do_i_get_usepackage_to_ignore_the_bundled/).

Second, you need to load org mode when you generate, or want to edit, your config
file. This can lead to slower load times in general, and if you have a large config,
it can take several seconds before you can start editing (some people might not mind
this but it tends to annoy me). I also think that, beyond the issue with start-up times,
the fact that someone new to emacs would have to add a further layer of abstraction
(i.e. org-mode and babel) to generate their init.file might be confusing.

Third, I find it a bit easier to keep modular files (e.g. separate files for
keybindings, for configuring specific packages, or for a theme, etc.) under version
control than to keep a single monolithic configuration file under vc.

Fourth, I often accidentally deleted or moved parts of my org config unintentionally,
due to editing when at least some headlines were collapsed. There are [ways to avoid
this](https://emacs.stackexchange.com/questions/2086/org-mode-prevent-editing-of-text-within-collapsed-subtree), but it leads to some unnecessary problems.

Fifth, and perhaps more subjectively than the above, I find it much easier to wrap my
head around separate modules when it comes to thinking about what I want to tweak or
change, or looking at a git log of what I have tweaked or changed.

Sixth, dealing with problems (debugging) is harder. Often you&rsquo;ll need to use the
tangled source for debugging and then go back and make changes in the org mode file.
Also, the links from **Help** and **Debugger** will jump to the tangled source rather than
the org file, which is what you actually need to edit. Also, if there are problems
you might need to bisect your org file (essentially commenting out parts of it until
you figure out what is wrong). I find it much easier to simply load or not load
specific modules from the init file.

Seventh, it is also easier to edit files in lisp mode than edit an org mode
containing lisp syntax.

Now, a modular config is perhaps not as immediately readable as a literate one,
but it _is_ easy to comment as necessary on one&rsquo;s code, and you can use packages
like the built-in outline library, with `(outline-minor-mode)` and `(outline-cycle)`
to allow for easy folding and cycling through levels of visibility just as with
org. I also use a few custom functions for navigating my setup files, which
makes things at least as easy to find as they were in my old literate config (in
some ways I find my current modular config even easier to search through). You
can see the setup of outline mode [here](https://github.com/Lambda-Emacs/lambda-emacs/blob/286860f01842a3be14d03fa99cc06942f6d03045/init.el#L278) and the search functions [here](https://github.com/Lambda-Emacs/lambda-emacs/blob/286860f01842a3be14d03fa99cc06942f6d03045/lambda-library/lambda-setup/lem-setup-functions.el#L48).

EDITED: Friday, November 18 2022 to update description of outline and search functions.
