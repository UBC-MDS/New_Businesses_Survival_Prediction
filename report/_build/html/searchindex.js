Search.setIndex({"docnames": ["report_business_survival_prediction"], "filenames": ["report_business_survival_prediction.ipynb"], "titles": ["Predicting the Survival of New Businesses in Vancouver"], "terms": {"By": 0, "arturo": 0, "boquin": 0, "beth": 0, "ou": 0, "yang": 0, "prabhjit": 0, "thind": 0, "weiran": 0, "zhao": 0, "2023": 0, "12": 0, "03": 0, "import": 0, "panda": 0, "pd": 0, "from": 0, "myst_nb": 0, "glue": 0, "pickl": 0, "test_scores_df": 0, "read_csv": 0, "tabl": 0, "test_scor": 0, "csv": 0, "round": 0, "2": 0, "accuraci": 0, "valu": 0, "0": 0, "displai": 0, "fals": 0, "f1": 0, "f1_score": 0, "style": 0, "format": 0, "hide": 0, "confusion_df": 0, "confusion_matrix": 0, "index_col": 0, "renam": 0, "column": 0, "inplac": 0, "true": 0, "index": 0, "name": 0, "actual": 0, "label": 0, "total": 0, "sum": 0, "axi": 0, "1": 0, "pred_correct": 0, "false_neg": 0, "open": 0, "model": 0, "lr_license_renewal_pipelin": 0, "rb": 0, "f": 0, "business_fit": 0, "load": 0, "thi": 0, "studi": 0, "focus": 0, "forecast": 0, "viabil": 0, "analyz": 0, "rang": 0, "econom": 0, "demograph": 0, "variabl": 0, "we": 0, "util": 0, "data": 0, "citi": 0, "licens": 0, "registri": 0, "supplementari": 0, "sourc": 0, "statist": 0, "canada": 0, "assess": 0, "impact": 0, "factor": 0, "like": 0, "locat": 0, "industri": 0, "type": 0, "condit": 0, "longev": 0, "our": 0, "approach": 0, "involv": 0, "develop": 0, "classif": 0, "us": 0, "logist": 0, "regress": 0, "leverag": 0, "aforement": 0, "ascertain": 0, "likelihood": 0, "sustain": 0, "oper": 0, "over": 0, "two": 0, "year": 0, "period": 0, "The": 0, "effect": 0, "final": 0, "wa": 0, "substanti": 0, "through": 0, "its": 0, "perform": 0, "separ": 0, "test": 0, "achiev": 0, "an": 0, "77": 0, "out": 0, "23817": 0, "case": 0, "accur": 0, "18442": 0, "nevertheless": 0, "incorrectli": 0, "classifi": 0, "862": 0, "neg": 0, "erron": 0, "indic": 0, "certain": 0, "would": 0, "thrive": 0, "when": 0, "thei": 0, "were": 0, "risk": 0, "These": 0, "inaccuraci": 0, "could": 0, "potenti": 0, "lead": 0, "detriment": 0, "outcom": 0, "especi": 0, "scenario": 0, "target": 0, "intervent": 0, "therefor": 0, "advoc": 0, "further": 0, "research": 0, "refin": 0, "befor": 0, "implement": 0, "tool": 0, "polici": 0, "maker": 0, "author": 0, "environ": 0, "dynam": 0, "influenc": 0, "trend": 0, "chang": 0, "plan": 0, "essenti": 0, "both": 0, "policymak": 0, "entrepreneur": 0, "central": 0, "question": 0, "project": 0, "can": 0, "To": 0, "answer": 0, "s": 0, "portal": 0, "supplement": 0, "censu": 0, "conduct": 0, "python": 0, "packag": 0, "includ": 0, "mckinnei": 0, "2010": 0, "altair": 0, "vanderpla": 0, "2018": 0, "scikit": 0, "learn": 0, "pedregosa": 0, "et": 0, "al": 0, "2011": 0, "primari": 0, "which": 0, "regularli": 0, "updat": 0, "renew": 0, "termin": 0, "enhanc": 0, "extern": 0, "provid": 0, "comprehens": 0, "view": 0, "methodolog": 0, "emploi": 0, "variou": 0, "divid": 0, "70": 0, "alloc": 0, "train": 0, "30": 0, "evalu": 0, "other": 0, "relev": 0, "metric": 0, "emphas": 0, "reduc": 0, "due": 0, "high": 0, "stake": 0, "initi": 0, "reveal": 0, "signific": 0, "correl": 0, "between": 0, "show": 0, "promis": 0, "though": 0, "presenc": 0, "warrant": 0, "investig": 0, "find": 0, "suggest": 0, "valuabl": 0, "aid": 0, "decis": 0, "make": 0, "look": 0, "featur": 0, "might": 0, "statu": 0, "plot": 0, "distribut": 0, "each": 0, "predictor": 0, "colour": 0, "class": 0, "fail": 0, "more": 0, "than": 0, "yr": 0, "green": 0, "orang": 0, "In": 0, "do": 0, "what": 0, "aim": 0, "omit": 0, "binari": 0, "have": 0, "similar": 0, "pattern": 0, "wai": 0, "mean": 0, "power": 0, "tell": 0, "apart": 0, "fit": 0, "them": 0, "comparison": 0, "numer": 0, "larg": 0, "varianc": 0, "feepaid": 0, "For": 0, "categor": 0, "gener": 0, "histogram": 0, "see": 0, "frequenc": 0, "observ": 0, "underli": 0, "where": 0, "spread": 0, "local": 0, "area": 0, "buiness": 0, "natur": 0, "appropri": 0, "whether": 0, "easier": 0, "interpret": 0, "anoth": 0, "reason": 0, "why": 0, "chose": 0, "It": 0, "linear": 0, "coeffici": 0, "easi": 0, "crucial": 0, "understand": 0, "ar": 0, "remain": 0, "valid": 0, "precis": 0, "recal": 0, "770000": 0, "860000": 0, "790000": 0, "950000": 0, "score": 0, "best": 0, "quit": 0, "well": 0, "overal": 0, "86": 0, "come": 0, "confus": 0, "matrix": 0, "onli": 0, "made": 0, "mistak": 0, "howev": 0, "all": 0, "given": 0, "implic": 0, "ha": 0, "economi": 0, "figur": 0, "number": 0, "insight": 0, "care": 0, "select": 0, "yield": 0, "also": 0, "highlight": 0, "critic": 0, "while": 0, "good": 0, "incorpor": 0, "addit": 0, "advanc": 0, "techniqu": 0, "deeper": 0, "tempor": 0, "even": 0, "nuanc": 0, "significantli": 0, "strateg": 0, "urban": 0, "demonstr": 0, "practic": 0, "applic": 0, "scienc": 0, "real": 0, "world": 0, "licenc": 0, "http": 0, "opendata": 0, "ca": 0, "explor": 0, "inform": 0, "disjunct": 0, "businesssubtyp": 0, "folderyear": 0, "23": 0, "www150": 0, "statcan": 0, "gc": 0, "n1": 0, "en": 0, "mm": 0, "structur": 0, "comput": 0, "proceed": 0, "9th": 0, "confer": 0, "edit": 0, "st\u00e9fan": 0, "van": 0, "der": 0, "walt": 0, "jarrod": 0, "millman": 0, "51": 0, "56": 0, "j": 0, "interact": 0, "visual": 0, "journal": 0, "softwar": 0, "3": 0, "32": 0, "p": 0, "1057": 0, "machin": 0, "oct": 0, "pp": 0, "2825": 0, "2830": 0}, "objects": {}, "objtypes": {}, "objnames": {}, "titleterms": {"predict": 0, "surviv": 0, "new": 0, "busi": 0, "vancouv": 0, "summari": 0, "introduct": 0, "method": 0, "dataset": 0, "descript": 0, "analysi": 0, "result": 0, "discuss": 0, "improv": 0, "refer": 0}, "envversion": {"sphinx.domains.c": 2, "sphinx.domains.changeset": 1, "sphinx.domains.citation": 1, "sphinx.domains.cpp": 6, "sphinx.domains.index": 1, "sphinx.domains.javascript": 2, "sphinx.domains.math": 2, "sphinx.domains.python": 3, "sphinx.domains.rst": 2, "sphinx.domains.std": 2, "sphinx.ext.intersphinx": 1, "sphinxcontrib.bibtex": 9, "sphinx": 56}})