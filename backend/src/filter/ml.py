from transformers import pipeline

pipe = pipeline("text-classification", model="eyeonyou/logs")


def get_recommendations(sequence):
    return pipe(sequence, top_k=4)