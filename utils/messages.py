import random


def funny_message():
    """ returns a random funny sentance """
    msg = "The {word[adjective1]} {word[noun1]} {word[verb]} the {word[adjective2]} {word[noun2]}."
    return msg.format(word=dict(verb=_get_random_word('verb'),
                                noun1=_get_random_word('noun'),
                                noun2=_get_random_word('noun'),
                                adjective1=_get_random_word('adjective'),
                                adjective2=_get_random_word('adjective')))


def _get_random_word(type_of_word):
    know_words = dict(
        noun=list(
            {'Bob', 'cat', 'dog', 'celery', 'neighbor', 'pickle', 'dave', 'page', 'fish', 'turnip',
             'collar', 'duke', 'cardboard', 'finger', 'hat', 'bloke', 'Richard', 'boss', 'boot', 'program'}),
        verb=list(
            {'reminded', 'soothed', 'united', 'bore', 'fried', 'announced', 'interrupted', 'watered', 'danced',
             'scraped', 'borked', 'melted', 'scribbled', 'smeared', 'placed', 'smelling', 'yawned', 'bricked',
             'interfered with', 'crashing', 'slapped', 'repeating', 'pop', 'pressed', 'kicked', 'warned', 'arrived',
             'disapproving', 'waved', 'squealing', 'marched on', 'purged'}),
        adjective=list(
            {'rich', 'slimy', 'malicious', 'female', 'instinctive', 'unaccountable', 'illegal', 'common', 'garrulous',
             'dramatic', 'glistening', 'hurried', 'sophisticated', 'rampant', 'low', 'handsome', 'misty', 'imaginary',
             'obedient', 'extra-large', 'tall', 'evasive', 'aloof', 'futuristic', 'ninth', 'hospitable', 'towering',
             'nifty', 'mindless', 'unarmed', 'cool', 'breezy', 'little', 'envious', 'clumsy', 'sloppy', 'high-pitched',
             'sassy', 'high', 'psychotic', 'hollow', 'supreme', 'messy', 'funny', 'foregoing', 'curly', 'afraid',
             'taboo', 'amused', 'loose'}))
    return random.choice(know_words[type_of_word])
