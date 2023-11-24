#Author: Prabhjit Thind
FROM quay.io/jupyter/minimal-notebook:2023-11-19

RUN conda install -y matplotlib=3.8.1 \
    scikit-learn=1.3.2 \
    python=3.12.0 \
    pandas=2.1.3 \
    altair=5.1.2 \
    ipykernel=6.26.0 \
    vegafusion-python-embed[version='>=1.4.0']=1.4.3 \
    vegafusion[version='>=1.4.0']=1.4.3 \
    vl-convert-python[version='>=0.14.0']=1.1.0


