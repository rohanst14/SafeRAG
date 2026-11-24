import math,re
from collections import Counter

def retrieve(question, documents, k=3):
    """Rank document text by cosine similarity of token counts."""
    if k < 1: raise ValueError("k must be positive")
    q=Counter(re.findall(r"\w+",question.lower()))
    rows=[]
    for key,text in documents.items():
        d=Counter(re.findall(r"\w+",text.lower()))
        norm=math.sqrt(sum(v*v for v in q.values())*sum(v*v for v in d.values()))
        rows.append((sum(v*d[t] for t,v in q.items())/norm if norm else 0.,key,text))
    return sorted(rows,key=lambda x:(-x[0],x[1]))[:k]

def answer(question,documents,threshold=.2):
    if not 0<=threshold<=1: raise ValueError("invalid threshold")
    hits=retrieve(question,documents,1)
    if not hits or hits[0][0]<=0 or hits[0][0]<threshold:
        return {"answer":None,"citations":[],"abstained":True}
    score,key,text=hits[0]
    return {"answer":text,"citations":[key],"similarity":score,"abstained":False}
