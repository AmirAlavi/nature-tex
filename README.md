# nature-tex
LaTeX template and build code for a Nature style research article submission

# Features
* Keeps your tex organized into separate `main.tex` and `sup.tex` files
* Preamble kept separate in `naturetex.sty` for cleaner tex code
* Allows you to use a separate bibliography file with `cite` commands as usual
* Generates the final single `.tex` file for you, as expected by Nature journals
* **Works in shared editors like Overleaf**

# Prerequisites
* Python
* A LaTeX distribution (You'll need `pdflatex`, `biber`, and `bibtex` in your path)

# Usage
1. Clone this repository
2. `$ cd nature-tex`
3. `$ make`
4. (Optional) You can use `$ make clean` to remove the generated temporary files.

This should have generated two folders, `submit` and `proof`. Inspect those to make sure everything is working.

```
proof/      # CONVENIENCE FILES, DO NOT SUBMIT TO NATURE
  main.pdf  # The the main manuscript as a pdf, with the figures included, for easy reading
  
submit/     # FILES READY FOR SUBMISSION TO NATURE
  main.tex  # The main manuscript tex, all as a single file, no figures
  sup.pdf   # The supplement as a pdf
```

Now, edit `tex/main.tex`, `tex/sup.tex`, and `tex/bibliography.bib` to your heart's desire, and replace the dummy tex with real science!
## TeX rules
To allow proper cross referencing between the main manuscript and supplement, you must use the labels specified in `cross_refs.json`

You may edit `cross_refs.json` to add/remove any keys you might want (e.g. Notes, Box, etc)

Each (key,value) pair in `cros_refs.json` specifies a label type which will be kept track of and a full string which will be printed. If you use any of those labels in either the main manuscript or supplement, the python code will correctly keep track of it and replace it with a correctly numbered string.

For example:
```
% main.tex
\label{fig:my_cool_fig}
Hey, check out this result in \ref{fig:my_cool_fig} and \ref{sup.fig:my_extra_fig}!
% sup.tex
\label{sup.fig:my_extra_fig}
This extra fig is kinda like \ref{fig:my_cool_fig}.
```
Will be processed into:
```
% main.tex
\label{fig:my_cool_fig}
Hey, check out this result in Figure 1 and Supplementary Figure 1!
% sup.tex
\label{sup.fig:my_extra_fig}
This extra fig is kinda like Figure 1.
```
