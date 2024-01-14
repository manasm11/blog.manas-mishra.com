+++
title = "Text Completions API"
linkTitle = "Completions"
weight=10
+++
[API Reference link](https://platform.openai.com/docs/api-reference/completions/create)
## Available Models
| Model                     | Max Tokens | Price (Input)  | Price (Output) |
| -----------               | ---------- | ---            | ---            |
| gpt-3.5-turbo-instruct    | 4,096      | $1.5/1M tokens | $2.0/1M tokens |
| davinci-002               | 16,384     | $2.0/1M tokens | $2.0/1M tokens |
| babbage-002               | 16,384     | $0.4/1M tokens | $0.4/1M tokens |
## Input Parameters
| Parameter  | Type   | Default     | Description                                |
| ---------  | ----   | -------     | ---------------                            |
| model      | string | [REQUIRED]  | The model to use.                          |
| prompt     | string | [REQUIRED]  | The prompt to complete.                    |
| max_tokens | integer    | 16          | The maximum number used (Input+Output).    |
| n          | integer    | 1           | Number of completions to generate.         |
| best_of | integer | 1 | Generates multiple completions internally and returns *n* best outputs. (Increases number of output tokens generated.) |
| stream     | boolean| false       | Send partial responses as being generated. |
| temperature| float  | 1.0 (0.0 to 2.0)   | Increases randomness by making probability distribution flattened.|
| top_p | float | 1.0 (0.0 to 2.0) | Increases randomness by increasing threshold of probability for accepted tokens. |
| echo       | boolean| false       | Includes input prompt along with output. (Doesn't affect pricing).
| presence_penalty | float | 0.0 (-2.0 to 2.0) | Reduce probability of re-occurrence of token once it occurred| 
| frequency_penalty | float | 0.0 (-2.0 to 2.0) | Reduce the probability of re-occurrence of token as it appears in the output. (May lead to non-sensible outputs.)|
| seed | int | 0 | Attempts to give deterministic output |
| suffix | string |  | Suffix after completion. |
| stop | string/array | | Upto 4 sequences of tokens to stop generation. (Sequence will not be included in output) |
| user | string | | A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.|1
| logit_bias | object | null | Not Sure |
| logprobs | integer | 0 | Not Sure |
## Output Parameters
| Parameter   | Type   | Description                                      |
| ---------   | ----   | ---------------                                  |
| id          | string | A unique identifier for the completion.          |
| model       | string | The model used for completion.                   |
| created     | integer| Unix timestamp (seconds) of completion creation. |
| usage       | object | Tokens usage statistics.                         |
| usage.completion_tokens | integer | Number of tokens generated.         |
| usage.prompt_tokens | integer | Number of input tokens.                 |
| usage.total_tokens | integer | Total number of tokens (Input + Output). |
| choices | array of objects | An array of completion choices.                       |
| choices[i].text | string | Output text generated. (most important output.) |
| choices[i].finish_reason | string | Reason for stopping token generation ("stop" if it was optimal stopping point as per model, "length" if model hit max_token limit, "content_filter" if output was flagged as per moderation API) |
| choices[i].index | integer | Index of the choice in the choices array. Basically "i" |
| choices[i].logprobs | object | Not Sure. |
