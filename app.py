import streamlit as st                          # For building the web app interface
from main import ContactManager, Contact        # Importing Contact class and ContactManager logic

# Predefined countries and codes
COUNTRIES = {
    "Afghanistan (+93)": "+93",
    "Albania (+355)": "+355",
    "Algeria (+213)": "+213",
    "Andorra (+376)": "+376",
    "Angola (+244)": "+244",
    "Argentina (+54)": "+54",
    "Armenia (+374)": "+374",
    "Australia (+61)": "+61",
    "Austria (+43)": "+43",
    "Azerbaijan (+994)": "+994",
    "Bahamas (+1-242)": "+1242",
    "Bahrain (+973)": "+973",
    "Bangladesh (+880)": "+880",
    "Belarus (+375)": "+375",
    "Belgium (+32)": "+32",
    "Belize (+501)": "+501",
    "Benin (+229)": "+229",
    "Bhutan (+975)": "+975",
    "Bolivia (+591)": "+591",
    "Bosnia and Herzegovina (+387)": "+387",
    "Botswana (+267)": "+267",
    "Brazil (+55)": "+55",
    "Brunei (+673)": "+673",
    "Bulgaria (+359)": "+359",
    "Burkina Faso (+226)": "+226",
    "Burundi (+257)": "+257",
    "Cambodia (+855)": "+855",
    "Cameroon (+237)": "+237",
    "Canada (+1)": "+1",
    "Chad (+235)": "+235",
    "Chile (+56)": "+56",
    "China (+86)": "+86",
    "Colombia (+57)": "+57",
    "Congo (+242)": "+242",
    "Costa Rica (+506)": "+506",
    "Croatia (+385)": "+385",
    "Cuba (+53)": "+53",
    "Cyprus (+357)": "+357",
    "Czech Republic (+420)": "+420",
    "Denmark (+45)": "+45",
    "Djibouti (+253)": "+253",
    "Dominican Republic (+1-809)": "+1809",
    "Ecuador (+593)": "+593",
    "Egypt (+20)": "+20",
    "El Salvador (+503)": "+503",
    "Estonia (+372)": "+372",
    "Eswatini (+268)": "+268",
    "Ethiopia (+251)": "+251",
    "Fiji (+679)": "+679",
    "Finland (+358)": "+358",
    "France (+33)": "+33",
    "Gabon (+241)": "+241",
    "Gambia (+220)": "+220",
    "Georgia (+995)": "+995",
    "Germany (+49)": "+49",
    "Ghana (+233)": "+233",
    "Greece (+30)": "+30",
    "Guatemala (+502)": "+502",
    "Honduras (+504)": "+504",
    "Hong Kong (+852)": "+852",
    "Hungary (+36)": "+36",
    "Iceland (+354)": "+354",
    "India (+91)": "+91",
    "Indonesia (+62)": "+62",
    "Iran (+98)": "+98",
    "Iraq (+964)": "+964",
    "Ireland (+353)": "+353",
    "Israel (+972)": "+972",
    "Italy (+39)": "+39",
    "Jamaica (+1-876)": "+1876",
    "Japan (+81)": "+81",
    "Jordan (+962)": "+962",
    "Kazakhstan (+7)": "+7",
    "Kenya (+254)": "+254",
    "Kuwait (+965)": "+965",
    "Kyrgyzstan (+996)": "+996",
    "Laos (+856)": "+856",
    "Latvia (+371)": "+371",
    "Lebanon (+961)": "+961",
    "Lesotho (+266)": "+266",
    "Liberia (+231)": "+231",
    "Libya (+218)": "+218",
    "Lithuania (+370)": "+370",
    "Luxembourg (+352)": "+352",
    "Macau (+853)": "+853",
    "Madagascar (+261)": "+261",
    "Malawi (+265)": "+265",
    "Malaysia (+60)": "+60",
    "Maldives (+960)": "+960",
    "Mali (+223)": "+223",
    "Malta (+356)": "+356",
    "Mauritania (+222)": "+222",
    "Mauritius (+230)": "+230",
    "Mexico (+52)": "+52",
    "Moldova (+373)": "+373",
    "Monaco (+377)": "+377",
    "Mongolia (+976)": "+976",
    "Montenegro (+382)": "+382",
    "Morocco (+212)": "+212",
    "Mozambique (+258)": "+258",
    "Myanmar (+95)": "+95",
    "Namibia (+264)": "+264",
    "Nepal (+977)": "+977",
    "Netherlands (+31)": "+31",
    "New Zealand (+64)": "+64",
    "Nicaragua (+505)": "+505",
    "Niger (+227)": "+227",
    "Nigeria (+234)": "+234",
    "North Korea (+850)": "+850",
    "North Macedonia (+389)": "+389",
    "Norway (+47)": "+47",
    "Oman (+968)": "+968",
    "Pakistan (+92)": "+92",
    "Panama (+507)": "+507",
    "Papua New Guinea (+675)": "+675",
    "Paraguay (+595)": "+595",
    "Peru (+51)": "+51",
    "Philippines (+63)": "+63",
    "Poland (+48)": "+48",
    "Portugal (+351)": "+351",
    "Qatar (+974)": "+974",
    "Romania (+40)": "+40",
    "Russia (+7)": "+7",
    "Rwanda (+250)": "+250",
    "Saudi Arabia (+966)": "+966",
    "Senegal (+221)": "+221",
    "Serbia (+381)": "+381",
    "Singapore (+65)": "+65",
    "Slovakia (+421)": "+421",
    "Slovenia (+386)": "+386",
    "Somalia (+252)": "+252",
    "South Africa (+27)": "+27",
    "South Korea (+82)": "+82",
    "Spain (+34)": "+34",
    "Sri Lanka (+94)": "+94",
    "Sudan (+249)": "+249",
    "Sweden (+46)": "+46",
    "Switzerland (+41)": "+41",
    "Syria (+963)": "+963",
    "Taiwan (+886)": "+886",
    "Tajikistan (+992)": "+992",
    "Tanzania (+255)": "+255",
    "Thailand (+66)": "+66",
    "Tunisia (+216)": "+216",
    "Turkey (+90)": "+90",
    "Uganda (+256)": "+256",
    "Ukraine (+380)": "+380",
    "United Arab Emirates (+971)": "+971",
    "United Kingdom (+44)": "+44",
    "United States (+1)": "+1",
    "Uruguay (+598)": "+598",
    "Uzbekistan (+998)": "+998",
    "Venezuela (+58)": "+58",
    "Vietnam (+84)": "+84",
    "Yemen (+967)": "+967",
    "Zambia (+260)": "+260",
    "Zimbabwe (+263)": "+263"
}

# Predefined tag options to classify contacts
TAGS = ["Myself", "Family", "Reletive", "Friends", "Work"]

# Creating a ContactManager instance to manage all operations
manager = ContactManager()

# Set page configuration for the Streamlit app
st.set_page_config(page_title="Contact Manager", layout="centered")

# Display the app title
st.title("📇 Contact Management System")

# Sidebar menu to navigate between functionalities
menu = ["Add Contact", "View Contacts", "Search Contact", "Edit Contact", "Delete Contact"]
choice = st.sidebar.radio("Menu", menu)

# Helper function to retrieve selected tags from checkboxes
def get_selected_tags():
    return [tag for tag in TAGS if st.checkbox(tag, key=f"tag_{tag}")]

# Option 1: Add a new contact
if choice == "Add Contact":
    st.subheader("Add New Contact")
    # Input fields for contact details
    name = st.text_input("Full Name")
    selected_country = st.selectbox("Select Country", list(COUNTRIES.keys()))
    raw_phone = st.text_input("Phone Number (10 digits only)")
    email = st.text_input("Email")

    # Tag checkboxes
    st.markdown("**Select Tags**")
    selected_tags = get_selected_tags()

    # Compose full phone number by adding country code
    country_code = COUNTRIES[selected_country]
    full_phone = f"{country_code}{raw_phone}"

    # On clicking 'Add Contact'
    if st.button("Add Contact"):
        try:
            # Create a contact object and add it using manager
            contact = Contact(name, full_phone, email, selected_tags)
            manager.add_contact(contact)
            st.success("✅ Contact added successfully!")
        except Exception as e:
            st.error(f"❌ {e}")

# Option 2: View all contacts
elif choice == "View Contacts":
    st.subheader("All Contacts")

    # Fetch and display all contacts
    contacts = manager.get_all_contacts()
    for c in contacts:
        st.write(f"**{c.name}**")
        st.write(f"📞 {c.phone}  |  ✉️ {c.email}")
        st.write(f"🏷️ Tags: {', '.join(c.tags)}")
        st.markdown("---")

# Option 3: Search contacts by name, phone, or tag (supports regex)
elif choice == "Search Contact":
    st.subheader("Search Contact")

    # Input field for search pattern
    pattern = st.text_input("Enter name, phone or tag (Regex supported)")
    if st.button("Search"):
        try:
            # Perform search and display results
            results = manager.search_contacts(pattern)
            for c in results:
                st.write(f"**{c.name}**")
                st.write(f"📞 {c.phone}  |  ✉️ {c.email}")
                st.write(f"🏷️ Tags: {', '.join(c.tags)}")
                st.markdown("---")
        except Exception as e:
            st.error(f"❌ {e}")

# Option 4: Delete a contact by selecting from dropdown
elif choice == "Delete Contact":
    st.subheader("Delete Contact")

    # Get list of all contacts
    contacts = manager.get_all_contacts()

    if contacts:
        
        # Create a mapping of display name to phone for dropdown
        phone_dict = {f"{c.name} ({c.phone})": c.phone for c in contacts}
        selection = st.selectbox("Select contact to delete", list(phone_dict.keys()))
        phone_to_delete = phone_dict[selection]

        # On click, delete the selected contact
        if st.button("Delete"):
            try:
                manager.delete_contact_by_phone(phone_to_delete)
                st.success("🗑️ Contact deleted successfully!")
            except Exception as e:
                st.error(f"❌ {e}")
    else:
        st.info("No contacts available to delete.")

# Option 5: Edit a selected contact
elif choice == "Edit Contact":
    st.subheader("Edit Contact")

    # Get current list of contacts
    contacts = manager.get_all_contacts()

    # Map contacts to dropdown selection
    phone_dict = {f"{c.name} ({c.phone})": c.phone for c in contacts}
    selection = st.selectbox("Select contact to edit", list(phone_dict.keys()))
    old_phone = phone_dict[selection]

    # Find the contact object by phone number
    contact = next((c for c in contacts if c.phone == old_phone), None)
    
    if contact:
        # Pre-fill input fields with current contact details
        new_name = st.text_input("New Name", value=contact.name)
        selected_country = st.selectbox("Select Country Code", list(COUNTRIES.keys()))
        raw_phone = st.text_input("New Phone Number (10 digits)", value=contact.phone[-10:])
        email = st.text_input("New Email", value=contact.email)

        # Re-select tags
        st.markdown("**Select New Tags**")
        selected_tags = get_selected_tags()

        # Form full updated phone number
        country_code = COUNTRIES[selected_country]
        full_phone = f"{country_code}{raw_phone}"

        # On click, save updated contact
        if st.button("Update Contact"):
            try:
                new_contact = Contact(new_name, full_phone, email, selected_tags)
                manager.edit_contact(old_phone, new_contact)
                st.success("✏️ Contact updated successfully!")
            except Exception as e:
                st.error(f"❌ {e}")
