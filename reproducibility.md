# Pipeline Setup

## Python environment

conda create -n enzyme_mining python=3.10
conda activate enzyme_mining

pip install biopython pandas matplotlib seaborn jupyter

---

## SignalP installation

Download:
https://services.healthtech.dtu.dk/services/SignalP-6.0/

Run prediction:

signalp6 \
--fastafile data/proteomes/trichoderma_reesei_QM6a.fasta \
--organism euk \
--mode slow-sequential \
--model_dir tools/signalp6_slow_sequential/models \
--output_dir results/signalp

---

## CAZyme annotation

Install HMMER (WSL):

sudo apt install hmmer

Download dbCAN database:
https://bcb.unl.edu/dbCAN2/download/

Run hmmscan (required installing Ubuntu through WSL):

hmmscan \
--domtblout results/dbcan_hits.txt \
tools/dbCAN-HMMdb-V14.txt \
results/secretome.fasta