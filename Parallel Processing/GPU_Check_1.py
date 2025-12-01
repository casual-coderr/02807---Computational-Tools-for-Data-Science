
import os
# Fix OpenMP library conflict
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

import torch

# Check if CUDA is available
print("CUDA available:", torch.cuda.is_available())

# GPU name and CUDA core count
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    print("CUDA cores (approx):", torch.cuda.get_device_properties(0).total_memory // 1024**2, "GB VRAM")
    print("Compute Capability:", torch.cuda.get_device_capability(0))  # Should show (8, 6) for RTX 3050 Ti