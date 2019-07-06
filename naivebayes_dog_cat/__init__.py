from naivebayes_dog_cat.naivebayes_naver_movie import NaiveBayesClassfier
context = './data/'
model = NaiveBayesClassfier()
model.train(context+'review_train.csv')
print(model.classfy('내 인생 최악의 영화'))