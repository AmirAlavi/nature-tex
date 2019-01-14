SHELL=/bin/bash
SRC_TEX=tex
SRC_PYTHON=python
SUBMIT_DIR=submit
PROOF_DIR=proof

all: submission_main.tex submission_sup.pdf
	mkdir -p $(SUBMIT_DIR)
	cp submission_sup.pdf $(SUBMIT_DIR)/sup.pdf
	cp submission_main.tex $(SUBMIT_DIR)/main.tex
	mkdir -p $(PROOF_DIR)
	cp proof_main.pdf $(PROOF_DIR)/main.pdf

submission_sup.pdf: submission_sup.tex
	pdflatex submission_sup.tex
	biber submission_sup
	pdflatex submission_sup.tex

submission_main.tex proof_main.pdf: processed_main.tex
	cp $(SRC_TEX)/naturetex.sty .
	cp $(SRC_TEX)/bibliography.bib .
	# Makes proof_main.pdf
	pdflatex processed_main.tex
	bibtex processed_main
	python $(SRC_PYTHON)/combine_tex.py # Puts bib and pramble into main tex file
	pdflatex proof_main.tex
	pdflatex proof_main.tex
	# Makes submission_main.tex
	python $(SRC_PYTHON)/remove_figs.py # Comments out figures in tex file

processed_main.tex submission_sup.tex: $(SRC_TEX)/main.tex $(SRC_TEX)/sup.tex
	python $(SRC_PYTHON)/ref_converter.py

clean:
	rm -f *.{ps,pdf,log,aux,out,dvi,bbl,blg,bcf,run.xml}
	rm -f processed_main.tex
	rm -f submission_main.tex
	rm -f proof_main.tex
	rm -f submission_sup.tex
	rm -f naturetex.sty bibliography.bib # Originals in SRC_TEX remain
