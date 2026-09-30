---
title: "Nobody Wrote This Down"
layout: page
description: "Nobody Wrote This Down: seven years of the MicroBinfie podcast, by Nabil-Fareed Alikhan, Lee Katz and Andrew J. Page. Free to read as EPUB, PDF and more; paperback on Amazon."
book:
  name: "Nobody Wrote This Down"
  subtitle: "Seven years of the MicroBinfie podcast"
  authors: ["Nabil-Fareed Alikhan", "Lee Katz", "Andrew J. Page"]
  year: "2026"
  cover: /assets/book/cover.jpg
# Book files are assets of this GitHub release, which counts every download (see
# scripts/book_downloads.sh). A new edition is a new release: change this one line.
downloads: https://github.com/MicroBinfie/MicroBinfie.github.io/releases/download/book-2026-09-29
amazon:
  asin: B0HG3VN36K
  url: https://www.amazon.com/dp/B0HG3VN36K
  # Set to true once the Amazon listing is live; until then the page says "coming soon".
  live: false
---

<img src="{{ '/assets/book/cover.jpg' | relative_url }}" alt="Cover of Nobody Wrote This Down: Seven years of the MicroBinfie podcast, by Nabil-Fareed Alikhan, Lee Katz and Andrew J. Page" width="300" style="float: right; margin: 0 0 1em 1.5em; max-width: 45%;">

## Seven years of the MicroBinfie podcast

*by Nabil-Fareed Alikhan, Lee Katz and Andrew J. Page*

**There is no manual.** The largest *Listeria* cluster anyone had ever seen turned out to be the
blood agar. German police spent sixteen years hunting a woman whose DNA was at murder scene after
murder scene; she worked in the factory that made the swabs. Neither was a sequencing failure.

Almost nothing you need to know to do this work is written down. You learn that a file of
nothing but capital letters in the quality string is old data lying to you, and you learn it
because somebody mentions it in a corridor — not because you read it anywhere. The trouble is
that most bioinformaticians don't have a corridor.

For seven years, three of them ran a podcast about it instead. This book is a hundred and
fifty-six episodes of MicroBinfie rearranged into something you can read: the file formats
nobody designed, the contamination that looked like a discovery, the assembler that stops exactly
where the interesting thing is, why nobody can agree what a species is, and a national pandemic
response stood up in a fortnight on five years of groundwork nobody had noticed at the time.

It is also a record of being wrong in public. Where somebody said a thing on air that the
following years demolished, the wrong version is still there and the correction follows it.

<div style="clear: both;"></div>

## Read it free

| Format | Best for | Size |
|---|---|---|
| [EPUB]({{ page.downloads }}/nobody-wrote-this-down.epub){: data-book-format="epub"} | E-readers, phones and tablets; Apple Books, Kobo, Google Play Books, and Kindle via Send to Kindle | 333&nbsp;KB |
| [PDF, paperback layout]({{ page.downloads }}/nobody-wrote-this-down-6x9.pdf){: data-book-format="pdf-6x9"} | Reading on screen exactly as printed (6 × 9 in, 188 pages) | 980&nbsp;KB |
| [PDF, A4]({{ page.downloads }}/nobody-wrote-this-down-a4.pdf){: data-book-format="pdf-a4"} | Printing at home, or annotating | 960&nbsp;KB |
| [PDF, phone]({{ page.downloads }}/nobody-wrote-this-down-phone.pdf){: data-book-format="pdf-phone"} | A narrow page sized for a phone screen | 1.1&nbsp;MB |
| [PDF, large print]({{ page.downloads }}/nobody-wrote-this-down-large-print.pdf){: data-book-format="pdf-large-print"} | 17-point type for easier reading | 1.1&nbsp;MB |
| [Web page]({{ '/assets/book/nobody-wrote-this-down.html' | relative_url }}){: data-book-format="web"} | Reading in a browser, one long page | 530&nbsp;KB |
| [Plain text]({{ page.downloads }}/nobody-wrote-this-down.txt){: data-book-format="txt"} | Anything at all; screen readers, slow connections | 500&nbsp;KB |

## Buy the paperback

{% if page.amazon.live %}
**[Buy the paperback on Amazon.com]({{ page.amazon.url }})** — 6 × 9 in, 188 pages.
{% else %}
**The paperback on Amazon.com is coming soon** (ASIN {{ page.amazon.asin }}).
{% endif %}

## About this book

The guests, and the colleagues they talk about, appear in the book under pseudonyms; the episodes
themselves, and the [episode pages on this site]({{ '/pages/Episodes.html' | relative_url }}),
are where to hear them in their own words. Quoted speech in the book is verbatim from the
recordings, and every episode behind each chapter is listed in its Note on Sources.

<script>
  /* Count book downloads in Google Analytics as one 'book_download' event with the format, so
     the EPUB and web edition are counted too (GA's automatic tracking only sees PDF and TXT).
     gtag exists only on the published site; locally this does nothing. */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[data-book-format]');
    if (!a || typeof gtag !== 'function') return;
    gtag('event', 'book_download', {
      format: a.getAttribute('data-book-format'),
      file_name: a.href.split('/').pop(),
      link_url: a.href,
      transport_type: 'beacon'
    });
  });
</script>

