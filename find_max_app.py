import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Among 3 Numbers")
    
    st.write("Enter three numbers:")
    a = st.number_input("Number 1", step=1)
    b = st.number_input("Number 2", step=1)
    c = st.number_input("Number 3", step=1)
    
    if st.button("Find Largest"):
        largest = find_largest(a, b, c)
        st.write(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
