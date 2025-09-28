import streamlit as st
import pandas as pd
from dsa import add_contact, view_contact, search_contact, update_contact, delete_contact, FIELDS

st.title("Contact Manager")

# Sidebar Menu
menu = ["Add", "View", "Search", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add":
    st.subheader("Add New Contact")
    contact_data = {}
    for field in FIELDS:
        if field == "Name":
            contact_data[field] = st.text_input(field, placeholder="Enter name")
        elif "Phone" in field or field == "WhatsApp":
            contact_data[field] = st.text_input(field, placeholder="Enter phone number")
        elif field == "Email":
            contact_data[field] = st.text_input(field, placeholder="Enter email")
        else:
            contact_data[field] = st.text_input(field, placeholder=f"Enter {field}")
    
    if st.button("Save Contact"):
        if contact_data["Name"].strip() != "":
            add_contact(contact_data)
            st.success(f"Contact {contact_data['Name']} added successfully!")
        else:
            st.error("Name cannot be empty.")

elif choice == "View":
    st.subheader("All Contacts")
    data = view_contact()
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.info("No contacts found.")

elif choice == "Search":
    st.subheader("Search Contact")
    name = st.text_input("Enter name to search")
    if st.button("Search"):
        results = search_contact(name)
        if results:
            st.write(pd.DataFrame(results))
        else:
            st.warning("No contact found with that name.")

elif choice == "Update":
    st.subheader("Update Contact")
    name = st.text_input("Enter name of contact to update")
    if st.button("Fetch Contact"):
        results = search_contact(name)
        if results:
            old_data = results[0]
            new_data = {}
            for field in FIELDS:
                new_data[field] = st.text_input(field, old_data.get(field, ""))
            
            if st.button("Update Contact"):
                success = update_contact(name, new_data)
                if success:
                    st.success(f"Contact {name} updated successfully!")
                else:
                    st.error("Update failed.")
        else:
            st.warning("No contact found with that name.")

elif choice == "Delete":
    st.subheader("Delete Contact")
    name = st.text_input("Enter name of contact to delete")
    if st.button("Delete"):
        deleted = delete_contact(name)
        if deleted:
            st.success(f"Contact {name} deleted successfully!")
        else:
            st.error("Contact not found.")

data = view_contact()
if data:
    df = pd.DataFrame(data)
    st.download_button(
        label="Download Contacts as CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="contacts.csv",
        mime="text/csv",
    )
