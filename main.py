import streamlit as st
import pandas as pd

# Sample checklists (you can expand with PPB requirements)
checklists = {
    "New Product Registration": [
        "Application Form",
        "Cover Letter",
        "Manufacturing License",
        "Product Samples",
        "Stability Data",
        "Pharmacovigilance System Master File"
    ],
    "Renewal": [
        "Renewal Application Form",
        "Updated Manufacturing License",
        "Annual Safety Report",
        "Product Labels and Leaflets"
    ],
    "Variation": [
        "Variation Application Form",
        "Justification Letter",
        "Updated Product Dossier",
        "Proof of Payment"
    ]
}

st.title("📋 Regulatory Submission Checklist")

# Choose submission type
submission_type = st.selectbox("Select Submission Type", list(checklists.keys()))

# Display checklist
st.subheader(f"Checklist for {submission_type}")
selected = st.multiselect("Mark completed items:", checklists[submission_type])

# Progress
progress = len(selected) / len(checklists[submission_type])
st.progress(progress)

# Export option
if st.button("Export to Excel"):
    df = pd.DataFrame({"Requirement": checklists[submission_type], 
                       "Completed": ["Yes" if item in selected else "No" for item in checklists[submission_type]]})
    df.to_excel("submission_checklist.xlsx", index=False)
    st.success("Checklist exported as submission_checklist.xlsx ✅")
