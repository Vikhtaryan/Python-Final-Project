import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re
from collections import Counter
import os

def load_stopwords(local_file='english_stopwords.txt'):
    """
    Load stopwords locally if exists, else fall back to a small predefined set.
    To avoid 404 errors from remote files.
    """
    if os.path.exists(local_file):
        print(f"Loading stopwords from local file: {local_file}")
        stopwords = set(pd.read_csv(local_file, header=None)[0].values)
    else:
        print("Local stopwords file not found, using minimal default stopwords set.")
        stopwords = set([
            'the', 'and', 'for', 'are', 'with', 'that', 'this', 'from', 'was',
            'were', 'which', 'has', 'have', 'had', 'not', 'but', 'they', 'his',
            'her', 'she', 'him'  # etc. - add more as needed
        ])
    return stopwords

def main():
    metadata_path = "metadata.csv.zip"  # Change to your downloaded file path
    print("Loading dataset...")
    df = pd.read_csv(metadata_path, low_memory=False)
    print(f"Dataset loaded with shape: {df.shape}\n")
    
    # Basic exploration
    print("Initial head of data:")
    print(df.head(), "\n")
    print("Data types:")
    print(df.dtypes, "\n")
    print("Missing values in important columns:")
    imp_cols = ['cord_uid', 'title', 'abstract', 'publish_time', 'journal']
    print(df[imp_cols].isnull().sum(), "\n")
    print("Basic statistics:")
    print(df.describe(include='all').transpose(), "\n")

    # Drop columns with more than 50% missing data
    missing_ratio = df.isnull().mean()
    cols_to_drop = missing_ratio[missing_ratio > 0.5].index.to_list()
    print(f"Dropping columns with >50% missing values: {cols_to_drop}")
    df.drop(columns=cols_to_drop, inplace=True)

    # Drop rows missing essential data
    df.dropna(subset=['title', 'publish_time'], inplace=True)

    # Convert dates and create features
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['pub_year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].fillna('').apply(lambda x: len(str(x).split()))
    
    print("Data cleaned and prepared:")
    print(df.info())

    # Visualization 1: Papers by year
    pubs_by_year = df['pub_year'].value_counts().sort_index()
    plt.figure(figsize=(10,6))
    sns.lineplot(x=pubs_by_year.index, y=pubs_by_year.values, marker='o')
    plt.title("Number of Papers Published Per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Papers")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("papers_per_year.png", dpi=300)
    print("Saved plot to papers_per_year.png")
    plt.show()

    # Visualization 2: Top 15 journals
    top_journals = df['journal'].value_counts().head(15)
    plt.figure(figsize=(12,7))
    sns.barplot(x=top_journals.values, y=top_journals.index, palette="viridis")
    plt.title("Top 15 Journals Publishing COVID-19 Research")
    plt.xlabel("Number of Papers")
    plt.ylabel("Journal")
    plt.tight_layout()
    plt.savefig("top_journals.png", dpi=300)
    print("Saved plot to top_journals.png")
    plt.show()

    # Visualization 3: Word cloud of titles
    stopwords = load_stopwords()
    
    def clean_and_tokenize(text):
        text = str(text).lower()
        words = re.findall(r'\b\w+\b', text)
        filtered = [word for word in words if word not in stopwords and len(word) > 2]
        return filtered

    all_words = df['title'].dropna().apply(clean_and_tokenize).sum()
    wordcloud_text = ' '.join(all_words)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(wordcloud_text)
    
    plt.figure(figsize=(16,8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud of Paper Titles")
    plt.tight_layout()
    plt.savefig("title_wordcloud.png", dpi=300)
    print("Saved plot to title_wordcloud.png")
    plt.show()

    # Visualization 4: Papers by source (if exists)
    if 'source_x' in df.columns:
        plt.figure(figsize=(12,7))
        source_counts = df['source_x'].value_counts()
        sns.barplot(x=source_counts.values, y=source_counts.index, palette="coolwarm")
        plt.title("Distribution of Paper Counts by Source")
        plt.xlabel("Number of Papers")
        plt.ylabel("Source")
        plt.tight_layout()
        plt.savefig("papers_by_source.png", dpi=300)
        print("Saved plot to papers_by_source.png")
        plt.show()

if __name__ == "__main__":
    main()
import pandas as pd
import matplotlib.pyplot as plt