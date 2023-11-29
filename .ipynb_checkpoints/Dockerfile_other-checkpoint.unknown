# Author : Gretel Tan, Riya Eliza, Charles Xu, Yan Zeng
FROM quay.io/jupyter/minimal-notebook:2023-11-19 

# Did not pin Python version due to conflict
RUN conda install -y matplotlib>=3.8.0 \
pandas>=2.1.1 \
scikit-learn=1.3.1 \
bzip2=1.0.8 \
ca-certificates=2023.7.22 \
libexpat=2.5.0 \
libffi=3.4.2 \
libsqlite=3.44.0 \
libzlib=1.2.13 \ 
openssl=3.1.4 \
pip=23.3.1 \
pytest=7.4.3 \
python \
setuptools=68.2.2 \ 
tk=8.6.13 \
tzdata=2023c \
wheel=0.41.3 \
xz=5.2.6 
 

RUN pip install ucimlrepo==0.0.3 \
altair==5.1.2 \
vl-convert-python \
vegafusion \
vegafusion-jupyter \
vegafusion-python-embed 