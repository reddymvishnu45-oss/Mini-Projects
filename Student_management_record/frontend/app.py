import streamlit as st
import requests as re
import pandas as pd

st.set_page_config(page_title='Student Record Manager',page_icon='📌')
st.title("📌 Student Record Manager")
API = "http://backend:8000"

# =========================
# ADD / UPDATE
# =========================

st.subheader("Student Records")

tab1, tab2 = st.tabs(["➕ Add Record", "✏️ Update Record"])


# =========================
# ADD RECORD
# =========================

with tab1:

    with st.form("add_form"):

        name = st.text_input("Name")
        email = st.text_input("Email")
        age = st.number_input(
            "Age",
            min_value=0,
            step=1
        )
        department = st.text_input("Department")

        add_button = st.form_submit_button("➕ Add Record")

    if add_button:

        data = {
            "name": name,
            "email": email,
            "age": age,
            "department": department
        }

        try:

            r = re.post(
                f"{API}/records",
                json=data
            )

            if r.ok:
                st.success("Record added successfully!")
                st.rerun()
            else:
                st.error(r.text)

        except re.RequestException as e:

            st.error(f"Backend error: {e}")


# =========================
# UPDATE RECORD
# =========================

with tab2:

    record_id = st.number_input(
        "Record ID",
        min_value=1,
        step=1,
        key="update_id"
    )

    with st.form("update_form"):

        name = st.text_input("Name", key="update_name")
        email = st.text_input("Email", key="update_email")
        age = st.number_input(
            "Age",
            min_value=0,
            step=1,
            key="update_age"
        )
        department = st.text_input(
            "Department",
            key="update_department"
        )

        update_button = st.form_submit_button("✏️ Update Record")

    if update_button:

        data = {
            "name": name,
            "email": email,
            "age": age,
            "department": department
        }

        try:

            r = re.put(
                f"{API}/records/{int(record_id)}",
                json=data
            )

            if r.ok:
                st.success("Record updated successfully!")
                st.rerun()
            else:
                st.error(r.text)

        except re.RequestException as e:

            st.error(f"Backend error: {e}")

st.subheader("Records")
try: 
    r = re.get(f'{API}/records')
    if r.ok:
        records = r.json()
        if records : st.dataframe(pd.DataFrame(records),use_container_width=True)
        else: st.info("No records yet. ")
    else: st.error(r.text)
except re.RequestException as e:
    st.error(f'Connot connect to FastAPI: {e}')

delete_id = st.number_input("Deleted Id",min_value=0,step=1,key='delete')
if st.button("Delete") and delete_id:
    try: 
        r=re.delete(f'{API}/records/{int(delete_id)}')
        if r.ok: st.success("Deleted");st.rerun()
        else:
            st.error(r.text)
    except re.RequestException as e:  st.error(e)
