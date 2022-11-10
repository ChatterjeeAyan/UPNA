# Improving Inductive Link Prediction through Learning Generalizable Node Representations

# Abstract 

Link prediction is a core task in graph machine learning, as it is useful in many application domains from social networks to biological networks. Link prediction can be performed under different experimental settings: (1) transductive, (2) semi-inductive, and (3) inductive. The most common setting is the transductive one, where the task is to predict whether two observed nodes have a link. In the semi-inductive setting, the task is to predict whether an observed node has a link to a newly observed node, which was unseen during training. For example, cold start in recommendation systems requires suggesting a known product to a new user. We study the inductive setting, where the task is to predict whether two newly observed nodes have a link. The inductive setting occurs in many real-world applications such as predicting interactions between two poorly investigated chemical structures or identifying collaboration possibilities between two new authors. In this paper, we demonstrate that current state-of-the-are techniques perform poorly under the inductive setting, i.e., when generalizing to new nodes, due to the overlapping information between the graph topology and the node attributes. To address this issue and improve the robustness of link prediction models in an inductive setting, we propose new methods for designing inductive tests on any graph dataset, accompanied by unsupervised pre-training of the node attributes. Our experiments show that the inductive test performances of the state-of-the-art link prediction models are substantially lower compared to the transductive scenario. These performances are comparable, and often lower than that of a simple multilayer perceptron on the node attributes. Unsupervised pre-training of the node attributes improves the inductive performance, hence the generalizability of the link prediction models.

# Experiments and Related Files

## Requirements

We use the OGB benchmark to develop and run the experiments. Please refer to the OGB documentation and setup for executing the experiments listed below: https://github.com/snap-stanford/ogb

Merge the files from /shortcuts-graph-machine-learning/Inductive-tests/ogb/ in the extracted ogb folder. 

For setting up the state-of-the-art link prediction model PLNLP, please refer to: https://github.com/zhitao-wang/plnlp

## Topological Shortcuts in Transductive Tests

Configuration models - traditional and duplex: /shortcuts-graph-machine-learning/Topological-Shortcuts/maximumentropymodels.py

Transductive link prediction on ogbl-ddi: /shortcuts-graph-machine-learning/Topological-Shortcuts/ogbl-ddi-configuration-model.ipynb

## Inductive Tests on State-of-the-art PLNLP with random node split

ogbl-ddi: /shortcuts-graph-machine-learning/Inductive-tests/PLNLP/main_ddi_node_split.py

ogbl-ppa: /shortcuts-graph-machine-learning/Inductive-tests/PLNLP/main_node_split_collab.py

ogbl-collab: /shortcuts-graph-machine-learning/Inductive-tests/PLNLP/main_node_split_ppa.py


## Pre-training of Node Attributes and Davis-Bouldin Score Analysis

ogbl-ddi: /shortcuts-graph-machine-learning/Node-Attributes-Analysis/ogbl-ddi-pretraining-data-analysis/mapping/

ogbl-ppa: /shortcuts-graph-machine-learning/Node-Attributes-Analysis/ogb-ppi-pretraining-data-analysis/

ogbl-collab: /shortcuts-graph-machine-learning/Node-Attributes-Analysis/ogbl-collab-pretraining-data-analysis/mapping/

## Inductive tests using MLPs and pre-trained node attributes 

ogbl-ddi: /shortcuts-graph-machine-learning/Inductive-tests/ogb/examples/linkproppred/ddi/

ogbl-ppa: /shortcuts-graph-machine-learning/Inductive-tests/ogb/examples/linkproppred/ppa/

ogbl-collab: /shortcuts-graph-machine-learning/Inductive-tests/ogb/examples/linkproppred/collab/