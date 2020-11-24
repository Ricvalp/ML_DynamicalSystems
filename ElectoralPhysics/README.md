<!-- Meta-Badges -->
</p>

<p align="center">
    <img alt="Size" src="https://img.shields.io/github/repo-size/pitmonticone/AppliedDynamicalSystems">
  </a>
  <img alt="Forks" src="https://img.shields.io/github/forks/pitmonticone/AppliedDynamicalSystems">
  </a>
  <img alt="Stars" src="https://img.shields.io/github/stars/pitmonticone/AppliedDynamicalSystems">
  </a>
  <img alt="Languages" src="https://img.shields.io/github/languages/count/pitmonticone/AppliedDynamicalSystems">
  </a>
  <a href="https://github.com/pitmonticone/AppliedDynamicalSystems/graphs/contributors">
    <img alt="Contributors" src="https://img.shields.io/github/contributors/pitmonticone/AppliedDynamicalSystems">
  </a>
  <img alt="Licence" src="https://img.shields.io/github/license/pitmonticone/AppliedDynamicalSystems">
  </a>
  <img alt="Twitter" src="https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fpitmonticone%2FAppliedDynamicalSystems"
  </a>

</p>

<!-- Title -->
<h1 align="center">
  Electoral Physics Project
</h1>

<!-- Subtitle -->
<h3 align="center">
  Building a coherent electoral modelling framework
</h3>

<!-- Badges -->
</p>

<p align="center">
  <a href="https://www.kaggle.com/">
    <img alt="Kaggle" src="https://kaggle.com/static/images/open-in-kaggle.svg">
  </a>
  <a href="https://nbviewer.jupyter.org/github/pitmonticone/AppliedDynamicalSystems/">
    <img alt="nbviewer" src="https://github.com/jupyter/design/blob/master/logos/Badges/nbviewer_badge.svg">
  </a>
  <a href="https://colab.research.google.com/github/pitmonticone/AppliedDynamicalSystems/blob/master">
    <img alt="Colab" src="https://colab.research.google.com/assets/colab-badge.svg">
  </a>

</p>

## Ideas

1. Instantiate N voters (id::Int, candidacy::Bool, add_directed_edge!(id,candidate) )
1. Instantiate GraphSpace ()
1. Sample M<<N candidates
1. Voter-Dynamics: add_directed_edge!(id,candidate)
1. Non-spectral centrality measures
1. Spectral centrality measures (Eigenvector centrality)

* Electoral Atlas / Spectrum / Portfolio

* From direct democracy to democratic tecnhocracy (we will always assume democratic regime, non-dictatorship axiom)

* Top-down vs. bottom-up (pure content-based or content+confidence-based vs. pure confidence-based)

* Graph-based vs. non graph-based (ML s.a. K-means, ...)

* Centrality-based ranking for graph-based systems (spectral vs. non-spectral: Map eqation, PageRank, ...)
* Community Detection for party formation (G-N, Modularityl, Map Equation, Clustering...)

* Parameters: 
    * *N*: Voter population size (fixed by current law)
    * *M*: Candidate population size (Exogenous vs. Endogenous)
    * *K*: Representative population size 

* Representative Ranking:
    * Party-based / Aggregated
    * Individual-based 

* Implement all or most of currently realized models (first-past-the-post, preferences, majority, proportial,...)
* Build models with pre-electoral party dogma.

* Experiments with epirica.ly and other tools. 

### Parallel Election 
               
1. Pick a known village / city with population size < 1000;
2. Wait for the next municipal election;
3. Call the administration to inform them and try to convince them to run parallel election;
4. Run the parallel election and collect relevant data
5. Analyze the data and inform the relevant stakeholders


## Tools 

* [Map Equation](https://www.mapequation.org)

## Resources

### Textbooks 

* [The Oxford Handbook of Electoral Systems](https://drive.google.com/file/d/1_9KVTYnR0K6SNA00a1CVYsK-QY_7P3yM/view?usp=sharing)
* [Handbook of Computational Social Choice](https://drive.google.com/open?id=1jt8HuFvkaPp0Pbie6wdkm5nBGpgvB46L)

* [Party Competition: An Agent-Based Model](https://drive.google.com/open?id=1tOx-3eoCyjt0pBxOjQXgCts7uoCqmVSd)
* [The Mathematics of Elections and Voting](https://www.springer.com/gp/book/9783319098098)
* [The Mathematics of Voting and Apportionment](https://drive.google.com/open?id=1ui1eQY0o_LEfK4wz-ZU1hvIuEgMi4Hvk)

* [Multi-Agent Based Modeling Using Multi-Criteria Decision Analysis and OLAP System for Decision Support Problems](https://www.researchgate.net/publication/290790217_Multi-Agent_Based_Modeling_Using_Multi-Criteria_Decision_Analysis_and_OLAP_System_for_Decision_Support_Problems)

### Readings  

* [Social Choice Theory](https://plato.stanford.edu/entries/social-choice/). *Stanford Encyclopedia of Philosophy* (2013). 

A. Telek (2016). [Power Networks: A network approach of voting theory](http://econ.core.hu/file/download/korosi/2016/telek.pdf), *arXiv pre-print*. 

Hernández Alexis R. et al., 2018. [A networked voting rule for democratic representation](https://doi.org/10.1098/rsos.172265), *Royal Society Open Science*. 

K Wiesner et al. (2018). [Stability of democracies: a complex systems perspective](https://doi.org/10.1088/1361-6404/aaeb4d), *European Journal of Physics*.

* [Universality in voting behavior: an ABM to calculate the distribution of votes among the candidates](https://terna.to.it/tesine/distribution_of_votes.pdf)

* [Agent Based Modeling of Individual Voting Preferences with Social Influence](https://link.springer.com/chapter/10.1007/978-3-642-24043-0_55)
* [Dynamic Parties and Social Turnout: An Agent‐Based Model](https://www.jstor.org/stable/10.1086/426554?seq=1#metadata_info_tab_contents)
* [Voting Behavior in Proportional Elections from Agent – Based Models](https://www.sciencedirect.com/science/article/pii/S1875389215000401)
* [Using Agent-Based Models to Simulate Strategic Behavior in Elections](http://www-personal.umich.edu/~wmebane/pm19.pdf)
* [Combining Machine Learning and Agent Based Modeling for Gold Price Prediction](https://link.springer.com/chapter/10.1007/978-3-030-21733-4_7)
(https://static1.squarespace.com/static/5c2e56155ffd20ae8ee2c3e4/t/5d77c784d5962f1579b4f3b7/1568130953777/Augmented+Democracy+Proposal_Vision_Indigena.pdf)

* [Cascade or echo chamber? A complex agent-based simulation of voter turnout](https://journals.sagepub.com/doi/pdf/10.1177/1354068815605671)


* [Decision Making in Agent-Based Models](https://link.springer.com/chapter/10.1007/978-3-319-17130-2_25)
* [Agent-based modeling: Methods and techniques for simulating human systems](https://www.pnas.org/content/99/suppl_3/7280)
* [Enhancing ABM into an Inevitable Tool for Policy Analysis](https://ii.tudelft.nl/~catholijn/publications/sites/default/files/enhancingAMB.pdf)
* [How Do Agents Make Decisions? A Survey](http://jasss.soc.surrey.ac.uk/17/4/13.html)


### Projects 

* [AUGMENTED DEMOCRACY](https://www.peopledemocracy.com)
    * [Theoretical Underpinnings of a Pure Digital Democracy Model of Government](https://static1.squarespace.com/static/5c2e56155ffd20ae8ee2c3e4/t/5d77c81dedd5084e5c931575/1568131114349/Theoretical+Underpinnings+of+a+Pure+Digital+Democracy+-+Preliminary+Version.pdf)
    * [Proof of Witness Presence: Blockchain Consensus for Augmented Democracy in Smart Cities](https://static1.squarespace.com/static/5c2e56155ffd20ae8ee2c3e4/t/5d77c8988b4c300d55be0dbd/1568131240537/view.pdf)
    * [iVote](https://static1.squarespace.com/static/5c2e56155ffd20ae8ee2c3e4/t/5d77c7e848eb396542e3a6ca/1568131061767/iVoteAD.pdf)
