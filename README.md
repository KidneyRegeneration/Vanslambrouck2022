Repository for code related to Vanslambrouck et al paper under review



<H3>Image Analysis</H3>

The image-analysis folder contains data and code used to quantify organoid tissue patterning within the proximity of IWR-soaked, or control beads. Analysis can be replicated by running the two included Jupyter Notebooks in order. An environment yml file is included to replicate the Conda Python environment used for analysis.

The first step in the analysis '01 read data and annotate' involves loading each image in sequence and manually annotating beads using the Napari viewer. As the output will vary between users we have included the annotation masks used for analysis (files 'labels_01.tif, labels_02.tif.....etc'). All output, including csv summary data and plots used for figures can be re-created by running the second notebook '02 analysis'.

