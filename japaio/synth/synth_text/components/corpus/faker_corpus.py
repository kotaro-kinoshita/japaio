from faker import Factory

from synthtiger.components.corpus.base_corpus import BaseCorpus
import numpy as np



class FakerCorpus(BaseCorpus):
    def __init__(
        self,
        paths=(),
        weights=(),
        min_length=None,
        max_length=None,
        charset=None,
        textcase=None,
        language="ja_JP",
        providers=(),
        
    ):
        super().__init__(paths, weights, min_length, max_length, charset, textcase)
        self.factory = Factory.create(language)
        self.providers = providers
        #self.augmentation = augmentation

    def sample(self, meta=None):
        if meta is None:
            meta = {}

        text = self._sample_text()
        text = self._random_textcase(text)
        text = meta.get("text", text)

        meta = {
            "text": text,
        }

        return meta

    def _sample_text(self):
        #key = np.random.choice(len(self.providers), p=self._probs)
        key = np.random.randint(0, len(self.providers))
        return eval(f"self.factory.{self.providers[key]}()")