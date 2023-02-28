## 3. Latent Prompt Tuning for Text Summarization
| Main Contribution  | The study firstly identifies the problem that control signals can help to improve the summarization quality, but they are usually unavailable
during inference time. Therefore, they propose a Latent Prompt Tuning framework LOTUS (i.e., a single model with both “controlled” and “uncontrolled” modes) to solve this problem. |
| Methodology  | 1. Constructing a graph representation of the radiology findings.|
|              | 2. Training a contrastive learning model to identify the most important findings.|
|              | 3. generating a summary based on the most important findings identified by the model.|
| --- | --- |
| Architecture  | (Figure is given below) The model achieves controllable summarization through prompts. During training time, the uncontrolled model learns a latent prompt from the controlled model using a contrastive learning objective. The model and the latent prompts are updated based on the loss. Finally the model can generate both controlled (e.g. summary with abstractiveness 60) and uncontrolled summarization (summary with abstractiveness).|
| Results  | The authors evaluate the LOTUS method on four benchmark datasets: CNN/Daily Mail, XSum, Gigaword, and NYT. They compare their approach to several state-of-the-art models, including, BART, BERTSUM, T5, PEGASUS, and CTRLSUM. The results show that LOTUS outperforms these models on all four datasets. |
| Future Work  | The proposed method could be extended to other text generation task such as machine translation, data-to-text generation and large generative language modeling. |
| Reference  | ***Zhang, Y., Zhang, X., Wang, X., Chen, S. Q., & Wei, F. (2022). Latent Prompt Tuning for Text Summarization. arXiv preprint arXiv:2211.01837.*** |



#### Architecture
![Architecture](https://github.com/SakibBinAlam/Natural-Language-Processing/blob/main/Reading%20Assignment/Paper3/architecture.png)
