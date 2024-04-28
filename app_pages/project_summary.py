import streamlit as st


def project_summary_body():

    st.write(
        f"## Project Summary\n\n"
        f"The 'Cherry Leaf Mildew Detector' is a machine learning project designed "
        f"to predict if a leaf from a cherry tree is infected with the Powdery Mildew "
        f"disease.\n\n"
        f"The ML model uses an image of a cherry tree leaf to determine the "
        f"probability of whether the leaf, and tree it came from, is infected or healthy."
    )

    st.write("---")

    st.success(
        f"### About The Powdery Mildew Disease\n\n"
        f"Powdery Mildew disease is caused by *Podosphaera clandestina*, "
        f"one of the common species of the powdery mildew group of fungi.\n\n"
        f"The disease affects cherry trees and damages and stunts new growth. "
        f"It can also affect crop return in commercial settings.\n\n"

        f"### Symptoms and Signs of Powdery Mildew\n\n"
        f"Powdery mildew presents as superficial, white, weblike growth on "
        f"leaves, shoots, or fruit.\n\n"
        f"At first, infected leaves curl upward and by mid-season, "
        f"the whitish "
        f"fungus can be seen growing over the leaves and shoots, sometimes in "
        f"patches and other times covering most of the new growth.\n\n"

        f"### Disease Life Cycle\n\n"
        f"The Podosphaera clandestina fungus waits out the winter season "
        f"in buds on twigs and as chasmothecia, "
        f"which are spore-containing structures, on the bark of twigs and "
        f"branches. Secondary spores are then produced in spring "
        f"and spread the fungus to new growth."
    )

    st.write("---")

    st.warning(
        f"### Business Requirements\n\n"
        f"This project addresses two business requirements:\n\n"
        f"1 - Conduct a study to visually differentiate a healthy leaf from "
        "a mildew infected leaf.\n\n"
        f"2 - Train a model to accurately predict whether a given leaf is infected by "
        "powdery mildew or not."
    )

    st.write("---")

    st.success(
        f"### Project Dataset\n\n"
        f"The available dataset contains images of 2104 healthy leaves and "
        f"2104 infected leaves."
    )

    st.write("---")