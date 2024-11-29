import pymorphy3

morph = pymorphy3.MorphAnalyzer()

def analyze_verb(word):
    parsed = morph.parse(word)[0]
    if 'VERB' in parsed.tag or 'INFN' in parsed.tag:
        return {
            "word": word,
            "time": parsed.tag.tense,  # час 
            "number": parsed.tag.number,  # однина/множина
            "gender": parsed.tag.gender if parsed.tag.tense == 'past' else None  # рід
        }
    else:
        return {"error": f"'{word}' is not a verb"}