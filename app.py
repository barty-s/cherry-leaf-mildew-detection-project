import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.summary import summary_body
from app_pages.project_hypothesis import project_hypothesis_body
from app_pages.leaves_visualiser import leaves_visualiser_body
from app_pages.ml_performance import ml_performance_body
from app_pages.mildew_detector import mildew_detector_body

app = MultiPage(app_name="Cherry Leaf Mildew Detector")

app.app_page("Project Summary", project_summary_body)
app.app_page("Project Findings", project_findings_body)
app.app_page("Image Data", image_data_body)
app.app_page("Project Hypotheses", project_hypotheses_body)
app.app_page("Model Performance", model_performance_body)

app.run()