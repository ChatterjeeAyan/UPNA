# Disentangling Node Attributes from Graph Topology for Improved Generalizability in Link Prediction

# Abstract 

Link prediction is a core task in graph machine learning, as it is useful in many application domains ranging from friendship recommendations in social networks to the discovery of new drugs in drug-target interaction networks. The most common setting in link prediction is the transductive scenario, where both the nodes of the test link are observed in training. When one or both of the test nodes are not seen during training, the link prediction settings are termed semi-inductive and inductive link prediction, respectively. For these unobserved isolated nodes, the absence of topological information enforces the link prediction models to leverage the node attributes for making accurate predictions. For example, recommending a new item to a user in the semi-inductive setting, or identifying the interaction between a novel protein target and a newly developed drug in the inductive setting demands meaningful pairwise learning on the node attributes. Furthermore, the semi-inductive and inductive link prediction scenarios are of interest in temporal networks where newly arrived nodes attach to temporal instances of the graph, creating a topology evolving in time.

In this work, we explore the interplay between the node attributes and the graph topology, and demonstrate how node attributes orthogonal to the graph topology from an informational standpoint improve the generalization power of the link prediction models quantified in terms of the inductive link prediction performance. Unsupervised pre-training of the node attributes independent of the topology and on large corpora enables us to learn the latent graph generation mechanism independent of the observed graph. By gaining insight into the growth mechanism of the graph via the node attributes, we discard the observational bias associated with a fixed snapshot of the network and are able to make meaningful predictions on unobserved nodes circumventing topological shortcuts. Unsupervised pre-training of the attributes can be extended to any pairwise learning task such as the cold-start problem in recommender systems and pairwise kernels. 

# Reproducing the Results 

## Requirements

We use the OGB benchmark to develop and run the experiments. Please refer to the OGB documentation and setup for executing the experiments listed below: https://github.com/snap-stanford/ogb

Merge the files from /Inductive-tests/ogb/ in the extracted ogb folder. 

For setting up the state-of-the-art link prediction model PLNLP, please refer to: https://github.com/zhitao-wang/plnlp

## Topological Shortcuts in Transductive Tests

Configuration models - traditional and duplex: /Topological-Shortcuts/maximumentropymodels.py

Transductive link prediction on ogbl-ddi: /Topological-Shortcuts/ogbl-ddi-configuration-model.ipynb

## Inductive Tests on State-of-the-art PLNLP with random node split

ogbl-ddi: /Inductive-tests/PLNLP/main_ddi_node_split.py

ogbl-ppa: /Inductive-tests/PLNLP/main_node_split_collab.py

ogbl-collab: /Inductive-tests/PLNLP/main_node_split_ppa.py

## Pre-training of Node Attributes and Davis-Bouldin Score Analysis

ogbl-ddi: /Node-Attributes-Analysis/ogbl-ddi-pretraining-data-analysis/mapping/

ogbl-ppa: /Node-Attributes-Analysis/ogb-ppi-pretraining-data-analysis/

ogbl-collab: /Node-Attributes-Analysis/ogbl-collab-pretraining-data-analysis/mapping/

## Inductive tests using MLPs and pre-trained node attributes 

ogbl-ddi: /Inductive-tests/ogb/examples/linkproppred/ddi/

ogbl-ppa: /Inductive-tests/ogb/examples/linkproppred/ppa/

ogbl-collab: /Inductive-tests/ogb/examples/linkproppred/collab/

## Temporal Networks

The open-source data can be downloaded from: http://snap.stanford.edu/data/soc-RedditHyperlinks.html

The Python notebooks to reproduce the results are available at: /Temporal_Networks/*

# Topological Shortcuts in DGL

We compare the performance of GraphSAGE \cite{graphsage} with the traditional configuration model and observe that the deep model leverages topological shortcuts. Both models achieve similar AUROC over multiple benchmark datasets in DGL \cite{dgl}. We use random edge split to create the train-validation-tests graphs. 


Datasets are available at: https://docs.dgl.ai/en/0.4.x/api/python/data.html

| Dataset | GraphSAGE AUROC | Configuration Model AUROC | 
| --- | --- | --- | 
| CitationGraphDataset - pubmed | 0.912 | 0.881 |
| --- | --- | --- | 
| CoraDataset | 0.864 | 0.829 |
| --- | --- | --- | 
| CoraFull  | 0.889 | 0.857 |
| --- | --- | --- | 
| AmazonCoBuy - computers | 0.499 | 0.891 |
| --- | --- | --- | 
| AmazonCoBuy - photo  | 0.5 | 0.897 |
| --- | --- | --- |
| Coauthor - cs  | 0.721 | 0.854 |
| --- | --- | --- | 
| Coauthor - physics  | 0.861 | 0.851 |
| --- | --- | --- |