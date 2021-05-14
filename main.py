from crawler import crawl
import multiprocessing


if __name__ == '__main__':
    batch = 50
    length = 3100
    for i in range(0, length, batch):
        with multiprocessing.Pool(processes=batch) as pool:
            result = pool.starmap(crawl, zip(range(i, i + batch)))
            for v in result:
                if v is not None:
                    print(v)