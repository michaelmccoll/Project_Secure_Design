from db.run_sql import run_sql

from models.project import Project
from models.triage import Triage
from models.risk import Risk
from models.control import Control
from models.categories import Category

import repositories.project_repository as project_repository
import repositories.triage_repository as triage_repository
import repositories.risk_repository as risk_repository
import repositories.control_repository as control_repository
import repositories.category_repository as category_repository

def save(categories):
    sql = "INSERT INTO categories(category) VALUES (%s) RETURNING id"
    values = [categories.category]
    results = run_sql(sql,values)
    categories.id = results[0]['id']
    return categories

def select_all():
    categories = []
    sql = "SELECT * FROM categories"
    results = run_sql(sql)

    for row in results:
        categories = Category(row['category'],row['id'])
        categories.append(categories)
    return categories

def select(id):
    categories = None
    sql = "SELECT * FROM categories WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        categories = Category(result['category'],result['id'])
    return categories

# def delete_all():
#     sql = "DELETE FROM categories"
#     run_sql(sql)

# def delete(id):
#     sql = "DELETE FROM categories WHERE id = %s"
#     values = [id]
#     run_sql(sql,values)

# def update(categories):
#     sql = "UPDATE categories SET (question) = (%s) WHERE id = %s"
#     values = [categories.question]
#     run_sql(sql,values)

# Find the categories by the consultant = xxx???
# def categories(consultant):
#     values = [consultant.id]
#     sql = f"""
#             SELECT categories.* FROM categories
#             INNER JOIN assignments
#             ON categories.id = assignments.categories_id
#             WHERE consultant_id = %s
#             """
#     results = run_sql(sql,values)
#     categories = []
#     for row in results:
#         categories = categories(row['title'],row['sponsor'],row['categories_manager'],row['start_date'],row['end_date'],row['status'],row['id'])
#         categories.append(categories)
#     return categories
# ----------------------------------------------
# def total_categories_spend():
#     sql = f"""
#             SELECT categories_id, SUM(total_cost) FROM categories
#             INNER JOIN assignments ON categories.id = assignments.categories_id
#             GROUP BY categories_id
#             """
#     total_categories_spend =run_sql(sql)
#     return total_categories_spend