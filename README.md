# UPNA (Unsupervised Pre-training of Node Attributes)

# Abstract 

Link prediction is a crucial task in graph machine learning with diverse applications. We explore the interplay between node attributes and graph topology and demonstrate that incorporating pre-trained node attributes improves the generalization power of link prediction models. Our proposed method, UPNA (Unsupervised Pre-training of Node Attributes), enables us to learn the latent mechanism of graph generation independent of the observed graph. By leveraging pre-trained node attributes, we overcome observational bias and make meaningful predictions about unobserved nodes, surpassing state-of-the-art performance (3X to 34X improvement on benchmark datasets). UPNA can be applied to various pairwise learning tasks and integrated with existing link prediction models to enhance their generalizability and bolster graph generative models.

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

For the details and the original implementation of DyHATR, check out: https://github.com/skx300/DyHATR

# Supplementary Material

## Topological Shortcuts in DGL

We compare the performance of GraphSAGE [1] with the traditional configuration model and observe that the deep model leverages topological shortcuts. Both models achieve similar AUROC over multiple benchmark datasets in DGL. We use random edge split to create the train-validation-tests graphs. 

Datasets are available at: https://docs.dgl.ai/en/0.4.x/api/python/data.html

| Dataset | GraphSAGE AUROC | Configuration Model AUROC | 
| --- | :---: | ---: |
| CitationGraphDataset - pubmed | 0.912 | 0.881 |
| CoraDataset | 0.864 | 0.829 |
| CoraFull  | 0.889 | 0.857 |
| AmazonCoBuy - computers | 0.499 | 0.891 |
| AmazonCoBuy - photo  | 0.5 | 0.897 |
| Coauthor - cs  | 0.721 | 0.854 |
| Coauthor - physics  | 0.861 | 0.851 |

## Description of the OGB MLP Architectures for Reproducibility

| Dataset | Layers | Parameters | Hidden Channels | Dropout | Batch Size | Learning Rate | Epochs
| --- | :---: | :---: | :---: | :---: | :---: | :---: | ---: |
| ogbl-ppa | 3 | 113,921 | 256 | 0.1 | 65,536 | 0.01 | 20 |
| ogbl-collab | 3 | 99,073 | 256 | 0.1 | 65,536 | 0.01 | 200 |
| ogbl-ddi | 3 | 99,073 | 256 | 0.1 | 65,536 | 0.01 | 100 |


## Benchmark Graph Datasets are insufficient for Inductive Tests

Open Graph Benchmark (OGB) [2] provides a useful benchmark for comparing link prediction models, but is limited only to the transductive setting. OGB-provided train-validation-test splits are inadequate for inductive tests. OGB  provides large-scale graph datasets from various domains like social networks, biological networks, and molecular graphs. The train-validation-test splits are specifically tailored to test generalization based on specific properties associated with each graph. For example, in ogbl-ppa (protein-protein interaction network), the training graph consists of the interactions obtained via high throughput technology or even text-mining. This method of obtaining the interactions is cost-effective but produces low-confidence data. The validation and the test datasets are obtained from low throughput and resource-intensive experiments. Thus, they are of high confidence and provide a challenging generalization scenario.
However, the large overlap between the nodes in the train, the validation, and the test graphs limits us from creating node-disjoint train and test datasets for an inductive test setting.
Thus, running an inductive test using the default OGB train-validation-tests splits is unfeasible. 
We summarize below the graph properties of the OGB link prediction datasets, which 
shows the node overlaps between the train-validation-test splits in the OGB datasets. We lose the majority of the training edges when we remove the edges from the training graph which share nodes with the test dataset. The OGB data splits are thus insufficient for inductive tests. 
The default train-validation-test splits in the OGB link prediction benchmark have overlapping nodes. Therefore, when we remove the edges from the training graph which share nodes with the test graph, we lose majority of the edges. 

The benchmark train-validation-test graphs in OGB have overlapping nodes, which hinder the creation of inductive tests:

| Dataset | Train Nodes | Validation Nodes | Test Nodes | Train - Test Nodes | Test - Train Nodes |
| :--- | :---: | :---: | :---: | :---: | :---: |
| ogbl-ppa | 576,289 | 276,199 | 576,071 | 0 | 0 |
| ogbl-collab | 235,868 | 144,942 | 143,679 | 0 | 0 |
| ogbl-ddi | 3,967 | 3,995 | 1,737 | 86 | 0 |

Inductive train-validation-test split using random edge split on the OGB benchmark:

| Dataset | Train Nodes | Validation Nodes | Test Nodes | Train Edges | Validation Edges | Test Edges | Edges lost |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| ogbl-ppa | 3,991 | 36,778 | 461,288 | 2,626 | 25,973 | 1,213,051 | 29,084,623 |
| ogbl-collab | 36,593 | 62,561 | 60,023 | 27,482 | 51,419 | 42,680 | 1,281,488 |
| ogbl-ddi | 0 | 3,759 | 508 | 0 | 53,396 | 5 | 445,109 |

# References 

[1] William L. Hamilton, Rex Ying, and Jure Leskovec. 2017. Inductive Representation Learning on Large Graphs. https://arxiv.org/abs/1706.02216

[2] Weihua Hu, Matthias Fey, Marinka Zitnik, Yuxiao Dong, Hongyu Ren, Bowen Liu, Michele Catasta, and Jure Leskovec. 2020. Open Graph Benchmark: Datasets for Machine Learning on Graphs. https://arxiv.org/abs/2005.00687
