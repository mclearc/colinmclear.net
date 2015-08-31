title: Maintain a CV in HTML and PDF
author: Colin McLear
date: 2015-07-23
tags: latex, geekery, markdown

Most people keep a CV or Resume on their website. It's nice to have it in
both html and pdf; the first for easy web viewing and the second for easy
distribution. The problem is that maintaining two versions of your CV can be a
pain. There are ways around this though. One method is to maintain a single
master version in a markdown file and then convert that to pdf and html. There
are [lots](http://mszep.github.io/pandoc_resume/) of [different
implementations](https://github.com/there4/markdown-resume) of [this
idea](http://barraq.github.io/pandoc-moderncv/).  

One alternative to going the markdown conversion route is to convert the [pdf
to html](http://coolwanglu.github.io/pdf2htmlEX/). The advantage of this is
that it is rather trivial to keep the pdf and html versions in sync. It also
means that the potentially more intricate stylings of the pdf version can be
easily represented in html. The two downsides that I see to this method are that
the html isn't responsive and so doesn't scale any better than pdf on a small
screen, and that the html file is comparatively large. This doesn't seem to
matter too much for modern web browsers though, so I'll probably stick with it
for now. 


