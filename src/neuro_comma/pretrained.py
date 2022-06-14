# TODO: rework with tokenizer special tags
from transformers import AutoModel, AutoTokenizer

# special tokens indices in different models available in transformers
TOKEN_IDX = {
    'bert': {
        'START_SEQ': 101,
        'PAD': 0,
        'END_SEQ': 102,
        'UNK': 100
    },
    'xlm': {
        'START_SEQ': 0,
        'PAD': 2,
        'END_SEQ': 1,
        'UNK': 3
    },
    'roberta': {
        'START_SEQ': 0,
        'PAD': 1,
        'END_SEQ': 2,
        'UNK': 3
    },
    'albert': {
        'START_SEQ': 2,
        'PAD': 0,
        'END_SEQ': 3,
        'UNK': 1
    },
}


# pretrained model name: (model class, model tokenizer, output dimension, token style)
PRETRAINED_MODELS = {
    'models/rubert-base-cased-sentence': (AutoModel, AutoTokenizer, 768, 'bert'),
}

