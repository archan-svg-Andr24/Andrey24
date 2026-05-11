# -*- coding: utf-8 -*-
import psycopg2
import sys

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "Stepanov_Variativka",
    "user": "postgres",
    "password": "pgAdmin777"
}

def get_connection():
    try:
        return psycopg2.connect(**DB_CONFIG)
    except psycopg2.Error as e:
        print(f"Ошибка подключения: {e}")
        sys.exit(1)

def execute_join_query():
    query = """
    SELECT
        p.code_project,
        c.price,
        cust.full_name AS customer_name,
        ch.full_name AS chief_name,
        p.date_conclusion,
        p.date_delivery
    FROM public.project p
    JOIN public.contract c ON p.code_contract = c.code_contract
    JOIN public.customer cust ON c.code_customer = cust.code_customer
    LEFT JOIN public.chief ch ON p.code_chief = ch.code_chief
    ORDER BY p.code_project;
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        if not rows:
            print("Нет данных.")
            return
        print("\nРезультаты JOIN-запроса:")
        print("-" * 125)
        print(f"{'Код проекта':<12} | {'Цена договора':<15} | {'Заказчик':<30} | {'Руководитель':<30} | {'Дата начала':<12} | {'Дата сдачи':<12}")
        print("-" * 125)
        for row in rows:
            proj, price, cust_name, chief, start, end = row
            price_str = f"{price:,.2f}" if price else "NULL"
            cust_str = cust_name[:30] if cust_name else "NULL"
            chief_str = chief[:30] if chief else "Не назначен"
            start_str = start.strftime("%Y-%m-%d") if start else "NULL"
            end_str = end.strftime("%Y-%m-%d") if end else "NULL"
            print(f"{proj:<12} | {price_str:<15} | {cust_str:<30} | {chief_str:<30} | {start_str:<12} | {end_str:<12}")
    except psycopg2.Error as e:
        print(f"Ошибка запроса: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    execute_join_query()