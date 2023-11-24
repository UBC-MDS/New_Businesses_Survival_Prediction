#Author: Prabhjit Thind, Beth Ou Yang, Arturo Boquin, Weiran Zhao.
FROM quay.io/jupyter/minimal-notebook:2023-11-19

RUN conda install -y matplotlib=3.8.1 \
    scikit-learn=1.3.2 \
    pandas=2.1.3 \
    altair=5.1.2 \
    ipykernel=6.26.0 \
    vegafusion-python-embed=1.4.3 \
    vegafusion=1.4.3 \
    vl-convert-python=1.1.0 \
    python=3.11.6

COPY . /home/jovyan/DSCI_522_group1/