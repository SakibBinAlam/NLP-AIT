## 2. Graph Enhanced Contrastive Learning for Radiology Findings Summarization

| Main Contributions  | The main contribution of the paper is the introduction of a graph-enhanced contrastive learning approach for radiology findings summarization. The approach uses a graph to represent the relationships between different findings, and contrastive learning to identify the most important findings and generate a summary. |
| --- | --- |                  
| Methodology  | 1. Constructing a graph representation of the radiology findings.|
|              | 2. Training a contrastive learning model to identify the most important findings.|
|              | 3. generating a summary based on the most important findings identified by the model.|
| Architecture  | (Figure is given below) For each input findings, it is encoded by a text encoder, and a graph is constructed through its entities and dependency tree. Then, a graph encoder (e.g., graph neural networks (GNNs)) is adopted to model relation information in the constructed graph. Finally, to emphasize the key words in the findings, contrastive learning is introduced to map positive samples (constructed by masking non-key words) closer and push apart negative ones (constructed by masking key words). They employed contrastive learning to assist the model in distinguishing between critical and secondary information, simultaneously improving        sensitivity to important word representation by comparing positive and negative examples. |
| Results  | - Methods that do not take entity information into account (Lead3ovr, GSumovr) perform significantly lower than the best methods in the same class which use entity information. |
|          | - Previously introduced methods (ConvNet, CTRLSum) for controllable summarization can not perform well on entity-centric summarization. |
|          | - Extractive approaches perform better than abstractive methods, which is expected due to the extractive nature of the ENTSUM data set. |
| Research gap/future directions  | -The absolute results also show there is further room for improvement in entity-centric summarization approaches, given that performance of automated methods still lags behind Lead3ent, whereas this is currently surpassed by automated methods in generic summarization. . |
|                                 | -A data set for entity-centric summarization can be created that is more abstractive in nature. |
| Reference  | ***Hu, J., Li, Z., Chen, Z., Li, Z., Wan, X., & Chang, T. H. (2022). Graph Enhanced Contrastive Learning for Radiology Findings Summarization. arXiv preprint arXiv:2204.00203..*** |

