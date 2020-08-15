"""
rename date to buy_date
"""

from yoyo import step

__depends__ = {'20200502_01_YI8zE-create-journal-table'}

steps = [
    step("ALTER TABLE journal RENAME COLUMN date to buy_date;")
]
