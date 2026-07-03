import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(query, key, value):
    """
    query: Matriz de consultas [batch, seq_len, d_k]
    key:   Matriz de claves   [batch, seq_len, d_k]
    value: Matriz de valores  [batch, seq_len, d_v]
    """
    d_k = query.size(-1)
    
    # 1. Producto punto entre Query y Key traspuesta
    scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
    
    # 2. Aplicar Softmax para obtener pesos de atención (suman 1)
    attention_weights = F.softmax(scores, dim=-1)
    
    # 3. Multiplicar pesos por los valores
    output = torch.matmul(attention_weights, value)
    return output, attention_weights

# --- Ejemplo de uso ---
seq_len, d_k = 3, 4 # 3 palabras, dimensión 4
q = torch.rand(1, seq_len, d_k)
k = torch.rand(1, seq_len, d_k)
v = torch.rand(1, seq_len, d_k)

output, weights = scaled_dot_product_attention(q, k, v)

print("Pesos de Atención (Matriz de enfoque):\n", weights)
print("\nSalida procesada:\n", output)