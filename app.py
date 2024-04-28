import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.project_summary import project_summary_body
from app_pages.project_findings import project_findings_body
from app_pages.image_data import image_data_body
from app_pages.project_hypotheses import project_hypotheses_body
from app_pages.model_performance import model_performance_body

app = MultiPage(app_name="Cherry Leaf Mildew Detector")

app.app_page("Project Summary", project_summary_body)
app.app_page("Project Findings", project_findings_body)
app.app_page("Image Data", image_data_body)
app.app_page("Project Hypotheses", project_hypotheses_body)
app.app_page("Model Performance", model_performance_body)

app.run()