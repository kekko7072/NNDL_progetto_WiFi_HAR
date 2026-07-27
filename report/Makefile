# Build the NNDL project report with pdflatex + bibtex.
# Works with GNU Make on macOS (MacTeX/BasicTeX) and on Windows
# (MiKTeX or TeX Live, with make from Git Bash, MSYS2, winget, or choco).

MAIN       := report
LATEX      := pdflatex
BIBTEX     := bibtex
LATEXFLAGS := -interaction=nonstopmode -halt-on-error

TEXSRC := $(MAIN).tex intro.tex related.tex model.tex results.tex conclusions.tex
FIGS   := $(wildcard figures/*.png figures/*.pdf figures/*.jpg)

# On Windows GNU Make may run under cmd/PowerShell, where `rm` does not exist.
ifeq ($(OS),Windows_NT)
  RM := cmd /C del /F /Q
else
  RM := rm -f
endif

.PHONY: all clean distclean

all: $(MAIN).pdf

$(MAIN).pdf: $(TEXSRC) biblio.bib IEEEtran.cls $(FIGS)
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex
	$(BIBTEX) $(MAIN)
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex

clean:
	$(RM) $(MAIN).aux $(MAIN).bbl $(MAIN).blg $(MAIN).log $(MAIN).out $(MAIN).synctex.gz

distclean: clean
	$(RM) $(MAIN).pdf
