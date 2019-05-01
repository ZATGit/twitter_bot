def extract_text_paragraph(paragraphs):
    """Extracts text from paragraph elements and returns random tokenized paragraph."""

    paragraphs = [paragraph.text_content() for paragraph in paragraphs if paragraph.text_content()]
    paragraph = random.choice(paragraphs)

    return tokenizer.tokenize(paragraph)

def extract_sentence(paragraph):
    """Returns random text if correct length from a paragraph."""

    # sort text from random paragraph.
    for _ in range(10):
        text = random.choice(paragraph)
        if text and 180 < len(text) < 280:
            return text

    #skip to next article if no matching sentence in 10 attempts.
    return None
