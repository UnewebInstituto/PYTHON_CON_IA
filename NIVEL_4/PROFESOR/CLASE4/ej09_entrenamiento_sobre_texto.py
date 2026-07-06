from google.colab import drive
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import numpy as np

# 1. Cargar el dataset desde tu archivo CSV
# 1. Carga de datos desde Drive
drive.mount('/content/drive')
dataset = load_dataset('csv', data_files='/content/drive/MyDrive/data/dataset_arroz_finetunig.csv')
# Dividir en entrenamiento (80%) y validación (20%)
dataset = dataset['train'].train_test_split(test_size=0.2)

# 2. Cargar el Tokenizer (convierte texto a números para el modelo)
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize_function(examples):
    return tokenizer(examples["texto_original"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# 3. Cargar el modelo base
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# 4. Configurar el entrenamiento
training_args = TrainingArguments(
    output_dir="/content/drive/MyDrive/resultado_entrenamiento",
    eval_strategy="epoch",
    per_device_train_batch_size=8,
    num_train_epochs=3, # Pocas épocas para evitar sobreajuste
    save_strategy="epoch"
)

# 5. Entrenar
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
)

trainer.train()
