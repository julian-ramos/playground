import graphlab
url = 'http://s3.amazonaws.com/dato-datasets/millionsong/song_data.csv'
filename="/Users/julian/Downloads/song_data.csv"
songs = graphlab.SFrame.read_csv(filename)
songs.show()


# songs['year'].mean()
# songs['num_words'] = songs['title'].apply(lambda x: len(x.split(' ')))
# songs.groupby('artist_name', {'total': graphlab.aggregate.COUNT})
# url = 'http://s3.amazonaws.com/dato-datasets/regression/Housing.csv'
# x = graphlab.SFrame.read_csv(url)
# m = graphlab.linear_regression.create(x, target='price')