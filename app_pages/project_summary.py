import streamlit as st


def project_summary_body():

    st.write(
        f"## Project Summary\n\n"
        f"The 'Cherry Leaf Mildew Detector' is a"
        f" machine learning project designed "
        f"to predict if a leaf from a cherry tree"
        f" is infected with the Powdery Mildew "
        f"disease.\n\n"
        f"The ML model uses an image of a cherry tree leaf to determine the "
        f"probability of whether the leaf, and"
        f" tree it came from, is infected or healthy."
    )

    st.write("---")

    st.success(
        f"### About The Powdery Mildew Disease\n\n"
        f"Powdery mildew of sweet and sour cherry"
        f" is caused by Podosphaera clandestina,"
        f" an obligate biotrophic fungus. Mid- and late-season sweet"
        f" cherry (Prunus avium) cultivars are commonly affected,"
        f" rendering them unmarketable due to the covering of white"
        f" fungal growth on the cherry surface.\n\n"

        f"### Symptoms and Signs of Powdery Mildew\n\n"
        f"Initial symptoms, often occurring 7 to 10 days after the"
        f"onset of the first irrigation, are light roughly-circular,"
        f" powdery looking patches on young, susceptible leaves (newly"
        f" unfolded, and light green expanding leaves)."
        f" Older leaves develop an age-related (ontogenic) resistance to"
        f" powdery mildew and are naturally more resistant to infection"
        f" than younger leaves. gGermination"
        f" and fungal growth are favored by high humidity."
        f" The disease is more likely to initiate on the"
        f" undersides of leaves but will occur on both sides at later stages."
        f" As the season progresses and"
        f" infection is spread by wind, leaves may become distorted, "
        f"curling upward. Severe infections may"
        f" cause leaves to pucker and twist.\n\n"

        f"### Disease Life Cycle\n\n"
        f"The Podosphaera clandestina fungus waits out the winter season "
        f"in buds on twigs and as chasmothecia, "
        f"which are spore-containing structures, on the bark of twigs and "
        f"branches. Secondary spores are then produced in spring "
        f"and spread the fungus to new growth."
    )

    st.write("---")

    st.info(
        f"### Business Requirements\n\n"
        f"This project addresses two business requirements:\n\n"
        f"1 - Conduct a study to visually differentiate a healthy leaf from "
        "a mildew infected leaf.\n\n"
        f"2 - Train a model to accurately predict"
        f" whether a given leaf is infected by "
        "powdery mildew or not."
    )

    st.write("---")

    st.success(
        f"### Project Dataset\n\n"
        f"The available dataset contains images of 2104 healthy leaves and "
        f"2104 infected leaves."
    )

    st.write("---")
