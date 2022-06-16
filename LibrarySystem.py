# import modules
import streamlit as st
# Import image from pillow to open images
from PIL import Image



# Page title
def homepage():
    img = Image.open("imageslib.jpg")
    st.image(img, width=700)
    st.title(" LIBRARY MANAGEMENT SYSTEM ")
    st.header("Welcome to the Library")
    st.subheader("""Keys to the past...Gateway to the future
                            Enrich your Knowledge""")


def registration():

    # Getting Users Information
    st.subheader("Create an Account")
    Fullnames = st.text_input("Enter your Fullnames: ")
    StudentID = st.text_input("Enter your Student Identity No: ")
    Email = st.text_input("Enter your Student Email: ")
    Faculty = st.text_input("Enter your Student Faculty: ")
    Phonenum = st.text_input("Enter your Phone number: ")
    Password = st.text_input("Enter your Password: ")

    Submit_button = st.button("Submit!")

    # if Submit button is successful
    if Submit_button == True:
        st.success("Hello {} you have just created an account".format(Fullnames))
        st.balloons()
    else:
        st.error("Please fill in all the above information")


# BORROWING BOOKS
# List of Available Books
def available_books():
    option = st.selectbox("Which Books did you select", ["Introduction to Blockchain", "Computer Vision for Beginner", "Search and          Optimization", "Neural Network for Data science",
                                                         "Bayesian theorem", "Inference", "Introduction to Machine Learning", "Climate Change Impacts", "Regression analysis", "Alawiye", "Internet of thing", "Stochastics", "Python Crash Course"])

    st.write("You have selected: ", option)


def issue_return_dates():
    Issue_date = st.date_input("Enter the issued date: ")
    Returning_date = st.date_input("Enter the returned date: ")
    submitdates = st.button("SUBMIT")
    if submitdates == True:
        def Disclaimer():
            warning = st.warning("""
            DISCLAIMER!
            All books borrowed are the property of the above named library. 
            Failure to return them or failure to return them on the said dates will attract  fine and school disciplinary actions. 
            Failure to maintain the books will attract charges for either repair or purchase of a new copy.""")
            agreement = st.radio("Agreement", ["Agree", "Disagree"])
            if agreement == "Agree":
                st.success('Success')
            elif agreement == "Disagree":
                st.error("Terms and conditions not met! Try Again!")

        Disclaimer()

# The Returning Book


def returning_books():
    Bookname = st.text_input("Enter the Book name: ")
    Issue_date = st.date_input("Enter the Issued date: ")
    Return_date = st.date_input("Enter the Returned date: ")
    submit = st.button("Submit!")
    if submit == True:
        st.success(
            "Thank you for using our service, you're welcome to borrow more books next time.")
        st.balloons()


# MENU
menu = st.sidebar.radio(
    "MAIN MENU", ["Home", "Register", "Borrow Books", "Return Books"])

if menu == "Home":
    homepage()
elif menu == "Register":
    registration()
elif menu == "Borrow Books":
    available_books()
    issue_return_dates()
elif menu == "Return Books":
    returning_books()
