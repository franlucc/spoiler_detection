import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

book_review_df = pd.read_json('goodreads_reviews_spoiler.json', lines=True)

# Bookreads dataset statistics

spoilers = book_review_df[book_review_df['has_spoiler'] == True]
no_spoilers = book_review_df[book_review_df['has_spoiler'] == False]

# plot dataset
plt.figure(0)
plt.pie([len(spoilers), len(no_spoilers)], autopct='%1.1f%%')
plt.title('All Goodreads Reviews')
plt.legend(['spoilers', 'no spoilers'])
plt.savefig("full_goodreads.png")
print(book_review_df.info())
print(len(spoilers), len(no_spoilers))

# balance dataset (remove neg labels)

# get indices of reviews with no spoilers
SPLIT = 89627
no_spoilers_indices = book_review_df.index[book_review_df['has_spoiler'] == False]
removed_indices = no_spoilers_indices[:SPLIT]
no_spoilers = book_review_df.iloc[removed_indices]

# plot dataset with neg labels removed
plt.figure(1)
plt.pie([len(spoilers), len(no_spoilers)], autopct='%1.1f%%')
plt.title('Balanced Goodreads Reviews')
plt.legend(['spoilers', 'no spoilers'])
plt.savefig("balanced_goodreads.png")

# get new dataframe
balanced_book_review_df = spoilers.append(no_spoilers, ignore_index=True)

print(balanced_book_review_df.info())
print(len(spoilers), len(no_spoilers))

# save to csv
balanced_book_review_df.to_csv("balanced_goodreads.csv")
