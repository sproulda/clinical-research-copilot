import re

def sentence_split(text):
    return re.split(r'(?<=[.!?]) +', text)

def overlap_score(sentence, context):
    sentence_words = set(sentence.lower().split())
    context_words = set(context.lower().split())
    if not sentence_words:
        return 0
    return len(sentence_words & context_words) / len(sentence_words)

def hallucination_check(answer, context_chunks, threshold=0.3):
    """
    Flags sentences that don't sufficiently overlap with context.
    """
    context = " ".join(context_chunks)
    sentences = sentence_split(answer)

    hallucinated_sentences = []

    for sentence in sentences:
        score = overlap_score(sentence, context)
        if score < threshold:
            hallucinated_sentences.append({
                "sentence": sentence,
                "overlap_score": score
            })

    return {
        "num_sentences": len(sentences),
        "num_flagged": len(hallucinated_sentences),
        "flagged_sentences": hallucinated_sentences
    }

def answer_quality_score(answer, context_chunks):
    context = " ".join(context_chunks)

    answer_length = len(answer.split())
    context_words = set(context.lower().split())
    answer_words = set(answer.lower().split())

    coverage = len(answer_words & context_words) / max(len(context_words), 1)

    return {
        "answer_length_words": answer_length,
        "context_coverage_ratio": coverage
    }
