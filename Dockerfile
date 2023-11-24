#Author: Prabhjit Thind
FROM quay.io/jupyter/minimal-notebook:2023-11-19

RUN conda install -y matplotlib=3.8.1 \
    scikit-learn=1.3.2

