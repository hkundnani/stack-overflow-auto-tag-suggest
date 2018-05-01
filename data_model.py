import pandas as pd
import matplotlib.pyplot as plt

original_df = pd.read_csv('stack-overflow.csv')

def update_val(row):
	tag_processed = ','.join(filter(None, unicode(row['tags'].replace('<', '')).split('>')))
	length = len(str(tag_processed).split(','))
	tags_stat[length]['question_count'] += 1
	tags_stat[length]['view_count'] += int(row['view_count'])

tags_stat = {
	1: {
	'question_count': 0,
	'view_count': 0
	},
	2: {
	'question_count': 0,
	'view_count': 0
	},
	3: {
	'question_count': 0,
	'view_count': 0
	},
	4: {
	'question_count': 0,
	'view_count': 0
	},
	5: {
	'question_count': 0,
	'view_count': 0
	}
}

for index, row in original_df.iterrows():
	update_val(row)

print (tags_stat)
tags = [1, 2, 3, 4, 5]

average_views = []

for tag in tags:
	average_views.append(tags_stat[tag]['view_count'] / tags_stat[tag]['question_count']) 

print (average_views)

plt.plot(tags, average_views)
plt.ylabel('Average number of views')
plt.xlabel('Number of tags')
plt.ylim([100, 900])
plt.grid(True)
plt.show()