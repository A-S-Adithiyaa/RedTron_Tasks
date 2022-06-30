import pandas as pd
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.utils import simple_preprocess



class SimilarityModel:

    def __init__(self, filename):
        self.filename = filename
        self.model = ""


    def create_model(self):
        def preprocessing_text(entry):
            text_l = entry.lower()
            
            tokens = word_tokenize(text_l)
            
            lang_stopwords = stopwords.words("english")
            remove_stopwords = [token for token in tokens if token not in lang_stopwords]
            
            return remove_stopwords


        data = pd.read_csv(self.filename)
        data.dropna(inplace = True)
        title_keys = data.title_keyword.apply(simple_preprocess)
        data['title_new'] = data.title_keyword.apply(preprocessing_text)


        # model = Word2Vec(vector_size=10, window=1, min_count=2, workers=4)
        self.model = Word2Vec(
            window = 2,
        )
        self.model.build_vocab(data.title_new)
        self.model.train(data.title_new, total_examples = self.model.corpus_count, epochs = self.model.epochs)


    def get_similar(self, key):

        similar_words = [word[0] for word in (self.model).wv.most_similar(key, topn = 100)]

        print("Top 5 similar words :", similar_words[:5])
        print("\nLength of the list :", len(similar_words))



if __name__ == '__main__':
    model = SimilarityModel("./sample.csv")
    model.create_model()

    key = input("Enter the keyword : ")
    model.get_similar(key)
