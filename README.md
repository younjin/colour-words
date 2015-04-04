colour-words
============

This repo generates [force-directed graphs](http://bl.ocks.org/mbostock/4062045) for basic colour words in a given language.
Nodes denote the basic colours, and edges between nodes signify that the connected nodes are represented by the same basic colour word.

Instructions:
* Create a local copy of this repo.
* Download a CSV version of [the BCT spreadsheet](goo.gl/LZe7wi) into the same directory.
* Rename the CSV file to be words.csv.
* Run 'make', then 'python -mSimpleHTTPServer' in the current directory using Terminal.
* Open 'localhost:8000/#' in your favourite browser.
