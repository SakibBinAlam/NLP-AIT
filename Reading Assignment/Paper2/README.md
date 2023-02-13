## 2. Graph Enhanced Contrastive Learning for Radiology Findings Summarization

| --- | --- |
| Main Contributions  | The main contribution of the paper is the introduction of a graph-enhanced contrastive learning approach for radiology findings summarization. The approach uses a graph to represent the relationships between different findings, and contrastive learning to identify the most important findings and generate a summary.|
|                     
|                     
| Methods used for evaluation  | Abstractive methods: ConvNet (Fan et al. 2018), CTRLSum (He et al., 2020), GSum (Dou et al., 2021), Adapting GSum for Entity-Centric Summarization.|
|                              | Extractive methods: Lead3ovr and Lead3ent (Nallapati et al., 2017), BERTSum (Liu and Lapata, 2019), Adapting BERTSum for Entity-Centric Summarization, Oracle - Lead3ent (salient), Oracle - Lead3ent (summary).|
| Results  | - Methods that do not take entity information into account (Lead3ovr, GSumovr) perform significantly lower than the best methods in the same class which use entity information. |
|          | - Previously introduced methods (ConvNet, CTRLSum) for controllable summarization can not perform well on entity-centric summarization. |
|          | - Extractive approaches perform better than abstractive methods, which is expected due to the extractive nature of the ENTSUM data set. |
| Research gap/future directions  | -The absolute results also show there is further room for improvement in entity-centric summarization approaches, given that performance of automated methods still lags behind Lead3ent, whereas this is currently surpassed by automated methods in generic summarization. . |
|                                 | -A data set for entity-centric summarization can be created that is more abstractive in nature. |
| Reference  | ***Hu, J., Li, Z., Chen, Z., Li, Z., Wan, X., & Chang, T. H. (2022). Graph Enhanced Contrastive Learning for Radiology Findings Summarization. arXiv preprint arXiv:2204.00203..*** |

