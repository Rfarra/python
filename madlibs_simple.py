def bohemian_rhapsody_madlib(
    adjective,
    plural_noun,
    past_verb,
    another_adjective,
    another_noun,
    one_more_noun,
    another_verb,
    emotion,
):
    madlib = f"""
    Is this the real {plural_noun}?
    Is this just {adjective}?
    Caught in a {past_verb} slide,
    No escape from reality.
    Open your eyes,
    Look up to the skies and see,
    I'm just a poor {another_noun}, I need no sympathy,
    Because I'm easy come, easy go,
    Little high, little low,
    Anyway the wind {another_verb} doesn't really matter to me, to me.

    Mama, just killed a {one_more_noun},
    Put a gun against his head,
    Pulled my trigger, now he's {another_adjective}.
    Mama, life had"""

    print(madlib)


# Collect user input
adjective = input("Enter an adjective: ")
plural_noun = input("Enter a noun (plural): ")
past_verb = input("Enter a verb (past tense): ")
another_adjective = input("Enter another adjective: ")
another_noun = input("Enter another noun: ")
one_more_noun = input("Enter one more noun: ")
another_verb = input("Enter another verb: ")
emotion = input("Enter an emotion: ")

# Call the bohemian_rhapsody_madlib function with user inputs
bohemian_rhapsody_madlib(
    adjective,
    plural_noun,
    past_verb,
    another_adjective,
    another_noun,
    one_more_noun,
    another_verb,
    emotion,
)
