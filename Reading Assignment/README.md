## Paper reading assignment
## 1. ENTSUM: A Data Set for Entity-Centric Summarization (ACL, 2022)

| Overview  | The paper introduced a human-annotated data set (ENTSUM) for controllable summarization with a focus on named entities as the aspects to control. Along with existing methods the also proposed extensions to state-of-the-art summarization approaches that achieve substantially better results on the data set. |
| --- | --- |
| Key Related Work  | 1. Deep Learning for Efficient Discriminative Parsing (Collobert, 2011) -> Proposed new NLP algorithm by using CNN with GTN for constituency parsing.|
|                   | 2. Trainsition-based Dependency Parsing Using Recursive Neural Networks (Stenetorp, 2013) -> Introduce new framework to use RvNNs for trainsition-based dependency parsing.|
|                   | 3. Natural Language Processing (almost) from Scratch (Collobert et al., 2009) -> Introduce new architecture and learning algorithm that can applied to many NLP tasks (e.g. POS, NER).
| Solution  | Combining POS tags and arc labels with words instead of discrete representation. Using Cube activation function. Use pre-computational technique to pre-compute top frequent words, all POS tags and arc labels|
| Results  | Accruacy improves around 2% in UAS and LAS scores. Improve parsing speed by 8 ~ 10 times. |

***Reference: Maddela, M., Kulkarni, M., & Preotiuc-Pietro, D. (2022). EntSUM: A Data Set for Entity-Centric Summarization. arXiv preprint arXiv:2204.02213.
