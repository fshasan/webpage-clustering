from py_files.webpage_clusterer import WebpageClusterer

open_tabs = [
    "https://computermania.com.bd/product-category/asus-laptop-price-in-bd/asus-tuf/",
    "https://www.startech.com.bd/component/CPU-Cooler/gamdias-cpu-cooler",
    "https://techlandbd.com/smartphone-and-tablet/tablet-pc",
    "https://www.cineplexbd.com/show-time",

]

clusterer = WebpageClusterer(open_tabs)

grouped_tabs= clusterer.cluster_tabs()

print("Clustered Tabs:")
print(grouped_tabs)
