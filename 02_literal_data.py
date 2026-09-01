# tipe data
# 1. string = karakter
# 2. integer = bilangan bulat
# 3. double = bilangan desimal
# 4. boolean = true / false
#  program 2.2
# print ("nama saya najwa")
# program 2.2
# variabel adalah tempat menyimpan nilai
# tipe data
# 1. string = karakter
# 2. integer = bilangan bulat
# 3. double / float = bilangan desimal
# 4.boolean = true / false

# tipe data pada python 
x = 5
y = 10
print(5)
print("nilai y adalah",y)
# aturan penamaan
nilai_y = 15       #menggunakan underscore
juta_10 = 10000000 # tidak boleh diawali dengan angka 
nilaiz = 17.5  # camelcase

# Program 2.2 Menampilkan output ke konsol 
# Variabel adalah tempat menyimpan data 
# menaruh / assignment nilai 
# di python tidak perlu deklarasi  
a = 10 
x = 5 
panjang = 1000 
# pemanggilan pertama 
print("Nilai a = ", a) 
print("Nilai x = ", x) 
print("Nilai panjang = ", panjang) 
# penamaan      
nilai_y = 15 # dengan menggunakan underscore   
juta10 = 10000000 # ini boleh   
nilaiZ = 17.5 # ini boleh    
# pemanggilan kedua  
print("Nilai a = ", a)  
a = 7  
print("Nilai a = ", a)   
# assignment indirect  
b = a  
print("Nilai b = ", b) 

# program 2.3
  # a = 10, a adalah variable dengan nilai 10 
 # tipe data: Angka satuan yang gak ada komanya (integer) 
data_integer = 1 
print("data : ", data_integer)
print("- bertipe ", type(data_integer))
  # tipe data: Angka dengan koma (float)
data_float = 1.5 
print("data : ", data_float) 
print("- bertipe ", type(data_float)) 
 # tipe data: kumpulan karakter (string) 
data_string = "ucup"    
print("data : ", data_string)   
print("- bertipe ", type(data_string)) 
 # tipe data: biner true/false (boolean)   
data_bool = True  
print("data : ", data_bool)   
print("- bertipe ", type(data_bool))
  ## tipe data khusus
# bilangan kompleks  
data_complex = complex(5,6)   
print("data : ",data_complex)
print("- bertipe ",type(data_complex)) 
 # tipe data dari bahasa C   
from ctypes import c_double   
data_c_double = c_double(10.5) 
print("data : ", data_c_double)  
print("- bertipe ", type(data_c_double)) 



# program 2.4
 # merubah tipe data ke tipe data lain 
 # tipe data = int, float, str, bool  
 # INTEGER ke Tipe data lain     
data_int = 9   
data_float = float(data_int) 
data_str = str(data_int)  
data_bool = bool(data_int)  # akan false jika nilai integer = 0 
print("data = ", data_float, ",type = ", type(data_float))  
print("data = ", data_str, ",type = ", type(data_str))   
print("data = ", data_bool, ",type = ", type(data_bool))
# FLOAT ke Tipe data lain  
data_float = 9.2    
data_int = int(data_float)  
data_str = str(data_float)  
data_bool = bool(data_float) # akan false jika nilai integer = 0  
print("data = ", data_int, ",type = ", type(data_int))  
print("data = ", data_str, ",type = ", type(data_str))  
print("data = ", data_bool, ",type = ", type(data_bool)) 
 # STRING ke Tipe data lain    
data_str = "10" 
data_int = int(data_str)  
data_float = float(data_str)  
data_bool = bool(data_str)  
print("data = ", data_int, ",type = ", type(data_int))  
print("data = ", data_float, ",type = ", type(data_float))  
print("data = ", data_bool, ",type = ", type(data_bool)) 

#program 2.5
# input data user 
# data yang dimasukan pasti string 
data = input("Masukan data: ") 
print("data ",data,",type =",type(data)) 
#jika kita ingin mengambil int, maka
angka = int(input("masukan angka: ")) 
print("data ",angka,",type =",type(angka))