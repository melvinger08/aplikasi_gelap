import streamlit as st

st.header('define number type apps', divider='rainbow')
st.write('ini adalah aplikasi untuk menentukan bilangan genap atau ganjil')



import streamlit as st

# Memasukkan dua bilangan dari pengguna
number1 = st.number_input("Insert the first number")
st.write("The first number is ", number1)
# Menentukan apakah bilangan pertama ganjil atau genap
if number1 % 2 == 0:
    st.write(f"{number1} is an even number.")
else:
    st.write(f"{number1} is an odd number.")
  

number2 = st.number_input("Insert the second number")
st.write("The second number is ", number2)
# Menampilkan kedua bilangan yang dimasukkan pengguna
# Menentukan apakah bilangan kedua ganjil atau genap
if number2 % 2 == 0:
    st.write(f"{number2} is an even number.")
else:
    st.write(f"{number2} is an odd number.")

# Mengalikan kedua bilangan
result = number1 * number2
st.write(f"The result of {number1} * {number2} = {result}")

# Menentukan apakah hasil perkaliannya ganjil atau genap
if result % 2 == 0:
    st.success(f"The result {result} is an even number.")
else:
    st.warning(f"The result {result} is an odd number.")


