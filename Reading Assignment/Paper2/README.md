## 2. Graph Enhanced Contrastive Learning for Radiology Findings Summarization

| Main Contributions  | The main contribution of the paper is the introduction of a graph-enhanced contrastive learning approach for radiology findings summarization. The approach uses a graph to represent the relationships between different findings, and contrastive learning to identify the most important findings and generate a summary. |
| --- | --- |                  
| Methodology  | 1. Constructing a graph representation of the radiology findings.|
|              | 2. Training a contrastive learning model to identify the most important findings.|
|              | 3. generating a summary based on the most important findings identified by the model.|
| Architecture  | (Figure is given below) For each input findings, it is encoded by a text encoder, and a graph is constructed through its entities and dependency tree. Then, a graph encoder (e.g., graph neural networks (GNNs)) is adopted to model relation information in the constructed graph. Finally, to emphasize the key words in the findings, contrastive learning is introduced to map positive samples (constructed by masking non-key words) closer and push apart negative ones (constructed by masking key words). They employed contrastive learning to assist the model in distinguishing between critical and secondary information, simultaneously improving        sensitivity to important word representation by comparing positive and negative examples. |
| Results  | - Base + Graph + CL outperforms Base + Graph and Base + CL |
|          | - While comparing with existing models the proposed model outperformed in every aspect. |
|          | (Figures are attached below). |
| Limitation  | -While doing human evaluation the model is less preferred for readability with a 10% gap. The main reason might be that many words removed in positive examples are used to keep sequence fluently, and our model tends to identify them as secondary information. |
|             | -The approach is only as accurate as the graph representation of the findings, which may be limited by the quality of the data used to construct the graph. |
| Reference  | ***Hu, J., Li, Z., Chen, Z., Li, Z., Wan, X., & Chang, T. H. (2022). Graph Enhanced Contrastive Learning for Radiology Findings Summarization. arXiv preprint arXiv:2204.00203..*** |

#### Architecture
https://github.com/SakibBinAlam/Natural-Language-Processing/blob/main/Reading%20Assignment/Paper2/architecture.png

#### Result 1
(https://github.com/SakibBinAlam/Natural-Language-Processing/blob/main/Reading%20Assignment/Paper2/result1.png)

#### Result 2
(https://github.com/SakibBinAlam/Natural-Language-Processing/blob/main/Reading%20Assignment/Paper2/result2.png)

