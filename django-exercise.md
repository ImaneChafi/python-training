# Django Exercise

Create a website for managing and displaying a collection of musical scores.
Each score will have a scan (PDF) and a transcription (MEI). It would be useful
to display both versions side-by-side to notice any transcription errors
that need fixing.

Example PDF and MEI files are available in the `scores` folder. PDFs were
obtained from [IMSLP](http://www.imslp.org) and MEI files were obtained from the
[Verovio website code](https://github.com/rism-ch/verovio/tree/gh-pages/examples/downloads).

## Stage 1
Create a static web page (no server-side code) that shows a score PDF file
side-by-side with the score's MEI file. Use the
[Verovio JavaScript toolkit](http://www.verovio.org/javascript.xhtml) to display
the MEI file.

Create a score index page with a list of links to view each score. The score page should accept the score name as a URL query parameter.

## Stage 2
Make the list of scores dynamic by adding Django. Add an ability to add and manage scores using the Django admin site.

## Stage 3
Add the ability to comment on scores. Each comment will have the fields 'author', 'text' and 'date'. Comments will be displayed on the score page, ordered by date (newest first).
