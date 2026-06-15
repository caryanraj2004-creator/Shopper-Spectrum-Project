import streamlit as st
import pandas as pd

st.set_page_config(page_title="Shopper Spectrum")

st.title("🛒 Shopper Spectrum")
st.subheader("Customer Segmentation and Product Recommendation System")

rfm = pd.read_csv("models/customer_segments.csv")

st.header("Customer Segment Distribution")

segment_counts = rfm['Segment'].value_counts()

st.bar_chart(segment_counts)

st.header("Customer Segment Summary")

st.dataframe(
    rfm[['CustomerID','Recency','Frequency','Monetary','Segment']].head(20)
)

st.header("Segment Counts")

st.write(segment_counts)

st.success("Customer Segmentation Completed Successfully")

st.success("Product Recommendation Model Ready")