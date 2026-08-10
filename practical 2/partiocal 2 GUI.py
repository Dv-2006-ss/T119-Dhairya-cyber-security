import tkinter as tk
from tkinter import messagebox
import random
from math import gcd

# ---------- RSA Functions ----------

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime():
    while True:
        num = random.randint(100, 300)
        if is_prime(num):
            return num

def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

    g, x, y = egcd(e, phi)
    if g != 1:
        return None
    return x % phi

# ---------- Key Generation ----------

def generate_keys():
    global e, d, n

    p = generate_prime()
    q = generate_prime()

    while p == q:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 3
    while gcd(e, phi) != 1:
        e += 2

    d = mod_inverse(e, phi)

    public_key_var.set(f"({e}, {n})")
    private_key_var.set(f"({d}, {n})")

# ---------- Encryption ----------

def encrypt():
    try:
        msg = int(message_entry.get())

        if msg >= n:
            messagebox.showerror("Error", "Message must be smaller than n.")
            return

        cipher = pow(msg, e, n)
        cipher_var.set(str(cipher))

    except ValueError:
        messagebox.showerror("Error", "Enter a valid integer.")

# ---------- Decryption ----------

def decrypt():
    try:
        cipher = int(cipher_var.get())
        plain = pow(cipher, d, n)
        decrypted_var.set(str(plain))

    except ValueError:
        messagebox.showerror("Error", "Invalid Cipher Text.")

# ---------- GUI ----------

root = tk.Tk()
root.title("RSA Encryption & Decryption")
root.geometry("500x400")
root.resizable(False, False)

public_key_var = tk.StringVar()
private_key_var = tk.StringVar()
cipher_var = tk.StringVar()
decrypted_var = tk.StringVar()

tk.Label(root, text="RSA Algorithm", font=("Arial", 16, "bold")).pack(pady=10)

tk.Button(root, text="Generate Keys", command=generate_keys,
          bg="lightblue").pack(pady=5)

tk.Label(root, text="Public Key").pack()
tk.Entry(root, textvariable=public_key_var,
         width=50, state="readonly").pack()

tk.Label(root, text="Private Key").pack()
tk.Entry(root, textvariable=private_key_var,
         width=50, state="readonly").pack()

tk.Label(root, text="Enter Numeric Message").pack(pady=5)
message_entry = tk.Entry(root, width=30)
message_entry.pack()

tk.Button(root, text="Encrypt", command=encrypt,
          bg="lightgreen").pack(pady=5)

tk.Label(root, text="Cipher Text").pack()
tk.Entry(root, textvariable=cipher_var, width=40).pack()

tk.Button(root, text="Decrypt", command=decrypt,
          bg="orange").pack(pady=5)

tk.Label(root, text="Decrypted Message").pack()
tk.Entry(root, textvariable=decrypted_var,
         width=40, state="readonly").pack(pady=5)

root.mainloop()