## 4. PSP: Pre-trained Soft Prompts for Few-Shot Abstractive Summarization

| Main Contributions  | This study finds the necessity of using prompt pre-training for few-shot/zero-shot abstractive summarization. The work presents a novel pre-trained soft prompts architecture (PSP) specifically designed for few-shot abstractive summarization. It designs continuous input embeddings across an encoder and a decoder alongside several kinds of inner prompts placed in the text, assisting the model better to understand documents and guide accurate generation.  |
| --- | --- |                      
| Architecture  | (Figure is given below) The framework includes continuous prompts across the encoder and decoder inputs, as well as inner-prompts to capture the dependencies between documents and target summaries. To better understand a given document, this adds a prompt pre-training process before fewshot tuning.|
| Results  | Experimental results on the CNN/DailyMail and XSum datasets show that the proposed method, with only 0.1% of the parameters, outperforms fullmodel tuning where all model parameters are tuned. It also surpasses Prompt Tuning by a large margin and delivers competitive results against Prefix-Tuning with 3% of the parameters. |
| Reference  | ***Liu, X., Bai, Y., Li, J., Hu, Y., & Gao, Y. (2022). Psp: Pre-trained soft prompts for few-shot abstractive summarization. arXiv preprint arXiv:2204.04413.*** |

#### Architecture
![Architecture](https://github.com/SakibBinAlam/Natural-Language-Processing/blob/main/Reading%20Assignment/Paper4/PSP-architecture.png)
