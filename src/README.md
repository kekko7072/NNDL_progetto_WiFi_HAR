# Human Activity Recognition from Wi-Fi CSI Doppler Spectrograms

Neural Networks and Deep Learning project.

- Marco Carraro (baseline pipeline)
- Francesco Vezzani (Supervised Contrastive Learning extension)

This folder contains a single, self-contained notebook,
**`NNDL_project_Carraro_Vezzani.ipynb`**, which reproduces every number and
figure discussed in the project report: the baseline CNN, the sliding-window
front-end, multi-antenna decision fusion, and the Supervised Contrastive
Learning (SupCon) extension with linear probe, fine-tuning and t-SNE
visualization.

## How to run it

The notebook is written for **Google Colab** and downloads the dataset by
itself, so no manual setup is required beyond opening it and running the
cells in order.

1. Upload `NNDL_project_Carraro_Vezzani.ipynb` to Google Colab (or open it
   directly from Google Drive / GitHub).
2. Set the runtime as described below (**Runtime > Change runtime type**).
3. Run the cells from top to bottom (**Runtime > Run all**).

No dataset files need to be uploaded manually and no paths need to be edited.

## Runtime settings used

These are the settings we used to produce the results in the report
(**Runtime > Change runtime type** in Colab):

| Setting            | Value                    |
|---------------------|--------------------------|
| Runtime type         | Python 3                 |
| Hardware accelerator | **T4 GPU**               |
| High-RAM             | **on**                   |
| Runtime version      | Latest (recommended)     |

A GPU is required for training in reasonable time, and the **High-RAM**
option is required, not optional: the sliding-window front-end (stride 30,
~91% overlap) materializes the whole windowed dataset in memory, which takes
roughly 20 GB of RAM at steady state and peaks around 31 GB while it is being
built. Without High-RAM, Colab's standard runtime (~12 GB) will run out of
memory in Section 2 of the notebook.

If you don't have access to a High-RAM T4 runtime, you can still run the
notebook by raising `STRIDE` in Section 2 (e.g. back to `STRIDE = 340` for
non-overlapping windows), at the cost of far fewer training windows and the
lower accuracy numbers reported for that regime.


## Expected running time

On a T4 GPU with High-RAM enabled, a full top-to-bottom run takes roughly
45-60 minutes: a few minutes for the baseline (dataset download/build plus
~27 training epochs), and the bulk of the time for the SupCon contrastive
pre-training (30 epochs, ~75 s/epoch) plus the optional fine-tuning stage.

## Reproducibility

The notebook fixes `seed = 0` (NumPy and PyTorch) at the start and again
before the contrastive section. Minor run-to-run differences are still
possible on GPU due to non-deterministic CUDA kernels; the numbers in the
report were produced by a single run under the settings above.
