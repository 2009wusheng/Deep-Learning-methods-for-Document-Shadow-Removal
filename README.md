# Document Shadow Removal: AI-Powered Solutions for Flawless Digitization

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![PyTorch](https://img.shields.io/badge/PyTorch-1.9%2B-red)
![Framework](https://img.shields.io/badge/Framework-PyTorch_Lightning-orange)

## 📖 Project Overview

This project focuses on AI-powered document shadow removal to enhance document digitization quality. Shadows frequently occur on scanned or photographed documents due to uneven lighting, paper folds, or object coverage during capture, significantly degrading content quality and impairing both human readability and machine-driven information extraction.

**Group Members:**  Zhibo Hu, Xinyue Zhao

## 🎯 Project Significance

- **Problem**: Shadows reduce document readability, impair information extraction, and undermine archival value
- **Solution**: Advanced deep learning models for effective shadow removal while preserving document content
- **Innovation**: Custom DSR dataset generation and specialized model fine-tuning for real-world applications

## 🔍 Evaluated Methods

### Traditional Methods (Baseline)
- **Adaptive Thresholding**: Dynamic local threshold calculation
  - Limitations: Color information loss, over-removed background, visible borders
- **Gamma Correction**: Binarization with contrast enhancement
  - Limitations: Color distortion, content detail loss on complex documents

### Deep Learning Methods (SOTA)

#### 1. SpA-Former (2022 - Ranked #7)
- GAN-based architecture
- Vision Transformer Encoder
- Gated Feed-Forward Network
- Lightweight (0.47MB)

#### 2. DC-ShadowNet (2022 - Ranked #5)
- GAN-based approach
- Domain classifier integration
- Multiple shadow-specific losses
- Unsupervised learning capability

#### 3. ShadowFormer (2023 - Ranked #1) - **Best Performer**
- **Channel Attention**: Efficient global information capture
- **Shadow-Interaction Attention**: 
  - Resizes shadow mask to feature map size
  - Categorizes patches into shadow/non-shadow regions
  - Exploits correlation maps between regions
  - Reweights attention to emphasize similarity

## 📊 Dataset: Document Shadow Removal (DSR)

### Custom Dataset Generation using Blender
- **150 training sets** + **50 testing sets**
- Each set contains: shadowed image, shadow mask, and non-shadow image
- Enhanced diversity through strategic variations:

#### Diversity Strategies:
1. **Material Variation**: Different document textures applied to 3D paper models
2. **Shadow Complexity**: Various 3D model shapes generating diverse shadow patterns
3. **Dynamic Lighting**: Adjustable light sources creating realistic illumination conditions

#### Lighting Scenarios:
- Single Strong Light Source: Sharp, well-defined shadows
- Strong + Weak Light Source: Uneven shadow coloration with subtle illumination
- Single Moderate Light Source: Soft, blurred shadow edges
- Multiple Light Sources: Overlapping shadows with mixed edge sharpness

## ⚙️ Evaluation Methodology

### Dataset: ISTD Test Dataset
- Standard benchmark for shadow removal evaluation

### Quantitative Metrics:
- **PSNR (Peak Signal-to-Noise Ratio)**: Objective visual error measurement (higher = better)
- **SSIM (Structural Similarity Index)**: Image similarity assessment (higher = better)

### Qualitative Assessment:
- Visual comparison of shadow removal effectiveness
- Content preservation evaluation
- Border artifact analysis

## 📈 Results

### Quantitative Evaluation on ISTD Dataset

| Model | PSNR (↑) | SSIM (↑) | 
|-------|----------|----------|
| SpA-Former | 29.09 | 0.71 |
| DC-ShadowNet | 28.67 | 0.68 |
| **ShadowFormer** | **28.23** | **0.96** |

### Fine-tuning Results (Custom DSR Dataset)

| Model | PSNR (↑) | SSIM (↑) | 
|-------|----------|----------|
| ShadowFormer (Original) | 19.50 | 0.79 |
| **ShadowFormer (Fine-tuned)** | **26.06** | **0.94** |

### Key Findings:
1. **ShadowFormer outperformed** all other models in both PSNR and SSIM metrics
2. **Fine-tuning significantly enhanced** performance on document-specific shadow removal
3. **Custom DSR dataset** proved effective for domain-specific adaptation
4. **Lighting diversity** in training data improved model robustness


## 📝 Citation

If you use this work in your research, please cite:

```bibtex
@misc{Documentshadowremoval2025,
  title={AI-Powered Document Shadow Removal for Flawless Digitization},
  author={ Hu, Zhibo and Zhao, Xinyue },
  year={2025},
  publisher={GitHub},
  howpublished={\url{https://github.com/your-username/document-shadow-removal}}
}
```

## 👥 Contributors

- **Xinyue Zhao** - Dataset generation, traditional model implementation
- **Zhibo Hu** - Deep Learning Model implementation, Evaluation, fine-tuning

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔮 Future Work

- Expansion to more document types and lighting conditions
- Development of real-time shadow removal for mobile applications
- Integration with OCR systems for end-to-end document processing
- Exploration of larger datasets and enhanced computational resources
- Addressing current limitations in complex shadow scenarios

