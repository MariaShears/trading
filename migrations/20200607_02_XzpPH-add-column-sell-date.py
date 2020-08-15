"""
add column sell_date
"""

from yoyo import step

__depends__ = {'20200607_01_rVt3Q-rename-date-to-buy-date'}

steps = [
    step("ALTER TABLE journal RENAME TO TempOldJOurnal;")
]
