[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pitmonticone/AppliedDynamicalSystems/master)
[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)]()
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pitmonticone/AppliedDynamicalSystems/blob/master)
[![nbviewer](https://github.com/jupyter/design/blob/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/pitmonticone/AppliedDynamicalSystems/)

# Software

## Languages 

### R

* [Download](https://www.r-project.org)
* [IDE](https://rstudio.com)
* [Kaggle Simulations](https://www.kaggle.com/simulations)

### Python

* [Download](https://julialang.org)
* [IDE](https://rstudio.com)

### Julia

* [Download](https://julialang.org)
* [IDE](https://junolab.org/)
* [MDE](https://juliadynamics.github.io/JuliaDynamics/)
* [Packages](https://pkg.julialang.org/)
* [YouTube](https://www.youtube.com/user/JuliaLanguage)
* [GitHub](https://github.com/JuliaLang/julia)
* [Learning Resources](https://julialang.org/learning/)
* [Academy](https://juliaacademy.com)
* [Cheat Sheet](https://juliadocs.github.io/Julia-Cheat-Sheet/)
* [Style Guide](https://docs.julialang.org/en/v1/manual/style-guide/index.html)
* [Practical Julia](https://github.com/PraCTES/MIT-PraCTES/tree/master/demos): Julia vs. Python vs. Matlab.
* [JuMPTutorials.jl](https://github.com/jump-dev/JuMPTutorials.jl)

* [A Deep Introduction to Julia for Data Science and Scientific Computing](http://ucidatascienceinitiative.github.io/IntroToJulia/).

### NetLogo
* [Download](http://ccl.northwestern.edu/netlogo)
* [User Manual](https://ccl.northwestern.edu/netlogo/docs/)
* [Modelling Commons](http://modelingcommons.org/)
* [OpenABM](http://www.openabm.org/)

### Web 

* [Empirica](https://empirica.ly): open-source JavaScript framework for running multiplayer interactive experiments and games in the browser. It was created to make it easy to develop and iterate on sophisticated designs in a statistically sound manner, and offers a unique combination of power, flexibility, and speed.
    * Abdullah Almaatouq et al. [Empirica: a virtual lab for high-throughput macro-level experiments](https://arxiv.org/pdf/2006.11398.pdf). *arXiv pre-print* (2020). 
    
## Tutorials 

* Carlotta Dotto. [How to use network analysis to explore social media and disinformation](https://firstdraftnews.org/latest/how-to-use-network-analysis-to-explore-social-media-and-disinformation/). (2020).

## Tools 

### Data Visualization 

[`pylustrator`](https://pylustrator.readthedocs.io/en/)

### Network Analysis 

#### Julia 

* [`JuliaGraphs`](https://juliagraphs.org): Graph analysis Julia packages.

#### Python 

* [`networkx`](https://networkx.github.io): network analysis and visualization (Python)
* [`graph-tool`](https://graph-tool.skewed.de): network analysis and visualization (Python, C/C++)

#### R 

* [`igraph`](https://igraph.org/redirect.html): network analysis tools (Python, C/C++, R, Mathematica)

### Network Visualization 

* [Gephi](https://gephi.org): network visualization software
* [Cytoscape](https://cytoscape.org): platform for visualizing complex networks and integrating these with any type of attribute data

* [`netwulf`](https://github.com/benmaier/netwulf):  offers an ultra-simple API for reproducible interactive visualization of networks directly from a Python prompt or Jupyter notebook. 
* [`snahelper`](https://github.com/schochastics/snahelper): provides a set RStudio Addin for social network analysis. The main addin is the `SNAhelper` which provides a simple GUI to do common network analytic tasks and visualize a network with `ggraph`.
* [`webweb`](https://github.com/dblarremore/webweb): tool for creating, displaying, and sharing interactive network visualizations on the web, designed for simplicity and ease of use. It's made for users of Python, NetworkX, and MATLAB. 

### Community Detection  

* [Map Equation](https://www.mapequation.org/apps/MapDemo.html)

The following material has been taken from the review article by [Santo Fortunato and Darko Hric (2016)](https://doi.org/10.1016/j.physrep.2016.09.002).

**Artificial benchmarks**. Code to generate LFR benchmark graphs can be found [here](https://sites.google.com/site/andrealancichinetti/files). The code for the dynamic benchmark by Granell et al. is available [here](https://github.com/rkdarst/dynbench).

**Partition similarity measures**. Many partition similarity measures have their own function in `R`, `Python` and `MatLab` and are easy to find. The variant of the NMI for covers proposed by Lancichinetti et al. can be found [here](https://sites.google.com/site/andrealancichinetti/mutual), the one by Esquivel and Rosvall  [here](https://bitbucket.org/dsign/gecmi/wiki/Home).

**Consensus clustering**. The technique proposed by Lancichinetti and Fortunato to derive consensus partitions from multiple outputs of stochastic clustering algorithms can be downloaded from [here](https://sites.google.com/site/andrealancichinetti/software).

**Spectral methods**. The spectral clustering method by Krzakala et al., based on the non-backtracking matrix can be downloaded [here](http://lib.itp.ac.cn/html/panzhang/dea/dea.tar.gz).

**Edge clustering**. The code for the edge clustering technique by Ahn et al. can be found [here](http://barabasilab.neu.edu/projects/linkcommunities/). The link to the stochastic block model based on edge clustering by Ball et al. is provided below.

**Methods based on statistical inference**. The code to perform the inference of the degree-corrected stochastic block model46 by Karrer and Newman is available [here](http://www-personal.umich.edu/~mejn/dcbm/). The weighted stochastic block model by Aicher et al. can be found [here](http://tuvalu.santafe.edu/~aaronc/wsbm/). The code for the overlapping stochastic block model based on edge clustering by Ball et al. is [here](http://www-personal.umich.edu/~mejn/OverlappingLinkCommunities.zip). The model combining structure and metadata by Newman and Clauset is coded [here](http://www-personal.umich.edu/~mejn/Newman_Clauset_code.zip). The program to infer the bipartite stochastic block model by Larremore et al. can be found at [here](http://danlarremore.com/bipartiteSBM/). 

The algorithms for the inference of community structure developed by Tiago Peixoto are implemented within the Python module `graph-tool` and can be found [here](https://graph-tool.skewed.de/static/doc/dev/community.html). They allow us to perform model selection of various kinds of stochastic block models: degree-corrected, with overlapping groups, and for networks with layers, with valued edges and evolving in time. The hierarchical block model, that searches for clusters at high resolution, is also available. All such variants can be combined at ease by selecting a suitable set of options.

The algorithms for the inference of overlapping communities via the Community-Affiliation Graph Model (AGM)  and the Cluster Affiliation Model for Big Networks (BIGCLAM) can be found in the [package](http://infolab.stanford.edu/~crucis/code/agm-package.zip).

**Methods based on optimisation**. There is a lot of free software for modularity optimisation. In the [`igraph` library](http://igraph.org) there are several functions, both in the and in the Python package: cluster_fast_greedy (R) and community_fastgreedy (Python), implementing the fast greedy optimisation by Clauset et al.; cluster_leading_eigen (R) and community_leading_eigenvector (Python) for the optimisation based on the leading eigenvector of the modularity matrix; cluster_louvain (R) and community_multilevel (Python) are the implementations of the Louvain method; cluster_optimal (R) and community_optimal_modularity turn the task into an integer programming problem; cluster_spinglass (R) and community_spinglass (Python) optimise the multi-resolution modularity proposed by Reichardt and Bornholdt.

Some methods based on the optimisation of cluster quality functions are also available. The code for the optimisation of the local modularity by Clauset can be found at http://tuvalu.santafe.edu/~aaronc/shared/LocalCommunity2005_GPL.zip. The code for OSLOM is downloadable from the dedicated website http://www.oslom.org.

**Methods based on dynamics**. Infomap is currently a very popular algorithm and its code can be found in various places. It has a dedicated website http://www.mapequation.org, where several extensions can be downloaded, including hierarchical community structure, overlapping clusters   and memory. Infomap has also its own functions on igraph, both in the R and in the Python package (cluster_infomap and community_infomap, respectively). Walktrap, another popular method based on random walk dynamics, is available on igraph, via the functions cluster_walktrap (R) and community_walktrap (Python). The local community detection algorithms proposed in can be downloaded from http://people.maths.ox.ac.uk/jeub/code.html.

**Dynamic clustering**. The code to optimise the multislice modularity by Mucha et al. is available at http://netwiki.amath.unc.edu/GenLouvain/GenLouvain. Detection of dynamic communities can be performed as well with consensus clustering and via stochastic block models. Links to the related code have been provided above.

<br><br>

</a>
<a name="Language_Logos"/>
<div align="center">
<a href="https://www.r-project.org" target="_blank">
<img src="https://www.r-project.org/logo/Rlogo.png" alt="R Logo" width="160" height="100"></img> 
<a href="https://www.python.org/psf-landing/" target="_blank">
<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python Logo" width="300" height="100"></img>
<a href="https://julialang.org/" target="_blank">
<img src="https://julialang.org/images/logo_hires.png" alt="Julia Logo" width="150" height="100"></img>
</a>

    
