# Crawling-Naverblog

## Requirements

- Python 2.7
- Install [scrapy](http://scrapy.org)

        $pip install scrapy

## Items

- The item is defined in the class:

        naverblog.items.NaverblogItem

- See the source code for more details

## Spider : naver

- The `naver` spider scrapes the naverblog post (blog.naver.com)
- This spider crawls the entire blog.naver.com site (defined in the `start_urls` attribute)
- The basic form of a website : 

        "http://section.blog.naver.com/sub/PostListByDirectory.nhn?option.page.currentPage=1&option.templateKind=0&option.directorySeq=5&option.viewType=default&option.orderBy=date&option.latestOnly=0"

- `currentPage`is in the range of 1 to 100 and `directorySeq`(=Category) is in the range of 5 to 35  
- So, if you run the spider regularly (with `scrapy crawl naver`) it will scrape 3,100 pages.

## Pipelines

- This project uses a pipeline to extract all blog posts in a specific date(ex '2015-01-14')
- This pipeline is defined in the class:

        naverblog.pipelines.NaverblogPipeline

- So, before run the spider, check the pipeline source code

## Run
### Data crawling

        $ cd naverblog
        $ scrapy crawl naver -o naverblog.csv -t csv
        $ scrapy crawl naver -o naverblog.json -t json

- Be careful of running the code twice because the json file gets appended, rather than overwritten.

## Author

- [jinbae Im](http://github.com/jinbae)
