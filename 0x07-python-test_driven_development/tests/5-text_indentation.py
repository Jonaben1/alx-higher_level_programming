Using ``text_indentation``
-----------------------


First import ``text_indentation``

    >>> text_indentation = __import__('5-text_indentation').text_indentation

Now use it:

Basic usage:
    >>> text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    ... Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    ... Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    ... Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    ... Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    ... rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    ... stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    ... cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    ... beatiorem! Iam ruinas videres""")
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <BLANKLINE>
    Quonam modo?
    <BLANKLINE>
    Utrum igitur tibi litteram videor an totas paginas commovere?
    <BLANKLINE>
    Non autem hoc:
    <BLANKLINE>
    igitur ne illud quidem.
    <BLANKLINE>
    Fortasse id optimum, sed ubi illud:
    <BLANKLINE>
    Plus semper voluptatis?
    <BLANKLINE>
    Teneo, inquit, finem illi videri nihil dolere.
    <BLANKLINE>
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.
    <BLANKLINE>
    Si id dicis, vicimus.
    <BLANKLINE>
    Inde sermone vario sex illa a Dipylo stadia confecimus.
    <BLANKLINE>
    Sin aliud quid voles, postea.
    <BLANKLINE>
    Quae animi affectio suum cuique tribuens atque hanc, quam dico.
    <BLANKLINE>
    Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres

Non string input:
    >>> text_indentation(3)
    Traceback (most recent call last):
    ...
    TypeError: text must be a string

No special char in string input:
    >>> text_indentation("hello")
    hello

QA case:
    >>> text_indentation("Holberton. School? How are you: John")
    Holberton.
    <BLANKLINE>
    School?
    <BLANKLINE>
    How are you:
    <BLANKLINE>
    John

No input:
    >>> text_indentation()
    Traceback (most recent call last):
    ...
    TypeError: text_indentation() missing 1 required positional argument: 'text'

