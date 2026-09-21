# CSPC Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

## PW1 Lab A: Reproducible Foundations

**What I built:**
A foundational course repository containing conda environment and an automated testing framework.

**Speed comparison (loop vs NumPy):**
- loop: 0.1450 s
- numpy: 0.0025 s
- speed-up: 58.00 x faster

**Tests:** all passing? yes

**Conclusion:**
Setting up the environment and linking it to GitHub went smoothly.
I learned how to use pytest to verify my code and was surprised by exactly how much faster NumPy array operations are compared to native Python loops.
