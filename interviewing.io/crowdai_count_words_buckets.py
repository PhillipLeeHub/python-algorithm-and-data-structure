'''
  Given a URL and a pattern, return a "time series" of words at that URL matching the given prefix. Any space character should be considered a word delimeter.
  Sample result for get_time_series_by_url("https://crowdai-text.s3.amazonaws.com/disc.txt", "th"): [(x,y), ...]

  [(1,match_count),(2,match_count)]


The Risk of Discovery

January 2017

Because biographies of famous scientists tend to edit out their mistakes, we underestimate the degree of risk they were willing to take. And because anything a famous scientist did that wasn't a mistake has probably now become the conventional wisdom, those choices don't seem risky either.

Biographies of Newton, for example, understandably focus more on physics than alchemy or theology. The impression we get is that his unerring judgment led him straight to truths no one else had noticed. How to explain all the time he spent on alchemy and theology? Well, smart people are often kind of crazy.

But maybe there is a simpler explanation. Maybe the smartness and the craziness were not as separate as we think. Physics seems to us a promising thing to work on, and alchemy and theology obvious wastes of time. But that's because we know how things turned out. In Newton's day the three problems seemed roughly equally promising. No one knew yet what the payoff would be for inventing what we now call physics; if they had, more people would have been working on it. And alchemy and theology were still then in the category Marc Andreessen would describe as "huge, if true."

Newton made three bets. One of them worked. But they were all risky.

'''

'''
More error checking
Add documentation/comments
Check edge cases
Limit the user input as much as possible(validate user input)

Known return for error/throw error?
'''
import requests
from typing import List, Tuple


def get_time_series_by_url(url: str, pattern: str, bucket_size: int = 60) -> List[Tuple[int, int]]:
    text_data = requests.get(url)
    if text_data.status_code != 200:
        raise Exception('URL request failed with status code: ', text_data.status_code)

    word_list = text_data.text.split(' ')

    remainder = 0 if len(word_list) % bucket_size == 0 else 1
    num_buckets = len(word_list) // bucket_size + remainder
    result_list = []
    bucket_index = 0
    match_count = 0

    for index, word in enumerate(word_list):
        if pattern == word:
            match_count += 1

        if index % bucket_size == 0 and index != 0:
            result_list.append((bucket_index, match_count))
            word_index = 0
            match_count = 0
            bucket_index += 1

    if match_count:
        result_list.append((bucket_index, match_count))

    return result_list


url = 'https://crowdai-text.s3.amazonaws.com/disc.txt'
print(get_time_series_by_url(url, 'to'))

assert get_time_series_by_url(url, 'to') == [(0, 2), (1, 2), (2, 2)]






