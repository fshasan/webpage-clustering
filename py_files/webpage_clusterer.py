from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np
import re

class WebpageClusterer:
    def __init__(self, urls):
        self.urls = urls
        self.page_texts = self._collect_page_texts()

    def _get_page_text(self, url):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.headless = True
        chrome_options.add_argument("--window-size=1920,1200")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        page_text = driver.page_source
        driver.quit()
        return page_text

    def _clean_text(self, text):
        cleaned_text = re.sub('<.*?>', '', text)
        cleaned_text = re.sub('\s+', ' ', cleaned_text)
        return cleaned_text

    def _collect_page_texts(self):
        return [self._clean_text(self._get_page_text(url)) for url in self.urls]

    def cluster_tabs(self):
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(self.page_texts)

        pca = PCA(n_components=2)
        reduced_X = pca.fit_transform(X.toarray())

        kmeans = KMeans(n_clusters=3)
        clusters = kmeans.fit_predict(reduced_X)

        grouped_tabs = {cluster: [] for cluster in set(clusters)}
        for i, url in enumerate(self.urls):
            grouped_tabs[clusters[i]].append(url)

        return grouped_tabs
