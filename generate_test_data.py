import pandas as pd
import re

count = 0;

# Read both original stack-overflow dataset and train dataset 
so_df = pd.read_csv('stack-overflow.csv')
train_df = pd.read_csv('train_dataset_new.csv')
train_id_list = train_df['id'].tolist()
del train_df

# Filter those dataset which are not present in train dataset
filtered_df = (so_df.loc[~so_df['id'].isin(train_id_list)]).copy()
del so_df

# Read each tag from most_common_tags file one by one
for tag in pd.read_csv('most_common_tags.csv', chunksize=1):
	tag_present = pd.DataFrame([])
	tag_notpresent = pd.DataFrame([])
	final_dataset = pd.DataFrame([])
	common_tag = str(tag['tag'].tolist()[0])
	print (common_tag)
	
	# Filter the dataset in which tag is present
	result_dataset = filtered_df['tags'].str.contains('<' + re.escape(common_tag) + '>')
	tag_present = filtered_df[result_dataset].copy()
	tag_present['common_tag'] = 'present ' + common_tag

	# Copy dataset in which the tags are not present
	tag_notpresent = filtered_df[~result_dataset].copy()
	tag_notpresent['common_tag'] = 'notpresent ' + common_tag

	# Append 10 random questions in which tag is present
	final_dataset = final_dataset.append(tag_present.sample(n=10, random_state=42))
	
	# Append 10 random questions in which tag is not present
	final_dataset = final_dataset.append(tag_notpresent.sample(n=10, random_state=42))
	if count == 0:
		header = True
	else:
		header = False 
	final_dataset.to_csv("test_dataset_new.csv", encoding='utf-8', mode = 'a', index=False, header=header)
	count += 1