# NNDL_progetto_WiFi_HAR

Human Activity Recognition from Wi-Fi CSI Doppler spectrograms — course project
for Neural Networks and Deep Learning.

## Compiling the report locally

The LaTeX report lives in `report/` and builds with `pdflatex` + `bibtex`
(the `IEEEtran.cls` class file is bundled, no extra class installation needed).
A `Makefile` automates the full sequence:

```sh
cd report
make            # builds report.pdf (pdflatex -> bibtex -> pdflatex x2)
make clean      # removes auxiliary files (.aux, .bbl, .log, ...)
make distclean  # also removes report.pdf
```

### macOS

1. Install a TeX distribution, e.g. [MacTeX](https://www.tug.org/mactex/):

   ```sh
   brew install --cask mactex-no-gui
   ```

   (or `brew install --cask basictex` for a minimal install — you may need
   `sudo tlmgr install collection-latexextra` for a few packages).

2. `make` ships with the Xcode Command Line Tools (`xcode-select --install`).

3. Build:

   ```sh
   cd report && make
   ```

### Windows

1. Install a TeX distribution: [MiKTeX](https://miktex.org/download) or
   [TeX Live](https://www.tug.org/texlive/). MiKTeX auto-installs any missing
   packages on the first compile. Make sure `pdflatex` and `bibtex` are on
   your `PATH` (the installers do this by default).

2. Install GNU Make (any one of these):
   - `winget install ezwinports.make`
   - `choco install make`
   - MSYS2: `pacman -S make`
   - or use the `make` bundled with Git Bash / MSYS2 environments.

3. Build from Git Bash, PowerShell, or cmd:

   ```sh
   cd report
   make
   ```

The output is `report/report.pdf`.
