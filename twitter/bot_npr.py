def npr_scrape():
    """Scrape articles from npr.org"""

    #fetch & save page info to r
    url = 'https://npr.org'
    r = requests.get(url, headers=HEADERS)
    #r.content 'inspect element' source html, pass to fromstring (lxml library)
    tree = fromstring(r.content)
    links = tree.xpath('//section[@class="featured-group"]//div[@class="story-text"]/a/@href')
    print(links)

    #fetch paragraphs and extract text
    for link in links:
        r = requests.get(link, headers=HEADERS)
        page_tree = fromstring(r.content)
        paragraphs = page_tree.xpath('//div[@class="storytext"]/p')
        paragraph = extract_text_paragraph(paragraphs)
        text = extract_text(paragraph)

        if not text:
            continue

        #yield instead of return to avoid always getting first article in list and fewer requests
        yield '"%s" %s' % (text, link)