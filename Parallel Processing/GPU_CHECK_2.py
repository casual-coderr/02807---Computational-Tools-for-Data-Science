import os
# Fix OpenMP library conflict
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

import torch
import subprocess
import platform

def check_gpu_capabilities():
    print("=" * 50)
    print("GPU Capabilities Check for ML Applications")
    print("=" * 50)
    
    # Check CUDA availability
    cuda_available = torch.cuda.is_available()
    print(f"\nCUDA Available: {cuda_available}")
    
    if not cuda_available:
        print("\nScore: 0/100 - No GPU detected for ML")
        print("Recommendation: Use CPU or consider cloud GPU services")
        return 0
    
    # GPU Information
    gpu_count = torch.cuda.device_count()
    print(f"Number of GPUs: {gpu_count}")
    
    score = 0
    
    for i in range(gpu_count):
        print(f"\n--- GPU {i} ---")
        gpu_name = torch.cuda.get_device_name(i)
        print(f"Name: {gpu_name}")
        
        # Memory
        total_memory = torch.cuda.get_device_properties(i).total_memory / (1024**3)
        print(f"Total Memory: {total_memory:.2f} GB")
        
        # Compute Capability
        major = torch.cuda.get_device_properties(i).major
        minor = torch.cuda.get_device_properties(i).minor
        compute_capability = f"{major}.{minor}"
        print(f"Compute Capability: {compute_capability}")
        
        # CUDA Cores (approximate for common GPUs)
        multi_processor_count = torch.cuda.get_device_properties(i).multi_processor_count
        print(f"Multi-Processors: {multi_processor_count}")
        
        # Scoring Logic
        memory_score = min(total_memory / 24 * 40, 40)  # Max 40 points for 24GB+
        compute_score = min((major - 3) * 10, 30)  # Max 30 points for compute >= 6.0
        cores_score = min(multi_processor_count / 100 * 30, 30)  # Max 30 points
        
        gpu_score = memory_score + compute_score + cores_score
        score = max(score, gpu_score)
        
        print(f"\nGPU {i} Score Breakdown:")
        print(f"  Memory Score: {memory_score:.1f}/40")
        print(f"  Compute Score: {compute_score:.1f}/30")
        print(f"  Cores Score: {cores_score:.1f}/30")
    
    # Overall Assessment
    print(f"\n{'=' * 50}")
    print(f"Overall ML GPU Score: {score:.1f}/100")
    print(f"{'=' * 50}")
    
    if score >= 80:
        print("Rating: Excellent - High-end ML workloads supported")
    elif score >= 60:
        print("Rating: Good - Medium to large ML models supported")
    elif score >= 40:
        print("Rating: Fair - Small to medium ML models supported")
    elif score >= 20:
        print("Rating: Basic - Limited ML capability")
    else:
        print("Rating: Poor - Consider upgrading for ML work")
    
    return score

if __name__ == "__main__":
    check_gpu_capabilities()