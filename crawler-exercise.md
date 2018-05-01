# Web Crawler Exercise

## Stage 1
Create a Python program that crawls a web page by downloading the page and all HTML pages that are linked from that page. The crawler should continue following links recursively, up to a certain depth.

Command-line argument can include:
 - start URL
 - maximum crawling depth
 - page download timeout
 - whether to limit crawling only to the original page’s domain

HTTP errors should be recorded.
Progress should be reported on the command line.

## Stage 2
Speed up the crawler by downloading pages concurrently. A command line argument should specify the max concurrency.

## Stage 3
Add to the crawler the ability to resume an interrupted crawl. The crawler should not re-download pages that have not been modified since the last update.

## Stage 4
Optionally download images as well, up to a certain file size.
Generate an HTML report at the end of the crawling.
