import pandas as pd
import re

count = 0;
so_df = pd.read_csv('stack-overflow.csv')

# Read each tag from most_common_tags file one by one
for tag in pd.read_csv('most_common_tags.csv', chunksize=1):
	tag_present = pd.DataFrame([])
	tag_notpresent = pd.DataFrame([])
	final_dataset = pd.DataFrame([])
	common_tag = str(tag['tag'].tolist()[0])
	print (common_tag)
	
	# Filter the stack-overflow dataset in which tag is present
	result_dataset = so_df['tags'].str.contains('<' + re.escape(common_tag) + '>')
	tag_present = so_df[result_dataset].copy()
	tag_present['common_tag'] = 'present ' + common_tag

	# Copy dataset in which the tags are not present
	tag_notpresent = so_df[~result_dataset].copy()
	tag_notpresent['common_tag'] = 'notpresent ' + common_tag

	# Append 60 random questions in which tag is present
	final_dataset = final_dataset.append(tag_present.sample(n=60, random_state=42))
	# Append 1500 random questions in which tag is not present
	final_dataset = final_dataset.append(tag_notpresent.sample(n=1500, random_state=42))
	if count == 0:
		header = True
	else:
		header = False 
	final_dataset.to_csv("train_dataset.csv", encoding='utf-8', mode = 'a', index=False, header=header)
	count += 1