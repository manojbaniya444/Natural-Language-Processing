## LSTM Encoder Decoder Architecture
![Encoder Decoder](./images/encoder_decoder.webp)

## In LSTM there are 3 important parameters:

1. **UNITS** : Dimensionality of the output space
2. **Return Sequences** : Whether to return the last output only or the intermediate state at each `timestep`.
3. **Return State** : Whether to return the last state in addition to the output.

So According to these, there are several behaviour LSTM can behave

1. Default: Last Hidden State as Output

![Default State](./images/lstm_1.png)

2. Return Sequences=True: All Hidden State output

![Return Sequence](./images/lstm_2.png)

3. Return State = True: Last Hidden State + Last Hidden State(again) + Last Cell State

![Return State](./images/lstm_3.png)

4. Return Sequence and Return State both true: All Hidden States(from each timestep) + Last Hidden State(only last timestep) + Last Cell State(of last timestep)

![Get All State](./images/lstm_f.png)

## This kind of Model is useful in task like `**Machine Translation**`

![Machine Translation](./images/machine_translation.png)