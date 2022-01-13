# [Inception](https://inception-project.github.io/)

A semantic annotation platform offering intelligent assistance and knowledge management

The annotation of specific semantic phenomena often require compiling task-specific corpora and creating or extending task-specific knowledge bases. Presently, researchers require a broad range of skills and tools to address such semantic annotation tasks.

In the recently funded INCEpTION project, UKP Lab at TU Darmstadt aims towards building an annotation platform that incorporates all the related tasks into a joint web-based platform.

## Setup
- https://inception-project.github.io//releases/0.8.4/docs/admin-guide.
- https://github.com/inception-project/external-recommender-spacy

```
# to download spacys models
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
python -m spacy download en_core_web_lg
```

```
# methods to load model and disable parsing
import en_core_web_sm
nlp = en_core_web_sm.load(disable=['parser'])
#nlp = spacy.load("en_core_web_sm", disable=['parser'])
```