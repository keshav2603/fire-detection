from icrawler.builtin import BingImageCrawler, GoogleImageCrawler
import os

save_dir = "data/no_fire"
os.makedirs(save_dir, exist_ok=True)

# 10 queries x 40 images = ~400 images total
queries = [
    "indoor living room",
    "outdoor street daytime",
    "forest trees green",
    "kitchen interior",
    "sunset sky orange red",    # hard negative
    "autumn leaves orange",     # hard negative
    "red car street",           # hard negative
    "warm light lamp room",     # hard negative
    "red flowers close up",     # hard negative
    "park outdoor daytime",
]

for i, query in enumerate(queries):
    print(f"[{i+1}/{len(queries)}] {query}")
    
    # bing = 20 images
    BingImageCrawler(
        storage={"root_dir": save_dir},
        feeder_threads=1, parser_threads=1, downloader_threads=2
    ).crawl(keyword=query, max_num=20)

    # google = 20 images
    GoogleImageCrawler(
        storage={"root_dir": save_dir},
        feeder_threads=1, parser_threads=1, downloader_threads=2
    ).crawl(keyword=query, max_num=20)

    print(f"  ✓ done  |  total so far: {len(os.listdir(save_dir))}")

print(f"\nFinal count: {len(os.listdir(save_dir))} images in no_fire/")