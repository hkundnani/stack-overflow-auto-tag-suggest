
import pandas as pd
from collections import Counter

chunksize = 100000
count = 0
tag_final = []


for chunk in pd.read_csv("processed_data.csv", chunksize=chunksize):
	tag_list = (chunk['tags'].map(lambda tag: str(tag).split(','))).tolist()
	tag_final = tag_final + [tag for tags in tag_list for tag in tags]
	print ('Chunk {}'.format(count))
	count += 1

most_common_tags = dict([item for item in Counter(tag_final).most_common(850)])
most_common_tags_df = pd.DataFrame(list(most_common_tags.items()), columns=['tag', 'frequency'])
most_common_tags_df.to_csv("most_common_tags.csv", encoding='utf-8', mode = 'a', index=False)

