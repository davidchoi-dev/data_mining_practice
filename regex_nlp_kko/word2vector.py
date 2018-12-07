from gensim.models.word2vec import Word2Vec
import ast
import pandas as pd


tokens = pd.read_csv("./result/all_token_1.csv")
print(len(tokens))
tokens = tokens[tokens["contents"] != "이모티콘"]
tokens = tokens[tokens["contents"] != "사진"]
tokens = tokens[tokens["contents"] != "동영상"]
tokens = tokens[tokens["contents"].apply(lambda x: 'http' not in x)]

print(len(tokens))

sentence = tokens["token"].apply(lambda x: ast.literal_eval(x)).tolist()
print(sentence[0:100])
model = Word2Vec(sentence, min_count=15, iter=10)
model.init_sims(replace=True)

print("용돈과 관련된 키워드 : ", model.most_similar("용돈"))
print("지영와 관련된 키워드 : ", model.most_similar("졍이"))
print("찬호와 관련된 키워드 : ", model.most_similar("쭈니"))

model.save("a.model")