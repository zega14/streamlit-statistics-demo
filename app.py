import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Central Limit Theorem Demo")

dist = st.selectbox("Choose Distribution",
                    ["Uniform", "Exponential", "Normal"])

sample_size = st.slider("Sample Size", 1, 100, 30)
num_samples = st.slider("Number of Samples", 100, 5000, 1000)

means = []

for _ in range(num_samples):
    if dist == "Uniform":
        data = np.random.uniform(0, 1, sample_size)
    elif dist == "Exponential":
        data = np.random.exponential(1, sample_size)
    else:
        data = np.random.normal(0, 1, sample_size)

    means.append(np.mean(data))

fig, ax = plt.subplots()
ax.hist(means, bins=30)
ax.set_title("Distribution of Sample Means")

st.pyplot(fig)
