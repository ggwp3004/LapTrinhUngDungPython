import sqlite3

def connect():
    return sqlite3.connect("nhansu.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nhansu (
        cccd TEXT PRIMARY KEY,
        hoten TEXT,
        ngaysinh TEXT,
        gioitinh TEXT,
        diachi TEXT
    )
    """)

    conn.commit()
    conn.close()

def them_nhansu(cccd, hoten, ngaysinh, gioitinh, diachi):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO nhansu VALUES (?, ?, ?, ?, ?)",
                   (cccd, hoten, ngaysinh, gioitinh, diachi))

    conn.commit()
    conn.close()

def hien_thi():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM nhansu")
    data = cursor.fetchall()

    conn.close()
    return data

def sua_nhansu(cccd, hoten, ngaysinh, gioitinh, diachi):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE nhansu
    SET hoten=?, ngaysinh=?, gioitinh=?, diachi=?
    WHERE cccd=?
    """, (hoten, ngaysinh, gioitinh, diachi, cccd))

    conn.commit()
    conn.close()

def xoa_nhansu(cccd):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM nhansu WHERE cccd=?", (cccd,))

    conn.commit()
    conn.close()

def tim_kiem(keyword):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM nhansu
    WHERE cccd LIKE ? OR hoten LIKE ? OR diachi LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))

    data = cursor.fetchall()
    conn.close()
    return data
