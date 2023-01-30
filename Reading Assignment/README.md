## Paper reading assignment
## 1. ENTSUM: A Data Set for Entity-Centric Summarization (ACL, 2022)

| Overview  | The paper introduced a human-annotated data set (ENTSUM) for controllable summarization with a focus on named entities as the aspects to control. Along      with existing methods the also proposed extensions to state-of-the-art summarization approaches that achieve substantially better results on the data set. |
| --- | --- |
| Main Contributions  | 1.The first annotated data set for controllable summarization with entities as targets for control (ENTSUM - Entity SUMmarization).|
|                     | 2. Evaluation of generic and also controllable summarization methods on the ENTSUM data set.|
|                     | 3. Adaptations of extractive and abstractive summarization methods for performing entity-centric summarization when trained with generic summaries only.|
| Methods used for evaluation  | Abstractive methods: ConvNet (Fan et al. 2018), CTRLSum (He et al., 2020), GSum (Dou et al., 2021), Adapting GSum for Entity-Centric Summarization.|
|                              | Extractive methods: Lead3ovr and Lead3ent (Nallapati et al., 2017), BERTSum (Liu and Lapata, 2019), Adapting BERTSum for Entity-Centric Summarization, Oracle - Lead3ent (salient), Oracle - Lead3ent (summary).|
| Results  | Accruacy improves around 2% in UAS and LAS scores. Improve parsing speed by 8 ~ 10 times. |

***Reference: Maddela, M., Kulkarni, M., & Preotiuc-Pietro, D. (2022). EntSUM: A Data Set for Entity-Centric Summarization. arXiv preprint arXiv:2204.02213.
