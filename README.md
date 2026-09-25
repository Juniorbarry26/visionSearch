# VisionSearch 🔍

VisionSearch is a visual image retrieval system built with Python and PyTorch. Instead of assigning a single class label to an image, VisionSearch converts images into embedding vectors and uses those vectors to find visually similar images.

## 🎯 Project Goal

Build practical experience in:

- Machine Learning
- Deep Learning
- Computer Vision
- PyTorch
- Transfer Learning
- Image Embeddings
- Similarity Search
- Metric Learning
- Model Evaluation
- ML experimentation

The project is developed incrementally: start with a pretrained model baseline, then experiment with fine-tuning, transformers, and metric-learning objectives.

## 🧠 How it Works

High-level pipeline:

Dataset → Preprocessing → Vision Model (ResNet / ViT) → Image Embedding → Similarity Search → Top-K Results

Query flow:

Query Image → Preprocessing → Vision Model → Embedding Vector → Compare with Dataset Embeddings → Top-K Similar Images

## 🚀 Development Roadmap

Version 1 — Baseline

- Pretrained ResNet → Feature Extraction → Image Embeddings → Cosine Similarity → Top-K
- Goals: load dataset, preprocess, load model, generate & store embeddings, compute cosine similarity, retrieve similar images

Version 2 — Fine-Tuning

- Fine-tune on the selected dataset and compare against the pretrained baseline

Version 3 — Vision Transformer (ViT)

- Replace backbone with ViT and compare performance with ResNet

Version 4 — Metric Learning

- Explore Triplet Loss, Contrastive Loss, InfoNCE to explicitly learn similarity-preserving embeddings

## 📊 Evaluation

Use retrieval metrics instead of classification accuracy. Primary metrics:

- Recall@1, Recall@5, Recall@10, Recall@50
- Mean Average Precision (mAP)

Example (illustrative only):

| Model | Recall@1 | Recall@5 | Recall@10 |
|---|---:|---:|---:|
| ResNet Baseline | 62% | 79% | 85% |
| Fine-Tuned ResNet | 70% | 86% | 91% |
| ViT | 74% | 89% | 94% |

## 📁 Project Structure

visionSearch/
```
├── data/                # raw, processed, splits
├── datasets/            # dataset classes (image_dataset.py)
├── models/              # backbone, embedding model, projection head
├── training/            # train loop, trainer, checkpointing
├── evaluation/          # metrics, retrieval, evaluation scripts
├── inference/           # embed.py, search.py
├── notebooks/           # experiments & exploration
├── experiments/         # saved experiments and configs
├── scripts/             # prepare_data.py, generate_embeddings.py, evaluate_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

Structure may evolve as the project develops.

## 🛠️ Technologies

- Python, PyTorch, Torchvision
- NumPy, Scikit-learn
- Pillow
- ResNet, Vision Transformer (ViT)
- Jupyter Notebook, Git, virtual environments

Optional tools for later experiments:

- Hugging Face Transformers, OpenCLIP, Weights & Biases, CUDA, vector DBs

## 📚 Dataset

Use a dataset with multiple images per identity/product so retrieval can be evaluated (e.g., multiple views of the same product). Split into training, validation and test sets with care to avoid data leakage.

Example layout for a product:

Product_A/
├── img_001.jpg
├── img_002.jpg
└── img_003.jpg

## 🧪 Experiments

Record for each experiment:

- Model, Dataset, Learning rate, Batch size, Epochs
- Loss function, Embedding dimension
- Recall@1, Recall@5, Recall@10, mAP, training time

Example experiment format:

- Experiment: EXP-003
- Model: ResNet50
- Embedding Dim: 512
- Loss: Triplet Loss
- LR: 1e-4
- Batch Size: 32
- Epochs: 20
- Results: Recall@1, Recall@5, Recall@10, mAP

## 🔬 Research Questions

1. Pretrained vs Fine-Tuned: how much does domain fine-tuning improve retrieval?
2. CNN vs Transformer: how do ResNet and ViT compare for retrieval?
3. Learning Objectives: which metric-learning losses produce the best embeddings?
4. Embedding Dimensionality: trade-offs between accuracy and compute/storage

## ⚙️ Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd visionSearch
```

2. Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the project (examples)

Prepare the dataset:

```bash
python scripts/prepare_data.py
```

Train a model:

```bash
python training/train.py
```

Generate embeddings for the dataset:

```bash
python scripts/generate_embeddings.py
```

Evaluate a trained model:

```bash
python evaluation/evaluate.py
```

Run an image search (example):

```bash
python inference/search.py --image path/to/query.jpg --top_k 10
```

The command-line interface may evolve; check the scripts for exact flags.

## 📈 Example Workflow

Query image → Preprocessing → Vision model → 512-D vector → Similarity calculation → Top-K results (with scores)

## 🧩 Future Improvements

- CLIP-based embeddings
- Contrastive / Triplet learning with hard-negative mining
- Better augmentations
- Approximate nearest neighbors (FAISS / Annoy)
- Vector databases and scalable search
- Text-to-image or multimodal search
- Model compression and GPU optimization

## 🧭 Project Philosophy

Prioritize understanding over unnecessary complexity. For every change ask: what changed, why, and did it improve performance?

## Status

:construction: In Development

Current focus:

- [ ] Set up Python environment
- [ ] Select dataset
- [ ] Explore and clean dataset
- [ ] Build PyTorch dataset
- [ ] Implement baseline
- [ ] Generate embeddings
- [ ] Implement similarity search
- [ ] Evaluate Recall@K
- [ ] Fine-tune model
- [ ] Experiment with ViT
- [ ] Experiment with metric learning
- [ ] Document results

## Author

Alsainey Barry

BSc Computer Science — University of The Gambia

Focus areas: Machine Learning, Deep Learning, Computer Vision, Backend Engineering, Distributed Systems

