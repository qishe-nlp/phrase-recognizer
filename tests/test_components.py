from spacy.language import Language
from phrase_detective import NounPhraseRecognizer, PrepPhraseRecognizer, VerbKnowledgeRecognizer
from phrase_detective import PKG_INDICES
import spacy

@Language.factory("nprecog")
def create_np_parser(nlp: Language, name: str):
  return NounPhraseRecognizer(nlp) 

@Language.factory("pprecog")
def create_pp_parser(nlp: Language, name: str):
  return PrepPhraseRecognizer(nlp) 

@Language.factory("vkbrecog")
def create_vkb_parser(nlp: Language, name: str):
  return VerbKnowledgeRecognizer(nlp) 


def test_nprecog():
  lang = "es"
  sentence = "Qué día más chungo hace, no papá?"
  sentence = "Pero lo más rollo es hacer las fichas por la trade."
  sentence = "Más tragedias encima ahora mismo?"
  sentence = "No es lo mío."
  sentence = "Porqué no haces un timelapse de esos para que todo esto pase rápido?"
  nlp = spacy.load(PKG_INDICES[lang])
  nlp.add_pipe("nprecog")
  doc = nlp(sentence)
  nps = []
  for np in doc._.noun_phrases:
    nps.append(np.text)
  print(nps)
  #assert len(nps) == 1
  #assert nps[0] == "der nächste Supermarkt"


def test_pprecog():
  lang = "es"
  sentence = "Lo que tengo ganas es de que podamos salir a la calle."
  #sentence = "Es que en el ordenador las ponemos a cámara rápida, se llama Timelapse."
  nlp = spacy.load(PKG_INDICES[lang])
  nlp.add_pipe("pprecog")
  doc = nlp(sentence)
  pps = []
  for pp in doc._.prep_phrases:
    pps.append(pp.text)
  print(pps)
  #assert len(pps) == 1
  #assert pps[0] == "auf dem Tisch"

def test_vkbrecog():
  lang = "de"
  sentence = "Diese Katze spielt auf dem Tisch."
  nlp = spacy.load(PKG_INDICES[lang])
  nlp.add_pipe("vkbrecog")
  doc = nlp(sentence)

  for v in doc._.verbs:
    print("TEXT: {}, TAG: {}, FORM: {}, ORIGNAL: {}".format(v.text, v.tag_, spacy.explain(v.tag_), v.lemma_))
  for pp in doc._.passive_phrases:
    print(pp.text)
  for vp in doc._.verb_phrases:
    print(vp)

