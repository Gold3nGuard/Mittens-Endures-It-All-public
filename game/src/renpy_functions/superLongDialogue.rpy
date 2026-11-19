define punctuation = "?!."

init python:
    def combineEllipses(sentences):
        """Combines text that were unintentionally seperated by ellipses
        """

        indicies_to_combine = []
        for i, s in enumerate(sentences):
            if s[-3:] == "...":
                indicies_to_combine.append(i)

        while indicies_to_combine != []:
            i = indicies_to_combine.pop()
            if i+1 < len(sentences):
                sentences[i] = sentences[i] + " " + sentences[i+1]
                sentences.pop(i+1)

        return sentences


label superLongDialogue(speaker, speech):
    # Displays super long dialogue by breaking it up into sentences

    $ sentences = [(s.strip() + ("." if s[-1] not in punctuation else "")) + ("." if s[-2:] == ".." else "") for s in speech.split(". ") if s.strip() != ""]
    $ sentences = combineEllipses(sentences)
    $ n = len(sentences)
    $ i = 0

    if speaker is None:
        while i < n:
            "[sentences[i]]"
            $ i += 1
    else:
        while i < n:
            speaker "[sentences[i]]"
            $ i += 1
            
